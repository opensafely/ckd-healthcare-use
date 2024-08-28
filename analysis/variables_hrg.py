from cohortextractor import filter_codes_by_category, patients, combine_codelists
from codelists import *
from datetime import datetime, timedelta

def generate_variables_hrg(index_date_variable):
    variables_hrg = dict(    

    FD01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
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
    
    GC17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
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
    
    DZ10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WJ01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ01,
        returning="total_bed_days_in_period",
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

    DZ51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WJ06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WJ03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ03,
        returning="total_bed_days_in_period",
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

    DZ14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    UZ03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WJ02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ02,
        returning="total_bed_days_in_period",
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

    CB02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CB02,
        returning="total_bed_days_in_period",
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

    DZ22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ22,
        returning="total_bed_days_in_period",
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

    EB14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB14,
        returning="total_bed_days_in_period",
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

    DZ11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WJ04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ04,
        returning="total_bed_days_in_period",
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

    BZ24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ24,
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

    LA04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA04,
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

    HD25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WD02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD02,
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

    JD07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JD07,
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

    GC01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WJ10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ10,
        returning="total_bed_days_in_period",
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

    EB02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    UZ01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ01,
        returning="total_bed_days_in_period",
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

    CB01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CB01,
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

    FD11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD11,
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

    GC12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA08,
        returning="total_bed_days_in_period",
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

    DZ17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ17,
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

    HD40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD40,
        returning="total_bed_days_in_period",
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

    AA24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA24,
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

    HC30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC30,
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

    JA12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MB05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MB05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB05,
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

    LB58_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB58,
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

    LB06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB06,
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

    LB35_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB35,
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

    KA06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA17,
        returning="total_bed_days_in_period",
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

    DZ16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MB09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MB09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    UZ02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ02,
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

    FD10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD10,
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

    HD24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD24,
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

    HD21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD21,
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

    LB28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WJ11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
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
    
    SA04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA36_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA36_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA37_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA37_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA37,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA03,
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

    LA07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA35_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA35_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA35,
        returning="total_bed_days_in_period",
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

    DZ29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ29,
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

    KA07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA07,
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

    KB02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB02,
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

    LA09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA09,
        returning="total_bed_days_in_period",
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

    AA26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA26,
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

    KB03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB03,
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

    KA08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA08,
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

    KA05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA05,
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

    KC05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KC05,
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

    FD04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD04,
        returning="total_bed_days_in_period",
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

    DZ27_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ27,
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

    KC04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KC04,
        returning="total_bed_days_in_period",
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

    AA25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA25,
        returning="total_bed_days_in_period",
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

    DZ13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WD09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WD01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WD08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WD07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WD06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WD05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WD04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WD03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WD03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WD03,
        returning="total_bed_days_in_period",
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

    AA28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA28,
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

    HC28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC28,
        returning="total_bed_days_in_period",
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

    AA30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA30,
        returning="total_bed_days_in_period",
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

    AA31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA31,
        returning="total_bed_days_in_period",
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

    AA29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA29,
        returning="total_bed_days_in_period",
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

    AA43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA43,
        returning="total_bed_days_in_period",
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

    DZ18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ18,
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

    HD23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD23,
        returning="total_bed_days_in_period",
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

    EB06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB06,
        returning="total_bed_days_in_period",
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

    EB04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB04,
        returning="total_bed_days_in_period",
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

    EB03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB03,
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

    LA08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA08,
        returning="total_bed_days_in_period",
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

    EB13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB13,
        returning="total_bed_days_in_period",
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

    EB10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB10,
        returning="total_bed_days_in_period",
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

    DZ09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ09,
        returning="total_bed_days_in_period",
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

    EB15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB15,
        returning="total_bed_days_in_period",
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

    EB07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB07,
        returning="total_bed_days_in_period",
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

    EB05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB05,
        returning="total_bed_days_in_period",
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

    AA23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA23,
        returning="total_bed_days_in_period",
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

    AA35_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA35,
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

    YQ51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ51,
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

    FD03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD03,
        returning="total_bed_days_in_period",
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

    EB08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB08,
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

    JA13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA13,
        returning="total_bed_days_in_period",
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

    DZ23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ23,
        returning="total_bed_days_in_period",
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

    DZ65_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ65,
        returning="total_bed_days_in_period",
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

    DZ15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ15,
        returning="total_bed_days_in_period",
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

    DZ12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ12,
        returning="total_bed_days_in_period",
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

    DZ25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ25,
        returning="total_bed_days_in_period",
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

    DZ24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ24,
        returning="total_bed_days_in_period",
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

    DZ20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ20,
        returning="total_bed_days_in_period",
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

    DZ26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ26,
        returning="total_bed_days_in_period",
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

    DZ19_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ19,
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

    FD02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    UZ04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ04,
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

    HD26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD26,
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

    HC27_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC27,
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

    HC29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC29,
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

    HC31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC31,
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

    HC20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC20,
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

    HC32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC32,
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

    HD39_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HD39,
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

    LB40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB40,
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

    LB19_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB19,
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

    LB57_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB57,
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

    LB37_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB37,
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

    LB16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MB08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MB08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MB08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ19_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ19_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ19,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ17,
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

    HC21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC21,
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

    HE52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH15,
        returning="total_bed_days_in_period",
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

    EB09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB09,
        returning="total_bed_days_in_period",
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

    DZ28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ28,
        returning="total_bed_days_in_period",
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

    EB12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EB12,
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

    FD05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FD05,
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

    GC18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GC18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH09,
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

    LB38_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WJ07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WJ07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH17,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH13,
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

    HE72_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE72,
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

    HE71_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE71,
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

    HE42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE42,
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

    HE12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE12,
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

    HE22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE22,
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

    HE32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE32,
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

    HE51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE51,
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

    HE83_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE83,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    UZ15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ15,
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

    JB91_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JB91,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH07,
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

    LB20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB20,
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

    HE82_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE82,
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

    HE81_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE81,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH01,
        returning="total_bed_days_in_period",
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

    DX21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DX21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH19_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH19_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH19,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH99_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH99,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH99_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH99,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH20,
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

    HE41_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE41,
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

    HE21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE21,
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

    HE31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HE31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA71_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA71_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    UZ06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA60_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA60_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA55_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA55_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA83_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA83,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA83_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA83,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA57_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA57_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA57,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ84_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ84,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ84_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ84,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC70_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC70_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC70,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC71_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC71_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA61_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA61_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA61,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC72_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC72,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC72_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC72,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN93_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN93,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN93_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN93,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN35_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN35_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN35,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN45_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN45_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA38_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA38_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ86_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ86,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ86_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ86,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YC01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YC01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YC01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YC01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YC10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YC10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YC10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YC10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ63_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ63_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ64_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ64_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ64,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KA04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KA04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA38_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA38_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA45_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA45_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YJ13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YJ13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YJ13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YJ13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YJ09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YJ09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YJ09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YJ09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YJ11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YJ11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YJ11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YJ11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YJ15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YJ15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YJ15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YJ15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA34_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA34_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JA30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JA30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JA30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ56_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ56_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ45_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ45_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ41_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ41_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ46_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ46_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ44_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ44_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN34_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN34_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ57_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ57_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ57,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN65_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN65_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ72_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ72,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ72_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ72,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ73_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ73,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ73_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ73,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ63_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ63_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ62_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ62_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ62,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ64_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ64_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ64,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ60_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ60_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ61_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ61_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ61,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN64_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN64_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN64,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ65_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ65_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ92_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ92,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ92_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ92,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ81_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ81,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ81_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ81,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ93_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ93,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ93_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ93,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ95_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ95,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ95_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ95,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ94_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ94,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ94_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ94,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ91_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ91,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ91_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ91,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ83_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ83,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ83_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ83,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ80_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ80,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ80_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ80,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ87_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ87,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ87_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ87,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ89_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ89,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ89_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ89,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ88_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ88,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ88_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ88,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA34_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA34_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA55_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA55_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA36_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA36_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA39_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA39,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA39_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA39,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA35_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA35_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA35,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA29_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA29,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA27_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA27_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA27,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA81_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA81,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA81_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA81,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA62_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA62_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA62,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA86_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA86,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA86_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA86,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA84_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA84,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA84_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA84,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA68_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA68,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA68_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA68,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA67_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA67,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA67_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA67,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA71_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA71_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA69_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA69,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA69_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA69,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA83_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA83,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA83_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA83,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA82_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA82,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA82_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA82,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA85_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA85,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA85_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA85,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ67_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ67,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ67_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ67,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ68_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ68,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ68_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ68,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ69_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ69,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ69_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ69,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ70_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ70_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ70,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ37_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ37_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ37,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ38_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ38_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ60_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ60_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ57_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ57_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ57,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ56_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ56_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ58_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ58,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ58_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ58,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ59_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ59,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ59_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ59,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ45_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ45_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ46_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ46_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ55_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ55_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ36_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ36_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ49_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ49,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ49_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ49,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA66_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA66,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA66_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA66,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA65_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA65_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA64_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA64_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA64,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA60_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA60_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    BZ74_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ74,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    BZ74_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_BZ74,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    UZ05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    UZ05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_UZ05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA70_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA70_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA70,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YF01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YF01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YF01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YF01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF37_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF37_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF37,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF34_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF34_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF36_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF36_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE34_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE34_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE35_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE35_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE35,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE36_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE36_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA80_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA80,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA80_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA80,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF41_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF41_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR57_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR57_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR57,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA63_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA63_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GB11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GB11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GB11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YG02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YG02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YG02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ71_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ71_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED27_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED27_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED27,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY41_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY41_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY17,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CD01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CD01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CD01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA93_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA93,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA93_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA93,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA92_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA92,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA92_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA92,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR67_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR67,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR67_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR67,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR63_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR63_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ41_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ41_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR48_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR48_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR48,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB47_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB47_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB47,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR44_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR44_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR41_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR41_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR45_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR45_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB60_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB60_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB61_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB61_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB61,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB65_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB65_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB64_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB64_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB64,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB75_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB75,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB75_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB75,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB36_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB36_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB39_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB39,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB39_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB39,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB68_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB68,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB68_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB68,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB72_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB72,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB72_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB72,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB17,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB59_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB59,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB59_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB59,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB55_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB55_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB70_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB70_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB70,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB78_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB78,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB78_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB78,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB77_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB77,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB77_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB77,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB76_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB76,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB76_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB76,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YL30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YL30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YL30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB29_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB29,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR56_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR56_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB56_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB56_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB48_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB48_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB48,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB74_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB74,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB74_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB74,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN86_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN86,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN86_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN86,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN81_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN81,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN81_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN81,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA38_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA38_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA35_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA35,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA35_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA35,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA56_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA56_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA44_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA44_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MC12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MC12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MC12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA36_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA36_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ71_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ71_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ72_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ72,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ72_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ72,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ27_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ27_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ27,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    NZ22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    NZ22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_NZ22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC41_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC41_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC46_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC46_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC47_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC47_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC47,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JB71_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JB71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JB71_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JB71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    GA10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    GA10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_GA10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YD02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YD02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YD02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF63_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF63_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF60_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF60_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF62_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF62_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF62,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF61_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF61_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF61,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FF50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FF50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FF50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YF04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YF04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YF04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YF04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN44_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN44_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN46_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN46_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WH54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WH54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WH54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    FE50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    FE50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_FE50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EC21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EC21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EC21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA81_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA81,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA81_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA81,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AA32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AA32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AA32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA37_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA37_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA37,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC45_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC45_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC44_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC44_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    EY11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    EY11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_EY11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA94_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA94,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA94_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA94,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA96_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA96,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA96_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA96,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA98_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA98,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA98_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA98,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA97_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA97,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA97_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA97,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA95_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA95,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA95_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA95,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC62_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC62_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC62,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC61_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC61_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC61,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC64_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC64,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC64_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC64,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC65_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC65_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC60_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC60_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    ED18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    ED18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_ED18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HC63_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HC63_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HC63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR65_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR65,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR65_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR65,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR66_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR66,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR66_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR66,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA19_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA19_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA19,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YH31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YH31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YH31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YA13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YA13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YA13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB71_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB71,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB71_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB71,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB67_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB67,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB67_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB67,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN62_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN62,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN62_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN62,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    KB04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    KB04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_KB04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA45_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA45_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA44_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA44_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA27_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA27_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA27,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA48_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA48_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA48,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LA05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LA05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LA05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LB46_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LB46_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LB46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SA18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SA18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SA18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    DZ33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    DZ33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_DZ33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WF01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WF01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WF01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WF01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    WF02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WF02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    WF02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WF02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    AB11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    AB11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_AB11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YR42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YR42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YR42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN63_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN63,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN63_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN63,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    MA29_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    MA29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_MA29,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JC40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JC40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JC40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    CA91_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA91,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    CA91_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_CA91,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    JB70_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JB70,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    JB70_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_JB70,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    HN55_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    HN55_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_HN55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    YQ26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    YQ26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB17,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SB11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SB11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SB11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD90_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD90,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD90_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD90,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD91_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD91,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD91_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD91,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD03_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD03,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD03_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD03,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD05_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD05,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD05_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD05,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD37_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD37,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD37_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD37,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD39_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD39,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD39_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD39,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD41_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD41,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD41_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD41,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD47_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD47_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD47,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD11_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD11,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD11_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD11,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD38_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD38_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD17,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD48_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD48_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD48,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD19_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD19_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD19,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD49_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD49,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD49_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD49,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD43_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD43,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD43_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD43,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD44_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD44_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD27_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD27_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD27,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD29_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD29,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD45_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD45_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD46_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD46,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD46_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD46,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD55_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD55_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD56_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD56_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD57_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD57_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD57,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD34_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD34_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    XD58_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD58,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    XD58_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_XD58,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN19_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN19,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN19_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN19,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN34_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN34_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN31_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN31,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN31_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN31,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD60_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD60,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD60_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD60,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN09_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN09,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN09_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN09,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD47_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD47_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD47,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN21_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN21,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN21_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN21,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN23_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN23,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN23_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN23,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN15_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN15,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN15_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN15,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN17_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN17,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN17_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN17,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN29_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN29,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD61_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD61,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD61_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD61,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN33_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN33,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN33_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN33,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN07_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN07,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN07_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN07,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN13_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN13,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN13_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN13,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN27_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN27,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN27_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN27,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RD48_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD48,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RD48_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RD48,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN50_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN50,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN50_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN50,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    RN52_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN52,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    RN52_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_RN52,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC44_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC44,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC44_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC44,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC45_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC45,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC45_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC45,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC47_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC47,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC47_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC47,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC49_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC49,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC49_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC49,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC51_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC51,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC51_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC51,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC56_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC56,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC56_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC56,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC53_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC53,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC53_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC53,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC54_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC54,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC54_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC54,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC55_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC55,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC55_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC55,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC57_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC57,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC57_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC57,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC25_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC25,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC25_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC25,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC29_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC29,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC29_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC29,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    SC30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    SC30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_SC30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC14_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC14,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC14_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC14,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC16_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC16,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC16_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC16,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC18_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC18,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC18_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC18,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC20_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC20,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC20_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC20,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC22_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC22,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC22_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC22,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC24_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC24,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC24_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC24,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC06_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC06,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC06_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC06,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC08_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC08,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC08_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC08,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC10_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC10,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC10_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC10,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC12_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC12,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC12_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC12,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC26_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC26,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC26_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC26,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC28_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC28,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC28_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC28,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC32_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC32,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC32_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC32,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC34_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC34,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC34_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC34,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC30_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC30,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC30_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC30,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC36_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC36,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC36_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC36,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC38_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC38,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC38_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC38,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC40_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC40,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC40_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC40,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC04_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC04,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC04_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC04,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    VC42_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC42,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    VC42_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_VC42,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LE01_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LE01,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LE01_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LE01,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    LE02_count=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LE02,
        returning="binary_flag",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={"incidence": 0.05},
    ),

    LE02_days=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_LE02,
        returning="total_bed_days_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    )
    return variables_hrg
