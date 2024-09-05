
from cohortextractor import filter_codes_by_category, patients, combine_codelists
from codelists import *
from datetime import datetime, timedelta

def generate_variables_hrg4(index_date_variable):
    variables_hrg4 = dict(    
    
    WJ11_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_WJ11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YQ51_admissions=patients.admitted_to_hospital(
        with_these_primary_diagnoses=hrg_YQ51,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD06_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD06,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD08_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD08,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD12_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD12,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD14_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD14,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD18_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD18,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD28_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD28,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD34_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD34,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD38_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD38,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD40_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD40,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD42_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD42,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD44_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD44,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD46_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD46,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD48_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD48,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD56_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD56,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD58_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD58,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    XD91_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_XD91,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YA04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YA11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YA13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YA13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YC10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YC10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YD02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YD04_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YD04,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YF01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YF01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YG01_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG01,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YG05_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG05,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YG07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YG11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YG11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YH02_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH02,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YH10_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH10,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YH30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YH32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YH32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YJ11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YJ15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YJ15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YL11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YL20_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL20,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YL30_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YL30,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YQ07_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ07,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YQ09_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ09,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YQ13_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ13,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YQ16_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ16,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YQ26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YQ32_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ32,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YQ41_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YQ41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR11_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR11,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR15_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR15,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR22_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR22,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR24_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR24,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR26_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR26,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR33_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR33,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR41_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR41,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR43_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR43,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR45_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR45,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR50_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR50,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR52_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR52,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR54_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR54,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR57_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR57,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR65_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR65,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
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
    
    YR67_admissions=patients.admitted_to_hospital(
        with_these_procedures=hrg_YR67,
        returning="number_of_matches_in_period",
        between = ["index_date", "index_date + 364 days"],
        return_expectations={
            "int": {"distribution": "normal", "mean": 3, "stddev": 2},
            "incidence": 0.10,
        }
    ),
    
    )
    return variables_hrg4
    