sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/`dataset'_healthcare_use_v3_dialysis.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/`dataset'_healthcare_use_v3_dialysis.csv, write text replace
**Column headings
*Measures of each outcome by month
*Column n_`dataset' is the total number in each CKD group as of the beginning of April of each year
file write tablecontent _tab _tab ("n_`dataset'") _tab ("April") _tab ("May") _tab ("June") _tab ("July") _tab ("August") _tab ("September") _tab ("October") _tab ("November") _tab ("December") _tab ("January") _tab ("February") _tab ("March") _n(2)
use ./output/`dataset'_ckd_complete_v3.dta, clear

**For code development from dummy data
/*
sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap file close tablecontent
file open tablecontent using ./output/2017_healthcare_use_v3_dialysis.csv, write text replace
file write tablecontent _tab _tab ("n_2017'") _tab ("April") _tab ("May") _tab ("June") _tab ("July") _tab ("August") _tab ("September") _tab ("October") _tab ("November") _tab ("December") _tab ("January") _tab ("February") _tab ("March") _n(2)
use ./output/2017_ckd_complete_v3.dta, clear
qui safecount
local baseline_ckd = round(r(N),5)
foreach binary of varlist m4_fistula_formation m5_fistula_formation m6_fistula_formation m7_fistula_formation m8_fistula_formation m9_fistula_formation m10_fistula_formation m11_fistula_formation m12_fistula_formation m1_fistula_formation m2_fistula_formation m3_fistula_formation m4_pd_insertion m5_pd_insertion m6_pd_insertion m7_pd_insertion m8_pd_insertion m9_pd_insertion m10_pd_insertion m11_pd_insertion m12_pd_insertion m1_pd_insertion m2_pd_insertion m3_pd_insertion {
*Number of people in each CKD group coded for each binary measure each month
qui safecount if `binary'==1
local ckd_`binary' = round(r(N),5)
}
file write tablecontent ("All CKD groups") _tab _tab (`baseline_ckd') _n
file write tablecontent _tab ("AVF formations") _tab _tab (`ckd_m4_fistula_formation') _tab (`ckd_m5_fistula_formation') _tab (`ckd_m6_fistula_formation') _tab (`ckd_m7_fistula_formation') _tab (`ckd_m8_fistula_formation') _tab (`ckd_m9_fistula_formation') _tab (`ckd_m10_fistula_formation') _tab (`ckd_m11_fistula_formation') _tab (`ckd_m12_fistula_formation') _tab (`ckd_m1_fistula_formation') _tab (`ckd_m2_fistula_formation') _tab (`ckd_m3_fistula_formation') _n
file write tablecontent _tab ("PD insertions") _tab _tab (`ckd_m4_pd_insertion') _tab (`ckd_m5_pd_insertion') _tab (`ckd_m6_pd_insertion') _tab (`ckd_m7_pd_insertion') _tab (`ckd_m8_pd_insertion') _tab (`ckd_m9_pd_insertion') _tab (`ckd_m10_pd_insertion') _tab (`ckd_m11_pd_insertion') _tab (`ckd_m12_pd_insertion') _tab (`ckd_m1_pd_insertion') _tab (`ckd_m2_pd_insertion') _tab (`ckd_m3_pd_insertion') _n

