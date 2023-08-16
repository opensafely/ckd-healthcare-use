sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_ckd_complete, replace t
clear

*Merge `dataset'_ckd with `dataset'_ckd_complete
capture noisily import delimited ./output/`dataset'_ckd.csv, clear
tempfile `dataset'_ckd
save ``dataset'_ckd', replace
capture noisily import delimited ./output/input_`dataset'_ckd_complete.csv, clear
merge 1:1 patient_id using ``dataset'_ckd'
keep if _merge==3
drop _merge
tempfile `dataset'_ckd_complete
save ``dataset'_ckd_complete', replace

/*Generate dummy data
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

*CKD stage classification
foreach var of varlist 	dialysis_baseline_primary_care	///
						dialysis_baseline_icd_10		///
						dialysis_baseline_opcs_4		///
						dialysis_baseline_date			///
						kt_baseline_primary_care		///
						kt_baseline_icd_10				///
						kt_baseline_opcs_4				{
	drop `var'
	}
tab modality_baseline, m
*To reduce misclassification of dialysis, anyone with eGFR >15 with modality_baseline=="Dialysis" will be reclassified as non-dialysis (e.g. they may have received acute dialysis and recovered)
*For modality_baseline="Modality unclear" (i.e. whose dialysis and kidney transplant baseline dates are identical), those with eGFR <15 will be assumed to be on dialysis and those >15 as kidney transplant
egen esrd_egfr = cut(baseline_egfr), at (0, 15, 5000)
recode esrd_egfr 0=1 15=0
tab esrd_egfr, m
gen dialysis = 0
replace dialysis = 1 if modality_baseline=="Dialysis"
replace dialysis = 1 if modality_baseline=="Modality unclear" & esrd_egfr!=.
replace dialysis = 0 if esrd_egfr==0
gen kidney_transplant = 0
replace kidney_transplant = 1 if kidney_transplant_baseline_date!=""
replace kidney_transplant = 0 if dialysis==1
gen modality_unclear = 0
replace modality_unclear = 1 if modality_baseline=="Modality unclear"
replace modality_unclear = 0 if dialysis==1
replace modality_unclear = 0 if kidney_transplant==1
tab modality_baseline dialysis
tab modality_baseline kidney_transplant
tab modality_baseline modality_unclear
tab dialysis kidney_transplant
egen ckd_group = cut(baseline_egfr), at(0, 30, 60, 5000)
recode ckd_group 0=3 30=2 60=1
replace ckd_group = 4 if dialysis==1
replace ckd_group = 5 if kidney_transplant==1
replace ckd_group = 6 if modality_unclear==1
*ckd_group==. are those with albuminuria without available eGFR measurement or code for KRT
replace ckd_group = 1 if ckd_group==.
label define ckd_group 1 "Albuminuria" 2 "CKD stage 3" 3 "CKD stage 4/5" 4 "Dialysis" 5 "Transplant" 6 "KRT unclear modality"
label values ckd_group ckd_group
label var ckd_group "CKD group"
tab ckd_group, m
drop if ckd_group==.
tab ckd_group modality_baseline

*Dialysis & kidney transplant outcome classification
foreach var of varlist 	dialysis_outcome_primary_care	///
						dialysis_outcome_icd_10			///
						dialysis_outcome_opcs_4			///
						dialysis_outcome_date			///
						kt_outcome_primary_care			///
						kt_outcome_icd_10				///
						kt_outcome_opcs_4				///
						kidney_transplant_outcome_date 	///
						died							{
	drop `var'
	}
tab ckd_group modality_outcome, m

*eGFR outcome classification based on updated mean eGFR over previous 18 months by the end of year
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
recode egfr_end 0=3 30=2 60=1
label define egfr_end 1 "≥60" 2 "30-59" 3 "<30"
label values egfr_end egfr_end
label var egfr_end "Final eGFR"
gen ckd_progression = 0
replace ckd_progression = 1 if egfr_end==2 & ckd_group==1
replace ckd_progression = 2 if egfr_end==3 & ckd_group==1
replace ckd_progression = 2 if egfr_end==3 & ckd_group==2
egen esrd_egfr_end = cut(egfr_outcome), at (0, 15, 5000)
recode esrd_egfr_end 0=1 15=0
tab esrd_egfr_end, m
gen dialysis_outcome = 0
replace dialysis_outcome = 1 if modality_outcome=="Dialysis"
replace dialysis_outcome = 1 if modality_outcome=="Modality unclear" & esrd_egfr_end==1
gen kidney_transplant_outcome = 0
replace kidney_transplant_outcome = 1 if modality_outcome=="Kidney transplant"
replace kidney_transplant_outcome = 1 if modality_outcome=="Modality unclear" & esrd_egfr_end==0
replace ckd_progression = 5 if modality_outcome=="Modality unclear"
replace ckd_progression = 3 if dialysis_outcome==1
replace ckd_progression = 4 if kidney_transplant_outcome==1
replace ckd_progression = 6 if modality_outcome=="Deceased"
label define ckd_progression 0 "No progression" 1 "CKD 3" 2 "CKD 4/5 pre-KRT" 3 "Dialysis" 4 "Kidney transplant" 5 "KRT unclear modality" 6 "Deceased"
label values ckd_progression ckd_progression
label var ckd_progression "CKD progression"
tab ckd_progression, m

*eGFR cut-offs to investigate timing of access formation
egen access_egfr = cut(baseline_egfr), at (0, 15, 5000)
recode access_egfr 0=1 15=2
replace access_egfr=0 if ckd_group==4
replace access_egfr=3 if access_egfr==.
label define access_egfr 0 "Dialysis" 1 "eGFR 0-14" 2 "eGFR >= 15" 3 "Unknown"
label values access_egfr access_egfr

*Totals for non-binary healthcare resource outcomes
foreach aggregate of varlist m4_hospital_days m5_hospital_days m6_hospital_days m7_hospital_days m8_hospital_days m9_hospital_days m10_hospital_days m11_hospital_days m12_hospital_days m1_hospital_days m2_hospital_days m3_hospital_days m4_critical_care_days m5_critical_care_days m6_critical_care_days m7_critical_care_days m8_critical_care_days m9_critical_care_days m10_critical_care_days m11_critical_care_days m12_critical_care_days m1_critical_care_days m2_critical_care_days m3_critical_care_days m4_emergency_days m5_emergency_days m6_emergency_days m7_emergency_days m8_emergency_days m9_emergency_days m10_emergency_days m11_emergency_days m12_emergency_days m1_emergency_days m2_emergency_days m3_emergency_days m4_op_appts m5_op_appts m6_op_appts m7_op_appts m8_op_appts m9_op_appts m10_op_appts m11_op_appts m12_op_appts m1_op_appts m2_op_appts m3_op_appts m4_neph_appts m5_neph_appts m6_neph_appts m7_neph_appts m8_neph_appts m9_neph_appts m10_neph_appts m11_neph_appts m12_neph_appts m1_neph_appts m2_neph_appts m3_neph_appts m4_tx_appts m5_tx_appts m6_tx_appts m7_tx_appts m8_tx_appts m9_tx_appts m10_tx_appts m11_tx_appts m12_tx_appts m1_tx_appts m2_tx_appts m3_tx_appts m4_gp_interactions m5_gp_interactions m6_gp_interactions m7_gp_interactions m8_gp_interactions m9_gp_interactions m10_gp_interactions m11_gp_interactions m12_gp_interactions m1_gp_interactions m2_gp_interactions m3_gp_interactions {
bysort ckd_group: egen total_`aggregate' = total(`aggregate')
egen overall_`aggregate' = total(`aggregate')
tab ckd_group, sum(total_`aggregate')
sum overall_`aggregate'
}

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

/*
save "./output/2017_ckd_complete.dta", replace
*/


