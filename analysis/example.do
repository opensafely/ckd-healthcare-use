sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_ckd, replace t
clear

import delimited ./output/input_`dataset'.csv, delimiter(comma) varnames(1) case(preserve) 

**Exclusions
* Age <18 at index date
drop if age <18

* Anyone not registered at one practice for 3 months before index date
drop if has_follow_up==0
drop has_follow_up

* Deceased before index date
drop if deceased==1
drop deceased

* Region
tab region
drop if region==""

* IMD
tab imd
drop if imd==0
drop if imd==.

Example code