forvalues egfr = 0/3 {
use ./output/2017_ckd_complete_v3.dta, clear
drop if access_egfr!=`egfr'
qui safecount
local baseline_ckd_`egfr' = round(r(N),5)
foreach binary of varlist m4_fistula_formation m5_fistula_formation m6_fistula_formation m7_fistula_formation m8_fistula_formation m9_fistula_formation m10_fistula_formation m11_fistula_formation m12_fistula_formation m1_fistula_formation m2_fistula_formation m3_fistula_formation m4_pd_insertion m5_pd_insertion m6_pd_insertion m7_pd_insertion m8_pd_insertion m9_pd_insertion m10_pd_insertion m11_pd_insertion m12_pd_insertion m1_pd_insertion m2_pd_insertion m3_pd_insertion {
*Number of people in each CKD group coded for each binary measure each month
qui safecount if `binary'==1
local ckd_`binary'_`egfr' = round(r(N),5)
}
local lab`egfr': label access_egfr `egfr'
file write tablecontent ("`lab`egfr''") _tab _tab (`baseline_ckd_`egfr'') _n
file write tablecontent _tab ("AVF formations") _tab _tab (`ckd_m4_fistula_formation_`egfr'') _tab (`ckd_m5_fistula_formation_`egfr'') _tab (`ckd_m6_fistula_formation_`egfr'') _tab (`ckd_m7_fistula_formation_`egfr'') _tab (`ckd_m8_fistula_formation_`egfr'') _tab (`ckd_m9_fistula_formation_`egfr'') _tab (`ckd_m10_fistula_formation_`egfr'') _tab (`ckd_m11_fistula_formation_`egfr'') _tab (`ckd_m12_fistula_formation_`egfr'') _tab (`ckd_m1_fistula_formation_`egfr'') _tab (`ckd_m2_fistula_formation_`egfr'') _tab (`ckd_m3_fistula_formation_`egfr'') _n
file write tablecontent _tab ("PD insertions") _tab _tab (`ckd_m4_pd_insertion_`egfr'') _tab (`ckd_m5_pd_insertion_`egfr'') _tab (`ckd_m6_pd_insertion_`egfr'') _tab (`ckd_m7_pd_insertion_`egfr'') _tab (`ckd_m8_pd_insertion_`egfr'') _tab (`ckd_m9_pd_insertion_`egfr'') _tab (`ckd_m10_pd_insertion_`egfr'') _tab (`ckd_m11_pd_insertion_`egfr'') _tab (`ckd_m12_pd_insertion_`egfr'') _tab (`ckd_m1_pd_insertion_`egfr'') _tab (`ckd_m2_pd_insertion_`egfr'') _tab (`ckd_m3_pd_insertion_`egfr'') _n(2)
}

use ./output/2017_ckd_complete_v3.dta, clear

**Extract healthcare use measures for dialysis group only
*CKD group categories:
*1 = eGFR >60 with albuminuria
*2 = CKD 3A
*3 = CKD 4/5 without kidney replacement therapy
*4 = Dialysis
*5 = Kidney transplant
*6 = Kidney replacement therapy unknown modality
drop if ckd_group!=4
*Disclosure minimisation:
*safecount provides a count with any counts <=5 returned at "<=5"
*round(r(N),5) rounds counts to the nearest 5 with any counts <=5 returned as "."
qui safecount
local baseline_dia = round(r(N),5)
*Monthly resources measures through financial year:
*m4 = April, m5 = May... m1 = January of subsequent year
foreach binary of varlist m4_admitted_patients m5_admitted_patients m6_admitted_patients m7_admitted_patients m8_admitted_patients m9_admitted_patients m10_admitted_patients m11_admitted_patients m12_admitted_patients m1_admitted_patients m2_admitted_patients m3_admitted_patients m4_critical_care_patients m5_critical_care_patients m6_critical_care_patients m7_critical_care_patients m8_critical_care_patients m9_critical_care_patients m10_critical_care_patients m11_critical_care_patients m12_critical_care_patients m1_critical_care_patients m2_critical_care_patients m3_critical_care_patients {
*Number of people in each CKD group coded for each binary measure each month
qui safecount if `binary'==1
local `binary' = round(r(N),5)
}
foreach aggregate of varlist m4_hospital_days m5_hospital_days m6_hospital_days m7_hospital_days m8_hospital_days m9_hospital_days m10_hospital_days m11_hospital_days m12_hospital_days m1_hospital_days m2_hospital_days m3_hospital_days m4_critical_care_days m5_critical_care_days m6_critical_care_days m7_critical_care_days m8_critical_care_days m9_critical_care_days m10_critical_care_days m11_critical_care_days m12_critical_care_days m1_critical_care_days m2_critical_care_days m3_critical_care_days m4_emergency_days m5_emergency_days m6_emergency_days m7_emergency_days m8_emergency_days m9_emergency_days m10_emergency_days m11_emergency_days m12_emergency_days m1_emergency_days m2_emergency_days m3_emergency_days m4_op_appts m5_op_appts m6_op_appts m7_op_appts m8_op_appts m9_op_appts m10_op_appts m11_op_appts m12_op_appts m1_op_appts m2_op_appts m3_op_appts m4_gp_interactions m5_gp_interactions m6_gp_interactions m7_gp_interactions m8_gp_interactions m9_gp_interactions m10_gp_interactions m11_gp_interactions m12_gp_interactions m1_gp_interactions m2_gp_interactions m3_gp_interactions {
qui su total_`aggregate'
local `aggregate' = r(mean)
}

