sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/unit_costs_overall.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/unit_costs_overall.csv, write text replace
file write tablecontent ("Date") _tab ("stratum") _tab ("ip") _tab ("ed") _tab ("opd") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("all") _tab
use ./output/`x'_ckd_complete.dta, clear
foreach aggregate of varlist hospital_days emergency_days op_appts {
qui su overall_`aggregate'
local `aggregate' = r(mean)
}
foreach cost of varlist apcs_cost ec_cost opa_cost {
qui su overall_`cost'
local `cost' = r(mean)
}
local apcs_unit = `apcs_cost'/`hospital_days'
local ec_unit = `ec_cost'/`emergency_days'
local opa_unit = `opa_cost'/`op_appts'
file write tablecontent %5.0f (`apcs_unit') _tab %5.0f (`ec_unit') _tab %5.0f (`opa_unit') _n
}

forvalues i=1/9 {
local label`i': label region `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
foreach aggregate of varlist hospital_days emergency_days op_appts {
qui su region_`aggregate' if region==`i'
local `aggregate' = r(mean)
}
foreach cost of varlist apcs_cost ec_cost opa_cost {
qui su overall_`cost'
local `cost' = r(mean)
}
local apcs_unit = `apcs_cost'/`hospital_days'
local ec_unit = `ec_cost'/`emergency_days'
local opa_unit = `opa_cost'/`op_appts'
file write tablecontent %5.0f (`apcs_unit') _tab %5.0f (`ec_unit') _tab %5.0f (`opa_unit') _n
}
}

file close tablecontent
