sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

cap log close
log using ./logs/2020_dialysis, replace t
clear

import delimited ./output/input_2020.csv, delimiter(comma) varnames(1) case(preserve) 


**Exclusions
* Age <18 at index date
drop if age <18

* Anyone not registered at one practice for 3 months before index date
drop if has_follow_up==0
drop has_follow_up

* Deceased before index date
drop if deceased==1
drop deceased

* Region
tab region
drop if region==""

* IMD
tab imd
drop if imd==0
drop if imd==.

* Calculate eGFR
assert inlist(sex, "M", "F")
gen male = (sex=="M")
drop sex
label define sexLab 1 "Male" 0 "Female"
label values male sexLab
label var male "Sex (0=F 1=M)"
replace latest_creatinine = . if !inrange(latest_creatinine, 20, 3000)
gen mgdl_latest_creatinine = latest_creatinine/88.4
gen min_latest_creatinine=.
replace min_latest_creatinine = mgdl_latest_creatinine/0.7 if male==0
replace min_latest_creatinine = mgdl_latest_creatinine/0.9 if male==1
replace min_latest_creatinine = min_latest_creatinine^-0.329  if male==0
replace min_latest_creatinine = min_latest_creatinine^-0.411  if male==1
replace min_latest_creatinine = 1 if min_latest_creatinine<1
gen max_latest_creatinine=.
replace max_latest_creatinine = mgdl_latest_creatinine/0.7 if male==0
replace max_latest_creatinine = mgdl_latest_creatinine/0.9 if male==1
replace max_latest_creatinine = max_latest_creatinine^-1.209
replace max_latest_creatinine = 1 if max_latest_creatinine>1
gen latest_egfr = min_latest_creatinine*max_latest_creatinine*141
replace latest_egfr = latest_egfr*(0.993^age)
replace latest_egfr = latest_egfr*1.018 if male==0
drop latest_creatinine
drop mgdl_latest_creatinine
drop min_latest_creatinine
drop max_latest_creatinine
egen esrd_egfr = cut(latest_egfr), at(0, 15, 5000)
recode esrd_egfr 0=1 15=0
replace esrd_egfr = 0 if latest_egfr==.

* Correlate dialysis codes
tab dialysis_primary_care dialysis_icd_10
tab dialysis_primary_care dialysis_opcs_4
tab esrd_egfr dialysis_primary_care
tab esrd_egfr dialysis_icd_10
tab esrd_egfr dialysis_opcs_4

gen dialysis_sus = dialysis_icd_10
replace dialysis_sus = 1 if dialysis_opcs_4==1
tab esrd_egfr dialysis_sus
tab dialysis_primary_care dialysis_sus

gen dialysis_sus_egfr = dialysis_sus
replace dialysis_sus_egfr = 0 if esrd_egfr==0
tab dialysis_primary_care dialysis_sus_egfr

tab ukrr

log close


