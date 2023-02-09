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
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    dialysis_baseline_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=dialysis_icd_10_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    dialysis_baseline_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=dialysis_opcs_4_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    kt_baseline_primary_care=patients.with_these_clinical_events(
        kidney_transplant_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    kt_baseline_icd_10=patients.admitted_to_hospital(
        with_these_diagnoses=kidney_transplant_icd_10_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    kt_baseline_opcs_4=patients.admitted_to_hospital(
        with_these_procedures=kidney_transplant_opcs_4_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
    krt_baseline=patients.categorised_as(
        {
            "KRT":      """
                        dialysis_baseline_primary_care="1"
                        OR dialysis_baseline_icd_10="1"
                        OR dialysis_baseline_opcs_4="1"
                        OR kt_baseline_primary_care="1"
                        OR kt_baseline_icd_10="1"
                        OR kt_baseline_opcs_4="1"
                        """,
            "Pre-KRT":  "DEFAULT",
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "KRT": 0.20,
                    "Pre-KRT": 0.80,
                }
            },
        },
    ),    
    dialysis_baseline_primary_care_date=patients.with_these_clinical_events(
        dialysis_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    dialysis_baseline_icd_10_date=patients.admitted_to_hospital(
        with_these_diagnoses=dialysis_icd_10_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["1970-01-01", "index_date - 1 day"],
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    dialysis_baseline_opcs_4_date=patients.admitted_to_hospital(
        with_these_procedures=dialysis_opcs_4_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["1970-01-01", "index_date - 1 day"],
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    dialysis_baseline_date=patients.maximum_of(
        "dialysis_baseline_primary_care_date", "dialysis_baseline_icd_10_date", "dialysis_baseline_opcs_4_date",
    ),
    kt_baseline_primary_care_date=patients.with_these_clinical_events(
        kidney_transplant_codes,
        between = ["1970-01-01", "index_date - 1 day"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    kt_baseline_icd_10_date=patients.admitted_to_hospital(
        with_these_diagnoses=kidney_transplant_icd_10_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["1970-01-01", "index_date - 1 day"],
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    kt_baseline_opcs_4_date=patients.admitted_to_hospital(
        with_these_procedures=kidney_transplant_opcs_4_codes,
        returning="date_admitted",
        date_format="YYYY-MM-DD",
        between = ["1970-01-01", "index_date - 1 day"],
        find_last_match_in_period=True,
        return_expectations={"incidence": 0.05, "date": {"earliest" : "1970-01-01", "latest": "index_date - 1 day"}}
    ),
    kidney_transplant_baseline_date=patients.maximum_of(
        "kt_baseline_primary_care_date", "kt_baseline_icd_10_date", "kt_baseline_opcs_4_date",
    ),
    modality_baseline_date=patients.maximum_of(
        "dialysis_baseline_date", "kidney_transplant_baseline_date",
    ),
    modality_baseline=patients.categorised_as(
        {
            "Dialysis":             """
                                    modality_baseline_date=dialysis_baseline_date
                                    AND modality_baseline_date!=kidney_transplant_baseline_date
                                    """,
            "Kidney transplant":    """
                                    modality_baseline_date=kidney_transplant_baseline_date
                                    AND modality_baseline_date!=dialysis_baseline_date
                                    """,
            "Modality unclear":     """
                                    krt_baseline="KRT"
                                    AND modality_baseline_date=dialysis_baseline_date
                                    AND modality_baseline_date=kidney_transplant_baseline_date
                                    """,
            "Pre KRT":              "DEFAULT",
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "Dialysis": 0.09,
                    "Kidney transplant": 0.09,
                    "Modality unclear": 0.02,
                    "Pre KRT": 0.80,
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
                            krt_baseline="Pre KRT"
                            AND dialysis_outcome_primary_care="1"
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
                                    AND NOT modality_baseline="Dialysis"
                                    AND NOT died="1"
                                    """,
            "Kidney transplant":    """
                                    modality_outcome_date=kidney_transplant_outcome_date
                                    AND modality_outcome_date!=dialysis_outcome_date
                                    AND NOT modality_baseline="Kidney transplant"
                                    AND NOT died="1"
                                    """,
            "Modality unclear":     """
                                    krt_baseline="Pre KRT"
                                    AND modality_outcome_date=dialysis_outcome_date
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
    m4_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m5_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m6_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m7_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m8_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m9_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m10_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m11_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m12_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m1_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m2_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m3_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m4_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m5_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m6_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m7_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m8_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m9_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m10_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m11_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m12_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m1_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m2_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m3_admitted_patients=patients.admitted_to_hospital(
        returning="binary_flag",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m4_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={"incidence": 0.02},
    ),
    m5_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={"incidence": 0.02},
    ),
    m6_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={"incidence": 0.02},
    ),
    m7_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={"incidence": 0.02},
    ),
    m8_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={"incidence": 0.02},
    ),
    m9_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.02},
    ),
    m10_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={"incidence": 0.02},
    ),
    m11_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={"incidence": 0.02},
    ),
    m12_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.02},
    ),
    m1_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={"incidence": 0.02},
    ),
    m2_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={"incidence": 0.02},
    ),
    m3_fistula_formation=patients.admitted_to_hospital(
        with_these_procedures=avf_formation_codes,
        returning="binary_flag",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.02},
    ),
    m4_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={"incidence": 0.02},
    ),
    m5_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={"incidence": 0.02},
    ),
    m6_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={"incidence": 0.02},
    ),
    m7_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={"incidence": 0.02},
    ),
    m8_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={"incidence": 0.02},
    ),
    m9_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.02},
    ),
    m10_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={"incidence": 0.02},
    ),
    m11_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={"incidence": 0.02},
    ),
    m12_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.02},
    ),
    m1_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={"incidence": 0.02},
    ),
    m2_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={"incidence": 0.02},
    ),
    m3_pd_insertion=patients.admitted_to_hospital(
        with_these_procedures=pd_insertion_codes,
        returning="binary_flag",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.02},
    ),
    m4_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m5_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m6_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m7_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m8_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m9_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m10_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m11_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m12_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m1_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m2_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m3_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m4_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date", "index_date + 29 days"],
        return_expectations={"incidence": 0.10},
    ),
    m5_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={"incidence": 0.10},
    ),
    m6_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={"incidence": 0.10},
    ),
    m7_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={"incidence": 0.10},
    ),
    m8_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={"incidence": 0.10},
    ),
    m9_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.10},
    ),
    m10_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={"incidence": 0.10},
    ),
    m11_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={"incidence": 0.10},
    ),
    m12_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.10},
    ),
    m1_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={"incidence": 0.10},
    ),
    m2_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={"incidence": 0.10},
    ),
    m3_critical_care_patients=patients.admitted_to_hospital(
        with_at_least_one_day_in_critical_care=True,
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.10},
    ),
    m4_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m5_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m6_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m7_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m8_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m9_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m10_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m11_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m12_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m1_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m2_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m3_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m4_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={"incidence": 0.10},
    ),
    m5_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={"incidence": 0.10},
    ),
    m6_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={"incidence": 0.10},
    ),
    m7_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={"incidence": 0.10},
    ),
    m8_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={"incidence": 0.10},
    ),
    m9_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.10},
    ),
    m10_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={"incidence": 0.10},
    ),
    m11_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={"incidence": 0.10},
    ),
    m12_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.10},
    ),
    m1_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={"incidence": 0.10},
    ),
    m2_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={"incidence": 0.10},
    ),
    m3_emergency_patients=patients.attended_emergency_care(
        returning="binary_flag",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.10},
    ),
    m4_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m5_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m6_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m7_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m8_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m9_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m10_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m11_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m12_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m1_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m2_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m3_op_appts=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m4_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m5_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m6_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m7_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m8_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m9_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m10_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m11_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m12_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m1_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m2_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m3_neph_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m4_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m5_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m6_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m7_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m8_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m9_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m10_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m11_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m12_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m1_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m2_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m3_tx_appts=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m4_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m5_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m6_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m7_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m8_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m9_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m10_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m11_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m12_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m1_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m2_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m3_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    m4_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={"incidence": 0.30},
    ),
    m5_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={"incidence": 0.30},
    ),
    m6_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={"incidence": 0.30},
    ),
    m7_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={"incidence": 0.30},
    ),
    m8_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={"incidence": 0.30},
    ),
    m9_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.30},
    ),
    m10_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={"incidence": 0.30},
    ),
    m11_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={"incidence": 0.30},
    ),
    m12_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.30},
    ),
    m1_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={"incidence": 0.30},
    ),
    m2_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={"incidence": 0.30},
    ),
    m3_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.30},
    ),
    m4_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={"incidence": 0.05},
    ),
    m5_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={"incidence": 0.05},
    ),
    m6_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={"incidence": 0.05},
    ),
    m7_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={"incidence": 0.05},
    ),
    m8_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={"incidence": 0.05},
    ),
    m9_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.05},
    ),
    m10_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={"incidence": 0.05},
    ),
    m11_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={"incidence": 0.05},
    ),
    m12_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.05},
    ),
    m1_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={"incidence": 0.05},
    ),
    m2_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={"incidence": 0.05},
    ),
    m3_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),
    m4_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date", "index_date + 29 days"],
        return_expectations={"incidence": 0.20},
    ),
    m5_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 30 days", "index_date + 60 days"],
        return_expectations={"incidence": 0.20},
    ),
    m6_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 61 days", "index_date + 90 days"],
        return_expectations={"incidence": 0.20},
    ),
    m7_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 121 days"],
        return_expectations={"incidence": 0.20},
    ),
    m8_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 122 days", "index_date + 152 days"],
        return_expectations={"incidence": 0.20},
    ),
    m9_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 153 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.20},
    ),
    m10_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 213 days"],
        return_expectations={"incidence": 0.20},
    ),
    m11_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 214 days", "index_date + 243 days"],
        return_expectations={"incidence": 0.20},
    ),
    m12_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 244 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.20},
    ),
    m1_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 305 days"],
        return_expectations={"incidence": 0.20},
    ),
    m2_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 306 days", "index_date + 333 days"],
        return_expectations={"incidence": 0.20},
    ),
    m3_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date + 334 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.20},
    ),
    )
    return variables_additional
