sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
macro drop hr
log using ./logs/hrg2_`dataset'.log, replace t

*Merge `dataset'_ckd with `dataset'_ckd_hrg2
capture noisily import delimited ./output/`dataset'_ckd.csv, clear
tempfile `dataset'_ckd
save ``dataset'_ckd', replace
capture noisily import delimited ./output/input_`dataset'_ckd_hrg2.csv, clear
merge 1:1 patient_id using ``dataset'_ckd'
keep if _merge==3
drop _merge
tempfile `dataset'_ckd_hrg2
save ``dataset'_ckd_hrg2', replace

/*Generate dummy data
cd ckd-healthcare-use
capture noisily import delimited ./output/2017_ckd.csv, clear
tempfile 2017_ckd
save ./output/2017_ckd, replace
capture noisily import delimited ./output/input_2017_ckd_hrg2.csv, clear
merge 1:1 patient_id using ./output/2017_ckd
keep if _merge==3
drop _merge
tempfile 2017_ckd_hrg2
save ./output/2017_ckd_hrg2, replace
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
save ``dataset'_ckd_hrg2', replace

*Merge `dataset'_nockd with `dataset'_nockd_hrg2
capture noisily import delimited ./output/`dataset'_nockd.csv, clear
tempfile `dataset'_nockd
save ``dataset'_nockd', replace
capture noisily import delimited ./output/input_`dataset'_nockd_hrg2.csv, clear
merge 1:1 patient_id using ``dataset'_nockd'
keep if _merge==3
drop _merge
gen ckd_group = 1

merge 1:1 patient_id using ``dataset'_ckd_hrg2'


cap file close tablecontent
file open tablecontent using ./output/hrg2_`dataset'.csv, write text replace

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

global hrg "ey22 ey23 ey30 ey31 ey32 ey40 ey41 ey42 ey43 ey50 ey51 fd01 fd02 fd03 fd04 fd05 fd10 fd11 fe01 fe02 fe03 fe10 fe11 fe12 fe13 fe20 fe21 fe22 fe30 fe31 fe32 fe33 fe34 fe35 fe36 fe50 ff01 ff02 ff04 ff05 ff12 ff13 ff14 ff20 ff21 ff22 ff30 ff31 ff32 ff33 ff34 ff36 ff37 ff40 ff41 ff42 ff43 ff50 ff51 ff52 ff53 ff60 ff61 ff62 ff63 ga03 ga04 ga05 ga06 ga07 ga10 ga11 ga13 ga15 ga16 gb05 gb06 gb09 gb10 gb11 gb12 gb13 gc01 gc12 gc17 gc18 hc20 hc21 hc26 hc27 hc28 hc29 hc30 hc31 hc32 hc50 hc53 hc54 hc60 hc61 hc62 hc63 hc64 hc65 hc70 hc71 hc72 hd21 hd23 hd24 hd25 hd26 hd39 hd40 he11 he12 he21 he22 he31 he32 he41 he42 he51 he52 he71 he72 he81 he82 he83 hn12 hn13 hn14 hn15 hn22 hn23 hn24 hn25 hn32 hn33 hn34 hn35 hn42 hn43 hn44 hn45 hn46 hn52 hn53 hn54 hn55 hn62 hn63 hn64 hn65 hn81 hn86 hn93 ja12 ja13 ja20 ja30 ja34 ja38 ja43 ja45 jb70 jb71 jb91 jc40 jc41 jc42 jc43 jc44 jc45 jc46 jc47 jd07 ka03 ka04 ka05 ka06 ka07 ka08 ka09 kb02 kb03 kb04 kc04 kc05 la01 la02 la03 la04 la05 la07 la08 la09 la10 la11 la12 la13 la14 lb06 lb09 lb10 lb12 lb13 lb14 lb15 lb16 lb17 lb18 lb19 lb20 lb21 lb25 lb26 lb28 lb29 lb33 lb35 lb36 lb37 lb38 lb39 lb40 lb42 lb43 lb46 lb47 lb48 lb50 lb51 lb52 lb53 lb54 lb55 lb56 lb57 lb58 lb59 lb60 lb61 lb64 lb65 lb67 lb68 lb70 lb71 lb72"

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