sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_ukrr_v3, replace t
clear

use ./output/`dataset'_ckd_complete_v3.dta, clear

tab ukrr
rename ukrr ukrr_string
gen ukrr = 0
replace ukrr = 1 if ukrr_string=="HD"
replace ukrr = 1 if ukrr_string=="HHD"
replace ukrr = 1 if ukrr_string=="ICHD"
replace ukrr = 1 if ukrr_string=="PD"
replace ukrr = 2 if ukrr_string=="Tx"
drop ukrr_string

tab ckd_group ukrr, m

log close