**Populate table for each CKD group with redacted counts
file write tablecontent ("Dialysis healthcare use") _tab _tab (`baseline_dia') _n
file write tablecontent _tab ("Hospital days") _tab _tab (`m4_hospital_days') _tab (`m5_hospital_days') _tab (`m6_hospital_days') _tab (`m7_hospital_days') _tab (`m8_hospital_days') _tab (`m9_hospital_days') _tab (`m10_hospital_days') _tab (`m11_hospital_days') _tab (`m12_hospital_days') _tab (`m1_hospital_days') _tab (`m2_hospital_days') _tab (`m3_hospital_days') _n
file write tablecontent _tab ("Hospitalised patients") _tab _tab (`m4_admitted_patients') _tab (`m5_admitted_patients') _tab (`m6_admitted_patients') _tab (`m7_admitted_patients') _tab (`m8_admitted_patients') _tab (`m9_admitted_patients') _tab (`m10_admitted_patients') _tab (`m11_admitted_patients') _tab (`m12_admitted_patients') _tab (`m1_admitted_patients') _tab (`m2_admitted_patients') _tab (`m3_admitted_patients') _n
file write tablecontent _tab ("ICU days") _tab _tab (`m4_critical_care_days') _tab (`m5_critical_care_days') _tab (`m6_critical_care_days') _tab (`m7_critical_care_days') _tab (`m8_critical_care_days') _tab (`m9_critical_care_days') _tab (`m10_critical_care_days') _tab (`m11_critical_care_days') _tab (`m12_critical_care_days') _tab (`m1_critical_care_days') _tab (`m2_critical_care_days') _tab (`m3_critical_care_days') _n
file write tablecontent _tab ("ICU patients") _tab _tab (`m4_critical_care_patients') _tab (`m5_critical_care_patients') _tab (`m6_critical_care_patients') _tab (`m7_critical_care_patients') _tab (`m8_critical_care_patients') _tab (`m9_critical_care_patients') _tab (`m10_critical_care_patients') _tab (`m11_critical_care_patients') _tab (`m12_critical_care_patients') _tab (`m1_critical_care_patients') _tab (`m2_critical_care_patients') _tab (`m3_critical_care_patients') _n
file write tablecontent _tab ("ED days") _tab _tab (`m4_emergency_days') _tab (`m5_emergency_days') _tab (`m6_emergency_days') _tab (`m7_emergency_days') _tab (`m8_emergency_days') _tab (`m9_emergency_days') _tab (`m10_emergency_days') _tab (`m11_emergency_days') _tab (`m12_emergency_days') _tab (`m1_emergency_days') _tab (`m2_emergency_days') _tab (`m3_emergency_days') _n
file write tablecontent _tab ("OPD appts") _tab _tab (`m4_op_appts') _tab (`m5_op_appts') _tab (`m6_op_appts') _tab (`m7_op_appts') _tab (`m8_op_appts') _tab (`m9_op_appts') _tab (`m10_op_appts') _tab (`m11_op_appts') _tab (`m12_op_appts') _tab (`m1_op_appts') _tab (`m2_op_appts') _tab (`m3_op_appts') _n
file write tablecontent _tab ("GP interactions") _tab _tab (`m4_gp_interactions') _tab (`m5_gp_interactions') _tab (`m6_gp_interactions') _tab (`m7_gp_interactions') _tab (`m8_gp_interactions') _tab (`m9_gp_interactions') _tab (`m10_gp_interactions') _tab (`m11_gp_interactions') _tab (`m12_gp_interactions') _tab (`m1_gp_interactions') _tab (`m2_gp_interactions') _tab (`m3_gp_interactions') _n(2)
file close tablecontent


**Redact counts of 0 from each column in table (adapted from code by Emily Herrett)
import delimited ./output/2017_healthcare_use_v3_dialysis.csv, clear
local columns " "n_`dataset'" "april" "may" "june" "july" "august" "september" "october" "november" "december" "january" "february" "march" "april" "
foreach col in `columns' {
replace `col'=. if `col'<=5
}
*/

