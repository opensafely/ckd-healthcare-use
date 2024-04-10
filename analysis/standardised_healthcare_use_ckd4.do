sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/standardised_healthcare_use_ckd4.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/standardised_healthcare_use_ckd4.csv, write text replace
**Column headings
*Ratios are per 100 patients
file write tablecontent ("Date") _tab ("stratum") _tab ("ip") _tab ("ip_ll") _tab ("ip_ul") _tab ("icu") _tab ("icu_ll") _tab ("icu_ul") _tab ("ed") _tab ("ed_ll") _tab ("ed_ul") _tab ("avf") _tab ("avf_ll") _tab ("avf_ul") _tab ("pd") _tab ("pd_ll") _tab ("pd_ul") _tab ("opd") _tab ("opd_ll") _tab ("opd_ul") _tab ("neph") _tab ("neph_ll") _tab ("neph_ul") _tab ("tx") _tab ("tx_ll") _tab ("tx_ul") _tab ("gp") _tab ("gp_ll") _tab ("gp_ul") _tab ("bp") _tab ("bp_ll") _tab ("bp_ul") _tab ("uacr") _tab ("uacr_ll") _tab ("uacr_ul") _tab ("scr") _tab ("scr_ll") _tab ("scr_ul")_tab ("icd1") _tab ("icd2") _tab ("icd3") _tab ("icd4") _tab ("icd5") _tab ("icd6") _tab ("icd7") _tab ("icd8") _tab ("icd9") _tab ("icd10") _tab ("icd11") _tab ("icd12") _tab ("icd13") _tab ("icd14") _tab ("icd15") _tab ("icd16") _tab ("icd17") _tab ("icd18") _tab ("icd19") _tab ("icd20") _tab ("icd21") _tab ("icd22") _tab ("icd1_ll") _tab ("icd2_ll") _tab ("icd3_ll") _tab ("icd4_ll") _tab ("icd5_ll") _tab ("icd6_ll") _tab ("icd7_ll") _tab ("icd8_ll") _tab ("icd9_ll") _tab ("icd10_ll") _tab ("icd11_ll") _tab ("icd12_ll") _tab ("icd13_ll") _tab ("icd14_ll") _tab ("icd15_ll") _tab ("icd16_ll") _tab ("icd17_ll") _tab ("icd18_ll") _tab ("icd19_ll") _tab ("icd20_ll") _tab ("icd21_ll") _tab ("icd22_ll") _tab ("icd1_ul") _tab ("icd2_ul") _tab ("icd3_ul") _tab ("icd4_ul") _tab ("icd5_ul") _tab ("icd6_ul") _tab ("icd7_ul") _tab ("icd8_ul") _tab ("icd9_ul") _tab ("icd10_ul") _tab ("icd11_ul") _tab ("icd12_ul") _tab ("icd13_ul") _tab ("icd14_ul") _tab ("icd15_ul") _tab ("icd16_ul") _tab ("icd17_ul") _tab ("icd18_ul") _tab ("icd19_ul") _tab ("icd20_ul") _tab ("icd21_ul") _tab ("icd22_ul") _n

local year "2017 2018 2019 2020 2021 2022"

foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("all") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
qui safecount
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions fistula_formation pd_insertion blood_pressure albuminuria creatinine icd1_days icd2_days icd3_days icd4_days icd5_days icd6_days icd7_days icd8_days icd9_days icd10_days icd11_days icd12_days icd13_days icd14_days icd15_days icd16_days icd17_days icd18_days icd19_days icd20_days icd21_days icd22_days {
qui su std_`outcome'
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_fistula_formation_ll') _tab %10.2f (``x'_fistula_formation_ul') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_pd_insertion_ll') _tab %10.2f (``x'_pd_insertion_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_tx_appts_ll') _tab %10.2f (``x'_tx_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _tab %10.2f (``x'_icd1_days') _tab %10.2f (``x'_icd2_days') _tab %10.2f (``x'_icd3_days') _tab %10.2f (``x'_icd4_days') _tab %10.2f (``x'_icd5_days') _tab %10.2f (``x'_icd6_days') _tab %10.2f (``x'_icd7_days') _tab %10.2f (``x'_icd8_days') _tab %10.2f (``x'_icd9_days') _tab %10.2f (``x'_icd10_days') _tab %10.2f (``x'_icd11_days') _tab %10.2f (``x'_icd12_days') _tab %10.2f (``x'_icd13_days') _tab %10.2f (``x'_icd14_days') _tab %10.2f (``x'_icd15_days') _tab %10.2f (``x'_icd16_days') _tab %10.2f (``x'_icd17_days') _tab %10.2f (``x'_icd18_days') _tab %10.2f (``x'_icd19_days') _tab %10.2f (``x'_icd20_days') _tab %10.2f (``x'_icd21_days') _tab %10.2f (``x'_icd22_days') _tab %10.2f (``x'_icd1_days_ll') _tab %10.2f (``x'_icd2_days_ll') _tab %10.2f (``x'_icd3_days_ll') _tab %10.2f (``x'_icd4_days_ll') _tab %10.2f (``x'_icd5_days_ll') _tab %10.2f (``x'_icd6_days_ll') _tab %10.2f (``x'_icd7_days_ll') _tab %10.2f (``x'_icd8_days_ll') _tab %10.2f (``x'_icd9_days_ll') _tab %10.2f (``x'_icd10_days_ll') _tab %10.2f (``x'_icd11_days_ll') _tab %10.2f (``x'_icd12_days_ll') _tab %10.2f (``x'_icd13_days_ll') _tab %10.2f (``x'_icd14_days_ll') _tab %10.2f (``x'_icd15_days_ll') _tab %10.2f (``x'_icd16_days_ll') _tab %10.2f (``x'_icd17_days_ll') _tab %10.2f (``x'_icd18_days_ll') _tab %10.2f (``x'_icd19_days_ll') _tab %10.2f (``x'_icd20_days_ll') _tab %10.2f (``x'_icd21_days_ll') _tab %10.2f (``x'_icd22_days_ll') _tab %10.2f (``x'_icd1_days_ul') _tab %10.2f (``x'_icd2_days_ul') _tab %10.2f (``x'_icd3_days_ul') _tab %10.2f (``x'_icd4_days_ul') _tab %10.2f (``x'_icd5_days_ul') _tab %10.2f (``x'_icd6_days_ul') _tab %10.2f (``x'_icd7_days_ul') _tab %10.2f (``x'_icd8_days_ul') _tab %10.2f (``x'_icd9_days_ul') _tab %10.2f (``x'_icd10_days_ul') _tab %10.2f (``x'_icd11_days_ul') _tab %10.2f (``x'_icd12_days_ul') _tab %10.2f (``x'_icd13_days_ul') _tab %10.2f (``x'_icd14_days_ul') _tab %10.2f (``x'_icd15_days_ul') _tab %10.2f (``x'_icd16_days_ul') _tab %10.2f (``x'_icd17_days_ul') _tab %10.2f (``x'_icd18_days_ul') _tab %10.2f (``x'_icd19_days_ul') _tab %10.2f (``x'_icd20_days_ul') _tab %10.2f (``x'_icd21_days_ul') _tab %10.2f (``x'_icd22_days_ul') _n
}

forvalues i=1/6 {
local label`i': label ethnicity `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
qui safecount if ethnicity==`i'
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions fistula_formation pd_insertion blood_pressure albuminuria creatinine icd1_days icd2_days icd3_days icd4_days icd5_days icd6_days icd7_days icd8_days icd9_days icd10_days icd11_days icd12_days icd13_days icd14_days icd15_days icd16_days icd17_days icd18_days icd19_days icd20_days icd21_days icd22_days {
qui su ethnicity_`outcome'_ckd if ethnicity==`i' 
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_fistula_formation_ll') _tab %10.2f (``x'_fistula_formation_ul') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_pd_insertion_ll') _tab %10.2f (``x'_pd_insertion_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_tx_appts_ll') _tab %10.2f (``x'_tx_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _tab %10.2f (``x'_icd1_days') _tab %10.2f (``x'_icd2_days') _tab %10.2f (``x'_icd3_days') _tab %10.2f (``x'_icd4_days') _tab %10.2f (``x'_icd5_days') _tab %10.2f (``x'_icd6_days') _tab %10.2f (``x'_icd7_days') _tab %10.2f (``x'_icd8_days') _tab %10.2f (``x'_icd9_days') _tab %10.2f (``x'_icd10_days') _tab %10.2f (``x'_icd11_days') _tab %10.2f (``x'_icd12_days') _tab %10.2f (``x'_icd13_days') _tab %10.2f (``x'_icd14_days') _tab %10.2f (``x'_icd15_days') _tab %10.2f (``x'_icd16_days') _tab %10.2f (``x'_icd17_days') _tab %10.2f (``x'_icd18_days') _tab %10.2f (``x'_icd19_days') _tab %10.2f (``x'_icd20_days') _tab %10.2f (``x'_icd21_days') _tab %10.2f (``x'_icd22_days') _tab %10.2f (``x'_icd1_days_ll') _tab %10.2f (``x'_icd2_days_ll') _tab %10.2f (``x'_icd3_days_ll') _tab %10.2f (``x'_icd4_days_ll') _tab %10.2f (``x'_icd5_days_ll') _tab %10.2f (``x'_icd6_days_ll') _tab %10.2f (``x'_icd7_days_ll') _tab %10.2f (``x'_icd8_days_ll') _tab %10.2f (``x'_icd9_days_ll') _tab %10.2f (``x'_icd10_days_ll') _tab %10.2f (``x'_icd11_days_ll') _tab %10.2f (``x'_icd12_days_ll') _tab %10.2f (``x'_icd13_days_ll') _tab %10.2f (``x'_icd14_days_ll') _tab %10.2f (``x'_icd15_days_ll') _tab %10.2f (``x'_icd16_days_ll') _tab %10.2f (``x'_icd17_days_ll') _tab %10.2f (``x'_icd18_days_ll') _tab %10.2f (``x'_icd19_days_ll') _tab %10.2f (``x'_icd20_days_ll') _tab %10.2f (``x'_icd21_days_ll') _tab %10.2f (``x'_icd22_days_ll') _tab %10.2f (``x'_icd1_days_ul') _tab %10.2f (``x'_icd2_days_ul') _tab %10.2f (``x'_icd3_days_ul') _tab %10.2f (``x'_icd4_days_ul') _tab %10.2f (``x'_icd5_days_ul') _tab %10.2f (``x'_icd6_days_ul') _tab %10.2f (``x'_icd7_days_ul') _tab %10.2f (``x'_icd8_days_ul') _tab %10.2f (``x'_icd9_days_ul') _tab %10.2f (``x'_icd10_days_ul') _tab %10.2f (``x'_icd11_days_ul') _tab %10.2f (``x'_icd12_days_ul') _tab %10.2f (``x'_icd13_days_ul') _tab %10.2f (``x'_icd14_days_ul') _tab %10.2f (``x'_icd15_days_ul') _tab %10.2f (``x'_icd16_days_ul') _tab %10.2f (``x'_icd17_days_ul') _tab %10.2f (``x'_icd18_days_ul') _tab %10.2f (``x'_icd19_days_ul') _tab %10.2f (``x'_icd20_days_ul') _tab %10.2f (``x'_icd21_days_ul') _tab %10.2f (``x'_icd22_days_ul') _n
}
}

