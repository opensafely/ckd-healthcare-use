sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/costs_ckd4.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/costs_ckd4.csv, write text replace
**Column headings
file write tablecontent ("Date") _tab ("stratum") _tab ("apcs") _tab ("ec") _tab ("opa") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("all") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
foreach cost of varlist apcs_cost ec_cost opa_cost {
qui su total_`cost'
local `x'_`cost' = r(mean)
}
file write tablecontent %10.2f (``x'_apcs_cost') _tab %10.2f (``x'_ec_cost') _tab %10.2f (``x'_opa_cost') _n
}

forvalues i=1/6 {
local label`i': label ethnicity `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
foreach cost of varlist apcs_cost ec_cost opa_cost {
qui su ethnicity_`cost' if ethnicity==`i'
local `x'_`cost' = r(mean)
}
file write tablecontent %10.2f (``x'_apcs_cost') _tab %10.2f (``x'_ec_cost') _tab %10.2f (``x'_opa_cost') _n
}
}

forvalues i=1/5 {
local label`i': label imd `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
foreach cost of varlist apcs_cost ec_cost opa_cost {
qui su imd_`cost' if imd==`i'
local `x'_`cost' = r(mean)
}
file write tablecontent %10.2f (``x'_apcs_cost') _tab %10.2f (``x'_ec_cost') _tab %10.2f (``x'_opa_cost') _n
}
}

forvalues i=1/9 {
local label`i': label region `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
foreach cost of varlist apcs_cost ec_cost opa_cost {
qui su region_`cost' if region==`i'
local `x'_`cost' = r(mean)
}
file write tablecontent %10.2f (``x'_apcs_cost') _tab %10.2f (``x'_ec_cost') _tab %10.2f (``x'_opa_cost') _n
}
}

forvalues i=0/1 {
local label`i': label urban `i'
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab ("`label`i''") _tab
use ./output/`x'_ckd_complete.dta, clear
drop if ckd_group!=3
foreach cost of varlist apcs_cost ec_cost opa_cost {
qui su urban_`cost' if urban==`i'
local `x'_`cost' = r(mean)
}
file write tablecontent %10.2f (``x'_apcs_cost') _tab %10.2f (``x'_ec_cost') _tab %10.2f (``x'_opa_cost') _n
}
}

file close tablecontent