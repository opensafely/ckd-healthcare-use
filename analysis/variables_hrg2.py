from cohortextractor import filter_codes_by_category, patients, combine_codelists
from codelists import *
from datetime import datetime, timedelta

def generate_variables_hrg2(index_date_variable):
    variables_hrg2 = dict(    
    
    FD01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FD01_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FD01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FD02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FD02_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FD02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FD03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FD03_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FD03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FD04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FD04_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FD04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FD05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FD05_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FD05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FD10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FD10_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FD10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FD11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FD11_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FD11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GC01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GC01_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GC01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GC12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GC12_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GC12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GC17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GC17_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GC17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC17,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GC18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GC18_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GC18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC20_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC21_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC26_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC27_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC27_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC27,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC27_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC27,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC28_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC29_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC29_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC29,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC29,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC30_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC31_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC32_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HD21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HD21_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HD21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HD23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HD23_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HD23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HD24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HD24_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HD24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HD25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HD25_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HD25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HD26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HD26_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HD26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HD39_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD39,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HD39_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD39,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HD39_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD39,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HD40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HD40_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HD40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE11_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE12_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE21_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE22_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE31_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE32_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE41_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE41_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE41_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE42_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE51_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE52_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE71_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE71_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE71,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE71_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE72_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE72,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE72_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE72,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE72_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE72,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE81_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE81,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE81_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE81,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE81_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE81,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE82_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE82,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE82_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE82,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE82_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE82,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HE83_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE83,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HE83_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE83,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HE83_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE83,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA12_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JA12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA13_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JA13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JB91_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JB91,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JB91_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JB91,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JB91_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JB91,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JD07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JD07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JD07_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JD07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JD07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JD07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA05_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KA05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA06_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KA06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA07_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KA07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA08_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KA08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KB02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KB02_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KB02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KB03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KB03_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KB03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KC04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KC04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KC04_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KC04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KC04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KC04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KC05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KC05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KC05_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KC05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KC05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KC05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA04_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA07_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA08_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA09_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB06_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB16_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB19_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB19_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB19,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB19_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB19,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB20_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB28_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB35_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB35_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB35,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB35_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB35,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB37_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB37_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB37,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB37_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB37,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB38_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB38_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB38,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB38_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB40_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB57_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB57_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB57,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB57_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB57,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB58_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB58,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB58_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB58,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB58_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB58,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY22_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY23_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY23_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY23_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY30_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY31_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY32_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY40_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY41_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY41_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY41_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY42_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY43_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY50_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    EY51_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE01_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE02_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE03_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE20_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE21_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE22_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE30_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE31_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE32_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE33_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE34_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE34_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE34,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE34_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE35_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE35_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE35,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE35_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE35,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE36_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE36_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE36,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE36_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FE50_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FE50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF01_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF02_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF04_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF05_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF14_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF20_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF21_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF22_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF30_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF31_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF32_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF33_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF34_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF34_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF34,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF34_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF36_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF36_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF36,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF36_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF37_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF37_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF37,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF37_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF37,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF40_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF41_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF41_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF41_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF42_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF43_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF50_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF51_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF52_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF52_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF53_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF60_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF60_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF60,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF60_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF61_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF61_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF61,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF61_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF61,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF62_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF62_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF62,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF62_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF62,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF63_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF63_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF63,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    FF63_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_FF63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA03_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA04_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA05_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA06_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA06_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA07_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA07_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA15_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GA16_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GA16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GB05_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB06_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GB06_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GB09_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GB10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GB11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GB12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    GB13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_GB13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC50_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC53_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC54_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC60_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC60_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC60,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC60_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC61_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC61_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC61,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC61_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC61,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC62_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC62_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC62,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC62_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC62,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC63_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC63_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC63,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC63_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC64_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC64_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC64,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC64_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC64,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC65_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC65_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC65,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC65_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC70_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC70_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC70,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC70_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC70,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC71_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC71_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC71,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC71_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC72_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC72,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC72_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC72,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HC72_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HC72,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN14_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN15_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN22_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN23_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN23_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN23_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN24_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN25_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN25_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN25_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN32_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN33_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN34_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN34_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN34,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN34_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN35_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN35_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN35,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN35_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN35,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN42_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN43_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN44_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN44_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN44,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN44_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN45_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN45_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN46_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN46_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN46,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN46_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN52_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN52_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN53_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN54_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN55_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN55_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN55,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN55_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN62_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN62_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN62,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN62_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN62,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN63_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN63_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN63,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN63_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN64_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN64_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN64,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN64_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN64,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN65_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN65_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN65,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN65_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN81_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN81,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN81_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN81,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN81_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN81,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN86_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN86,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN86_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN86,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN86_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN86,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN93_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN93,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN93_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN93,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    HN93_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_HN93,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JA20_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JA30_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA34_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA34_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA34,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JA34_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA38_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA38_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA38,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JA38_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JA43_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA45_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JA45_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JA45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JB70_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JB70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JB70_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JB70,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JB70_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JB70,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JB71_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JB71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JB71_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JB71,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JB71_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JB71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JC40_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC41_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC41_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JC41_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JC42_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JC43_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC44_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC44_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC44,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JC44_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC45_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JC45_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC46_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC46_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC46,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JC46_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC47_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC47_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC47,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    JC47_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_JC47,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_KA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_KA03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KA03_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_KA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_KA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_KA04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KA04_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_KA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_KA09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_KA09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KA09_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_KA09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KB04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_KB04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KB04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_KB04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    KB04_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_KB04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA01_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA02_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA03_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA05_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA11_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LA14_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LA14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB09_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB10_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB12_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB13_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB14_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB15_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB17_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB17_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB17_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB17,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB18_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB18_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB18_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB21_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB25_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB25_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB25_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB26_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB29_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB29_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB29,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB29_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB29,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB33_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB36_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB36_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB36,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB36_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB39_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB39,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB39_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB39,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB39_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB39,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB42_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB43_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB46_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB46_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB46,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB46_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB47_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB47_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB47,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB47_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB47,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB48_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB48_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB48,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB48_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB48,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB50_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB51_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB52_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB52_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB53_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB54_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB55_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB55_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB55,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB55_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB56_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB56_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB56,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB56_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB59_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB59,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB59_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB59,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB59_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB59,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB60_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB60_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB60,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB60_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB61_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB61_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB61,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB61_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB61,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB64_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB64_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB64,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB64_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB64,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB65_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB65_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB65,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB65_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB67_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB67,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB67_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB67,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB67_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB67,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB68_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB68,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB68_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB68,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB68_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB68,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB70_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB70_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB70,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB70_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB70,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB71_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB71_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB71,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB71_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB72_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB72,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB72_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB72,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),

    LB72_days=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB72,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    )
    return variables_hrg2
    