qui safecount
local baseline_ckd = round(r(N),5)
foreach binary of varlist m4_fistula_formation m5_fistula_formation m6_fistula_formation m7_fistula_formation m8_fistula_formation m9_fistula_formation m10_fistula_formation m11_fistula_formation m12_fistula_formation m1_fistula_formation m2_fistula_formation m3_fistula_formation m4_pd_insertion m5_pd_insertion m6_pd_insertion m7_pd_insertion m8_pd_insertion m9_pd_insertion m10_pd_insertion m11_pd_insertion m12_pd_insertion m1_pd_insertion m2_pd_insertion m3_pd_insertion {
*Number of people in each CKD group coded for each binary measure each month
qui safecount if `binary'==1
local ckd_`binary' = round(r(N),5)
}
file write tablecontent ("All CKD groups") _tab _tab (`baseline_ckd') _n
file write tablecontent _tab ("AVF formations") _tab _tab (`ckd_m4_fistula_formation') _tab (`ckd_m5_fistula_formation') _tab (`ckd_m6_fistula_formation') _tab (`ckd_m7_fistula_formation') _tab (`ckd_m8_fistula_formation') _tab (`ckd_m9_fistula_formation') _tab (`ckd_m10_fistula_formation') _tab (`ckd_m11_fistula_formation') _tab (`ckd_m12_fistula_formation') _tab (`ckd_m1_fistula_formation') _tab (`ckd_m2_fistula_formation') _tab (`ckd_m3_fistula_formation') _n
file write tablecontent _tab ("PD insertions") _tab _tab (`ckd_m4_pd_insertion') _tab (`ckd_m5_pd_insertion') _tab (`ckd_m6_pd_insertion') _tab (`ckd_m7_pd_insertion') _tab (`ckd_m8_pd_insertion') _tab (`ckd_m9_pd_insertion') _tab (`ckd_m10_pd_insertion') _tab (`ckd_m11_pd_insertion') _tab (`ckd_m12_pd_insertion') _tab (`ckd_m1_pd_insertion') _tab (`ckd_m2_pd_insertion') _tab (`ckd_m3_pd_insertion') _n

forvalues egfr = 0/3 {
use ./output/`dataset'_ckd_complete_v3.dta, clear
drop if access_egfr!=`egfr'
qui safecount
local baseline_ckd_`egfr' = round(r(N),5)
foreach binary of varlist m4_fistula_formation m5_fistula_formation m6_fistula_formation m7_fistula_formation m8_fistula_formation m9_fistula_formation m10_fistula_formation m11_fistula_formation m12_fistula_formation m1_fistula_formation m2_fistula_formation m3_fistula_formation m4_pd_insertion m5_pd_insertion m6_pd_insertion m7_pd_insertion m8_pd_insertion m9_pd_insertion m10_pd_insertion m11_pd_insertion m12_pd_insertion m1_pd_insertion m2_pd_insertion m3_pd_insertion {
*Number of people in each CKD group coded for each binary measure each month
qui safecount if `binary'==1
local ckd_`binary'_`egfr' = round(r(N),5)
}
local lab`egfr': label access_egfr `egfr'
file write tablecontent ("`lab`egfr''") _tab _tab (`baseline_ckd_`egfr'') _n
file write tablecontent _tab ("AVF formations") _tab _tab (`ckd_m4_fistula_formation_`egfr'') _tab (`ckd_m5_fistula_formation_`egfr'') _tab (`ckd_m6_fistula_formation_`egfr'') _tab (`ckd_m7_fistula_formation_`egfr'') _tab (`ckd_m8_fistula_formation_`egfr'') _tab (`ckd_m9_fistula_formation_`egfr'') _tab (`ckd_m10_fistula_formation_`egfr'') _tab (`ckd_m11_fistula_formation_`egfr'') _tab (`ckd_m12_fistula_formation_`egfr'') _tab (`ckd_m1_fistula_formation_`egfr'') _tab (`ckd_m2_fistula_formation_`egfr'') _tab (`ckd_m3_fistula_formation_`egfr'') _n
file write tablecontent _tab ("PD insertions") _tab _tab (`ckd_m4_pd_insertion_`egfr'') _tab (`ckd_m5_pd_insertion_`egfr'') _tab (`ckd_m6_pd_insertion_`egfr'') _tab (`ckd_m7_pd_insertion_`egfr'') _tab (`ckd_m8_pd_insertion_`egfr'') _tab (`ckd_m9_pd_insertion_`egfr'') _tab (`ckd_m10_pd_insertion_`egfr'') _tab (`ckd_m11_pd_insertion_`egfr'') _tab (`ckd_m12_pd_insertion_`egfr'') _tab (`ckd_m1_pd_insertion_`egfr'') _tab (`ckd_m2_pd_insertion_`egfr'') _tab (`ckd_m3_pd_insertion_`egfr'') _n(2)
}

