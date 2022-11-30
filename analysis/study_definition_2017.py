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

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1980-01-01", "latest": "2017-04-01"},
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

    index_date="2017-04-01",

    age=patients.age_as_of(
       "index_date",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),
    region=patients.registered_practice_as_of(
        "index_date",
        returning="nuts1_region_name",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and The Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East": 0.1,
                    "London": 0.2,
                    "South East": 0.1,
                    "South West": 0.1,
                },
            },
        },
    ),
    imd=patients.categorised_as(
        {
            "0": "DEFAULT",
            "1": """index_of_multiple_deprivation >=0 AND index_of_multiple_deprivation < 32844*1/5""",
            "2": """index_of_multiple_deprivation >= 32844*1/5 AND index_of_multiple_deprivation < 32844*2/5""",
            "3": """index_of_multiple_deprivation >= 32844*2/5 AND index_of_multiple_deprivation < 32844*3/5""",
            "4": """index_of_multiple_deprivation >= 32844*3/5 AND index_of_multiple_deprivation < 32844*4/5""",
            "5": """index_of_multiple_deprivation >= 32844*4/5 AND index_of_multiple_deprivation < 32844""",
        },
        index_of_multiple_deprivation=patients.address_as_of(
            "index_date",
            returning="index_of_multiple_deprivation",
            round_to_nearest=100,
        ),
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0.05,
                    "1": 0.19,
                    "2": 0.19,
                    "3": 0.19,
                    "4": 0.19,
                    "5": 0.19,
                }
            },
        },

    ),
    deceased=patients.with_death_recorded_in_primary_care(
        returning="binary_flag",
        between = ["1970-01-01", "index_date - 1 day"],
        return_expectations={"incidence": 0.10, "date": {"earliest" : "2005-04-01", "latest": "2017-03-31"}},
        ),
    dialysis_primary_care=patients.with_these_clinical_events(
        dialysis_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="binary_flag",
        return_expectations = {"incidence": 0.05},
    ),
    dialysis_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=dialysis_icd_10_codes,
        returning="binary_flag",
        between = ["1970-01-01", "index_date - 1 day"],
        return_expectations={"incidence": 0.05},
    ),
    dialysis_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=dialysis_opcs_4_codes,
        returning="binary_flag",
        between = ["1970-01-01", "index_date - 1 day"],
        return_expectations={"incidence": 0.05},
    ),
    kidney_transplant_primary_care=patients.with_these_clinical_events(
        kidney_transplant_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="binary_flag",
        return_expectations = {"incidence": 0.05},
    ),
    kidney_transplant_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=kidney_transplant_icd_10_codes,
        returning="binary_flag",
        between = ["1970-01-01", "index_date - 1 day"],
        return_expectations={"incidence": 0.05},
    ),
    kidney_transplant_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=kidney_transplant_opcs_4_codes,
        returning="binary_flag",
        between = ["1970-01-01", "index_date - 1 day"],
        return_expectations={"incidence": 0.05},
    ),
    baseline_creatinine=patients.mean_recorded_value(
        creatinine_codes,
        on_most_recent_day_of_measurement=False,
        between=["index_date - 18 months","index_date - 1 day"],
        return_expectations={
            "float": {"distribution": "normal", "mean": 80, "stddev": 40},
            "incidence": 0.60,
        }
    ),
    has_follow_up=patients.registered_with_one_practice_between(
        "index_date - 3 months", "index_date",
        return_expectations={"incidence":0.95,
    }
    ),
)