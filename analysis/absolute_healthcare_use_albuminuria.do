sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/absolute_healthcare_use_albuminuria.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/absolute_healthcare_use_albuminuria.csv, write text replace
**Column headings
file write tablecontent ("Date") _tab ("ip") _tab ("icu") _tab ("ed") _tab ("opd") _tab ("neph") _tab ("gp") _tab ("bp") _tab ("uacr") _tab ("scr") _tab ("icd1") _tab ("icd2") _tab ("icd3") _tab ("icd4") _tab ("icd5") _tab ("icd6") _tab ("icd7") _tab ("icd8") _tab ("icd9") _tab ("icd10") _tab ("icd11") _tab ("icd12") _tab ("icd13") _tab ("icd14") _tab ("icd15") _tab ("icd16") _tab ("icd17") _tab ("icd18") _tab ("icd19") _tab ("icd20") _tab ("icd21") _tab ("icd22") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=1
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts gp_interactions icd1_days icd2_days icd3_days icd4_days icd5_days icd6_days icd7_days icd8_days icd9_days icd10_days icd11_days icd12_days icd13_days icd14_days icd15_days icd16_days icd17_days icd18_days icd19_days icd20_days icd21_days icd22_days {
qui su total_`aggregate'
local `x'_`aggregate' = r(mean)
}
foreach binary of varlist blood_pressure albuminuria creatinine {
qui safecount if `binary'==1
local `x'_`binary' = round(r(N),5)
}
file write tablecontent (``x'_hospital_days') _tab (``x'_critical_care_days') _tab (``x'_emergency_days') _tab (``x'_op_appts') _tab (``x'_neph_appts') _tab (``x'_gp_interactions') _tab (``x'_blood_pressure') _tab (``x'_albuminuria') _tab (``x'_creatinine') _tab (``x'_icd1_days') _tab (``x'_icd2_days') _tab (``x'_icd3_days') _tab (``x'_icd4_days') _tab (``x'_icd5_days') _tab (``x'_icd6_days') _tab (``x'_icd7_days') _tab (``x'_icd8_days') _tab (``x'_icd9_days') _tab (``x'_icd10_days') _tab (``x'_icd11_days') _tab (``x'_icd12_days') _tab (``x'_icd13_days') _tab (``x'_icd14_days') _tab (``x'_icd15_days') _tab (``x'_icd16_days') _tab (``x'_icd17_days') _tab (``x'_icd18_days') _tab (``x'_icd19_days') _tab (``x'_icd20_days') _tab (``x'_icd21_days') _tab (``x'_icd22_days') _n
}

file close tablecontent

import delimited ./output/absolute_healthcare_use_albuminuria.csv, clear
local columns ""ip" "icu" "ed" "opd" "neph" "gp" "bp" "uacr" "scr" "icd1" "icd2" "icd3" "icd4" "icd5" "icd6" "icd7" "icd8" "icd9" "icd10" "icd11" "icd12" "icd13" "icd14" "icd15" "icd16" "icd17" "icd18" "icd19" "icd20" "icd21" "icd22""
foreach col of local columns {
    replace `col' = . if `col' <= 5
}


export delimited "./output/absolute_healthcare_use_albuminuria.csv", replace
