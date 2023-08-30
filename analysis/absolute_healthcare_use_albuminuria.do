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
file write tablecontent ("Date") _tab ("stratum") _tab ("ip") _tab ("icu") _tab ("ed") _tab ("opd") _tab ("neph") _tab ("gp") _tab ("bp") _tab ("uacr") _tab ("scr") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("all") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=1
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts gp_interactions {
qui su total_`aggregate'
local `x'_`aggregate' = r(mean)
}
foreach binary of varlist blood_pressure albuminuria creatinine {
qui safecount if `binary'==1
local `x'_`binary' = round(r(N),5)
}
file write tablecontent (``x'_hospital_days') _tab (``x'_critical_care_days') _tab (``x'_emergency_days') _tab (``x'_op_appts') _tab (``x'_neph_appts') _tab (``x'_gp_interactions') _tab (``x'_blood_pressure') _tab (``x'_albuminuria') _tab (``x'_creatinine') _n
}

file close tablecontent

import delimited ./output/absolute_healthcare_use_albuminuria.csv, clear
local columns ""ip" "icu" "ed" "opd" "neph" "gp" "bp" "uacr" "scr""
foreach col of local columns {
    replace `col' = . if `col' <= 5
}


export delimited "./output/absolute_healthcare_use_albuminuria.csv", replace
