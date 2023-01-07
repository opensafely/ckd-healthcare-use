sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_ckd_complete, replace t
clear

* Merge `dataset'_ckd with `dataset'_ckd_complete
capture noisily import delimited ./output/`dataset'_ckd.csv, clear
tempfile `dataset'_ckd
save ``dataset'_ckd', replace
capture noisily import delimited ./output/input_`dataset'_ckd_complete.csv, clear
merge 1:1 patient_id using ``dataset'_ckd'
keep if _merge==3
drop _merge
tempfile `dataset'_ckd_complete
save ``dataset'_ckd_complete', replace

/* Generate dummy data
cd ckd-healthcare-use
capture noisily import delimited ./output/2017_ckd.csv, clear
tempfile 2017_ckd
save 2017_ckd, replace
capture noisily import delimited ./output/input_2017_ckd_complete.csv, clear
merge 1:1 patient_id using 2017_ckd
keep if _merge==3
drop _merge
tempfile 2017_ckd_complete
save 2017_ckd_complete, replace
*/

* Baseline dialysis & kidney transplant group classification
drop dialysis_baseline_primary_care
drop dialysis_baseline_icd_10
drop dialysis_baseline_opcs_4
drop kt_baseline_primary_care
drop kt_baseline_icd_10
drop kt_baseline_opcs_4
gen dialysis_baseline = date(dialysis_baseline_date, "YMD")
format dialysis_baseline %td
drop dialysis_baseline_date
gen kidney_transplant_baseline = date(kidney_transplant_baseline_date, "YMD")
format kidney_transplant_baseline %td
drop kidney_transplant_baseline_date
sum dialysis_baseline, detail
sum kidney_transplant_baseline, detail
gen dialysis_baseline2 = dialysis_baseline - kidney_transplant_baseline
gen dialysis_baseline3 = 0
replace dialysis_baseline3 = 1 if dialysis_baseline2 > 0
gen kidney_transplant_baseline2 = kidney_transplant_baseline - dialysis_baseline
gen kidney_transplant_baseline3 = 0
replace kidney_transplant_baseline3 = 1 if kidney_transplant_baseline2 > 0
gen dialysis = 0
replace dialysis = 1 if dialysis_baseline!=.
replace dialysis = 0 if kidney_transplant_baseline > dialysis_baseline
gen kidney_transplant = 0
replace kidney_transplant = 1 if kidney_transplant_baseline!=.
replace kidney_transplant = 0 if dialysis_baseline > kidney_transplant_baseline
drop dialysis_baseline
drop kidney_transplant_baseline
tab dialysis dialysis_baseline3, m
tab kidney_transplant kidney_transplant_baseline3, m
tab dialysis kidney_transplant, m

* CKD stage classification based on baseline eGFR
egen ckd_group = cut(baseline_egfr), at(0, 30, 60, 5000)
drop baseline_egfr
recode ckd_group 0=3 30=2 60=1
replace ckd_group = 4 if dialysis==1
drop dialysis
replace ckd_group = 5 if kidney_transplant==1
drop kidney_transplant
label define ckd_group 1 "eGFR ≥60 with albuminuria" 2 "CKD 3" 3 "CKD 4/5 without kidney replacement therapy" 4 "Dialysis" 5 "Kidney transplant"
label values ckd_group ckd_group
label var ckd_group "CKD group"

* Dialysis & kidney transplant outcome classification
drop dialysis_outcome_primary_care
drop dialysis_outcome_icd_10
drop dialysis_outcome_opcs_4
gen dialysis_outcome_date = date(dialysis_outcome, "YMD")
format dialysis_outcome_date %td
drop dialysis_outcome
gen kidney_transplant_outcome_date = date(kidney_transplant_outcome, "YMD")
format kidney_transplant_outcome_date %td
drop kidney_transplant_outcome
sum dialysis_outcome_date, detail
sum kidney_transplant_outcome_date, detail
gen index_date = mdy(04, 01, 2017)
gen dialysis_outcome = dialysis_outcome_date - index_date
gen kidney_transplant_outcome = kidney_transplant_outcome_date - index_date
sum dialysis_outcome, detail
sum kidney_transplant_outcome, detail
gen dialysis_outcome2 = dialysis_outcome_date - kidney_transplant_outcome_date
gen dialysis_outcome3 = 0
replace dialysis_outcome3 = 1 if dialysis_outcome2 > 0
gen kidney_transplant_outcome2 = kidney_transplant_outcome_date - dialysis_outcome_date
gen kidney_transplant_outcome3 = 0
replace kidney_transplant_outcome3 = 1 if kidney_transplant_outcome2 > 0
gen dialysis_new = 0
replace dialysis_new = 1 if dialysis_outcome_date!=.
replace dialysis_new = 0 if kidney_transplant_outcome_date > dialysis_outcome_date
replace dialysis_new = 0 if ckd_group==4
replace dialysis_new = 0 if ckd_group==5
gen kidney_transplant_new = 0
replace kidney_transplant_new = 1 if kidney_transplant_outcome_date!=.
replace kidney_transplant_new = 0 if dialysis_outcome_date > kidney_transplant_outcome_date
replace kidney_transplant_new = 0 if ckd_group==4
replace kidney_transplant_new = 0 if ckd_group==5
tab dialysis_new kidney_transplant_new, m
tab dialysis_new dialysis_outcome3, m
tab kidney_transplant_new kidney_transplant_outcome3, m
drop dialysis_outcome_date
drop kidney_transplant_outcome_date

