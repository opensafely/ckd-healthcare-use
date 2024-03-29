sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/age_death_distribution.log, replace t

cap file close tablecontent
file open tablecontent using ./output/age_death_distribution.csv, write text replace

file write tablecontent ("start_status") _tab ("agecat") _tab ("count_2017") _tab ("count_2018") _tab ("count_2019") _tab ("count_2020") _tab ("count_2021") _tab ("count_2022") _n

local year "2017 2018 2019 2020 2021 2022"
local age "18 45 50 55 60 65 70 75 80 85"

local lab18 "18-44"
local lab45 "45-49"
local lab50 "50-54"
local lab55 "55-59"
local lab60 "60-64"
local lab65 "65-69"
local lab70 "70-74"
local lab75 "75-79"
local lab80 "80-84"
local lab85 "85+"

local ckd0 "No CKD"
local ckd1 "Albuminuria"
local ckd2 "CKD stage 3"
local ckd3 "CKD stage 4/5"
local ckd4 "Dialysis"
local ckd5 "Transplant"

*Overall
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
drop agecat
drop if ckd_progression!=6
egen agecat = cut(age), at(0,18,45,50,55,60,65,70,75,80,85,200)
drop if agecat==0
foreach y of local age {
qui count if agecat==`y'
local age_`y'_`x' = round(r(N),5)
}
}
foreach y of local age {
file write tablecontent ("All") _tab ("`lab`y''")
foreach x of local year {
file write tablecontent _tab (`age_`y'_`x'')
}
file write tablecontent _n
}


foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
drop agecat
drop if ckd_progression!=6
egen agecat = cut(age), at(0,18,45,50,55,60,65,70,75,80,85,200)
drop if agecat==0
forvalues i = 0/5 {
foreach y of local age {
qui count if agecat==`y' & ckd_group==`i'
local age_`y'_`x'_`i' = round(r(N),5)
}
}
}

forvalues i=0/5 {
foreach y of local age {
file write tablecontent ("`ckd`i''") _tab ("`lab`y''")
foreach x of local year {
file write tablecontent _tab (`age_`y'_`x'_`i'')
}
file write tablecontent _n
}
}

file close tablecontent

import delimited ./output/age_death_distribution.csv, clear
local columns ""count_2017" "count_2018" "count_2019" "count_2020" "count_2021" "count_2022""
foreach col of local columns {
    replace `col' = . if `col' <= 5
}


export delimited "./output/age_death_distribution.csv", replace