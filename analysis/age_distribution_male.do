sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/age_distribution_male.log, replace t

cap file close tablecontent
file open tablecontent using ./output/age_distribution_male.csv, write text replace

file write tablecontent ("group") _tab ("stratum") _tab ("agecat") _tab ("count_2017") _tab ("count_2018") _tab ("count_2019") _tab ("count_2020") _tab ("count_2021") _tab ("count_2022") _n

local year "2017 2018 2019 2020 2021 2022"

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
drop if sex==0
forvalues i=0/5 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
qui safecount if agecat==`y' & ckd_group==`i'
local age_`y'_`x'_`i' = round(r(N),5)
}
}
}
forvalues i=0/5 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
file write tablecontent ("`ckd`i''") _tab ("Overall") _tab ("`y'")
foreach x of local year {
if `age_`y'_`x'_`i''>5 & `age_`y'_`x'_`i''!=. {
file write tablecontent _tab (`age_`y'_`x'_`i'')
}
else {
file write tablecontent _tab ("REDACTED")
}
}
file write tablecontent _n
}
}


*Ethnicity
local lab1 "White"
local lab2 "South Asian"
local lab3 "Black"
local lab4 "Mixed"
local lab5 "Other"
local lab6 "Unknown"

*Ethnicity
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
drop if sex==0
forvalues i=0/5 {
forvalues j=1/6 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
qui safecount if agecat==`y' & ckd_group==`i' & ethnicity==`j'
local age_`y'_`x'_`i'_`j' = round(r(N),5)
}
}
}
}

forvalues i=0/5 {
forvalues j=1/6 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
file write tablecontent ("`ckd`i''") _tab ("`lab`j''") _tab ("`y'")
foreach x of local year {
if `age_`y'_`x'_`i'_`j''>5 & `age_`y'_`x'_`i'_`j''!=. {
file write tablecontent _tab (`age_`y'_`x'_`i'_`j'')
}
else {
file write tablecontent _tab ("REDACTED")
}
}
file write tablecontent _n
}
}
}

*IMD
local lab1 "IMD1 (Most deprived)"
local lab2 "IMD2"
local lab3 "IMD3"
local lab4 "IMD4"
local lab5 "IMD5 (Least deprived)"

foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
drop if sex==0
forvalues i=0/5 {
forvalues j=1/5 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
qui safecount if agecat==`y' & ckd_group==`i' & imd==`j'
local age_`y'_`x'_`i'_`j' = round(r(N),5)
}
}
}
}

forvalues i=0/5 {
forvalues j=1/5 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
file write tablecontent ("`ckd`i''") _tab ("`lab`j''") _tab ("`y'")
foreach x of local year {
if `age_`y'_`x'_`i'_`j''>5 & `age_`y'_`x'_`i'_`j''!=. {
file write tablecontent _tab (`age_`y'_`x'_`i'_`j'')
}
else {
file write tablecontent _tab ("REDACTED")
}
}
file write tablecontent _n
}
}
}

*Region
local lab1 "East Midlands"
local lab2 "East"   						
local lab3 "London" 							
local lab4 "North East" 						
local lab5 "North West" 						
local lab6 "South East" 						
local lab7 "South West"						
local lab8 "West Midlands" 					
local lab9 "Yorkshire and The Humber"		

foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
drop if sex==0
forvalues i=0/5 {
forvalues j=1/9 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
qui safecount if agecat==`y' & ckd_group==`i' & region==`j'
local age_`y'_`x'_`i'_`j' = round(r(N),5)
}
}
}
}

forvalues i=0/5 {
forvalues j=1/9 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
file write tablecontent ("`ckd`i''") _tab ("`lab`j''") _tab ("`y'")
foreach x of local year {
if `age_`y'_`x'_`i'_`j''>5 & `age_`y'_`x'_`i'_`j''!=. {
file write tablecontent _tab (`age_`y'_`x'_`i'_`j'')
}
else {
file write tablecontent _tab ("REDACTED")
}
}
file write tablecontent _n
}
}
}

*Urban/rural
local lab0 "Rural"
local lab1 "Urban"   						

foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
drop if sex==0
forvalues i=0/5 {
forvalues j=0/1 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
qui safecount if agecat==`y' & ckd_group==`i' & urban==`j'
local age_`y'_`x'_`i'_`j' = round(r(N),5)
}
}
}
}

forvalues i=0/5 {
forvalues j=0/1 {
foreach y in 18 25 30 35 40 45 50 55 60 65 70 75 80 85 90 {
file write tablecontent ("`ckd`i''") _tab ("`lab`j''") _tab ("`y'")
foreach x of local year {
if `age_`y'_`x'_`i'_`j''>5 & `age_`y'_`x'_`i'_`j''!=. {
file write tablecontent _tab (`age_`y'_`x'_`i'_`j'')
}
else {
file write tablecontent _tab ("REDACTED")
}
}
file write tablecontent _n
}
}
}

file close tablecontent