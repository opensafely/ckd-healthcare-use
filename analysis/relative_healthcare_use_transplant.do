sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/relative_healthcare_use_transplant.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/relative_healthcare_use_transplant.csv, write text replace
**Column headings
*Ratios are per 100 patients
file write tablecontent ("Date") _tab ("stratum") _tab ("ip") _tab ("icu") _tab ("ed") _tab ("avf") _tab ("pd") _tab ("opd") _tab ("neph") _tab ("tx") _tab ("gp") _tab ("bp") _tab ("uacr") _tab ("scr") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("all") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=5
qui safecount
local denom = round(r(N),5)
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions {
qui su total_`aggregate'
local `x'_`aggregate' = (r(mean)/`denom')*100
}
foreach binary of varlist fistula_formation pd_insertion blood_pressure albuminuria creatinine {
qui safecount if `binary'==1
local `x'_`binary' = (round(r(N),5)/`denom')*100
}
file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_creatinine') _n
}

forvalues i=1/6 {
local label`i': label ethnicity `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=5
qui safecount if ethnicity==`i'
local denom = round(r(N),5)
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions {
qui su ethnicity_`aggregate' if ethnicity==`i'
local `x'_`aggregate' = (r(mean)/`denom')*100
}
foreach binary of varlist fistula_formation pd_insertion blood_pressure albuminuria creatinine {
qui safecount if `binary'==1 & ethnicity==`i'
local `x'_`binary' = (round(r(N),5)/`denom')*100
}
file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_creatinine') _n
}
}

forvalues i=1/5 {
local label`i': label imd `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=5
qui safecount if imd==`i'
local denom = round(r(N),5)
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions {
qui su imd_`aggregate' if imd==`i'
local `x'_`aggregate' = (r(mean)/`denom')*100
}
foreach binary of varlist fistula_formation pd_insertion blood_pressure albuminuria creatinine {
qui safecount if `binary'==1 & imd==`i'
local `x'_`binary' = (round(r(N),5)/`denom')*100
}
file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_creatinine') _n
}
}

forvalues i=1/9 {
local label`i': label region `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=5
qui safecount if region==`i'
local denom = round(r(N),5)
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions {
qui su region_`aggregate' if region==`i'
local `x'_`aggregate' = (r(mean)/`denom')*100
}
foreach binary of varlist fistula_formation pd_insertion blood_pressure albuminuria creatinine {
qui safecount if `binary'==1 & region==`i'
local `x'_`binary' = (round(r(N),5)/`denom')*100
}
file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_creatinine') _n
}
}

forvalues i=0/1 {
local label`i': label urban `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=5
qui safecount if urban==`i'
local denom = round(r(N),5)
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions {
qui su urban_`aggregate' if urban==`i'
local `x'_`aggregate' = (r(mean)/`denom')*100
}
foreach binary of varlist fistula_formation pd_insertion blood_pressure albuminuria creatinine {
qui safecount if `binary'==1 & urban==`i'
local `x'_`binary' = (round(r(N),5)/`denom')*100
}
file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_creatinine') _n
}
}

file close tablecontent


