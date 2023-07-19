from cohortextractor import (
    StudyDefinition,
    Measure,
    patients,
    codelist,
    combine_codelists,
    filter_codes_by_category,
    codelist_from_csv,
)

from codelists import *

from variables_initial import generate_variables_initial
variables_initial= generate_variables_initial(index_date_variable="index_date")

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1980-01-01", "latest": "2022-04-01"},
        "rate": "uniform",
        "incidence": 0.7, 
    },

    population=patients.satisfying(
        """
        has_follow_up
        AND (age >=18)
        AND (sex = "M" OR sex = "F")
        AND NOT region = ""
        AND NOT deceased = "1"
        """,
    ),
    index_date="2023-04-01",

    **variables_initial,
)

