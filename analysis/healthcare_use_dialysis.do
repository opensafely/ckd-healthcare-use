sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/healthcare_use_dialysis.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/healthcare_use_dialysis.csv, write text replace
**Column headings
file write tablecontent ("Date") _tab ("ip") _tab ("icu") _tab ("ed") _tab ("avf") _tab ("pd") _tab ("opd") _tab ("neph") _tab ("tx") _tab ("gp") _tab ("bp") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=4
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions {
qui su total_`aggregate'
local `x'_`aggregate' = r(mean)
}
foreach binary of varlist fistula_formation pd_insertion blood_pressure {
qui safecount if `binary'==1
local `x'_`binary' = round(r(N),5)
}
file write tablecontent (``x'_hospital_days') _tab (``x'_critical_care_days') _tab (``x'_emergency_days') _tab (``x'_fistula_formation') _tab (``x'_pd_insertion') _tab (``x'_op_appts') _tab (``x'_neph_appts') _tab (``x'_tx_appts') _tab (``x'_gp_interactions') _tab (``x'_blood_pressure') _n
}
file close tablecontent

import delimited ./output/healthcare_use_dialysis.csv, clear
local columns ""ip" "icu" "ed" "avf" "pd" "opd" "neph" "tx" "gp" "bp""
foreach col of local columns {
    replace `col' = . if `col' <= 5
}


export delimited "./output/healthcare_use_dialysis.csv", replace