* eGFR outcome classification based on updated mean eGFR over previous 18 months by the end of year
gen sex = 1 if male == "Male"
replace sex = 0 if male == "Female"
label define sex 0"Female" 1"Male"
label values sex sex
replace creatinine_outcome = . if !inrange(creatinine_outcome, 20, 3000)
gen mgdl_creatinine_outcome = creatinine_outcome/88.4
gen min_creatinine_outcome=.
replace min_creatinine_outcome = mgdl_creatinine_outcome/0.7 if sex==0
replace min_creatinine_outcome = mgdl_creatinine_outcome/0.9 if sex==1
replace min_creatinine_outcome = min_creatinine_outcome^-0.329  if sex==0
replace min_creatinine_outcome = min_creatinine_outcome^-0.411  if sex==1
replace min_creatinine_outcome = 1 if min_creatinine_outcome<1
gen max_creatinine_outcome=.
replace max_creatinine_outcome = mgdl_creatinine_outcome/0.7 if sex==0
replace max_creatinine_outcome = mgdl_creatinine_outcome/0.9 if sex==1
replace max_creatinine_outcome = max_creatinine_outcome^-1.209
replace max_creatinine_outcome = 1 if max_creatinine_outcome>1
gen egfr_outcome = min_creatinine_outcome*max_creatinine_outcome*141
replace egfr_outcome = egfr_outcome*(0.993^age)
replace egfr_outcome = egfr_outcome*1.018 if sex==0
drop creatinine_outcome
drop mgdl_creatinine_outcome
drop min_creatinine_outcome
drop max_creatinine_outcome
egen egfr_end = cut(egfr_outcome), at(0, 30, 60, 5000)
drop egfr_outcome
recode egfr_end 0=3 30=2 60=1
label define egfr_end 1 "≥60" 2 "30-59" 3 "<30"
label values egfr_end egfr_end
label var egfr_end "Final eGFR"
gen ckd_progression = 0
replace ckd_progression = 1 if egfr_end==2 & ckd_group==1
replace ckd_progression = 2 if egfr_end==3 & ckd_group==1
replace ckd_progression = 2 if egfr_end==3 & ckd_group==2
replace ckd_progression = 3 if dialysis_new==1
replace ckd_progression = 4 if kidney_transplant_new==1
replace ckd_progression = 5 if died==1
drop dialysis_new
drop kidney_transplant_new
label define ckd_progression 0 "No progression" 1 "CKD 3" 2 "CKD 4/5 without kidney replacement therapy" 3 "Dialysis" 4 "Kidney transplant" 5 "Died"
label values ckd_progression ckd_progression
label var ckd_progression "CKD progression"

**Potential effect modifiers
* Ethnicity
* 1 = White ethnicities (white British, white Irish, with other)
* 2 = Mixed ethnicities (white & black Caribbean, white & black African, white & Asian, other mixed ethnicities)
* 3 = South Asian ethnicities (Indian, Pakistani, Bangladeshi, other South Asian)
* 4 = Black ethnicities (black Caribbean, black African, other black)
* 5 = Other ethnicities (Chinese, all other ethnicities)
* . = Unknown ethnicity
replace ethnicity = . if ethnicity==.
replace ethnicity=6 if ethnicity==2
replace ethnicity=2 if ethnicity==3
replace ethnicity=3 if ethnicity==4
replace ethnicity=4 if ethnicity==6
replace ethnicity=6 if ethnicity==.
label define ethnicity	1 "White"  					///
						2 "South Asian"				///						
						3 "Black"  					///
						4 "Mixed"					///
						5 "Other"					///
						6 "Unknown"	
label values ethnicity ethnicity

* Index of multiple deprivation
* Ordered 1-5 from most deprived to least deprived
label define imd 1 "1 Most deprived" 2 "2" 3 "3" 4 "4" 5 "5 Least deprived"
label values imd imd

* Region
rename region region_string
gen region = 1 if region_string=="East Midlands"
replace region = 2 if region_string=="East"
replace region = 3 if region_string=="London"
replace region = 4 if region_string=="North East"
replace region = 5 if region_string=="North West"
replace region = 6 if region_string=="South East"
replace region = 7 if region_string=="South West"
replace region = 8 if region_string=="West Midlands"
replace region = 9 if region_string=="Yorkshire and The Humber"
label define region 	1 "East Midlands" 					///
						2 "East"   							///
						3 "London" 							///
						4 "North East" 						///
						5 "North West" 						///
						6 "South East" 						///
						7 "South West"						///
						8 "West Midlands" 					///
						9 "Yorkshire and The Humber"		
label values region region
label var region "Region"

* Urban/rural
replace rural_urban=. if rural_urban<1|rural_urban>8
label define rural_urban 1 "Urban major conurbation" 						///
						 2 "Urban minor conurbation" 						///
						 3 "Urban city and town" 							///
						 4 "Urban city and town in a sparse setting" 		///
						 5 "Rural town and fringe" 							///
						 6 "Rural town and fringe in a sparse setting" 		///
						 7 "Rural village and dispersed" 					///
						 8 "Rural village and dispersed in a sparse setting"
label values rural_urban rural_urban
* Urban (binary)
* Urban = 1-4 + missing, Rural = 5-8
generate urban=.
replace urban=1 if rural_urban<=4|rural_urban==.
replace urban=0 if rural_urban>4 & rural_urban!=.
label var urban "Urban/rural"
label define urban 0 "Rural" 1 "Urban"
label values urban urban
drop rural_urban

save "./output/`dataset'_ckd_complete.dta", replace

log close
