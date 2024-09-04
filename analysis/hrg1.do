sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
macro drop hr
log using ./logs/hrg1_`dataset'.log, replace t

*Merge `dataset'_ckd with `dataset'_ckd_hrg1
capture noisily import delimited ./output/`dataset'_ckd.csv, clear
tempfile `dataset'_ckd
save ``dataset'_ckd', replace
capture noisily import delimited ./output/input_`dataset'_ckd_hrg1.csv, clear
merge 1:1 patient_id using ``dataset'_ckd'
keep if _merge==3
drop _merge
tempfile `dataset'_ckd_hrg1
save ``dataset'_ckd_hrg1', replace

/*Generate dummy data
cd ckd-healthcare-use
capture noisily import delimited ./output/2017_ckd.csv, clear
tempfile 2017_ckd
save ./output/2017_ckd, replace
capture noisily import delimited ./output/input_2017_ckd_hrg1.csv, clear
merge 1:1 patient_id using ./output/2017_ckd
keep if _merge==3
drop _merge
tempfile 2017_ckd_hrg1
save ./output/2017_ckd_hrg1, replace
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
save ``dataset'_ckd_hrg1', replace

*Merge `dataset'_nockd with `dataset'_nockd_hrg1
capture noisily import delimited ./output/`dataset'_nockd.csv, clear
tempfile `dataset'_nockd
save ``dataset'_nockd', replace
capture noisily import delimited ./output/input_`dataset'_nockd_hrg1.csv, clear
merge 1:1 patient_id using ``dataset'_nockd'
keep if _merge==3
drop _merge
gen ckd_group = 1

merge 1:1 patient_id using ``dataset'_ckd_hrg1'


cap file close tablecontent
file open tablecontent using ./output/hrg1_`dataset'.csv, write text replace

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

global hrg "aa22 aa23 aa24 aa25 aa26 aa28 aa29 aa30 aa31 aa32 aa33 aa35 aa43 aa50 aa51 aa52 aa53 aa54 aa55 aa57 aa60 aa61 aa71 aa81 aa83 ab11 ab15 ab16 ab18 ab20 ab21 ab22 ab23 ab24 ab26 bz24 bz31 bz32 bz33 bz41 bz42 bz44 bz45 bz46 bz51 bz53 bz54 bz56 bz57 bz60 bz61 bz62 bz63 bz64 bz65 bz72 bz73 bz74 bz80 bz81 bz83 bz84 bz86 bz87 bz88 bz89 bz91 bz92 bz93 bz94 bz95 ca01 ca02 ca03 ca04 ca05 ca10 ca11 ca12 ca13 ca14 ca15 ca16 ca20 ca21 ca22 ca23 ca24 ca25 ca26 ca27 ca28 ca29 ca30 ca31 ca32 ca33 ca34 ca35 ca36 ca37 ca38 ca39 ca40 ca42 ca43 ca50 ca51 ca52 ca53 ca54 ca55 ca60 ca62 ca63 ca64 ca65 ca66 ca67 ca68 ca69 ca70 ca71 ca80 ca81 ca82 ca83 ca84 ca85 ca86 ca91 ca92 ca93 ca94 ca95 ca96 ca97 ca98 cb01 cb02 cd01 cd02 cd03 cd04 cd05 cd06 cd07 cd08 cd09 cd10 cd11 cd12 dx21 dz01 dz02 dz09 dz10 dz11 dz12 dz13 dz14 dz15 dz16 dz17 dz18 dz19 dz20 dz22 dz23 dz24 dz25 dz26 dz27 dz28 dz29 dz30 dz31 dz32 dz33 dz36 dz37 dz38 dz42 dz45 dz46 dz49 dz50 dz51 dz55 dz56 dz57 dz58 dz59 dz60 dz63 dz64 dz65 dz67 dz68 dz69 dz70 dz71 eb02 eb03 eb04 eb05 eb06 eb07 eb08 eb09 eb10 eb12 eb13 eb14 eb15 ec11 ec12 ec13 ec14 ec15 ec21 ed01 ed05 ed08 ed09 ed11 ed12 ed13 ed14 ed15 ed18 ed24 ed25 ed26 ed27 ed28 ed30 ed31 ey01 ey02 ey04 ey06 ey08 ey11 ey12 ey13 ey17"

foreach hrg of global hrg {
file write tablecontent ("`hrg'")
bysort ckd_group: egen total_`hrg'_admissions = total(`hrg'_admissions)
drop `hrg'_admissions
forvalues i=1/5 {
qui safecount if ckd_group==`i' & `hrg'_count==1
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
drop total_`hrg'_admissions
drop `hrg'_count
file write tablecontent _n
}

file close tablecontent