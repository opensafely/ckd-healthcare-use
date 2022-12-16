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
    q1_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q2_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q3_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q4_hospital_days=patients.admitted_to_hospital(
        returning="total_bed_days_in_period",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q1_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q2_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q3_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q4_critical_care_days=patients.admitted_to_hospital(
        returning="total_critical_care_days_in_period",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q1_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q2_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q3_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q4_emergency_days=patients.attended_emergency_care(
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q1_outpatient_appointments=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q2_outpatient_appointments=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q3_outpatient_appointments=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q4_outpatient_appointments=patients.outpatient_appointment_date(
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q1_nephrology_appointments=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q2_nephrology_appointments=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q3_nephrology_appointments=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q4_nephrology_appointments=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="361",
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q1_transplant_appointments=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="102",
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q2_transplant_appointments=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="102",
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q3_transplant_appointments=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="102",
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q4_transplant_appointments=patients.outpatient_appointment_date(
        with_these_treatment_function_codes="102",
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    q1_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 5, "stddev": 3},
            "incidence": 0.80,
        }
    ),
    q2_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 5, "stddev": 3},
            "incidence": 0.80,
        }
    ),
    q3_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 5, "stddev": 3},
            "incidence": 0.80,
        }
    ),
    q4_gp_interactions=patients.with_gp_consultations(
        returning="number_of_matches_in_period",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 5, "stddev": 3},
            "incidence": 0.80,
        }
    ),
    q1_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,
        returning="binary_flag",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={"incidence": 0.30},
    ),
    q2_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,        
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.30},
    ),
    q3_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,        
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.30},
    ),
    q4_blood_pressure=patients.with_these_clinical_events(
        blood_pressure_codes,        
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.30},
    ),
    q1_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,
        returning="binary_flag",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={"incidence": 0.05},
    ),
    q2_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,        
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.05},
    ),
    q3_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,        
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.05},
    ),
    q4_albuminuria=patients.with_these_clinical_events(
        albuminuria_codes,        
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),
    q1_creatinine=patients.with_these_clinical_events(
        creatinine_codes,
        returning="binary_flag",
        between = ["index_date", "index_date + 90 days"],
        return_expectations={"incidence": 0.20},
    ),
    q2_creatinine=patients.with_these_clinical_events(
        creatinine_codes,        
        returning="binary_flag",
        between = ["index_date + 91 days", "index_date + 182 days"],
        return_expectations={"incidence": 0.20},
    ),
    q3_creatinine=patients.with_these_clinical_events(
        creatinine_codes,        
        returning="binary_flag",
        between = ["index_date + 183 days", "index_date + 274 days"],
        return_expectations={"incidence": 0.20},
    ),
    q4_creatinine=patients.with_these_clinical_events(
        creatinine_codes,        
        returning="binary_flag",
        between = ["index_date + 275 days", "index_date + 364 days"],
        return_expectations={"incidence": 0.20},
    ),
    )
    return variables_additional
