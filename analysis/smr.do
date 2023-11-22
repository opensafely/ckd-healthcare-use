sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/smr.log, replace t

cap file close tablecontent
file open tablecontent using ./output/smr.csv, write text replace

file write tablecontent ("stratum") _tab ("start_status") _tab ("smr_2017") _tab ("smr_2018") _tab ("smr_2019") _tab ("smr_2020") _tab ("smr_2021") _tab ("smr_2022")  _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
label drop ckd_group
label define ckd_group 0 "No CKD" 1 "Albuminuria" 2 "CKD stage 3" 3 "CKD stage 4/5" 4 "Dialysis" 5 "Transplant" 6 "KRT unclear modality"
label values ckd_group ckd_group
gen died = 0
replace died = weight if ckd_progression==6
egen overall_weight = total(weight)
egen overall_smr = total(died)
bysort ckd_group: egen ckd_weight = total(weight)
bysort ckd_group: egen ckd_smr = total(died)
foreach var of varlist ethnicity imd region urban {
bysort `var': egen `var'_weight = total(weight)
bysort `var' ckd_group: egen `var'_weight_ckd = total(weight)
bysort `var': egen `var'_smr = total(died)
bysort `var' ckd_group: egen `var'_smr_ckd = total(died)
}

qui su overall_weight
local overall_weight = r(mean)
qui su overall_smr
local `x'_smr_overall = (r(mean)/`overall_weight')*100000
local `x'_smr_overall_ef = exp(1.96 * sqrt(1 / ``x'_smr_overall'))
local `x'_smr_overall_ul = ``x'_smr_overall' * ``x'_smr_overall_ef'
local `x'_smr_overall_ll = ``x'_smr_overall' / ``x'_smr_overall_ef'

forvalues i=0/6 {
local ckdlabel`i': label ckd_group `i'
qui su ckd_weight if ckd_group==`i'
local ckd_weight = r(mean)
qui su ckd_smr if ckd_group==`i'
local `x'_smr_ckd_`i' = (r(mean)/`ckd_weight')*100000
local `x'_smr_ckd_`i'_ef = exp(1.96 * sqrt(1 / ``x'_smr_ckd_`i''))
local `x'_smr_ckd_`i'_ul = ``x'_smr_ckd_`i'' * ``x'_smr_ckd_`i'_ef'
local `x'_smr_ckd_`i'_ll = ``x'_smr_ckd_`i'' / ``x'_smr_ckd_`i'_ef'
}


forvalues j=1/6 {
local ethlabel`j': label ethnicity `j'
qui su ethnicity_weight if ethnicity==`j'
local ethnicity_weight = r(mean)
qui su ethnicity_smr if ethnicity==`j'
local `x'_smr_ethnicity_`j' = (r(mean)/`ethnicity_weight')*100000
local `x'_smr_ethnicity_`j'_ef = exp(1.96 * sqrt(1 / ``x'_smr_ethnicity_`j''))
local `x'_smr_ethnicity_`j'_ul = ``x'_smr_ethnicity_`j'' * ``x'_smr_ethnicity_`j'_ef'
local `x'_smr_ethnicity_`j'_ll = ``x'_smr_ethnicity_`j'' / ``x'_smr_ethnicity_`j'_ef'


forvalues i=0/6 {
qui su ethnicity_weight_ckd if ckd_group==`i' & ethnicity==`j'
local ethnicity_weight = r(mean)
qui su ethnicity_smr_ckd if ckd_group==`i' & ethnicity==`j'
local `x'_ethnicity_`j'_smr_ckd_`i' = (r(mean)/`ethnicity_weight')*100000
local `x'_ethnicity_`j'_smr_ckd_`i'_ef = exp(1.96 * sqrt(1 / ``x'_ethnicity_`j'_smr_ckd_`i''))
local `x'_ethnicity_`j'_smr_ckd_`i'_ul = ``x'_ethnicity_`j'_smr_ckd_`i'' * ``x'_ethnicity_`j'_smr_ckd_`i'_ef'
local `x'_ethnicity_`j'_smr_ckd_`i'_ll = ``x'_ethnicity_`j'_smr_ckd_`i'' / ``x'_ethnicity_`j'_smr_ckd_`i'_ef'
}
}



