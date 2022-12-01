from cohortextractor import filter_codes_by_category, patients, combine_codelists
from codelists import *
from datetime import datetime, timedelta

def generate_variables_additional(index_date_variable):
    variables_additional = dict(    
    ethnicity=patients.with_these_clinical_events(
        ethnicity_codes,
        returning="category",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
            "category": {"ratios": {"1": 0.8, "2": 0.05, "3": 0.05, "4": 0.05, "5": 0.05}},
            "incidence": 0.75,
        },
    ),
    rural_urban=patients.address_as_of(
        "index_date",
        returning="rural_urban_classification",
        return_expectations={
            "rate": "universal",
            "category": 
                {"ratios": {
                    "1": 0.1,
                    "2": 0.1,
                    "3": 0.1,
                    "4": 0.1,
                    "5": 0.1,
                    "6": 0.1,
                    "7": 0.2,
                    "8": 0.2,
                }
            },
        },
    ),
    dialysis_baseline_primary_care=patients.with_these_clinical_events(
        dialysis_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    dialysis_baseline_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=dialysis_icd_10_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["1970-01-01", "index_date - 1 day"],
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    dialysis_baseline_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=dialysis_opcs_4_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["1970-01-01", "index_date - 1 day"],
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    dialysis_baseline_date=patients.minimum_of(
        "dialysis_baseline_primary_care", "dialysis_baseline_icd_10", "dialysis_baseline_opcs_4",
    ),
    kt_baseline_primary_care=patients.with_these_clinical_events(
        kidney_transplant_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    kt_baseline_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=kidney_transplant_icd_10_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["1970-01-01", "index_date - 1 day"],
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    kt_baseline_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=kidney_transplant_opcs_4_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["1970-01-01", "index_date - 1 day"],
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    kidney_transplant_baseline_date=patients.minimum_of(
        "kt_baseline_primary_care", "kt_baseline_icd_10", "kt_baseline_opcs_4",
    ),
    creatinine_outcome=patients.mean_recorded_value(
        creatinine_codes,
        on_most_recent_day_of_measurement=False,
        between=["index_date - 6 months","index_date + 365 days"],
        return_expectations={
            "float": {"distribution": "normal", "mean": 80, "stddev": 40},
            "incidence": 0.60,
        }
    ),
    dialysis_outcome_primary_care=patients.with_these_clinical_events(
        dialysis_codes,
        between = ["index_date", "index_date + 365 days"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 365 days"}}
    ),
    dialysis_outcome_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=dialysis_icd_10_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["index_date", "index_date + 365 days"],
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 365 days"}}
    ),
    dialysis_outcome_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=dialysis_opcs_4_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["index_date", "index_date + 365 days"],
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 365 days"}}
    ),
    dialysis_outcome_date=patients.minimum_of(
        "dialysis_outcome_primary_care", "dialysis_outcome_icd_10", "dialysis_outcome_opcs_4",
    ),
    kt_outcome_primary_care=patients.with_these_clinical_events(
        kidney_transplant_codes,
        between = ["index_date", "index_date + 365 days"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 365 days"}}
    ),
    kt_outcome_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=kidney_transplant_icd_10_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["index_date", "index_date + 365 days"],
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 365 days"}}
    ),
    kt_outcome_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=kidney_transplant_opcs_4_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["index_date", "index_date + 365 days"],
        find_first_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 365 days"}}
    ),
    kidney_transplant_outcome_date=patients.minimum_of(
        "kt_outcome_primary_care", "kt_outcome_icd_10", "kt_outcome_opcs_4",
    ),
    )
    return variables_additional
