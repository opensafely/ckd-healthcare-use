**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/`dataset'_healthcare_use_region.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/`dataset'_healthcare_use_region.csv, write text replace
**Column headings
*Measures of each outcome by month
*Column n_`dataset' is the total number in each CKD group as of the beginning of April of each year
file write tablecontent _tab _tab ("n_`dataset'") _tab ("April") _tab ("May") _tab ("June") _tab ("July") _tab ("August") _tab ("September") _tab ("October") _tab ("November") _tab ("December") _tab ("January") _tab ("February") _tab ("March") _n(2)
use ./output/`dataset'_ckd_complete.dta, clear

forvalues region = 1/9 {
use ./output/`dataset'_ckd_complete.dta, clear
drop if region !=`region'
qui safecount
local baseline_ckd`region' = round(r(N),5)
foreach binary of varlist m4_admitted_patients m5_admitted_patients m6_admitted_patients m7_admitted_patients m8_admitted_patients m9_admitted_patients m10_admitted_patients m11_admitted_patients m12_admitted_patients m1_admitted_patients m2_admitted_patients m3_admitted_patients m4_fistula_formation m5_fistula_formation m6_fistula_formation m7_fistula_formation m8_fistula_formation m9_fistula_formation m10_fistula_formation m11_fistula_formation m12_fistula_formation m1_fistula_formation m2_fistula_formation m3_fistula_formation m4_pd_insertion m5_pd_insertion m6_pd_insertion m7_pd_insertion m8_pd_insertion m9_pd_insertion m10_pd_insertion m11_pd_insertion m12_pd_insertion m1_pd_insertion m2_pd_insertion m3_pd_insertion m4_critical_care_patients m5_critical_care_patients m6_critical_care_patients m7_critical_care_patients m8_critical_care_patients m9_critical_care_patients m10_critical_care_patients m11_critical_care_patients m12_critical_care_patients m1_critical_care_patients m2_critical_care_patients m3_critical_care_patients m4_blood_pressure m5_blood_pressure m6_blood_pressure m7_blood_pressure m8_blood_pressure m9_blood_pressure m10_blood_pressure m11_blood_pressure m12_blood_pressure m1_blood_pressure m2_blood_pressure m3_blood_pressure m4_albuminuria m5_albuminuria m6_albuminuria m7_albuminuria m8_albuminuria m9_albuminuria m10_albuminuria m11_albuminuria m12_albuminuria m1_albuminuria m2_albuminuria m3_albuminuria m4_creatinine m5_creatinine m6_creatinine m7_creatinine m8_creatinine m9_creatinine m10_creatinine m11_creatinine m12_creatinine m1_creatinine m2_creatinine m3_creatinine {
*Number of people in each CKD group coded for each binary measure each month
qui safecount if `binary'==1
local ckd_`binary'`region' = round(r(N),5)
}
foreach aggregate of varlist m4_hospital_days m5_hospital_days m6_hospital_days m7_hospital_days m8_hospital_days m9_hospital_days m10_hospital_days m11_hospital_days m12_hospital_days m1_hospital_days m2_hospital_days m3_hospital_days m4_critical_care_days m5_critical_care_days m6_critical_care_days m7_critical_care_days m8_critical_care_days m9_critical_care_days m10_critical_care_days m11_critical_care_days m12_critical_care_days m1_critical_care_days m2_critical_care_days m3_critical_care_days m4_emergency_days m5_emergency_days m6_emergency_days m7_emergency_days m8_emergency_days m9_emergency_days m10_emergency_days m11_emergency_days m12_emergency_days m1_emergency_days m2_emergency_days m3_emergency_days m4_op_appts m5_op_appts m6_op_appts m7_op_appts m8_op_appts m9_op_appts m10_op_appts m11_op_appts m12_op_appts m1_op_appts m2_op_appts m3_op_appts m4_neph_appts m5_neph_appts m6_neph_appts m7_neph_appts m8_neph_appts m9_neph_appts m10_neph_appts m11_neph_appts m12_neph_appts m1_neph_appts m2_neph_appts m3_neph_appts m4_tx_appts m5_tx_appts m6_tx_appts m7_tx_appts m8_tx_appts m9_tx_appts m10_tx_appts m11_tx_appts m12_tx_appts m1_tx_appts m2_tx_appts m3_tx_appts m4_gp_interactions m5_gp_interactions m6_gp_interactions m7_gp_interactions m8_gp_interactions m9_gp_interactions m10_gp_interactions m11_gp_interactions m12_gp_interactions m1_gp_interactions m2_gp_interactions m3_gp_interactions {
qui su overall_`aggregate'
local ckd_`aggregate'`region' = r(mean)
}
local lab0: label region `region'
file write tablecontent ("`lab0'") _n(2)
file write tablecontent ("All CKD groups") _tab _tab (`baseline_ckd`region'') _n
file write tablecontent _tab ("Hospital days") _tab _tab (`ckd_m4_hospital_days`region'') _tab (`ckd_m5_hospital_days`region'') _tab (`ckd_m6_hospital_days`region'') _tab (`ckd_m7_hospital_days`region'') _tab (`ckd_m8_hospital_days`region'') _tab (`ckd_m9_hospital_days`region'') _tab (`ckd_m10_hospital_days`region'') _tab (`ckd_m11_hospital_days`region'') _tab (`ckd_m12_hospital_days`region'') _tab (`ckd_m1_hospital_days`region'') _tab (`ckd_m2_hospital_days`region'') _tab (`ckd_m3_hospital_days`region'') _n
file write tablecontent _tab ("Hospitalised patients") _tab _tab (`ckd_m4_admitted_patients`region'') _tab (`ckd_m5_admitted_patients`region'') _tab (`ckd_m6_admitted_patients`region'') _tab (`ckd_m7_admitted_patients`region'') _tab (`ckd_m8_admitted_patients`region'') _tab (`ckd_m9_admitted_patients`region'') _tab (`ckd_m10_admitted_patients`region'') _tab (`ckd_m11_admitted_patients`region'') _tab (`ckd_m12_admitted_patients`region'') _tab (`ckd_m1_admitted_patients`region'') _tab (`ckd_m2_admitted_patients`region'') _tab (`ckd_m3_admitted_patients`region'') _n
file write tablecontent _tab ("AVF formations") _tab _tab (`ckd_m4_fistula_formation`region'') _tab (`ckd_m5_fistula_formation`region'') _tab (`ckd_m6_fistula_formation`region'') _tab (`ckd_m7_fistula_formation`region'') _tab (`ckd_m8_fistula_formation`region'') _tab (`ckd_m9_fistula_formation`region'') _tab (`ckd_m10_fistula_formation`region'') _tab (`ckd_m11_fistula_formation`region'') _tab (`ckd_m12_fistula_formation`region'') _tab (`ckd_m1_fistula_formation`region'') _tab (`ckd_m2_fistula_formation`region'') _tab (`ckd_m3_fistula_formation`region'') _n
file write tablecontent _tab ("PD insertions") _tab _tab (`ckd_m4_pd_insertion`region'') _tab (`ckd_m5_pd_insertion`region'') _tab (`ckd_m6_pd_insertion`region'') _tab (`ckd_m7_pd_insertion`region'') _tab (`ckd_m8_pd_insertion`region'') _tab (`ckd_m9_pd_insertion`region'') _tab (`ckd_m10_pd_insertion`region'') _tab (`ckd_m11_pd_insertion`region'') _tab (`ckd_m12_pd_insertion`region'') _tab (`ckd_m1_pd_insertion`region'') _tab (`ckd_m2_pd_insertion`region'') _tab (`ckd_m3_pd_insertion`region'') _n
file write tablecontent _tab ("ICU days") _tab _tab (`ckd_m4_critical_care_days`region'') _tab (`ckd_m5_critical_care_days`region'') _tab (`ckd_m6_critical_care_days`region'') _tab (`ckd_m7_critical_care_days`region'') _tab (`ckd_m8_critical_care_days`region'') _tab (`ckd_m9_critical_care_days`region'') _tab (`ckd_m10_critical_care_days`region'') _tab (`ckd_m11_critical_care_days`region'') _tab (`ckd_m12_critical_care_days`region'') _tab (`ckd_m1_critical_care_days`region'') _tab (`ckd_m2_critical_care_days`region'') _tab (`ckd_m3_critical_care_days`region'') _n
file write tablecontent _tab ("ICU patients") _tab _tab (`ckd_m4_critical_care_patients`region'') _tab (`ckd_m5_critical_care_patients`region'') _tab (`ckd_m6_critical_care_patients`region'') _tab (`ckd_m7_critical_care_patients`region'') _tab (`ckd_m8_critical_care_patients`region'') _tab (`ckd_m9_critical_care_patients`region'') _tab (`ckd_m10_critical_care_patients`region'') _tab (`ckd_m11_critical_care_patients`region'') _tab (`ckd_m12_critical_care_patients`region'') _tab (`ckd_m1_critical_care_patients`region'') _tab (`ckd_m2_critical_care_patients`region'') _tab (`ckd_m3_critical_care_patients`region'') _n
file write tablecontent _tab ("ED days") _tab _tab (`ckd_m4_emergency_days`region'') _tab (`ckd_m5_emergency_days`region'') _tab (`ckd_m6_emergency_days`region'') _tab (`ckd_m7_emergency_days`region'') _tab (`ckd_m8_emergency_days`region'') _tab (`ckd_m9_emergency_days`region'') _tab (`ckd_m10_emergency_days`region'') _tab (`ckd_m11_emergency_days`region'') _tab (`ckd_m12_emergency_days`region'') _tab (`ckd_m1_emergency_days`region'') _tab (`ckd_m2_emergency_days`region'') _tab (`ckd_m3_emergency_days`region'') _n
file write tablecontent _tab ("OPD appts") _tab _tab (`ckd_m4_op_appts`region'') _tab (`ckd_m5_op_appts`region'') _tab (`ckd_m6_op_appts`region'') _tab (`ckd_m7_op_appts`region'') _tab (`ckd_m8_op_appts`region'') _tab (`ckd_m9_op_appts`region'') _tab (`ckd_m10_op_appts`region'') _tab (`ckd_m11_op_appts`region'') _tab (`ckd_m12_op_appts`region'') _tab (`ckd_m1_op_appts`region'') _tab (`ckd_m2_op_appts`region'') _tab (`ckd_m3_op_appts`region'') _n
file write tablecontent _tab ("Neph appts") _tab _tab (`ckd_m4_neph_appts`region'') _tab (`ckd_m5_neph_appts`region'') _tab (`ckd_m6_neph_appts`region'') _tab (`ckd_m7_neph_appts`region'') _tab (`ckd_m8_neph_appts`region'') _tab (`ckd_m9_neph_appts`region'') _tab (`ckd_m10_neph_appts`region'') _tab (`ckd_m11_neph_appts`region'') _tab (`ckd_m12_neph_appts`region'') _tab (`ckd_m1_neph_appts`region'') _tab (`ckd_m2_neph_appts`region'') _tab (`ckd_m3_neph_appts`region'') _n
file write tablecontent _tab ("Tx appts") _tab _tab (`ckd_m4_tx_appts`region'') _tab (`ckd_m5_tx_appts`region'') _tab (`ckd_m6_tx_appts`region'') _tab (`ckd_m7_tx_appts`region'') _tab (`ckd_m8_tx_appts`region'') _tab (`ckd_m9_tx_appts`region'') _tab (`ckd_m10_tx_appts`region'') _tab (`ckd_m11_tx_appts`region'') _tab (`ckd_m12_tx_appts`region'') _tab (`ckd_m1_tx_appts`region'') _tab (`ckd_m2_tx_appts`region'') _tab (`ckd_m3_tx_appts`region'') _n
file write tablecontent _tab ("GP interactions") _tab _tab (`ckd_m4_gp_interactions`region'') _tab (`ckd_m5_gp_interactions`region'') _tab (`ckd_m6_gp_interactions`region'') _tab (`ckd_m7_gp_interactions`region'') _tab (`ckd_m8_gp_interactions`region'') _tab (`ckd_m9_gp_interactions`region'') _tab (`ckd_m10_gp_interactions`region'') _tab (`ckd_m11_gp_interactions`region'') _tab (`ckd_m12_gp_interactions`region'') _tab (`ckd_m1_gp_interactions`region'') _tab (`ckd_m2_gp_interactions`region'') _tab (`ckd_m3_gp_interactions`region'') _n
file write tablecontent _tab ("BP patients") _tab _tab (`ckd_m4_blood_pressure`region'') _tab (`ckd_m5_blood_pressure`region'') _tab (`ckd_m6_blood_pressure`region'') _tab (`ckd_m7_blood_pressure`region'') _tab (`ckd_m8_blood_pressure`region'') _tab (`ckd_m9_blood_pressure`region'') _tab (`ckd_m10_blood_pressure`region'') _tab (`ckd_m11_blood_pressure`region'') _tab (`ckd_m12_blood_pressure`region'') _tab (`ckd_m1_blood_pressure`region'') _tab (`ckd_m2_blood_pressure`region'') _tab (`ckd_m3_blood_pressure`region'') _n
file write tablecontent _tab ("uACR patients") _tab _tab (`ckd_m4_albuminuria`region'') _tab (`ckd_m5_albuminuria`region'') _tab (`ckd_m6_albuminuria`region'') _tab (`ckd_m7_albuminuria`region'') _tab (`ckd_m8_albuminuria`region'') _tab (`ckd_m9_albuminuria`region'') _tab (`ckd_m10_albuminuria`region'') _tab (`ckd_m11_albuminuria`region'') _tab (`ckd_m12_albuminuria`region'') _tab (`ckd_m1_albuminuria`region'') _tab (`ckd_m2_albuminuria`region'') _tab (`ckd_m3_albuminuria`region'') _n
file write tablecontent _tab ("SCr patients") _tab _tab (`ckd_m4_creatinine`region'') _tab (`ckd_m5_creatinine`region'') _tab (`ckd_m6_creatinine`region'') _tab (`ckd_m7_creatinine`region'') _tab (`ckd_m8_creatinine`region'') _tab (`ckd_m9_creatinine`region'') _tab (`ckd_m10_creatinine`region'') _tab (`ckd_m11_creatinine`region'') _tab (`ckd_m12_creatinine`region'') _tab (`ckd_m1_creatinine`region'') _tab (`ckd_m2_creatinine`region'') _tab (`ckd_m3_creatinine`region'') _n(2)
}
file close tablecontent