use ./output/`dataset'_ckd_complete_v3.dta, clear

**Extract healthcare use measures for dialysis group only
*CKD group categories:
*1 = eGFR >60 with albuminuria
*2 = CKD 3A
*3 = CKD 4/5 without kidney replacement therapy
*4 = Dialysis
*5 = Kidney transplant
*6 = Kidney replacement therapy unknown modality
drop if ckd_group!=4
*Disclosure minimisation:
*safecount provides a count with any counts <=5 returned at "<=5"
*round(r(N),5) rounds counts to the nearest 5 with any counts <=5 returned as "."
qui safecount
local baseline_dia = round(r(N),5)
*Monthly resources measures through financial year:
*m4 = April, m5 = May... m1 = January of subsequent year
foreach binary of varlist m4_admitted_patients m5_admitted_patients m6_admitted_patients m7_admitted_patients m8_admitted_patients m9_admitted_patients m10_admitted_patients m11_admitted_patients m12_admitted_patients m1_admitted_patients m2_admitted_patients m3_admitted_patients m4_critical_care_patients m5_critical_care_patients m6_critical_care_patients m7_critical_care_patients m8_critical_care_patients m9_critical_care_patients m10_critical_care_patients m11_critical_care_patients m12_critical_care_patients m1_critical_care_patients m2_critical_care_patients m3_critical_care_patients {
*Number of people in each CKD group coded for each binary measure each month
qui safecount if `binary'==1
local `binary' = round(r(N),5)
}
foreach aggregate of varlist m4_hospital_days m5_hospital_days m6_hospital_days m7_hospital_days m8_hospital_days m9_hospital_days m10_hospital_days m11_hospital_days m12_hospital_days m1_hospital_days m2_hospital_days m3_hospital_days m4_critical_care_days m5_critical_care_days m6_critical_care_days m7_critical_care_days m8_critical_care_days m9_critical_care_days m10_critical_care_days m11_critical_care_days m12_critical_care_days m1_critical_care_days m2_critical_care_days m3_critical_care_days m4_emergency_days m5_emergency_days m6_emergency_days m7_emergency_days m8_emergency_days m9_emergency_days m10_emergency_days m11_emergency_days m12_emergency_days m1_emergency_days m2_emergency_days m3_emergency_days m4_op_appts m5_op_appts m6_op_appts m7_op_appts m8_op_appts m9_op_appts m10_op_appts m11_op_appts m12_op_appts m1_op_appts m2_op_appts m3_op_appts m4_gp_interactions m5_gp_interactions m6_gp_interactions m7_gp_interactions m8_gp_interactions m9_gp_interactions m10_gp_interactions m11_gp_interactions m12_gp_interactions m1_gp_interactions m2_gp_interactions m3_gp_interactions {
qui su total_`aggregate'
local `aggregate' = r(mean)
}

**Populate table for each CKD group with redacted counts
file write tablecontent ("Dialysis healthcare use") _tab _tab (`baseline_dia') _n
file write tablecontent _tab ("Hospital days") _tab _tab (`m4_hospital_days') _tab (`m5_hospital_days') _tab (`m6_hospital_days') _tab (`m7_hospital_days') _tab (`m8_hospital_days') _tab (`m9_hospital_days') _tab (`m10_hospital_days') _tab (`m11_hospital_days') _tab (`m12_hospital_days') _tab (`m1_hospital_days') _tab (`m2_hospital_days') _tab (`m3_hospital_days') _n
file write tablecontent _tab ("Hospitalised patients") _tab _tab (`m4_admitted_patients') _tab (`m5_admitted_patients') _tab (`m6_admitted_patients') _tab (`m7_admitted_patients') _tab (`m8_admitted_patients') _tab (`m9_admitted_patients') _tab (`m10_admitted_patients') _tab (`m11_admitted_patients') _tab (`m12_admitted_patients') _tab (`m1_admitted_patients') _tab (`m2_admitted_patients') _tab (`m3_admitted_patients') _n
file write tablecontent _tab ("ICU days") _tab _tab (`m4_critical_care_days') _tab (`m5_critical_care_days') _tab (`m6_critical_care_days') _tab (`m7_critical_care_days') _tab (`m8_critical_care_days') _tab (`m9_critical_care_days') _tab (`m10_critical_care_days') _tab (`m11_critical_care_days') _tab (`m12_critical_care_days') _tab (`m1_critical_care_days') _tab (`m2_critical_care_days') _tab (`m3_critical_care_days') _n
file write tablecontent _tab ("ICU patients") _tab _tab (`m4_critical_care_patients') _tab (`m5_critical_care_patients') _tab (`m6_critical_care_patients') _tab (`m7_critical_care_patients') _tab (`m8_critical_care_patients') _tab (`m9_critical_care_patients') _tab (`m10_critical_care_patients') _tab (`m11_critical_care_patients') _tab (`m12_critical_care_patients') _tab (`m1_critical_care_patients') _tab (`m2_critical_care_patients') _tab (`m3_critical_care_patients') _n
file write tablecontent _tab ("ED days") _tab _tab (`m4_emergency_days') _tab (`m5_emergency_days') _tab (`m6_emergency_days') _tab (`m7_emergency_days') _tab (`m8_emergency_days') _tab (`m9_emergency_days') _tab (`m10_emergency_days') _tab (`m11_emergency_days') _tab (`m12_emergency_days') _tab (`m1_emergency_days') _tab (`m2_emergency_days') _tab (`m3_emergency_days') _n
file write tablecontent _tab ("OPD appts") _tab _tab (`m4_op_appts') _tab (`m5_op_appts') _tab (`m6_op_appts') _tab (`m7_op_appts') _tab (`m8_op_appts') _tab (`m9_op_appts') _tab (`m10_op_appts') _tab (`m11_op_appts') _tab (`m12_op_appts') _tab (`m1_op_appts') _tab (`m2_op_appts') _tab (`m3_op_appts') _n
file write tablecontent _tab ("GP interactions") _tab _tab (`m4_gp_interactions') _tab (`m5_gp_interactions') _tab (`m6_gp_interactions') _tab (`m7_gp_interactions') _tab (`m8_gp_interactions') _tab (`m9_gp_interactions') _tab (`m10_gp_interactions') _tab (`m11_gp_interactions') _tab (`m12_gp_interactions') _tab (`m1_gp_interactions') _tab (`m2_gp_interactions') _tab (`m3_gp_interactions') _n(2)
file close tablecontent


**Redact counts of 0 from each column in table (adapted from code by Emily Herrett)
import delimited ./output/`dataset'_healthcare_use_v3_dialysis.csv, clear
local columns " "n_`dataset'" "april" "may" "june" "july" "august" "september" "october" "november" "december" "january" "february" "march" "april" "
foreach col in `columns' {
replace `col'=. if `col'<=5
}
export delimited "./output/`dataset'_healthcare_use_v3_dialysis.csv", replace
/*
import delimited ./output/2017_healthcare_use_v3_dialysis.csv, clear
local columns " "n_2017" "april" "may" "june" "july" "august" "september" "october" "november" "december" "january" "february" "march" "april" "
foreach col in `columns' {
replace `col'=. if `col'<=5
}
export delimited "./output/2017_healthcare_use_v3_dialysis.csv", replace
*/