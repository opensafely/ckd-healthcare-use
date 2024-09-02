from cohortextractor import filter_codes_by_category, patients, combine_codelists
from codelists import *
from datetime import datetime, timedelta

def generate_variables_hrg4(index_date_variable):
    variables_hrg4 = dict(    
    
    WJ11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ11_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    WJ11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ50_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ51_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD01_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD02_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD03_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD04_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD05_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD06_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD06_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD07_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD07_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD08_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD09_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD14_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD15_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD16_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD17_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD17_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD17_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD17,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD18_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD18_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD18_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD19_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD19_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD19,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD19_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD19,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD20_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD21_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD22_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD23_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD23_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD23_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD24_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD25_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD25_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD25_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD26_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD27_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD27_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD27,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD27_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD27,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD28_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD28_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD28_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD29_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD29_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD29,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD29_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD29,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD30_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD31_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD32_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD33_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD34_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD34_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD34,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD34_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD37_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD37_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD37,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD37_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD37,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD38_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD38_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD38,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD38_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD39_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD39,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD39_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD39,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD39_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD39,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD40_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD41_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD41_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD41_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD42_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD43_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD44_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD44_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD44,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD44_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD45_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD45_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD46_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD46_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD46,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD46_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD47_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD47_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD47,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD47_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD47,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD48_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD48_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD48,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD48_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD48,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD49_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD49,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD49_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD49,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD49_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD49,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD50_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD51_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD52_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD52_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD53_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD54_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD55_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD55_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD55,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD55_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD56_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD56_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD56,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD56_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD57_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD57_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD57,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD57_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD57,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD58_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD58,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD58_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD58,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD58_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD58,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD90_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD90,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD90_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD90,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD90_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD90,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD91_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD91,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD91_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD91,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    XD91_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD91,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YA03_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YA04_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YA10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YA11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YA12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YA13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YC01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YC01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YC01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YC01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YC01_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YC01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YC10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YC10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YC10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YC10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YC10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YC10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YD01_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YD02_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YD03_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YD04_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YD05_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YF01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YF01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YF01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YF01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YF01_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YF01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YF04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YF04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YF04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YF04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YF04_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YF04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YG01_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YG02_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YG05_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG06_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YG06_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG07_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YG07_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YG10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YG11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YG12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YH02_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YH03_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YH10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YH20_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YH30_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YH31_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YH32_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YJ09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YJ09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YJ09_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YJ11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YJ11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YJ11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YJ13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YJ13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YJ13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YJ15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YJ15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YJ15_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YL02_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YL11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YL12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YL20_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YL21_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YL30_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ05_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ07_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ07_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ08_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ09_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ15_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ16_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ22_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ26_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ31_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ32_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ40_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ41_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ41_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ41_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YQ42_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR15_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR16_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR22_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR23_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR23_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR23_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR24_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR25_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR25_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR25_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR26_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR31_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR33_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR40_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR41_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR41_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR41_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR42_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR43_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR44_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR44_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR44,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR44_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR45_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR45_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR48_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR48_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR48,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR48_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR48,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR50_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR51_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR52_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR52_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR53_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR54_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR56_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR56_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR56,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR56_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR57_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR57_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR57,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR57_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR57,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR63_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR63_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR63,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR63_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR65_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR65_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR65,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR65_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR66_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR66,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR66_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR66,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR66_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR66,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR67_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR67,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR67_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR67,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    YR67_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR67,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    )
    return variables_hrg4
    