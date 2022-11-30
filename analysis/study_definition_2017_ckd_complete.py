from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists
)

from codelists import *

CKD = "output/2017_ckd.csv"

from common_variables import generate_common_variables
common_variables= generate_common_variables(index_date_variable="index_date")

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "2017-04-01", "latest": "2018-03-31"},
        "rate": "uniform",
        "incidence" : 0.2
    },
    population=patients.which_exist_in_file(CKD), 
    index_date="2017-04-01",

    **common_variables,
) 