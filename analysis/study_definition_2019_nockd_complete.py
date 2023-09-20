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

NOCKD = "output/2019_nockd.csv"

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "2019-04-01", "latest": "2020-03-31"},
        "rate": "uniform",
        "incidence" : 0.2
    },
    population=patients.which_exist_in_file(NOCKD), 
    index_date="2019-04-01",

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

    creatinine_outcome=patients.mean_recorded_value(
        creatinine_codes,
        on_most_recent_day_of_measurement=False,
        between=["index_date - 6 months","index_date + 364 days"],
        return_expectations={
            "float": {"distribution": "normal", "mean": 80, "stddev": 40},
            "incidence": 0.60,
        }
    ),
    dialysis_outcome_primary_care=patients.with_these_clinical_events(
        dialysis_codes,
        between = ["index_date", "index_date + 364 days"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    dialysis_outcome_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=dialysis_icd_10_codes,
        between = ["index_date", "index_date + 364 days"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    dialysis_outcome_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=dialysis_opcs_4_codes,
        between = ["index_date", "index_date + 364 days"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    kt_outcome_primary_care=patients.with_these_clinical_events(
        kidney_transplant_codes,
        between = ["index_date", "index_date + 364 days"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    kt_outcome_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=kidney_transplant_icd_10_codes,
        between = ["index_date", "index_date + 364 days"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    kt_outcome_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=kidney_transplant_opcs_4_codes,
        between = ["index_date", "index_date + 364 days"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    krt_outcome=patients.categorised_as(
        {
            "New KRT":      """
                            dialysis_outcome_primary_care="1"
                            OR dialysis_outcome_icd_10="1"
                            OR dialysis_outcome_opcs_4="1"
                            OR kt_outcome_primary_care="1"
                            OR kt_outcome_icd_10="1"
                            OR kt_outcome_opcs_4="1"
                            """,
            "Unchanged":    "DEFAULT",
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "New KRT": 0.10,
                    "Unchanged": 0.90,
                }
            },
        },
    ),    
    dialysis_outcome_primary_care_date=patients.with_these_clinical_events(
        dialysis_codes,
        between = ["index_date", "index_date + 364 days"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 364 days"}}
    ),
    dialysis_outcome_icd_10_date=patients.admitted_to_hospital(
        with_these_diagnoses=dialysis_icd_10_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["index_date", "index_date + 364 days"],
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 364 days"}}
    ),
    dialysis_outcome_opcs_4_date=patients.admitted_to_hospital(
        with_these_procedures=dialysis_opcs_4_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["index_date", "index_date + 364 days"],
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 364 days"}}
    ),
    dialysis_outcome_date=patients.maximum_of(
        "dialysis_outcome_primary_care_date", "dialysis_outcome_icd_10_date", "dialysis_outcome_opcs_4_date",
    ),
    kt_outcome_primary_care_date=patients.with_these_clinical_events(
        kidney_transplant_codes,
        between = ["index_date", "index_date + 364 days"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 364 days"}}
    ),
    kt_outcome_icd_10_date=patients.admitted_to_hospital(
        with_these_diagnoses=kidney_transplant_icd_10_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["index_date", "index_date + 364 days"],
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 364 days"}}
    ),
    kt_outcome_opcs_4_date=patients.admitted_to_hospital(
        with_these_procedures=kidney_transplant_opcs_4_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["index_date", "index_date + 364 days"],
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "index_date", "latest": "index_date + 364 days"}}
    ),
    kidney_transplant_outcome_date=patients.maximum_of(
        "kt_outcome_primary_care_date", "kt_outcome_icd_10_date", "kt_outcome_opcs_4_date",
    ),
    modality_outcome_date=patients.maximum_of(
        "dialysis_outcome_date", "kidney_transplant_outcome_date",
    ),
    died=patients.with_death_recorded_in_primary_care(
        between = ["index_date", "index_date + 364 days"],
        returning="binary_flag",
        return_expectations={"incidence": 0.10},
    ),
    modality_outcome=patients.categorised_as(
        {
            "Deceased":             """
                                    died="1"
                                    """,
            "Dialysis":             """
                                    modality_outcome_date=dialysis_outcome_date
                                    AND modality_outcome_date!=kidney_transplant_outcome_date
                                    AND NOT died="1"
                                    """,
            "Kidney transplant":    """
                                    modality_outcome_date=kidney_transplant_outcome_date
                                    AND modality_outcome_date!=dialysis_outcome_date
                                    AND NOT died="1"
                                    """,
            "Modality unclear":     """
                                    modality_outcome_date=dialysis_outcome_date
                                    AND modality_outcome_date=kidney_transplant_outcome_date
                                    AND NOT died="1"
                                    """,
            "Unchanged":            "DEFAULT",

        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "Deceased": 0.10,
                    "Dialysis": 0.05,
                    "Kidney transplant": 0.04,
                    "Modality unclear": 0.01,
                    "Unchanged": 0.80,
                }
            },
        },
    ),

    cardiovascular=patients.admitted_to_hospital(
        with_these_diagnoses=cardiovascular_codes,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

) 