forvalues j=1/5 {
local imdlabel`j': label imd `j'
qui su imd_weight if imd==`j'
local imd_weight = r(mean)
qui su imd_smr if imd==`j'
local `x'_smr_imd_`j' = (r(mean)/`imd_weight')*100000
local `x'_smr_imd_`j'_ef = exp(1.96 * sqrt(1 / ``x'_smr_imd_`j''))
local `x'_smr_imd_`j'_ul = ``x'_smr_imd_`j'' * ``x'_smr_imd_`j'_ef'
local `x'_smr_imd_`j'_ll = ``x'_smr_imd_`j'' / ``x'_smr_imd_`j'_ef'


forvalues i=0/6 {
qui su imd_weight_ckd if ckd_group==`i' & imd==`j'
local imd_weight = r(mean)
qui su imd_smr_ckd if ckd_group==`i' & imd==`j'
local `x'_imd_`j'_smr_ckd_`i' = (r(mean)/`imd_weight')*100000
local `x'_imd_`j'_smr_ckd_`i'_ef = exp(1.96 * sqrt(1 / ``x'_imd_`j'_smr_ckd_`i''))
local `x'_imd_`j'_smr_ckd_`i'_ul = ``x'_imd_`j'_smr_ckd_`i'' * ``x'_imd_`j'_smr_ckd_`i'_ef'
local `x'_imd_`j'_smr_ckd_`i'_ll = ``x'_imd_`j'_smr_ckd_`i'' / ``x'_imd_`j'_smr_ckd_`i'_ef'
}
}



forvalues j=1/9 {
local reglabel`j': label region `j'
qui su region_weight if region==`j'
local region_weight = r(mean)
qui su region_smr if region==`j'
local `x'_smr_region_`j' = (r(mean)/`region_weight')*100000
local `x'_smr_region_`j'_ef = exp(1.96 * sqrt(1 / ``x'_smr_region_`j''))
local `x'_smr_region_`j'_ul = ``x'_smr_region_`j'' * ``x'_smr_region_`j'_ef'
local `x'_smr_region_`j'_ll = ``x'_smr_region_`j'' / ``x'_smr_region_`j'_ef'
forvalues i=0/6 {
qui su region_weight_ckd if ckd_group==`i' & region==`j'
local region_weight = r(mean)
qui su region_smr_ckd if ckd_group==`i' & region==`j'
local `x'_region_`j'_smr_ckd_`i' = (r(mean)/`region_weight')*100000
local `x'_region_`j'_smr_ckd_`i'_ef = exp(1.96 * sqrt(1 / ``x'_region_`j'_smr_ckd_`i''))
local `x'_region_`j'_smr_ckd_`i'_ul = ``x'_region_`j'_smr_ckd_`i'' * ``x'_region_`j'_smr_ckd_`i'_ef'
local `x'_region_`j'_smr_ckd_`i'_ll = ``x'_region_`j'_smr_ckd_`i'' / ``x'_region_`j'_smr_ckd_`i'_ef'
}


