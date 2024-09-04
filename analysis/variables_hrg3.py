
from cohortextractor import filter_codes_by_category, patients, combine_codelists
from codelists import *
from datetime import datetime, timedelta

def generate_variables_hrg3(index_date_variable):
    variables_hrg3 = dict(    
    
    MB05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MB05_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    MB08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MB08_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    MB09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MB09_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    NZ16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ16_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    NZ17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ17_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    NZ18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ18_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    NZ19_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ19_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ19,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    NZ20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ20_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    NZ25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ25_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    NZ26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ26_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA01_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA02_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA03_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA04_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA05_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA06_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA07_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA08_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA09_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA11_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA12_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA17_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA24_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA25_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA30_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA31_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA32_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA35_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA35_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA35,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA36_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA36_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA36,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    SA37_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA37_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA37,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    UZ01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ01_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    UZ02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ02_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    UZ03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ03_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    UZ04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ04_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    UZ15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ15_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    VA10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VA10_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VA10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WD01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD01_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WD02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD02_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WD03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD03_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WD04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD04_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WD05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD05_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WD06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD06_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WD07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD07_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WD08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD08_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WD09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD09_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH01_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH02_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH03_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH04_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH05_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH06_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH07_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH08_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH09_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH10_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH11_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH12_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH13_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH14_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH15_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH16_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH17_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH18_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH19_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH19_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH19,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH20_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH21_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH22_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH23_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH50_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH51_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH52_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH53_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WH99_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH99,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH99_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH99,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WJ01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ01_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WJ02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ02_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WJ03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ03_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WJ04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ04_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WJ06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ06_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WJ07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ07_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    WJ10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ10_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    ),
    
    LB74_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB74,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB74_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB74,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB75_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB75,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB75_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB75,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB76_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB76,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB76_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB76,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB77_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB77,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB77_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB77,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB78_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB78,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB78_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LB78,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LE01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LE01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LE01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LE01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LE02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_LE02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LE02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_LE02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA07_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA23_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA23_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA25_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA25_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA29_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA29_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA29,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA35_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA35_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA35,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA36_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA36_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA36,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA38_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA38_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA38,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA44_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA44_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA44,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA48_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA48_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA48,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA52_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA56_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA56_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MA56,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC07_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_MC21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ27_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ27_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ27,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ71_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ71_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ71,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ72_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ72,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ72_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_NZ72,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD47_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD47_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD47,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD48_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD48_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD48,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD60_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD60_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD60,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD61_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD61_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RD61,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN07_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN17_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN17_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN18_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN18_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN19_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN19_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN19,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN23_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN23_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN25_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN25_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN27_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN27_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN27,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN28_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN28_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN29_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN29_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN29,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN31_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN31_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN31,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN34_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN34_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN34,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN50_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN52_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_RN52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA18_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA18_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA19_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA19_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA19,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA21_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA21_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA21,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA23_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA23_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA23,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA27_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA27_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA27,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA33_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA43_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA44_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA44_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA44,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA45_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SA45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB06_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB07_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB09_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB11_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB13_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB15_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB17_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB17_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SB17,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC25_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC25_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC25,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC28_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC28_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC29_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC29_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC29,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC44_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC44_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC44,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC45_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC47_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC47_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC47,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC49_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC49,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC49_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC49,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC51_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC51_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC53_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC53_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC53,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC55_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC55_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC55,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC56_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC56_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC56,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC57_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC57_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_SC57,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    UZ05_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_UZ05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_UZ05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    UZ06_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_UZ06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_UZ06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC03_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC03_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC03,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC04_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC06_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC08_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC10_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC12_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC14_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC16_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC18_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC18_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC20_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC22_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC24_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC26_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC28_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC28_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC30_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC32_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC34_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC34_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC34,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC36_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC36_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC36,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC38_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC38_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC38,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC40_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC42_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_VC42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WF01_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_WF01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WF01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_WF01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WF02_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_WF02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WF02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_WF02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH54_count=patients.admitted_to_hospital(
        with_these_procedures=hrg_WH54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_WH54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    )
    return variables_hrg3
    