forvalues i=1/5 {
local label`i': label imd `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
qui safecount if imd==`i'
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions fistula_formation pd_insertion blood_pressure albuminuria creatinine icd1_days icd2_days icd3_days icd4_days icd5_days icd6_days icd7_days icd8_days icd9_days icd10_days icd11_days icd12_days icd13_days icd14_days icd15_days icd16_days icd17_days icd18_days icd19_days icd20_days icd21_days icd22_days {
qui su imd_`outcome'_ckd if imd==`i' 
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_fistula_formation_ll') _tab %10.2f (``x'_fistula_formation_ul') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_pd_insertion_ll') _tab %10.2f (``x'_pd_insertion_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_tx_appts_ll') _tab %10.2f (``x'_tx_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _tab %10.2f (``x'_icd1_days') _tab %10.2f (``x'_icd2_days') _tab %10.2f (``x'_icd3_days') _tab %10.2f (``x'_icd4_days') _tab %10.2f (``x'_icd5_days') _tab %10.2f (``x'_icd6_days') _tab %10.2f (``x'_icd7_days') _tab %10.2f (``x'_icd8_days') _tab %10.2f (``x'_icd9_days') _tab %10.2f (``x'_icd10_days') _tab %10.2f (``x'_icd11_days') _tab %10.2f (``x'_icd12_days') _tab %10.2f (``x'_icd13_days') _tab %10.2f (``x'_icd14_days') _tab %10.2f (``x'_icd15_days') _tab %10.2f (``x'_icd16_days') _tab %10.2f (``x'_icd17_days') _tab %10.2f (``x'_icd18_days') _tab %10.2f (``x'_icd19_days') _tab %10.2f (``x'_icd20_days') _tab %10.2f (``x'_icd21_days') _tab %10.2f (``x'_icd22_days') _tab %10.2f (``x'_icd1_days_ll') _tab %10.2f (``x'_icd2_days_ll') _tab %10.2f (``x'_icd3_days_ll') _tab %10.2f (``x'_icd4_days_ll') _tab %10.2f (``x'_icd5_days_ll') _tab %10.2f (``x'_icd6_days_ll') _tab %10.2f (``x'_icd7_days_ll') _tab %10.2f (``x'_icd8_days_ll') _tab %10.2f (``x'_icd9_days_ll') _tab %10.2f (``x'_icd10_days_ll') _tab %10.2f (``x'_icd11_days_ll') _tab %10.2f (``x'_icd12_days_ll') _tab %10.2f (``x'_icd13_days_ll') _tab %10.2f (``x'_icd14_days_ll') _tab %10.2f (``x'_icd15_days_ll') _tab %10.2f (``x'_icd16_days_ll') _tab %10.2f (``x'_icd17_days_ll') _tab %10.2f (``x'_icd18_days_ll') _tab %10.2f (``x'_icd19_days_ll') _tab %10.2f (``x'_icd20_days_ll') _tab %10.2f (``x'_icd21_days_ll') _tab %10.2f (``x'_icd22_days_ll') _tab %10.2f (``x'_icd1_days_ul') _tab %10.2f (``x'_icd2_days_ul') _tab %10.2f (``x'_icd3_days_ul') _tab %10.2f (``x'_icd4_days_ul') _tab %10.2f (``x'_icd5_days_ul') _tab %10.2f (``x'_icd6_days_ul') _tab %10.2f (``x'_icd7_days_ul') _tab %10.2f (``x'_icd8_days_ul') _tab %10.2f (``x'_icd9_days_ul') _tab %10.2f (``x'_icd10_days_ul') _tab %10.2f (``x'_icd11_days_ul') _tab %10.2f (``x'_icd12_days_ul') _tab %10.2f (``x'_icd13_days_ul') _tab %10.2f (``x'_icd14_days_ul') _tab %10.2f (``x'_icd15_days_ul') _tab %10.2f (``x'_icd16_days_ul') _tab %10.2f (``x'_icd17_days_ul') _tab %10.2f (``x'_icd18_days_ul') _tab %10.2f (``x'_icd19_days_ul') _tab %10.2f (``x'_icd20_days_ul') _tab %10.2f (``x'_icd21_days_ul') _tab %10.2f (``x'_icd22_days_ul') _n
}
}

