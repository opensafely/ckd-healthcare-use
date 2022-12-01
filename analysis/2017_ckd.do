cap log close
log using ./logs/2017_ckd, replace t
clear

import delimited ./output/input_2017.csv, delimiter(comma) varnames(1) case(preserve) 

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

* eGFR>60 without albuminuria
assert inlist(sex, "M", "F")
gen male = (sex=="M")
drop sex
label define sexLab 1 "Male" 0 "Female"
label values male sexLab
label var male "Sex (0=F 1=M)"
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
gen ckd = 0
replace ckd = 1 if baseline_egfr <60
*replace ckd = 1 if albuminuria >3
foreach krt of varlist 	dialysis_primary_care 			///
						dialysis_icd_10					///
						dialysis_opcs_4					///
						kidney_transplant_primary_care	///
						kidney_transplant_icd_10		///
						kidney_transplant_opcs_4 		{
replace ckd = 1 if `krt'==1
drop `krt'
}
drop if ckd==0
drop ckd

export delimited using "./output/2017_ckd.csv", replace

log close
