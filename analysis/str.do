sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/str.log, replace t

cap file close tablecontent
file open tablecontent using ./output/str.csv, write text replace

file write tablecontent ("stratum") _tab ("str_2017") _tab ("str_2018") _tab ("str_2019") _tab ("str_2020") _tab ("str_2021") _tab ("str_2022")  _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
gen transplant = 0
replace transplant = weight if ckd_progression==5
egen overall_weight = total(weight)
egen overall_str = total(transplant)
bysort ckd_group: egen ckd_weight = total(weight)
bysort ckd_group: egen ckd_str = total(transplant)
foreach var of varlist ethnicity imd region urban {
bysort `var': egen `var'_weight = total(weight)
bysort `var' ckd_group: egen `var'_weight_ckd = total(weight)
bysort `var': egen `var'_str = total(transplant)
bysort `var' ckd_group: egen `var'_str_ckd = total(transplant)
}

qui su overall_weight
local overall_weight = r(mean)
qui su overall_str
local `x'_str_overall = (r(mean)/`overall_weight')*100000
local `x'_str_overall_ef = exp(1.96 * sqrt(1 / ``x'_str_overall'))
local `x'_str_overall_ul = ``x'_str_overall' * ``x'_str_overall_ef'
local `x'_str_overall_ll = ``x'_str_overall' / ``x'_str_overall_ef'

forvalues j=1/6 {
local ethlabel`j': label ethnicity `j'
qui su ethnicity_weight if ethnicity==`j'
local ethnicity_weight = r(mean)
qui su ethnicity_str if ethnicity==`j'
local `x'_str_ethnicity_`j' = (r(mean)/`ethnicity_weight')*100000
local `x'_str_ethnicity_`j'_ef = exp(1.96 * sqrt(1 / ``x'_str_ethnicity_`j''))
local `x'_str_ethnicity_`j'_ul = ``x'_str_ethnicity_`j'' * ``x'_str_ethnicity_`j'_ef'
local `x'_str_ethnicity_`j'_ll = ``x'_str_ethnicity_`j'' / ``x'_str_ethnicity_`j'_ef'
}

forvalues j=1/5 {
local imdlabel`j': label imd `j'
qui su imd_weight if imd==`j'
local imd_weight = r(mean)
qui su imd_str if imd==`j'
local `x'_str_imd_`j' = (r(mean)/`imd_weight')*100000
local `x'_str_imd_`j'_ef = exp(1.96 * sqrt(1 / ``x'_str_imd_`j''))
local `x'_str_imd_`j'_ul = ``x'_str_imd_`j'' * ``x'_str_imd_`j'_ef'
local `x'_str_imd_`j'_ll = ``x'_str_imd_`j'' / ``x'_str_imd_`j'_ef'
}

forvalues j=1/9 {
local reglabel`j': label region `j'
qui su region_weight if region==`j'
local region_weight = r(mean)
qui su region_str if region==`j'
local `x'_str_region_`j' = (r(mean)/`region_weight')*100000
local `x'_str_region_`j'_ef = exp(1.96 * sqrt(1 / ``x'_str_region_`j''))
local `x'_str_region_`j'_ul = ``x'_str_region_`j'' * ``x'_str_region_`j'_ef'
local `x'_str_region_`j'_ll = ``x'_str_region_`j'' / ``x'_str_region_`j'_ef'
}

forvalues j=0/1 {
local urblabel`j': label urban `j'
qui su urban_weight if urban==`j'
local urban_weight = r(mean)
qui su urban_str if urban==`j'
local `x'_str_urban_`j' = (r(mean)/`urban_weight')*100000
local `x'_str_urban_`j'_ef = exp(1.96 * sqrt(1 / ``x'_str_urban_`j''))
local `x'_str_urban_`j'_ul = ``x'_str_urban_`j'' * ``x'_str_urban_`j'_ef'
local `x'_str_urban_`j'_ll = ``x'_str_urban_`j'' / ``x'_str_urban_`j'_ef'
}
}


*Overall
file write tablecontent ("All")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_str_overall') (" (") %6.2f (``x'_str_overall_ll') ("-") %6.2f (``x'_str_overall_ul') (")")
}
forvalues j=1/6 {
file write tablecontent _n ("`ethlabel`j''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_str_ethnicity_`j'') (" (") %6.2f (``x'_str_ethnicity_`j'_ll') ("-") %6.2f (``x'_str_ethnicity_`j'_ul') (")")
}
}

forvalues j=1/5 {
file write tablecontent _n ("`imdlabel`j''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_str_imd_`j'') (" (") %6.2f (``x'_str_imd_`j'_ll') ("-") %6.2f (``x'_str_imd_`j'_ul') (")")
}
}
forvalues j=1/9 {
file write tablecontent _n ("`reglabel`j''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_str_region_`j'') (" (") %6.2f (``x'_str_region_`j'_ll') ("-") %6.2f (``x'_str_region_`j'_ul') (")")
}
}
forvalues j=0/1 {
file write tablecontent _n ("`urblabel`j''")
foreach x of local year {
file write tablecontent _tab %6.2f (``x'_str_urban_`j'') (" (") %6.2f (``x'_str_urban_`j'_ll') ("-") %6.2f (``x'_str_urban_`j'_ul') (")")
}
}

file close tablecontent