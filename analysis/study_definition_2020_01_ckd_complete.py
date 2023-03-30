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

CKD = "output/2020_01_ckd.csv"

from variables_additional_2020_01 import generate_variables_additional_2020_01
variables_additional_2020_01= generate_variables_additional_2020_01(index_date_variable="index_date")

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "2020-01-01", "latest": "2020-12-31"},
        "rate": "uniform",
        "incidence" : 0.2
    },
    population=patients.which_exist_in_file(CKD), 
    index_date="2020-01-01",

    ukrr_incident = patients.with_record_in_ukrr(
        from_dataset="2020_incidence",
        returning="treatment_modality_start",
        return_expectations={
                "category": {"ratios": {"ICHD": 0.5, "Tx": 0.5}},
                "incidence": 0.05,
            },
    ),

    **variables_additional_2020_01,
) 