**Redact counts of 0 from each column in table (adapted from code by Emily Herrett)
import delimited ./output/`dataset'_healthcare_use_region.csv, clear
local columns " "n_`dataset'" "april" "may" "june" "july" "august" "september" "october" "november" "december" "january" "february" "march" "april" "
foreach col in `columns' {
replace `col'=. if `col'<=5
}
export delimited "./output/`dataset'_healthcare_use_region.csv", replace


**For code development from dummy data
/*
sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap file close tablecontent
file open tablecontent using ./output/2017_healthcare_use_region.csv, write text replace
file write tablecontent _tab _tab ("n_2017'") _tab ("April") _tab ("May") _tab ("June") _tab ("July") _tab ("August") _tab ("September") _tab ("October") _tab ("November") _tab ("December") _tab ("January") _tab ("February") _tab ("March") _n(2)
use ./output/2017_ckd_complete.dta, clear
forvalues region = 1/9 {
use ./output/2017_ckd_complete.dta, clear
drop if region !=`region'
qui safecount
local baseline_ckd`region' = round(r(N),5)
foreach binary of varlist m4_admitted_patients m5_admitted_patients m6_admitted_patients m7_admitted_patients m8_admitted_patients m9_admitted_patients m10_admitted_patients m11_admitted_patients m12_admitted_patients m1_admitted_patients m2_admitted_patients m3_admitted_patients m4_fistula_formation m5_fistula_formation m6_fistula_formation m7_fistula_formation m8_fistula_formation m9_fistula_formation m10_fistula_formation m11_fistula_formation m12_fistula_formation m1_fistula_formation m2_fistula_formation m3_fistula_formation m4_pd_insertion m5_pd_insertion m6_pd_insertion m7_pd_insertion m8_pd_insertion m9_pd_insertion m10_pd_insertion m11_pd_insertion m12_pd_insertion m1_pd_insertion m2_pd_insertion m3_pd_insertion m4_critical_care_patients m5_critical_care_patients m6_critical_care_patients m7_critical_care_patients m8_critical_care_patients m9_critical_care_patients m10_critical_care_patients m11_critical_care_patients m12_critical_care_patients m1_critical_care_patients m2_critical_care_patients m3_critical_care_patients m4_blood_pressure m5_blood_pressure m6_blood_pressure m7_blood_pressure m8_blood_pressure m9_blood_pressure m10_blood_pressure m11_blood_pressure m12_blood_pressure m1_blood_pressure m2_blood_pressure m3_blood_pressure m4_albuminuria m5_albuminuria m6_albuminuria m7_albuminuria m8_albuminuria m9_albuminuria m10_albuminuria m11_albuminuria m12_albuminuria m1_albuminuria m2_albuminuria m3_albuminuria m4_creatinine m5_creatinine m6_creatinine m7_creatinine m8_creatinine m9_creatinine m10_creatinine m11_creatinine m12_creatinine m1_creatinine m2_creatinine m3_creatinine {
*Number of people in each CKD group coded for each binary measure each month
qui safecount if `binary'==1
local ckd_`binary'`region' = round(r(N),5)
}
foreach aggregate of varlist m4_hospital_days m5_hospital_days m6_hospital_days m7_hospital_days m8_hospital_days m9_hospital_days m10_hospital_days m11_hospital_days m12_hospital_days m1_hospital_days m2_hospital_days m3_hospital_days m4_critical_care_days m5_critical_care_days m6_critical_care_days m7_critical_care_days m8_critical_care_days m9_critical_care_days m10_critical_care_days m11_critical_care_days m12_critical_care_days m1_critical_care_days m2_critical_care_days m3_critical_care_days m4_emergency_days m5_emergency_days m6_emergency_days m7_emergency_days m8_emergency_days m9_emergency_days m10_emergency_days m11_emergency_days m12_emergency_days m1_emergency_days m2_emergency_days m3_emergency_days m4_op_appts m5_op_appts m6_op_appts m7_op_appts m8_op_appts m9_op_appts m10_op_appts m11_op_appts m12_op_appts m1_op_appts m2_op_appts m3_op_appts m4_neph_appts m5_neph_appts m6_neph_appts m7_neph_appts m8_neph_appts m9_neph_appts m10_neph_appts m11_neph_appts m12_neph_appts m1_neph_appts m2_neph_appts m3_neph_appts m4_tx_appts m5_tx_appts m6_tx_appts m7_tx_appts m8_tx_appts m9_tx_appts m10_tx_appts m11_tx_appts m12_tx_appts m1_tx_appts m2_tx_appts m3_tx_appts m4_gp_interactions m5_gp_interactions m6_gp_interactions m7_gp_interactions m8_gp_interactions m9_gp_interactions m10_gp_interactions m11_gp_interactions m12_gp_interactions m1_gp_interactions m2_gp_interactions m3_gp_interactions {
qui su overall_`aggregate'
local ckd_`aggregate'`region' = r(mean)
}
local lab0: label region `region'
file write tablecontent ("`lab0'") _n(2)
file write tablecontent ("All CKD groups") _tab _tab (`baseline_ckd`region'') _n
file write tablecontent _tab ("Hospital days") _tab _tab (`ckd_m4_hospital_days`region'') _tab (`ckd_m5_hospital_days`region'') _tab (`ckd_m6_hospital_days`region'') _tab (`ckd_m7_hospital_days`region'') _tab (`ckd_m8_hospital_days`region'') _tab (`ckd_m9_hospital_days`region'') _tab (`ckd_m10_hospital_days`region'') _tab (`ckd_m11_hospital_days`region'') _tab (`ckd_m12_hospital_days`region'') _tab (`ckd_m1_hospital_days`region'') _tab (`ckd_m2_hospital_days`region'') _tab (`ckd_m3_hospital_days`region'') _n
file write tablecontent _tab ("Hospitalised patients") _tab _tab (`ckd_m4_admitted_patients`region'') _tab (`ckd_m5_admitted_patients`region'') _tab (`ckd_m6_admitted_patients`region'') _tab (`ckd_m7_admitted_patients`region'') _tab (`ckd_m8_admitted_patients`region'') _tab (`ckd_m9_admitted_patients`region'') _tab (`ckd_m10_admitted_patients`region'') _tab (`ckd_m11_admitted_patients`region'') _tab (`ckd_m12_admitted_patients`region'') _tab (`ckd_m1_admitted_patients`region'') _tab (`ckd_m2_admitted_patients`region'') _tab (`ckd_m3_admitted_patients`region'') _n
file write tablecontent _tab ("AVF formations") _tab _tab (`ckd_m4_fistula_formation`region'') _tab (`ckd_m5_fistula_formation`region'') _tab (`ckd_m6_fistula_formation`region'') _tab (`ckd_m7_fistula_formation`region'') _tab (`ckd_m8_fistula_formation`region'') _tab (`ckd_m9_fistula_formation`region'') _tab (`ckd_m10_fistula_formation`region'') _tab (`ckd_m11_fistula_formation`region'') _tab (`ckd_m12_fistula_formation`region'') _tab (`ckd_m1_fistula_formation`region'') _tab (`ckd_m2_fistula_formation`region'') _tab (`ckd_m3_fistula_formation`region'') _n
file write tablecontent _tab ("PD insertions") _tab _tab (`ckd_m4_pd_insertion`region'') _tab (`ckd_m5_pd_insertion`region'') _tab (`ckd_m6_pd_insertion`region'') _tab (`ckd_m7_pd_insertion`region'') _tab (`ckd_m8_pd_insertion`region'') _tab (`ckd_m9_pd_insertion`region'') _tab (`ckd_m10_pd_insertion`region'') _tab (`ckd_m11_pd_insertion`region'') _tab (`ckd_m12_pd_insertion`region'') _tab (`ckd_m1_pd_insertion`region'') _tab (`ckd_m2_pd_insertion`region'') _tab (`ckd_m3_pd_insertion`region'') _n
file write tablecontent _tab ("ICU days") _tab _tab (`ckd_m4_critical_care_days`region'') _tab (`ckd_m5_critical_care_days`region'') _tab (`ckd_m6_critical_care_days`region'') _tab (`ckd_m7_critical_care_days`region'') _tab (`ckd_m8_critical_care_days`region'') _tab (`ckd_m9_critical_care_days`region'') _tab (`ckd_m10_critical_care_days`region'') _tab (`ckd_m11_critical_care_days`region'') _tab (`ckd_m12_critical_care_days`region'') _tab (`ckd_m1_critical_care_days`region'') _tab (`ckd_m2_critical_care_days`region'') _tab (`ckd_m3_critical_care_days`region'') _n
file write tablecontent _tab ("ICU patients") _tab _tab (`ckd_m4_critical_care_patients`region'') _tab (`ckd_m5_critical_care_patients`region'') _tab (`ckd_m6_critical_care_patients`region'') _tab (`ckd_m7_critical_care_patients`region'') _tab (`ckd_m8_critical_care_patients`region'') _tab (`ckd_m9_critical_care_patients`region'') _tab (`ckd_m10_critical_care_patients`region'') _tab (`ckd_m11_critical_care_patients`region'') _tab (`ckd_m12_critical_care_patients`region'') _tab (`ckd_m1_critical_care_patients`region'') _tab (`ckd_m2_critical_care_patients`region'') _tab (`ckd_m3_critical_care_patients`region'') _n
file write tablecontent _tab ("ED days") _tab _tab (`ckd_m4_emergency_days`region'') _tab (`ckd_m5_emergency_days`region'') _tab (`ckd_m6_emergency_days`region'') _tab (`ckd_m7_emergency_days`region'') _tab (`ckd_m8_emergency_days`region'') _tab (`ckd_m9_emergency_days`region'') _tab (`ckd_m10_emergency_days`region'') _tab (`ckd_m11_emergency_days`region'') _tab (`ckd_m12_emergency_days`region'') _tab (`ckd_m1_emergency_days`region'') _tab (`ckd_m2_emergency_days`region'') _tab (`ckd_m3_emergency_days`region'') _n
file write tablecontent _tab ("OPD appts") _tab _tab (`ckd_m4_op_appts`region'') _tab (`ckd_m5_op_appts`region'') _tab (`ckd_m6_op_appts`region'') _tab (`ckd_m7_op_appts`region'') _tab (`ckd_m8_op_appts`region'') _tab (`ckd_m9_op_appts`region'') _tab (`ckd_m10_op_appts`region'') _tab (`ckd_m11_op_appts`region'') _tab (`ckd_m12_op_appts`region'') _tab (`ckd_m1_op_appts`region'') _tab (`ckd_m2_op_appts`region'') _tab (`ckd_m3_op_appts`region'') _n
file write tablecontent _tab ("Neph appts") _tab _tab (`ckd_m4_neph_appts`region'') _tab (`ckd_m5_neph_appts`region'') _tab (`ckd_m6_neph_appts`region'') _tab (`ckd_m7_neph_appts`region'') _tab (`ckd_m8_neph_appts`region'') _tab (`ckd_m9_neph_appts`region'') _tab (`ckd_m10_neph_appts`region'') _tab (`ckd_m11_neph_appts`region'') _tab (`ckd_m12_neph_appts`region'') _tab (`ckd_m1_neph_appts`region'') _tab (`ckd_m2_neph_appts`region'') _tab (`ckd_m3_neph_appts`region'') _n
file write tablecontent _tab ("Tx appts") _tab _tab (`ckd_m4_tx_appts`region'') _tab (`ckd_m5_tx_appts`region'') _tab (`ckd_m6_tx_appts`region'') _tab (`ckd_m7_tx_appts`region'') _tab (`ckd_m8_tx_appts`region'') _tab (`ckd_m9_tx_appts`region'') _tab (`ckd_m10_tx_appts`region'') _tab (`ckd_m11_tx_appts`region'') _tab (`ckd_m12_tx_appts`region'') _tab (`ckd_m1_tx_appts`region'') _tab (`ckd_m2_tx_appts`region'') _tab (`ckd_m3_tx_appts`region'') _n
file write tablecontent _tab ("GP interactions") _tab _tab (`ckd_m4_gp_interactions`region'') _tab (`ckd_m5_gp_interactions`region'') _tab (`ckd_m6_gp_interactions`region'') _tab (`ckd_m7_gp_interactions`region'') _tab (`ckd_m8_gp_interactions`region'') _tab (`ckd_m9_gp_interactions`region'') _tab (`ckd_m10_gp_interactions`region'') _tab (`ckd_m11_gp_interactions`region'') _tab (`ckd_m12_gp_interactions`region'') _tab (`ckd_m1_gp_interactions`region'') _tab (`ckd_m2_gp_interactions`region'') _tab (`ckd_m3_gp_interactions`region'') _n
file write tablecontent _tab ("BP patients") _tab _tab (`ckd_m4_blood_pressure`region'') _tab (`ckd_m5_blood_pressure`region'') _tab (`ckd_m6_blood_pressure`region'') _tab (`ckd_m7_blood_pressure`region'') _tab (`ckd_m8_blood_pressure`region'') _tab (`ckd_m9_blood_pressure`region'') _tab (`ckd_m10_blood_pressure`region'') _tab (`ckd_m11_blood_pressure`region'') _tab (`ckd_m12_blood_pressure`region'') _tab (`ckd_m1_blood_pressure`region'') _tab (`ckd_m2_blood_pressure`region'') _tab (`ckd_m3_blood_pressure`region'') _n
file write tablecontent _tab ("uACR patients") _tab _tab (`ckd_m4_albuminuria`region'') _tab (`ckd_m5_albuminuria`region'') _tab (`ckd_m6_albuminuria`region'') _tab (`ckd_m7_albuminuria`region'') _tab (`ckd_m8_albuminuria`region'') _tab (`ckd_m9_albuminuria`region'') _tab (`ckd_m10_albuminuria`region'') _tab (`ckd_m11_albuminuria`region'') _tab (`ckd_m12_albuminuria`region'') _tab (`ckd_m1_albuminuria`region'') _tab (`ckd_m2_albuminuria`region'') _tab (`ckd_m3_albuminuria`region'') _n
file write tablecontent _tab ("SCr patients") _tab _tab (`ckd_m4_creatinine`region'') _tab (`ckd_m5_creatinine`region'') _tab (`ckd_m6_creatinine`region'') _tab (`ckd_m7_creatinine`region'') _tab (`ckd_m8_creatinine`region'') _tab (`ckd_m9_creatinine`region'') _tab (`ckd_m10_creatinine`region'') _tab (`ckd_m11_creatinine`region'') _tab (`ckd_m12_creatinine`region'') _tab (`ckd_m1_creatinine`region'') _tab (`ckd_m2_creatinine`region'') _tab (`ckd_m3_creatinine`region'') _n(2)
}
file close tablecontent
import delimited ./output/2017_healthcare_use_region.csv, clear
local columns " "n_2017" "april" "may" "june" "july" "august" "september" "october" "november" "december" "january" "february" "march" "april" "
foreach col in `columns' {
replace `col'=. if `col'<=5
}
export delimited "./output/2017_healthcare_use_region.csv", replace
*/