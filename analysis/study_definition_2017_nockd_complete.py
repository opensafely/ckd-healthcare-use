from cohortextractor import (
    StudyDefinition,
    Measure,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists
)

from codelists import *

NOCKD = "output/2017_nockd.csv"

from variables_nockd import generate_variables_nockd
variables_nockd= generate_variables_nockd(index_date_variable="index_date")

from variables_hrg import generate_variables_hrg
variables_hrg= generate_variables_hrg(index_date_variable="index_date")

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "2017-04-01", "latest": "2018-03-31"},
        "rate": "uniform",
        "incidence" : 0.2
    },
    population=patients.which_exist_in_file(NOCKD), 
    index_date="2017-04-01",

    **variables_nockd,
    **variables_hrg,
) 