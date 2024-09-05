sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
macro drop hr
log using ./logs/hrg3_`dataset'.log, replace t

*Merge `dataset'_ckd with `dataset'_ckd_hrg3
capture noisily import delimited ./output/`dataset'_ckd.csv, clear
tempfile `dataset'_ckd
save ``dataset'_ckd', replace
capture noisily import delimited ./output/input_`dataset'_ckd_hrg3.csv, clear
merge 1:1 patient_id using ``dataset'_ckd'
keep if _merge==3
drop _merge
tempfile `dataset'_ckd_hrg3
save ``dataset'_ckd_hrg3', replace

/*Generate dummy data
cd ckd-healthcare-use
capture noisily import delimited ./output/2017_ckd.csv, clear
tempfile 2017_ckd
save ./output/2017_ckd, replace
capture noisily import delimited ./output/input_2017_ckd_hrg3.csv, clear
merge 1:1 patient_id using ./output/2017_ckd
keep if _merge==3
drop _merge
tempfile 2017_ckd_hrg3
save ./output/2017_ckd_hrg3, replace
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
save ``dataset'_ckd_hrg3', replace

*Merge `dataset'_nockd with `dataset'_nockd_hrg3
capture noisily import delimited ./output/`dataset'_nockd.csv, clear
tempfile `dataset'_nockd
save ``dataset'_nockd', replace
capture noisily import delimited ./output/input_`dataset'_nockd_hrg3.csv, clear
merge 1:1 patient_id using ``dataset'_nockd'
keep if _merge==3
drop _merge
gen ckd_group = 1

merge 1:1 patient_id using ``dataset'_ckd_hrg3'


cap file close tablecontent
file open tablecontent using ./output/hrg3_`dataset'.csv, write text replace

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

global hrg "lb74 lb75 lb76 lb77 lb78 le01 le02 ma01 ma02 ma03 ma04 ma07 ma09 ma10 ma11 ma12 ma22 ma23 ma24 ma25 ma29 ma30 ma31 ma32 ma35 ma36 ma38 ma44 ma48 ma52 ma53 ma56 mb05 mb08 mb09 mc07 mc08 mc09 mc10 mc11 mc12 mc20 mc21 nz16 nz17 nz18 nz19 nz20 nz21 nz22 nz24 nz25 nz26 nz27 nz30 nz40 nz50 nz51 nz71 nz72 rd01 rd08 rd20 rd30 rd40 rd47 rd48 rd50 rd51 rd60 rd61 rn01 rn04 rn07 rn08 rn09 rn13 rn14 rn15 rn16 rn17 rn18 rn19 rn20 rn21 rn22 rn23 rn24 rn25 rn26 rn27 rn28 rn29 rn30 rn31 rn32 rn33 rn34 rn50 rn51 rn52 sa01 sa02 sa03 sa04 sa05 sa06 sa07 sa08 sa09 sa11 sa12 sa14 sa15 sa16 sa17 sa18 sa19 sa20 sa21 sa22 sa23 sa24 sa25 sa26 sa27 sa30 sa31 sa32 sa33 sa35 sa36 sa37 sa40 sa42 sa43 sa44 sa45 sb01 sb02 sb03 sb04 sb05 sb06 sb07 sb08 sb09 sb10 sb11 sb12 sb13 sb14 sb15 sb16 sb17 sc25 sc26 sc28 sc29 sc30 sc40 sc42 sc44 sc45 sc47 sc49 sc51 sc53 sc54 sc55 sc56 sc57 uz01 uz02 uz03 uz04 uz05 uz06 uz15 va10 vc01 vc02 vc03 vc04 vc06 vc08 vc10 vc12 vc14 vc16 vc18 vc20 vc22 vc24 vc26 vc28 vc30 vc32 vc34 vc36 vc38 vc40 vc42 wd01 wd02 wd03 wd04 wd05 wd06 wd07 wd08 wd09 wf01 wf02 wh01 wh02 wh03 wh04 wh05 wh06 wh07 wh08 wh09 wh10 wh11 wh12 wh13 wh14 wh15 wh16 wh17 wh18 wh19 wh20 wh21 wh22 wh23 wh50 wh51 wh52 wh53 wh54 wh99 wj01 wj02 wj03 wj04 wj06 wj07 wj10"

foreach hrg of global hrg {
file write tablecontent ("`hrg'")
bysort ckd_group: egen total_`hrg'_admissions = total(`hrg'_admissions)
forvalues i=1/5 {
qui safecount if ckd_group==`i' & `hrg'_admissions!=0
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