forvalues j=0/1 {
local urblabel`j': label urban `j'
qui su urban_weight if urban==`j'
local urban_weight = r(mean)
qui su urban_smr if urban==`j'
local `x'_smr_urban_`j' = (r(mean)/`urban_weight')*100000
local `x'_smr_urban_`j'_ef = exp(1.96 * sqrt(1 / ``x'_smr_urban_`j''))
local `x'_smr_urban_`j'_ul = ``x'_smr_urban_`j'' * ``x'_smr_urban_`j'_ef'
local `x'_smr_urban_`j'_ll = ``x'_smr_urban_`j'' / ``x'_smr_urban_`j'_ef'
forvalues i=0/6 {
qui su urban_weight_ckd if ckd_group==`i' & urban==`j'
local urban_weight = r(mean)
qui su urban_smr_ckd if ckd_group==`i' & urban==`j'
local `x'_urban_`j'_smr_ckd_`i' = (r(mean)/`urban_weight')*100000
local `x'_urban_`j'_smr_ckd_`i'_ef = exp(1.96 * sqrt(1 / ``x'_urban_`j'_smr_ckd_`i''))
local `x'_urban_`j'_smr_ckd_`i'_ul = ``x'_urban_`j'_smr_ckd_`i'' * ``x'_urban_`j'_smr_ckd_`i'_ef'
local `x'_urban_`j'_smr_ckd_`i'_ll = ``x'_urban_`j'_smr_ckd_`i'' / ``x'_urban_`j'_smr_ckd_`i'_ef'
}
}
}
}

*Overall
file write tablecontent ("All") _tab ("All")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_smr_overall') (" (") %6.2f (``x'_smr_overall_ll') ("-") %6.2f (``x'_smr_overall_ul') (")")
}
forvalues j=1/6 {
file write tablecontent _n ("`ethlabel`j''") _tab ("All")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_smr_ethnicity_`j'') (" (") %6.2f (``x'_smr_ethnicity_`j'_ll') ("-") %6.2f (``x'_smr_ethnicity_`j'_ul') (")")
}
}

forvalues j=1/5 {
file write tablecontent _n ("`imdlabel`j''") _tab ("All")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_smr_imd_`j'') (" (") %6.2f (``x'_smr_imd_`j'_ll') ("-") %6.2f (``x'_smr_imd_`j'_ul') (")")
}
}
forvalues j=1/9 {
file write tablecontent _n ("`reglabel`j''") _tab ("All")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_smr_region_`j'') (" (") %6.2f (``x'_smr_region_`j'_ll') ("-") %6.2f (``x'_smr_region_`j'_ul') (")")
}
}
forvalues j=0/1 {
file write tablecontent _n ("`urblabel`j''") _tab ("All")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_smr_urban_`j'') (" (") %6.2f (``x'_smr_urban_`j'_ll') ("-") %6.2f (``x'_smr_urban_`j'_ul') (")")
}
}

*By CKD status
forvalues i=0/5 {
file write tablecontent _n ("All") _tab ("`ckdlabel`i''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_smr_ckd_`i'') (" (") %6.2f (``x'_smr_ckd_`i'_ll') ("-") %6.2f (``x'_smr_ckd_`i'_ul') (")")
}
forvalues j=1/6 {
file write tablecontent _n ("`ethlabel`j''") _tab ("`ckdlabel`i''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_ethnicity_`j'_smr_ckd_`i'') (" (") %6.2f (``x'_ethnicity_`j'_smr_ckd_`i'_ll') ("-") %6.2f (``x'_ethnicity_`j'_smr_ckd_`i'_ul') (")")
}
}
forvalues j=1/5 {
file write tablecontent _n ("`imdlabel`j''") _tab ("`ckdlabel`i''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_imd_`j'_smr_ckd_`i'') (" (") %6.2f (``x'_imd_`j'_smr_ckd_`i'_ll') ("-") %6.2f (``x'_imd_`j'_smr_ckd_`i'_ul') (")")
}
}
forvalues j=1/9 {
file write tablecontent _n ("`reglabel`j''") _tab ("`ckdlabel`i''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_region_`j'_smr_ckd_`i'') (" (") %6.2f (``x'_region_`j'_smr_ckd_`i'_ll') ("-") %6.2f (``x'_region_`j'_smr_ckd_`i'_ul') (")")
}
}
forvalues j=0/1 {
file write tablecontent _n ("`urblabel`j''") _tab ("`ckdlabel`i''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_urban_`j'_smr_ckd_`i'') (" (") %6.2f (``x'_urban_`j'_smr_ckd_`i'_ll') ("-") %6.2f (``x'_urban_`j'_smr_ckd_`i'_ul') (")")
}
}
}

file close tablecontent