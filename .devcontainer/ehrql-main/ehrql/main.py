import json
import os
import shutil
import sys
from contextlib import nullcontext
from pathlib import Path

import structlog

from ehrql import assurance, sandbox
from ehrql.dummy_data import DummyDataGenerator
from ehrql.file_formats import (
    read_rows,
    split_directory_and_extension,
    write_rows,
    write_tables,
)
from ehrql.loaders import (
    isolation_report,
    load_dataset_definition,
    load_definition_unsafe,
    load_measure_definitions,
    load_test_definition,
)
from ehrql.measures import (
    DummyMeasuresDataGenerator,
    apply_sdc_to_measure_results,
    get_column_specs_for_measures,
    get_measure_results,
)
from ehrql.query_engines.local_file import LocalFileQueryEngine
from ehrql.query_engines.sqlite import SQLiteQueryEngine
from ehrql.query_model.column_specs import (
    get_column_specs,
    get_column_specs_from_schema,
)
from ehrql.query_model.graphs import graph_to_svg
from ehrql.serializer import serialize
from ehrql.utils.itertools_utils import eager_iterator
from ehrql.utils.sqlalchemy_query_utils import (
    clause_as_str,
    get_setup_and_cleanup_queries,
)


log = structlog.getLogger()


def generate_dataset(
    definition_file,
    dataset_file,
    *,
    dsn,
    backend_class,
    query_engine_class,
    dummy_tables_path,
    dummy_data_file,
    test_data_file,
    environ,
    user_args,
):
    log.info(f"Compiling dataset definition from {str(definition_file)}")
    variable_definitions, dummy_data_config = load_dataset_definition(
        definition_file, user_args, environ
    )

    if test_data_file:
        log.info(f"Testing dataset definition with tests in {str(definition_file)}")
        assure(test_data_file, environ=environ, user_args=user_args)

    if dsn:
        generate_dataset_with_dsn(
            variable_definitions,
            dataset_file,
            dsn,
            backend_class=backend_class,
            query_engine_class=query_engine_class,
            environ=environ,
        )
    else:
        generate_dataset_with_dummy_data(
            variable_definitions,
            dummy_data_config,
            dataset_file,
            dummy_data_file=dummy_data_file,
            dummy_tables_path=dummy_tables_path,
        )


def generate_dataset_with_dsn(
    variable_definitions, dataset_file, dsn, backend_class, query_engine_class, environ
):
    log.info("Generating dataset")
    column_specs = get_column_specs(variable_definitions)

    query_engine = get_query_engine(
        dsn,
        backend_class,
        query_engine_class,
        environ,
        default_query_engine_class=LocalFileQueryEngine,
    )
    results = query_engine.get_results(variable_definitions)
    # Because `results` is a generator we won't actually execute any queries until we
    # start consuming it. But we want to make sure we trigger any errors (or relevant
    # log output) before we create the output file. Wrapping the generator in
    # `eager_iterator` ensures this happens by consuming the first item upfront.
    results = eager_iterator(results)
    write_rows(dataset_file, results, column_specs)


def generate_dataset_with_dummy_data(
    variable_definitions,
    dummy_data_config,
    dataset_file,
    *,
    dummy_data_file,
    dummy_tables_path,
):
    log.info("Generating dummy dataset")
    column_specs = get_column_specs(variable_definitions)

    if dummy_data_file:
        log.info(f"Reading dummy data from {dummy_data_file}")
        reader = read_rows(dummy_data_file, column_specs)
        results = iter(reader)
    elif dummy_tables_path:
        log.info(f"Reading table data from {dummy_tables_path}")
        query_engine = LocalFileQueryEngine(dummy_tables_path)
        results = query_engine.get_results(variable_definitions)
    else:
        generator = DummyDataGenerator(
            variable_definitions,
            population_size=dummy_data_config.population_size,
        )
        results = generator.get_results()

    log.info("Building dataset and writing results")
    results = eager_iterator(results)
    write_rows(dataset_file, results, column_specs)


def create_dummy_tables(definition_file, dummy_tables_path, user_args, environ):
    log.info(f"Creating dummy data tables for {str(definition_file)}")
    variable_definitions, dummy_data_config = load_dataset_definition(
        definition_file, user_args, environ
    )
    generator = DummyDataGenerator(
        variable_definitions,
        population_size=dummy_data_config.population_size,
    )
    table_data = generator.get_data()

    directory, extension = split_directory_and_extension(dummy_tables_path)
    log.info(f"Writing tables as '{extension}' files to '{directory}'")
    table_specs = {
        table.name: get_column_specs_from_schema(table.schema)
        for table in table_data.keys()
    }
    write_tables(dummy_tables_path, table_data.values(), table_specs)


def dump_dataset_sql(
    definition_file, output_file, backend_class, query_engine_class, environ, user_args
):
    log.info(f"Generating SQL for {str(definition_file)}")

    variable_definitions, _ = load_dataset_definition(
        definition_file, user_args, environ
    )
    query_engine = get_query_engine(
        None,
        backend_class,
        query_engine_class,
        environ,
        default_query_engine_class=SQLiteQueryEngine,
    )

    all_query_strings = get_sql_strings(query_engine, variable_definitions)
    log.info("SQL generation succeeded")

    with open_output_file(output_file) as f:
        for query_str in all_query_strings:
            f.write(f"{query_str};\n\n")


