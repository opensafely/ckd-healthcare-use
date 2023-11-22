sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/sdr.log, replace t

cap file close tablecontent
file open tablecontent using ./output/sdr.csv, write text replace

file write tablecontent ("stratum") _tab ("sdr_2017") _tab ("sdr_2018") _tab ("sdr_2019") _tab ("sdr_2020") _tab ("sdr_2021") _tab ("sdr_2022")  _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
label drop ckd_group
label define ckd_group 0 "No CKD" 1 "Albuminuria" 2 "CKD stage 3" 3 "CKD stage 4/5" 4 "Dialysis" 5 "Transplant" 6 "KRT unclear modality"
label values ckd_group ckd_group
drop dialysis
gen dialysis = 0
replace dialysis = weight if ckd_progression==4
egen overall_weight = total(weight)
egen overall_sdr = total(dialysis)
bysort ckd_group: egen ckd_weight = total(weight)
bysort ckd_group: egen ckd_sdr = total(dialysis)
foreach var of varlist ethnicity imd region urban {
bysort `var': egen `var'_weight = total(weight)
bysort `var' ckd_group: egen `var'_weight_ckd = total(weight)
bysort `var': egen `var'_sdr = total(dialysis)
bysort `var' ckd_group: egen `var'_sdr_ckd = total(dialysis)
}

qui su overall_weight
local overall_weight = r(mean)
qui su overall_sdr
local `x'_sdr_overall = (r(mean)/`overall_weight')*100000
local `x'_sdr_overall_ef = exp(1.96 * sqrt(1 / ``x'_sdr_overall'))
local `x'_sdr_overall_ul = ``x'_sdr_overall' * ``x'_sdr_overall_ef'
local `x'_sdr_overall_ll = ``x'_sdr_overall' / ``x'_sdr_overall_ef'

forvalues j=1/6 {
local ethlabel`j': label ethnicity `j'
qui su ethnicity_weight if ethnicity==`j'
local ethnicity_weight = r(mean)
qui su ethnicity_sdr if ethnicity==`j'
local `x'_sdr_ethnicity_`j' = (r(mean)/`ethnicity_weight')*100000
local `x'_sdr_ethnicity_`j'_ef = exp(1.96 * sqrt(1 / ``x'_sdr_ethnicity_`j''))
local `x'_sdr_ethnicity_`j'_ul = ``x'_sdr_ethnicity_`j'' * ``x'_sdr_ethnicity_`j'_ef'
local `x'_sdr_ethnicity_`j'_ll = ``x'_sdr_ethnicity_`j'' / ``x'_sdr_ethnicity_`j'_ef'
}

forvalues j=1/5 {
local imdlabel`j': label imd `j'
qui su imd_weight if imd==`j'
local imd_weight = r(mean)
qui su imd_sdr if imd==`j'
local `x'_sdr_imd_`j' = (r(mean)/`imd_weight')*100000
local `x'_sdr_imd_`j'_ef = exp(1.96 * sqrt(1 / ``x'_sdr_imd_`j''))
local `x'_sdr_imd_`j'_ul = ``x'_sdr_imd_`j'' * ``x'_sdr_imd_`j'_ef'
local `x'_sdr_imd_`j'_ll = ``x'_sdr_imd_`j'' / ``x'_sdr_imd_`j'_ef'
}

forvalues j=1/9 {
local reglabel`j': label region `j'
qui su region_weight if region==`j'
local region_weight = r(mean)
qui su region_sdr if region==`j'
local `x'_sdr_region_`j' = (r(mean)/`region_weight')*100000
local `x'_sdr_region_`j'_ef = exp(1.96 * sqrt(1 / ``x'_sdr_region_`j''))
local `x'_sdr_region_`j'_ul = ``x'_sdr_region_`j'' * ``x'_sdr_region_`j'_ef'
local `x'_sdr_region_`j'_ll = ``x'_sdr_region_`j'' / ``x'_sdr_region_`j'_ef'
}

forvalues j=0/1 {
local urblabel`j': label urban `j'
qui su urban_weight if urban==`j'
local urban_weight = r(mean)
qui su urban_sdr if urban==`j'
local `x'_sdr_urban_`j' = (r(mean)/`urban_weight')*100000
local `x'_sdr_urban_`j'_ef = exp(1.96 * sqrt(1 / ``x'_sdr_urban_`j''))
local `x'_sdr_urban_`j'_ul = ``x'_sdr_urban_`j'' * ``x'_sdr_urban_`j'_ef'
local `x'_sdr_urban_`j'_ll = ``x'_sdr_urban_`j'' / ``x'_sdr_urban_`j'_ef'
}
}


*Overall
file write tablecontent ("All")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_sdr_overall') (" (") %6.2f (``x'_sdr_overall_ll') ("-") %6.2f (``x'_sdr_overall_ul') (")")
}
forvalues j=1/6 {
file write tablecontent _n ("`ethlabel`j''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_sdr_ethnicity_`j'') (" (") %6.2f (``x'_sdr_ethnicity_`j'_ll') ("-") %6.2f (``x'_sdr_ethnicity_`j'_ul') (")")
}
}

forvalues j=1/5 {
file write tablecontent _n ("`imdlabel`j''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_sdr_imd_`j'') (" (") %6.2f (``x'_sdr_imd_`j'_ll') ("-") %6.2f (``x'_sdr_imd_`j'_ul') (")")
}
}
forvalues j=1/9 {
file write tablecontent _n ("`reglabel`j''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_sdr_region_`j'') (" (") %6.2f (``x'_sdr_region_`j'_ll') ("-") %6.2f (``x'_sdr_region_`j'_ul') (")")
}
}
forvalues j=0/1 {
file write tablecontent _n ("`urblabel`j''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_sdr_urban_`j'') (" (") %6.2f (``x'_sdr_urban_`j'_ll') ("-") %6.2f (``x'_sdr_urban_`j'_ul') (")")
}
}

file close tablecontent