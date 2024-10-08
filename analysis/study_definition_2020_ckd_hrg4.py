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

CKD = "output/2020_ckd.csv"

from variables_additional import generate_variables_additional
variables_additional= generate_variables_additional(index_date_variable="index_date")

from variables_hrg4 import generate_variables_hrg4
variables_hrg4= generate_variables_hrg4(index_date_variable="index_date")

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "2020-04-01", "latest": "2021-03-31"},
        "rate": "uniform",
        "incidence" : 0.2
    },
    population=patients.which_exist_in_file(CKD), 
    index_date="2020-04-01",

    **variables_additional,
    **variables_hrg4,
) 