def get_sql_strings(query_engine, variable_definitions):
    results_query = query_engine.get_query(variable_definitions)
    setup_queries, cleanup_queries = get_setup_and_cleanup_queries(results_query)
    dialect = query_engine.sqlalchemy_dialect()
    sql_strings = []

    for i, query in enumerate(setup_queries, start=1):
        sql = clause_as_str(query, dialect)
        sql_strings.append(f"-- Setup query {i:03} / {len(setup_queries):03}\n{sql}")

    sql = clause_as_str(results_query, dialect)
    sql_strings.append(f"-- Results query\n{sql}")

    for i, query in enumerate(cleanup_queries, start=1):
        sql = clause_as_str(query, dialect)
        sql_strings.append(
            f"-- Cleanup query {i:03} / {len(cleanup_queries):03}\n{sql}"
        )

    return sql_strings


def open_output_file(output_file):
    # If a file path is supplied, create it and open for writing
    if output_file is not None:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        return output_file.open("w")
    # Otherwise return `stdout` wrapped in a no-op context manager
    else:
        return nullcontext(sys.stdout)


def get_query_engine(
    dsn, backend_class, query_engine_class, environ, default_query_engine_class
):
    # Construct backend if supplied
    if backend_class:
        backend = backend_class(config=environ)
    else:
        backend = None

    if not query_engine_class:
        # Use the query engine class specified by the backend, if we have one
        if backend:
            query_engine_class = backend.query_engine_class
        # Otherwise default to using SQLite
        else:
            query_engine_class = default_query_engine_class

    return query_engine_class(dsn=dsn, backend=backend, config=environ)


def generate_measures(
    definition_file,
    output_file,
    *,
    dsn,
    backend_class,
    query_engine_class,
    dummy_tables_path,
    dummy_data_file,
    environ,
    user_args,
):
    log.info(f"Compiling measure definitions from {str(definition_file)}")
    (
        measure_definitions,
        dummy_data_config,
        disclosure_control_config,
    ) = load_measure_definitions(definition_file, user_args, environ)

    if dsn:
        generate_measures_with_dsn(
            measure_definitions,
            disclosure_control_config,
            output_file,
            dsn,
            backend_class=backend_class,
            query_engine_class=query_engine_class,
            environ=environ,
        )
    else:
        generate_measures_with_dummy_data(
            measure_definitions,
            dummy_data_config,
            disclosure_control_config,
            output_file,
            dummy_tables_path,
            dummy_data_file,
        )


def generate_measures_with_dsn(
    measure_definitions,
    disclosure_control_config,
    output_file,
    dsn,
    backend_class,
    query_engine_class,
    environ,
):
    log.info("Generating measures data")
    column_specs = get_column_specs_for_measures(measure_definitions)

    query_engine = get_query_engine(
        dsn,
        backend_class,
        query_engine_class,
        environ,
        default_query_engine_class=LocalFileQueryEngine,
    )
    results = get_measure_results(query_engine, measure_definitions)
    if disclosure_control_config.enabled:
        results = apply_sdc_to_measure_results(results)
    results = eager_iterator(results)
    write_rows(output_file, results, column_specs)


def generate_measures_with_dummy_data(
    measure_definitions,
    dummy_data_config,
    disclosure_control_config,
    output_file,
    dummy_tables_path=None,
    dummy_data_file=None,
):
    log.info("Generating dummy measures data")
    column_specs = get_column_specs_for_measures(measure_definitions)

    if dummy_data_file:
        log.info(f"Reading dummy data from {dummy_data_file}")
        reader = read_rows(dummy_data_file, column_specs)
        results = iter(reader)
    elif dummy_tables_path:
        log.info(f"Reading data from {dummy_tables_path}")
        query_engine = LocalFileQueryEngine(dummy_tables_path)
        results = get_measure_results(query_engine, measure_definitions)
    else:
        generator = DummyMeasuresDataGenerator(measure_definitions, dummy_data_config)
        results = generator.get_results()

    log.info("Calculating measures and writing results")
    if disclosure_control_config.enabled:
        results = apply_sdc_to_measure_results(results)
    results = eager_iterator(results)
    write_rows(output_file, results, column_specs)


def run_sandbox(dummy_tables_path, environ):
    sandbox.run(dummy_tables_path)


def assure(test_data_file, environ, user_args):
    variable_definitions, test_data = load_test_definition(
        test_data_file, user_args, environ
    )
    results = assurance.validate(variable_definitions, test_data)
    print(assurance.present(results))


def test_connection(backend_class, url, environ):
    from sqlalchemy import select

    backend = backend_class()
    query_engine = backend.query_engine_class(url, backend, config=environ)
    with query_engine.engine.connect() as connection:
        connection.execute(select(1))
    print("SUCCESS")


def dump_example_data(environ):
    src_path = Path(__file__).parent / "example-data"
    dst_path = Path(os.getcwd()) / "example-data"
    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)


def serialize_definition(
    definition_type, definition_file, output_file, user_args, environ
):
    result = load_definition_unsafe(
        definition_type, definition_file, user_args, environ
    )
    with open_output_file(output_file) as f:
        f.write(serialize(result))


def run_isolation_report():
    print(json.dumps(isolation_report(Path.cwd()), indent=4))


def graph_query(definition_file, output_file, environ, user_args):  # pragma: no cover
    log.info(f"Graphing query for {str(definition_file)}")
    variable_definitions, _ = load_dataset_definition(
        definition_file, user_args, environ
    )
    graph_to_svg(variable_definitions, output_file)
