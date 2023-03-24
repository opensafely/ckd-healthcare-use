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

CKD = "output/2022_ckd_v2.csv"

from variables_additional_v2 import generate_variables_additional_v2
variables_additional_v2= generate_variables_additional_v2(index_date_variable="index_date")

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "2022-04-01", "latest": "2022-12-31"},
        "rate": "uniform",
        "incidence" : 0.2
    },
    population=patients.which_exist_in_file(CKD), 
    index_date="2022-04-01",

    **variables_additional_v2,
) 