forvalues i=1/9 {
local label`i': label region `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
qui safecount if region==`i'
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions fistula_formation pd_insertion blood_pressure albuminuria creatinine icd1_days icd2_days icd3_days icd4_days icd5_days icd6_days icd7_days icd8_days icd9_days icd10_days icd11_days icd12_days icd13_days icd14_days icd15_days icd16_days icd17_days icd18_days icd19_days icd20_days icd21_days icd22_days {
qui su region_`outcome'_ckd if region==`i'
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_fistula_formation_ll') _tab %10.2f (``x'_fistula_formation_ul') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_pd_insertion_ll') _tab %10.2f (``x'_pd_insertion_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_tx_appts_ll') _tab %10.2f (``x'_tx_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _tab %10.2f (``x'_icd1_days') _tab %10.2f (``x'_icd2_days') _tab %10.2f (``x'_icd3_days') _tab %10.2f (``x'_icd4_days') _tab %10.2f (``x'_icd5_days') _tab %10.2f (``x'_icd6_days') _tab %10.2f (``x'_icd7_days') _tab %10.2f (``x'_icd8_days') _tab %10.2f (``x'_icd9_days') _tab %10.2f (``x'_icd10_days') _tab %10.2f (``x'_icd11_days') _tab %10.2f (``x'_icd12_days') _tab %10.2f (``x'_icd13_days') _tab %10.2f (``x'_icd14_days') _tab %10.2f (``x'_icd15_days') _tab %10.2f (``x'_icd16_days') _tab %10.2f (``x'_icd17_days') _tab %10.2f (``x'_icd18_days') _tab %10.2f (``x'_icd19_days') _tab %10.2f (``x'_icd20_days') _tab %10.2f (``x'_icd21_days') _tab %10.2f (``x'_icd22_days') _tab %10.2f (``x'_icd1_days_ll') _tab %10.2f (``x'_icd2_days_ll') _tab %10.2f (``x'_icd3_days_ll') _tab %10.2f (``x'_icd4_days_ll') _tab %10.2f (``x'_icd5_days_ll') _tab %10.2f (``x'_icd6_days_ll') _tab %10.2f (``x'_icd7_days_ll') _tab %10.2f (``x'_icd8_days_ll') _tab %10.2f (``x'_icd9_days_ll') _tab %10.2f (``x'_icd10_days_ll') _tab %10.2f (``x'_icd11_days_ll') _tab %10.2f (``x'_icd12_days_ll') _tab %10.2f (``x'_icd13_days_ll') _tab %10.2f (``x'_icd14_days_ll') _tab %10.2f (``x'_icd15_days_ll') _tab %10.2f (``x'_icd16_days_ll') _tab %10.2f (``x'_icd17_days_ll') _tab %10.2f (``x'_icd18_days_ll') _tab %10.2f (``x'_icd19_days_ll') _tab %10.2f (``x'_icd20_days_ll') _tab %10.2f (``x'_icd21_days_ll') _tab %10.2f (``x'_icd22_days_ll') _tab %10.2f (``x'_icd1_days_ul') _tab %10.2f (``x'_icd2_days_ul') _tab %10.2f (``x'_icd3_days_ul') _tab %10.2f (``x'_icd4_days_ul') _tab %10.2f (``x'_icd5_days_ul') _tab %10.2f (``x'_icd6_days_ul') _tab %10.2f (``x'_icd7_days_ul') _tab %10.2f (``x'_icd8_days_ul') _tab %10.2f (``x'_icd9_days_ul') _tab %10.2f (``x'_icd10_days_ul') _tab %10.2f (``x'_icd11_days_ul') _tab %10.2f (``x'_icd12_days_ul') _tab %10.2f (``x'_icd13_days_ul') _tab %10.2f (``x'_icd14_days_ul') _tab %10.2f (``x'_icd15_days_ul') _tab %10.2f (``x'_icd16_days_ul') _tab %10.2f (``x'_icd17_days_ul') _tab %10.2f (``x'_icd18_days_ul') _tab %10.2f (``x'_icd19_days_ul') _tab %10.2f (``x'_icd20_days_ul') _tab %10.2f (``x'_icd21_days_ul') _tab %10.2f (``x'_icd22_days_ul') _n
}
}

