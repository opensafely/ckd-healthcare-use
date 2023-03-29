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
        "date": {"earliest": "1980-01-01", "latest": "2020-04-01"},
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
    index_date="2020-04-01",

    ukrr = patients.with_record_in_ukrr(
        from_dataset="2019_prevalence",
        returning="treatment_modality_prevalence",
        return_expectations={
                "category": {"ratios": {"ICHD": 0.5, "Tx": 0.5}},
                "incidence": 0.05,
            },
    ),

    **variables_initial,
)

