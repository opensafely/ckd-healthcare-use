sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
macro drop hr
log using ./logs/hrg4_`dataset'.log, replace t

*Merge `dataset'_ckd with `dataset'_ckd_hrg4
capture noisily import delimited ./output/`dataset'_ckd.csv, clear
tempfile `dataset'_ckd
save ``dataset'_ckd', replace
capture noisily import delimited ./output/input_`dataset'_ckd_hrg4.csv, clear
merge 1:1 patient_id using ``dataset'_ckd'
keep if _merge==3
drop _merge
tempfile `dataset'_ckd_hrg4
save ``dataset'_ckd_hrg4', replace

/*Generate dummy data
cd ckd-healthcare-use
capture noisily import delimited ./output/2017_ckd.csv, clear
tempfile 2017_ckd
save ./output/2017_ckd, replace
capture noisily import delimited ./output/input_2017_ckd_hrg4.csv, clear
merge 1:1 patient_id using ./output/2017_ckd
keep if _merge==3
drop _merge
tempfile 2017_ckd_hrg4
save ./output/2017_ckd_hrg4, replace
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
save ``dataset'_ckd_hrg4', replace

*Merge `dataset'_nockd with `dataset'_nockd_hrg4
capture noisily import delimited ./output/`dataset'_nockd.csv, clear
tempfile `dataset'_nockd
save ``dataset'_nockd', replace
capture noisily import delimited ./output/input_`dataset'_nockd_hrg4.csv, clear
merge 1:1 patient_id using ``dataset'_nockd'
keep if _merge==3
drop _merge
gen ckd_group = 1

merge 1:1 patient_id using ``dataset'_ckd_hrg4'


cap file close tablecontent
file open tablecontent using ./output/hrg4_`dataset'.csv, write text replace

file write tablecontent ("hrg") _tab ("nockd_count") _tab ("nockd_admissions") _tab ("ckd3_count") _tab ("ckd3_admissions") _tab ("ckd4_count") _tab ("ckd4_admissions") _tab ("dialysis_count") _tab ("dialysis_admissions") _tab ("kt_count") _tab ("kt_admissions") _n

file write tablecontent ("n")
forvalues i=1/5 {
qui safecount if ckd_group==`i'
local group_`i' = round(r(N),5)
if `group_`i'' > 5 & `group_`i''!=. {
file write tablecontent _tab (`group_`i'') _tab ("N/A")
}
else {
file write tablecontent _tab ("REDACTED") _tab ("N/A")
}
}
file write tablecontent _n

global hrg "wj11 xd01 xd02 xd03 xd04 xd05 xd06 xd07 xd08 xd09 xd10 xd11 xd12 xd13 xd14 xd15 xd16 xd17 xd18 xd19 xd20 xd21 xd22 xd23 xd24 xd25 xd26 xd27 xd28 xd29 xd30 xd31 xd32 xd33 xd34 xd37 xd38 xd39 xd40 xd41 xd42 xd43 xd44 xd45 xd46 xd47 xd48 xd49 xd50 xd51 xd52 xd53 xd54 xd55 xd56 xd57 xd58 xd90 xd91 ya03 ya04 ya10 ya11 ya12 ya13 yc01 yc10 yd01 yd02 yd03 yd04 yd05 yf01 yf04 yg01 yg02 yg05 yg06 yg07 yg10 yg11 yg12 yh02 yh03 yh10 yh20 yh30 yh31 yh32 yj09 yj11 yj13 yj15 yl02 yl11 yl12 yl20 yl21 yl30 yq05 yq07 yq08 yq09 yq12 yq13 yq15 yq16 yq22 yq26 yq31 yq32 yq40 yq41 yq42 yq50 yq51 yr11 yr12 yr15 yr16 yr22 yr23 yr24 yr25 yr26 yr31 yr33 yr40 yr41 yr42 yr43 yr44 yr45 yr48 yr50 yr51 yr52 yr53 yr54 yr56 yr57 yr63 yr65 yr66 yr67"

foreach hrg of global hrg {
file write tablecontent ("`hrg'")
bysort ckd_group: egen total_`hrg'_admissions = total(`hrg'_admissions)
forvalues i=1/5 {
qui safecount if ckd_group==`i' & `hrg'_admissions>0
local `hrg'_count_`i' = round(r(N),5)
qui su total_`hrg'_admissions if ckd_group==`i'
local `hrg'_admissions_`i' = r(mean)
if ``hrg'_count_`i'' >5 & ``hrg'_count_`i''!=. {
file write tablecontent _tab (``hrg'_count_`i'') _tab (``hrg'_admissions_`i'') 
}
else {
file write tablecontent _tab ("REDACTED") _tab ("REDACTED")
}
}
drop `hrg'_admissions
drop total_`hrg'_admissions
file write tablecontent _n
}



file close tablecontent