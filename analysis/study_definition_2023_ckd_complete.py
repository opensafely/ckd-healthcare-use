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

CKD = "output/2023_ckd.csv"

from variables_additional import generate_variables_additional
variables_additional= generate_variables_additional(index_date_variable="index_date")

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "2023-04-01", "latest": "2023-04-19"},
        "rate": "uniform",
        "incidence" : 0.2
    },
    population=patients.which_exist_in_file(CKD), 
    index_date="2023-04-01",

    **variables_additional,
) 