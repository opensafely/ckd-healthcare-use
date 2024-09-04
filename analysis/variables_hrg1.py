
from cohortextractor import filter_codes_by_category, patients, combine_codelists
from codelists import *
from datetime import datetime, timedelta

def generate_variables_hrg1(index_date_variable):
    variables_hrg1 = dict(    
    
    AA22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA22_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA23_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA24_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA25_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA26_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA28_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA29_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA29_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA29,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA30_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA31_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA35_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA35_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA35,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA43_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ24_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CB01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CB01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CB01_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CB01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CB02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CB02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CB02_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CB02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DX21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DX21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DX21_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DX21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ09_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ10_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ11_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ12_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ13_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ14_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ15_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ16_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ17_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ18_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ19_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ19_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ19,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ20_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ22_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ23_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ24_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ25_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ26_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ27_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ27_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ27,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ28_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ29_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ29_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ29,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ51_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ65_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ65_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ65,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB02_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB03_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB04_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB05_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB06_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB07_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB08_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB09_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB10_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB12_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB13_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB14_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EB15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EB15_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA52_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA55_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA55_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA55,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA57_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA57_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA57,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA60_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA60_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA60,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA61_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA61_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA61,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA71_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA71_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA71,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA81_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA81,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA81_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA81,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA83_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA83,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA83_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AA83,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB18_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB18_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB23_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB23_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_AB26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ41_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ41_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ44_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ44_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ44,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ45_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ46_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ46_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ46,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ56_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ56_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ56,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ57_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ57_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ57,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ60_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ60_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ60,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ61_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ61_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ61,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ62_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ62_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ62,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ63_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ63_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ63,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ64_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ64_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ64,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ65_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ65_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ65,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ72_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ72,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ72_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ72,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ73_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ73,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ73_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ73,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ74_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ74,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ74_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ74,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ80_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ80,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ80_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ80,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ81_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ81,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ81_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ81,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ83_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ83,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ83_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ83,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ84_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ84,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ84_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ84,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ86_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ86,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ86_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ86,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ87_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ87,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ87_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ87,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ88_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ88,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ88_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ88,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ89_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ89,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ89_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ89,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ91_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ91,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ91_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ91,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ92_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ92,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ92_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ92,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ93_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ93,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ93_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ93,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ94_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ94,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ94_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ94,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ95_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ95,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ95_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_BZ95,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA23_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA23_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA25_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA25_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA27_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA27_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA27,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA28_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA28_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA29_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA29_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA29,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA34_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA34_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA34,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA35_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA35_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA35,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA36_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA36_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA36,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA37_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA37_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA37,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA38_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA38_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA38,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA39_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA39,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA39_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA39,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA52_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA55_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA55_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA55,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA60_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA60_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA60,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA62_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA62_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA62,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA63_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA63_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA63,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA64_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA64_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA64,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA65_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA65_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA65,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA66_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA66,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA66_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA66,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA67_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA67,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA67_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA67,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA68_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA68,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA68_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA68,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA69_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA69,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA69_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA69,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA70_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA70_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA70,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA71_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA71_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA71,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA80_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA80,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA80_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA80,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA81_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA81,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA81_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA81,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA82_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA82,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA82_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA82,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA83_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA83,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA83_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA83,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA84_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA84,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA84_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA84,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA85_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA85,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA85_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA85,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA86_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA86,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA86_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA86,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA91_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA91,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA91_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA91,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA92_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA92,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA92_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA92,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA93_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA93,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA93_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA93,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA94_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA94,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA94_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA94,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA95_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA95,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA95_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA95,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA96_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA96,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA96_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA96,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA97_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA97,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA97_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA97,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA98_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA98,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA98_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CA98,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD06_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD07_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_CD12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ36_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ36_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ36,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ37_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ37_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ37,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ38_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ38_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ38,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ45_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ46_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ46_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ46,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ49_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ49,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ49_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ49,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ55_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ55_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ55,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ56_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ56_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ56,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ57_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ57_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ57,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ58_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ58,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ58_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ58,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ59_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ59,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ59_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ59,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ60_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ60_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ60,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ63_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ63_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ63,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ64_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ64_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ64,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ67_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ67,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ67_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ67,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ68_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ68,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ68_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ68,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ69_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ69,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ69_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ69,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ70_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ70_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ70,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ71_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ71_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_DZ71,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EC21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED18_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED18_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED25_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED25_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED27_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED27_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED27,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED28_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED28_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_ED31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY06_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY17_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY17_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_EY17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    )
    return variables_hrg1
    