sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_ckd, replace t
clear

import delimited ./output/input_`dataset'.csv, delimiter(comma) varnames(1) case(preserve)

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

* Code sex
assert inlist(sex, "M", "F")
gen male = (sex=="M")
drop sex
label define sexLab 1 "Male" 0 "Female"
label values male sexLab
label var male "Sex (0=F 1=M)"

save ./output/input_`dataset', replace

* eGFR>60 without albuminuria
gen albuminuria = 0
replace albuminuria = 1 if acr >=3
replace albuminuria = 0 if acr_operator =="<"
replace albuminuria = 0 if acr_operator =="<="
label define albuminuria 0 "No albuminuria" 1 "Albuminuria"
label values albuminuria albuminuria
replace baseline_creatinine = . if !inrange(baseline_creatinine, 20, 3000)
gen mgdl_baseline_creatinine = baseline_creatinine/88.4
gen min_baseline_creatinine=.
replace min_baseline_creatinine = mgdl_baseline_creatinine/0.7 if male==0
replace min_baseline_creatinine = mgdl_baseline_creatinine/0.9 if male==1
replace min_baseline_creatinine = min_baseline_creatinine^-0.329  if male==0
replace min_baseline_creatinine = min_baseline_creatinine^-0.411  if male==1
replace min_baseline_creatinine = 1 if min_baseline_creatinine<1
gen max_baseline_creatinine=.
replace max_baseline_creatinine = mgdl_baseline_creatinine/0.7 if male==0
replace max_baseline_creatinine = mgdl_baseline_creatinine/0.9 if male==1
replace max_baseline_creatinine = max_baseline_creatinine^-1.209
replace max_baseline_creatinine = 1 if max_baseline_creatinine>1
gen baseline_egfr = min_baseline_creatinine*max_baseline_creatinine*141
replace baseline_egfr = baseline_egfr*(0.993^age)
replace baseline_egfr = baseline_egfr*1.018 if male==0
drop baseline_creatinine
drop mgdl_baseline_creatinine
drop min_baseline_creatinine
drop max_baseline_creatinine
gen ckd = albuminuria
replace ckd = 1 if baseline_egfr <60
sum acr, de
tab acr_operator
tab albuminuria
tab ckd
egen egfr_status = cut(baseline_egfr), at(0, 60, 5000)
recode egfr_status 0=2 60=1
replace egfr_status = 0 if baseline_egfr==.
foreach krt of varlist 	dialysis_primary_care 			///
						dialysis_icd_10					///
						dialysis_opcs_4					///
						kidney_transplant_primary_care	///
						kidney_transplant_icd_10		///
						kidney_transplant_opcs_4 		{
tab `krt'
replace egfr_status=3 if `krt'==1
replace ckd = 1 if `krt'==1
drop `krt'
}
label define egfr_status 0 "No eGFR" 1 "eGFR >=60" 2 "eGFR <60" 3 "KRT"
label values egfr_status egfr_status
tab egfr_status albuminuria
tab ckd, m
drop if ckd==0
drop ckd
drop acr
drop acr_operator
tab egfr_status albuminuria
drop albuminuria
drop egfr_status

export delimited using "./output/`dataset'_ckd.csv", replace

*Create dataset of non-CKD
merge 1:1 patient_id using ./output/input_`dataset'
keep if _merge==2
drop _merge

***Random sample of 25% of non-CKD population for tariff distribution analysis - should not be run for main analyses
gen random_order = runiform()              
sort random_order                          
safecount                                   
local total_obs = r(N)                     
local drop_count = ceil(0.75 * `total_obs') 
drop in 1/`drop_count'  

export delimited using "./output/`dataset'_nockd.csv", replace

log close
