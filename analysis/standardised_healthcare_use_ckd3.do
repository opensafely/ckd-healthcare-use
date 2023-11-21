sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/standardised_healthcare_use_ckd3.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/standardised_healthcare_use_ckd3.csv, write text replace
**Column headings
*Ratios are per 100 patients
file write tablecontent ("Date") _tab ("stratum") _tab ("ip") _tab ("ip_ll") _tab ("ip_ul") _tab ("icu") _tab ("icu_ll") _tab ("icu_ul") _tab ("ed") _tab ("ed_ll") _tab ("ed_ul") _tab ("opd") _tab ("opd_ll") _tab ("opd_ul") _tab ("neph") _tab ("neph_ll") _tab ("neph_ul") _tab ("gp") _tab ("gp_ll") _tab ("gp_ul") _tab ("bp") _tab ("bp_ll") _tab ("bp_ul") _tab ("uacr") _tab ("uacr_ll") _tab ("uacr_ul") _tab ("scr") _tab ("scr_ll") _tab ("scr_ul") _n

local year "2017 2018 2019 2020 2021 2022"

foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("all") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=2
qui safecount
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts gp_interactions blood_pressure albuminuria creatinine {
qui su std_`outcome'
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _n
}

forvalues i=1/6 {
local label`i': label ethnicity `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=2
qui safecount if ethnicity==`i'
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts gp_interactions blood_pressure albuminuria creatinine {
qui su ethnicity_`outcome'_ckd if ethnicity==`i' 
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _n
}
}

forvalues i=1/5 {
local label`i': label imd `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=2
qui safecount if imd==`i'
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts gp_interactions blood_pressure albuminuria creatinine {
qui su imd_`outcome'_ckd if imd==`i' 
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _n
}
}


forvalues i=1/9 {
local label`i': label region `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=2
qui safecount if region==`i'
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts gp_interactions blood_pressure albuminuria creatinine {
qui su region_`outcome'_ckd if region==`i'
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _n
}
}


forvalues i=0/1 {
local label`i': label urban `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=2
qui safecount if urban==`i'
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts gp_interactions blood_pressure albuminuria creatinine {
qui su urban_`outcome'_ckd if urban==`i'
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _n
}
}

file close tablecontent