forvalues i=0/1 {
local label`i': label urban `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
qui safecount if urban==`i'
local denom = round(r(N),5)

foreach outcome of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions fistula_formation pd_insertion blood_pressure albuminuria creatinine icd1_days icd2_days icd3_days icd4_days icd5_days icd6_days icd7_days icd8_days icd9_days icd10_days icd11_days icd12_days icd13_days icd14_days icd15_days icd16_days icd17_days icd18_days icd19_days icd20_days icd21_days icd22_days {
qui su urban_`outcome'_ckd if urban==`i'
local `x'_`outcome' = (r(mean)/`denom')*10000
local `x'_`outcome'_ef = exp(1.96 * sqrt(1 / ``x'_`outcome''))
local `x'_`outcome'_ul = ``x'_`outcome'' * ``x'_`outcome'_ef'
local `x'_`outcome'_ll = ``x'_`outcome'' / ``x'_`outcome'_ef'
}

file write tablecontent %10.2f (``x'_hospital_days') _tab %10.2f (``x'_hospital_days_ll') _tab %10.2f (``x'_hospital_days_ul') _tab %10.2f (``x'_critical_care_days') _tab %10.2f (``x'_critical_care_days_ll') _tab %10.2f (``x'_critical_care_days_ul') _tab %10.2f (``x'_emergency_days') _tab %10.2f (``x'_emergency_days_ll') _tab %10.2f (``x'_emergency_days_ul') _tab %10.2f (``x'_fistula_formation') _tab %10.2f (``x'_fistula_formation_ll') _tab %10.2f (``x'_fistula_formation_ul') _tab %10.2f (``x'_pd_insertion') _tab %10.2f (``x'_pd_insertion_ll') _tab %10.2f (``x'_pd_insertion_ul') _tab %10.2f (``x'_op_appts') _tab %10.2f (``x'_op_appts_ll') _tab %10.2f (``x'_op_appts_ul') _tab %10.2f (``x'_neph_appts') _tab %10.2f (``x'_neph_appts_ll') _tab %10.2f (``x'_neph_appts_ul') _tab %10.2f (``x'_tx_appts') _tab %10.2f (``x'_tx_appts_ll') _tab %10.2f (``x'_tx_appts_ul') _tab %10.2f (``x'_gp_interactions') _tab %10.2f (``x'_gp_interactions_ll') _tab %10.2f (``x'_gp_interactions_ul') _tab %10.2f (``x'_blood_pressure') _tab %10.2f (``x'_blood_pressure_ll') _tab %10.2f (``x'_blood_pressure_ul') _tab %10.2f (``x'_albuminuria') _tab %10.2f (``x'_albuminuria_ll') _tab %10.2f (``x'_albuminuria_ul') _tab %10.2f (``x'_creatinine') _tab %10.2f (``x'_creatinine_ll') _tab %10.2f (``x'_creatinine_ul') _tab %10.2f (``x'_icd1_days') _tab %10.2f (``x'_icd2_days') _tab %10.2f (``x'_icd3_days') _tab %10.2f (``x'_icd4_days') _tab %10.2f (``x'_icd5_days') _tab %10.2f (``x'_icd6_days') _tab %10.2f (``x'_icd7_days') _tab %10.2f (``x'_icd8_days') _tab %10.2f (``x'_icd9_days') _tab %10.2f (``x'_icd10_days') _tab %10.2f (``x'_icd11_days') _tab %10.2f (``x'_icd12_days') _tab %10.2f (``x'_icd13_days') _tab %10.2f (``x'_icd14_days') _tab %10.2f (``x'_icd15_days') _tab %10.2f (``x'_icd16_days') _tab %10.2f (``x'_icd17_days') _tab %10.2f (``x'_icd18_days') _tab %10.2f (``x'_icd19_days') _tab %10.2f (``x'_icd20_days') _tab %10.2f (``x'_icd21_days') _tab %10.2f (``x'_icd22_days') _tab %10.2f (``x'_icd1_days_ll') _tab %10.2f (``x'_icd2_days_ll') _tab %10.2f (``x'_icd3_days_ll') _tab %10.2f (``x'_icd4_days_ll') _tab %10.2f (``x'_icd5_days_ll') _tab %10.2f (``x'_icd6_days_ll') _tab %10.2f (``x'_icd7_days_ll') _tab %10.2f (``x'_icd8_days_ll') _tab %10.2f (``x'_icd9_days_ll') _tab %10.2f (``x'_icd10_days_ll') _tab %10.2f (``x'_icd11_days_ll') _tab %10.2f (``x'_icd12_days_ll') _tab %10.2f (``x'_icd13_days_ll') _tab %10.2f (``x'_icd14_days_ll') _tab %10.2f (``x'_icd15_days_ll') _tab %10.2f (``x'_icd16_days_ll') _tab %10.2f (``x'_icd17_days_ll') _tab %10.2f (``x'_icd18_days_ll') _tab %10.2f (``x'_icd19_days_ll') _tab %10.2f (``x'_icd20_days_ll') _tab %10.2f (``x'_icd21_days_ll') _tab %10.2f (``x'_icd22_days_ll') _tab %10.2f (``x'_icd1_days_ul') _tab %10.2f (``x'_icd2_days_ul') _tab %10.2f (``x'_icd3_days_ul') _tab %10.2f (``x'_icd4_days_ul') _tab %10.2f (``x'_icd5_days_ul') _tab %10.2f (``x'_icd6_days_ul') _tab %10.2f (``x'_icd7_days_ul') _tab %10.2f (``x'_icd8_days_ul') _tab %10.2f (``x'_icd9_days_ul') _tab %10.2f (``x'_icd10_days_ul') _tab %10.2f (``x'_icd11_days_ul') _tab %10.2f (``x'_icd12_days_ul') _tab %10.2f (``x'_icd13_days_ul') _tab %10.2f (``x'_icd14_days_ul') _tab %10.2f (``x'_icd15_days_ul') _tab %10.2f (``x'_icd16_days_ul') _tab %10.2f (``x'_icd17_days_ul') _tab %10.2f (``x'_icd18_days_ul') _tab %10.2f (``x'_icd19_days_ul') _tab %10.2f (``x'_icd20_days_ul') _tab %10.2f (``x'_icd21_days_ul') _tab %10.2f (``x'_icd22_days_ul') _n
}
}

file close tablecontent
