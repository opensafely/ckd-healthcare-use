sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/age_death.log, replace t

cap file close tablecontent
file open tablecontent using ./output/age_death.csv, write text replace

file write tablecontent ("stratum") _tab ("start_status") _tab ("median_2017") _tab ("median_2018") _tab ("median_2019") _tab ("median_2020") _tab ("median_2021") _tab ("median_2022") _tab ("mode_2017") _tab ("mode_2018") _tab ("mode_2019") _tab ("mode_2020") _tab ("mode_2021") _tab ("mode_2022") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete, force
drop if ckd_progression!=6

qui su age, d
local `x'_q2 = r(p50)
local `x'_q1 = r(p25)
local `x'_q3 = r(p75)
egen mode_age = mode(age), minmode
qui su mode_age
local `x'_mode = r(mean)
drop mode_age

bysort ckd_group: egen mode_age = mode(age), minmode

forvalues i=0/5{
qui su age if ckd_group==`i', d
local `x'_q2_`i' = r(p50)
local `x'_q1_`i' = r(p25)
local `x'_q3_`i' = r(p75)
qui su mode_age if ckd_group==`i'
local `x'_mode_`i' = r(mean)
} 
}


file write tablecontent ("All") _tab ("All") _tab (`2017_q2') (" (") (`2017_q1') ("-") (`2017_q3') (")") _tab (`2018_q2') (" (") (`2018_q1') ("-") (`2018_q3') (")") _tab (`2019_q2') (" (") (`2019_q1') ("-") (`2019_q3') (")") _tab (`2020_q2') (" (") (`2020_q1') ("-") (`2020_q3') (")") _tab (`2021_q2') (" (") (`2021_q1') ("-") (`2021_q3') (")") _tab (`2022_q2') (" (") (`2022_q1') ("-") (`2022_q3') (")") _tab (`2017_mode') _tab (`2018_mode') _tab (`2019_mode') _tab (`2020_mode') _tab (`2021_mode') _tab (`2022_mode') _n
file write tablecontent ("All") _tab ("No CKD") _tab (`2017_q2_0') (" (") (`2017_q1_0') ("-") (`2017_q3_0') (")") _tab (`2018_q2_0') (" (") (`2018_q1_0') ("-") (`2018_q3_0') (")") _tab (`2019_q2_0') (" (") (`2019_q1_0') ("-") (`2019_q3_0') (")") _tab (`2020_q2_0') (" (") (`2020_q1_0') ("-") (`2020_q3_0') (")") _tab (`2021_q2_0') (" (") (`2021_q1_0') ("-") (`2021_q3_0') (")") _tab (`2022_q2_0') (" (") (`2022_q1_0') ("-") (`2022_q3_0') (")") _tab (`2017_mode_0') _tab (`2018_mode_0') _tab (`2019_mode_0') _tab (`2020_mode_0') _tab (`2021_mode_0') _tab (`2022_mode_0') _n
file write tablecontent ("All") _tab ("Albuminuria") _tab (`2017_q2_1') (" (") (`2017_q1_1') ("-") (`2017_q3_1') (")") _tab (`2018_q2_1') (" (") (`2018_q1_1') ("-") (`2018_q3_1') (")") _tab (`2019_q2_1') (" (") (`2019_q1_1') ("-") (`2019_q3_1') (")") _tab (`2020_q2_1') (" (") (`2020_q1_1') ("-") (`2020_q3_1') (")") _tab (`2021_q2_1') (" (") (`2021_q1_1') ("-") (`2021_q3_1') (")") _tab (`2022_q2_1') (" (") (`2022_q1_1') ("-") (`2022_q3_1') (")") _tab (`2017_mode_1') _tab (`2018_mode_1') _tab (`2019_mode_1') _tab (`2020_mode_1') _tab (`2021_mode_1') _tab (`2022_mode_1') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab (`2017_q2_2') (" (") (`2017_q1_2') ("-") (`2017_q3_2') (")") _tab (`2018_q2_2') (" (") (`2018_q1_2') ("-") (`2018_q3_2') (")") _tab (`2019_q2_2') (" (") (`2019_q1_2') ("-") (`2019_q3_2') (")") _tab (`2020_q2_2') (" (") (`2020_q1_2') ("-") (`2020_q3_2') (")") _tab (`2021_q2_2') (" (") (`2021_q1_2') ("-") (`2021_q3_2') (")") _tab (`2022_q2_2') (" (") (`2022_q1_2') ("-") (`2022_q3_2') (")") _tab (`2017_mode_2') _tab (`2018_mode_2') _tab (`2019_mode_2') _tab (`2020_mode_2') _tab (`2021_mode_2') _tab (`2022_mode_2') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab (`2017_q2_3') (" (") (`2017_q1_3') ("-") (`2017_q3_3') (")") _tab (`2018_q2_3') (" (") (`2018_q1_3') ("-") (`2018_q3_3') (")") _tab (`2019_q2_3') (" (") (`2019_q1_3') ("-") (`2019_q3_3') (")") _tab (`2020_q2_3') (" (") (`2020_q1_3') ("-") (`2020_q3_3') (")") _tab (`2021_q2_3') (" (") (`2021_q1_3') ("-") (`2021_q3_3') (")") _tab (`2022_q2_3') (" (") (`2022_q1_3') ("-") (`2022_q3_3') (")") _tab (`2017_mode_3') _tab (`2018_mode_3') _tab (`2019_mode_3') _tab (`2020_mode_3') _tab (`2021_mode_3') _tab (`2022_mode_3') _n
file write tablecontent ("All") _tab ("Dialysis") _tab (`2017_q2_4') (" (") (`2017_q1_4') ("-") (`2017_q3_4') (")") _tab (`2018_q2_4') (" (") (`2018_q1_4') ("-") (`2018_q3_4') (")") _tab (`2019_q2_4') (" (") (`2019_q1_4') ("-") (`2019_q3_4') (")") _tab (`2020_q2_4') (" (") (`2020_q1_4') ("-") (`2020_q3_4') (")") _tab (`2021_q2_4') (" (") (`2021_q1_4') ("-") (`2021_q3_4') (")") _tab (`2022_q2_4') (" (") (`2022_q1_4') ("-") (`2022_q3_4') (")") _tab (`2017_mode_4') _tab (`2018_mode_4') _tab (`2019_mode_4') _tab (`2020_mode_4') _tab (`2021_mode_4') _tab (`2022_mode_4') _n
file write tablecontent ("All") _tab ("Transplant") _tab (`2017_q2_5') (" (") (`2017_q1_5') ("-") (`2017_q3_5') (")") _tab (`2018_q2_5') (" (") (`2018_q1_5') ("-") (`2018_q3_5') (")") _tab (`2019_q2_5') (" (") (`2019_q1_5') ("-") (`2019_q3_5') (")") _tab (`2020_q2_5') (" (") (`2020_q1_5') ("-") (`2020_q3_5') (")") _tab (`2021_q2_5') (" (") (`2021_q1_5') ("-") (`2021_q3_5') (")") _tab (`2022_q2_5') (" (") (`2022_q1_5') ("-") (`2022_q3_5') (")") _tab (`2017_mode_5') _tab (`2018_mode_5') _tab (`2019_mode_5') _tab (`2020_mode_5') _tab (`2021_mode_5') _tab (`2022_mode_5') _n

local label1 "White"
local label2 "Non-white"
local label3 "Unknown"

*Ethnicity
forvalues j=1/3 {
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if ckd_progression!=6 
replace ethnicity=2 if ethnicity==3
replace ethnicity=2 if ethnicity==4
replace ethnicity=2 if ethnicity==5
replace ethnicity=3 if ethnicity==6
drop if ethnicity!=`j'

qui su age, d
local `x'_q2_`j' = r(p50)
local `x'_q1_`j' = r(p25)
local `x'_q3_`j' = r(p75)
egen mode_age = mode(age), minmode
qui su mode_age
local `x'_mode_`j' = r(mean)
drop mode_age

bysort ckd_group: egen mode_age = mode(age), minmode
forvalues i=0/5{
qui su age if ckd_group==`i', d
local `x'_q2_`i'_`j' = r(p50)
local `x'_q1_`i'_`j' = r(p25)
local `x'_q3_`i'_`j' = r(p75)
qui su mode_age if ckd_group==`i'
local `x'_mode_`i'_`j' = r(mean)
}
}
file write tablecontent ("`label`j''") _tab ("All") _tab (`2017_q2_`j'') (" (") (`2017_q1_`j'') ("-") (`2017_q3_`j'') (")") _tab (`2018_q2_`j'') (" (") (`2018_q1_`j'') ("-") (`2018_q3_`j'') (")") _tab (`2019_q2_`j'') (" (") (`2019_q1_`j'') ("-") (`2019_q3_`j'') (")") _tab (`2020_q2_`j'') (" (") (`2020_q1_`j'') ("-") (`2020_q3_`j'') (")") _tab (`2021_q2_`j'') (" (") (`2021_q1_`j'') ("-") (`2021_q3_`j'') (")") _tab (`2022_q2_`j'') (" (") (`2022_q1_`j'') ("-") (`2022_q3_`j'') (")") _tab (`2017_mode_`j'') _tab (`2018_mode_`j'') _tab (`2019_mode_`j'') _tab (`2020_mode_`j'') _tab (`2021_mode_`j'') _tab (`2022_mode_`j'') _n
file write tablecontent ("`label`j''") _tab ("No CKD") _tab (`2017_q2_0_`j'') (" (") (`2017_q1_0_`j'') ("-") (`2017_q3_0_`j'') (")") _tab (`2018_q2_0_`j'') (" (") (`2018_q1_0_`j'') ("-") (`2018_q3_0_`j'') (")") _tab (`2019_q2_0_`j'') (" (") (`2019_q1_0_`j'') ("-") (`2019_q3_0_`j'') (")") _tab (`2020_q2_0_`j'') (" (") (`2020_q1_0_`j'') ("-") (`2020_q3_0_`j'') (")") _tab (`2021_q2_0_`j'') (" (") (`2021_q1_0_`j'') ("-") (`2021_q3_0_`j'') (")") _tab (`2022_q2_0_`j'') (" (") (`2022_q1_0_`j'') ("-") (`2022_q3_0_`j'') (")") _tab (`2017_mode_0_`j'') _tab (`2018_mode_0_`j'') _tab (`2019_mode_0_`j'') _tab (`2020_mode_0_`j'') _tab (`2021_mode_0_`j'') _tab (`2022_mode_0_`j'') _n
file write tablecontent ("`label`j''") _tab ("Albuminuria") _tab (`2017_q2_1_`j'') (" (") (`2017_q1_1_`j'') ("-") (`2017_q3_1_`j'') (")") _tab (`2018_q2_1_`j'') (" (") (`2018_q1_1_`j'') ("-") (`2018_q3_1_`j'') (")") _tab (`2019_q2_1_`j'') (" (") (`2019_q1_1_`j'') ("-") (`2019_q3_1_`j'') (")") _tab (`2020_q2_1_`j'') (" (") (`2020_q1_1_`j'') ("-") (`2020_q3_1_`j'') (")") _tab (`2021_q2_1_`j'') (" (") (`2021_q1_1_`j'') ("-") (`2021_q3_1_`j'') (")") _tab (`2022_q2_1_`j'') (" (") (`2022_q1_1_`j'') ("-") (`2022_q3_1_`j'') (")") _tab (`2017_mode_1_`j'') _tab (`2018_mode_1_`j'') _tab (`2019_mode_1_`j'') _tab (`2020_mode_1_`j'') _tab (`2021_mode_1_`j'') _tab (`2022_mode_1_`j'') _n
file write tablecontent ("`label`j''") _tab ("CKD stage 3") _tab (`2017_q2_2_`j'') (" (") (`2017_q1_2_`j'') ("-") (`2017_q3_2_`j'') (")") _tab (`2018_q2_2_`j'') (" (") (`2018_q1_2_`j'') ("-") (`2018_q3_2_`j'') (")") _tab (`2019_q2_2_`j'') (" (") (`2019_q1_2_`j'') ("-") (`2019_q3_2_`j'') (")") _tab (`2020_q2_2_`j'') (" (") (`2020_q1_2_`j'') ("-") (`2020_q3_2_`j'') (")") _tab (`2021_q2_2_`j'') (" (") (`2021_q1_2_`j'') ("-") (`2021_q3_2_`j'') (")") _tab (`2022_q2_2_`j'') (" (") (`2022_q1_2_`j'') ("-") (`2022_q3_2_`j'') (")") _tab (`2017_mode_2_`j'') _tab (`2018_mode_2_`j'') _tab (`2019_mode_2_`j'') _tab (`2020_mode_2_`j'') _tab (`2021_mode_2_`j'') _tab (`2022_mode_2_`j'') _n
file write tablecontent ("`label`j''") _tab ("CKD stage 4/5") _tab (`2017_q2_3_`j'') (" (") (`2017_q1_3_`j'') ("-") (`2017_q3_3_`j'') (")") _tab (`2018_q2_3_`j'') (" (") (`2018_q1_3_`j'') ("-") (`2018_q3_3_`j'') (")") _tab (`2019_q2_3_`j'') (" (") (`2019_q1_3_`j'') ("-") (`2019_q3_3_`j'') (")") _tab (`2020_q2_3_`j'') (" (") (`2020_q1_3_`j'') ("-") (`2020_q3_3_`j'') (")") _tab (`2021_q2_3_`j'') (" (") (`2021_q1_3_`j'') ("-") (`2021_q3_3_`j'') (")") _tab (`2022_q2_3_`j'') (" (") (`2022_q1_3_`j'') ("-") (`2022_q3_3_`j'') (")") _tab (`2017_mode_3_`j'') _tab (`2018_mode_3_`j'') _tab (`2019_mode_3_`j'') _tab (`2020_mode_3_`j'') _tab (`2021_mode_3_`j'') _tab (`2022_mode_3_`j'') _n
file write tablecontent ("`label`j''") _tab ("Dialysis") _tab (`2017_q2_4_`j'') (" (") (`2017_q1_4_`j'') ("-") (`2017_q3_4_`j'') (")") _tab (`2018_q2_4_`j'') (" (") (`2018_q1_4_`j'') ("-") (`2018_q3_4_`j'') (")") _tab (`2019_q2_4_`j'') (" (") (`2019_q1_4_`j'') ("-") (`2019_q3_4_`j'') (")") _tab (`2020_q2_4_`j'') (" (") (`2020_q1_4_`j'') ("-") (`2020_q3_4_`j'') (")") _tab (`2021_q2_4_`j'') (" (") (`2021_q1_4_`j'') ("-") (`2021_q3_4_`j'') (")") _tab (`2022_q2_4_`j'') (" (") (`2022_q1_4_`j'') ("-") (`2022_q3_4_`j'') (")") _tab (`2017_mode_4_`j'') _tab (`2018_mode_4_`j'') _tab (`2019_mode_4_`j'') _tab (`2020_mode_4_`j'') _tab (`2021_mode_4_`j'') _tab (`2022_mode_4_`j'') _n
file write tablecontent ("`label`j''") _tab ("Transplant") _tab (`2017_q2_5_`j'') (" (") (`2017_q1_5_`j'') ("-") (`2017_q3_5_`j'') (")") _tab (`2018_q2_5_`j'') (" (") (`2018_q1_5_`j'') ("-") (`2018_q3_5_`j'') (")") _tab (`2019_q2_5_`j'') (" (") (`2019_q1_5_`j'') ("-") (`2019_q3_5_`j'') (")") _tab (`2020_q2_5_`j'') (" (") (`2020_q1_5_`j'') ("-") (`2020_q3_5_`j'') (")") _tab (`2021_q2_5_`j'') (" (") (`2021_q1_5_`j'') ("-") (`2021_q3_5_`j'') (")") _tab (`2022_q2_5_`j'') (" (") (`2022_q1_5_`j'') ("-") (`2022_q3_5_`j'') (")") _tab (`2017_mode_5_`j'') _tab (`2018_mode_5_`j'') _tab (`2019_mode_5_`j'') _tab (`2020_mode_5_`j'') _tab (`2021_mode_5_`j'') _tab (`2022_mode_5_`j'') _n
}

*IMD
forvalues j=1/5 {
local label`j': label imd `j'
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if ckd_progression!=6 
drop if imd!=`j'

qui su age, d
local `x'_q2_`j' = r(p50)
local `x'_q1_`j' = r(p25)
local `x'_q3_`j' = r(p75)
egen mode_age = mode(age), minmode
qui su mode_age
local `x'_mode_`j' = r(mean)
drop mode_age

bysort ckd_group: egen mode_age = mode(age), minmode
forvalues i=0/5{
qui su age if ckd_group==`i', d
local `x'_q2_`i'_`j' = r(p50)
local `x'_q1_`i'_`j' = r(p25)
local `x'_q3_`i'_`j' = r(p75)
qui su mode_age if ckd_group==`i'
local `x'_mode_`i'_`j' = r(mean)
}
}
file write tablecontent ("`label`j''") _tab ("All") _tab (`2017_q2_`j'') (" (") (`2017_q1_`j'') ("-") (`2017_q3_`j'') (")") _tab (`2018_q2_`j'') (" (") (`2018_q1_`j'') ("-") (`2018_q3_`j'') (")") _tab (`2019_q2_`j'') (" (") (`2019_q1_`j'') ("-") (`2019_q3_`j'') (")") _tab (`2020_q2_`j'') (" (") (`2020_q1_`j'') ("-") (`2020_q3_`j'') (")") _tab (`2021_q2_`j'') (" (") (`2021_q1_`j'') ("-") (`2021_q3_`j'') (")") _tab (`2022_q2_`j'') (" (") (`2022_q1_`j'') ("-") (`2022_q3_`j'') (")") _tab (`2017_mode_`j'') _tab (`2018_mode_`j'') _tab (`2019_mode_`j'') _tab (`2020_mode_`j'') _tab (`2021_mode_`j'') _tab (`2022_mode_`j'') _n
file write tablecontent ("`label`j''") _tab ("No CKD") _tab (`2017_q2_0_`j'') (" (") (`2017_q1_0_`j'') ("-") (`2017_q3_0_`j'') (")") _tab (`2018_q2_0_`j'') (" (") (`2018_q1_0_`j'') ("-") (`2018_q3_0_`j'') (")") _tab (`2019_q2_0_`j'') (" (") (`2019_q1_0_`j'') ("-") (`2019_q3_0_`j'') (")") _tab (`2020_q2_0_`j'') (" (") (`2020_q1_0_`j'') ("-") (`2020_q3_0_`j'') (")") _tab (`2021_q2_0_`j'') (" (") (`2021_q1_0_`j'') ("-") (`2021_q3_0_`j'') (")") _tab (`2022_q2_0_`j'') (" (") (`2022_q1_0_`j'') ("-") (`2022_q3_0_`j'') (")") _tab (`2017_mode_0_`j'') _tab (`2018_mode_0_`j'') _tab (`2019_mode_0_`j'') _tab (`2020_mode_0_`j'') _tab (`2021_mode_0_`j'') _tab (`2022_mode_0_`j'') _n
file write tablecontent ("`label`j''") _tab ("Albuminuria") _tab (`2017_q2_1_`j'') (" (") (`2017_q1_1_`j'') ("-") (`2017_q3_1_`j'') (")") _tab (`2018_q2_1_`j'') (" (") (`2018_q1_1_`j'') ("-") (`2018_q3_1_`j'') (")") _tab (`2019_q2_1_`j'') (" (") (`2019_q1_1_`j'') ("-") (`2019_q3_1_`j'') (")") _tab (`2020_q2_1_`j'') (" (") (`2020_q1_1_`j'') ("-") (`2020_q3_1_`j'') (")") _tab (`2021_q2_1_`j'') (" (") (`2021_q1_1_`j'') ("-") (`2021_q3_1_`j'') (")") _tab (`2022_q2_1_`j'') (" (") (`2022_q1_1_`j'') ("-") (`2022_q3_1_`j'') (")") _tab (`2017_mode_1_`j'') _tab (`2018_mode_1_`j'') _tab (`2019_mode_1_`j'') _tab (`2020_mode_1_`j'') _tab (`2021_mode_1_`j'') _tab (`2022_mode_1_`j'') _n
file write tablecontent ("`label`j''") _tab ("CKD stage 3") _tab (`2017_q2_2_`j'') (" (") (`2017_q1_2_`j'') ("-") (`2017_q3_2_`j'') (")") _tab (`2018_q2_2_`j'') (" (") (`2018_q1_2_`j'') ("-") (`2018_q3_2_`j'') (")") _tab (`2019_q2_2_`j'') (" (") (`2019_q1_2_`j'') ("-") (`2019_q3_2_`j'') (")") _tab (`2020_q2_2_`j'') (" (") (`2020_q1_2_`j'') ("-") (`2020_q3_2_`j'') (")") _tab (`2021_q2_2_`j'') (" (") (`2021_q1_2_`j'') ("-") (`2021_q3_2_`j'') (")") _tab (`2022_q2_2_`j'') (" (") (`2022_q1_2_`j'') ("-") (`2022_q3_2_`j'') (")") _tab (`2017_mode_2_`j'') _tab (`2018_mode_2_`j'') _tab (`2019_mode_2_`j'') _tab (`2020_mode_2_`j'') _tab (`2021_mode_2_`j'') _tab (`2022_mode_2_`j'') _n
file write tablecontent ("`label`j''") _tab ("CKD stage 4/5") _tab (`2017_q2_3_`j'') (" (") (`2017_q1_3_`j'') ("-") (`2017_q3_3_`j'') (")") _tab (`2018_q2_3_`j'') (" (") (`2018_q1_3_`j'') ("-") (`2018_q3_3_`j'') (")") _tab (`2019_q2_3_`j'') (" (") (`2019_q1_3_`j'') ("-") (`2019_q3_3_`j'') (")") _tab (`2020_q2_3_`j'') (" (") (`2020_q1_3_`j'') ("-") (`2020_q3_3_`j'') (")") _tab (`2021_q2_3_`j'') (" (") (`2021_q1_3_`j'') ("-") (`2021_q3_3_`j'') (")") _tab (`2022_q2_3_`j'') (" (") (`2022_q1_3_`j'') ("-") (`2022_q3_3_`j'') (")") _tab (`2017_mode_3_`j'') _tab (`2018_mode_3_`j'') _tab (`2019_mode_3_`j'') _tab (`2020_mode_3_`j'') _tab (`2021_mode_3_`j'') _tab (`2022_mode_3_`j'') _n
file write tablecontent ("`label`j''") _tab ("Dialysis") _tab (`2017_q2_4_`j'') (" (") (`2017_q1_4_`j'') ("-") (`2017_q3_4_`j'') (")") _tab (`2018_q2_4_`j'') (" (") (`2018_q1_4_`j'') ("-") (`2018_q3_4_`j'') (")") _tab (`2019_q2_4_`j'') (" (") (`2019_q1_4_`j'') ("-") (`2019_q3_4_`j'') (")") _tab (`2020_q2_4_`j'') (" (") (`2020_q1_4_`j'') ("-") (`2020_q3_4_`j'') (")") _tab (`2021_q2_4_`j'') (" (") (`2021_q1_4_`j'') ("-") (`2021_q3_4_`j'') (")") _tab (`2022_q2_4_`j'') (" (") (`2022_q1_4_`j'') ("-") (`2022_q3_4_`j'') (")") _tab (`2017_mode_4_`j'') _tab (`2018_mode_4_`j'') _tab (`2019_mode_4_`j'') _tab (`2020_mode_4_`j'') _tab (`2021_mode_4_`j'') _tab (`2022_mode_4_`j'') _n
file write tablecontent ("`label`j''") _tab ("Transplant") _tab (`2017_q2_5_`j'') (" (") (`2017_q1_5_`j'') ("-") (`2017_q3_5_`j'') (")") _tab (`2018_q2_5_`j'') (" (") (`2018_q1_5_`j'') ("-") (`2018_q3_5_`j'') (")") _tab (`2019_q2_5_`j'') (" (") (`2019_q1_5_`j'') ("-") (`2019_q3_5_`j'') (")") _tab (`2020_q2_5_`j'') (" (") (`2020_q1_5_`j'') ("-") (`2020_q3_5_`j'') (")") _tab (`2021_q2_5_`j'') (" (") (`2021_q1_5_`j'') ("-") (`2021_q3_5_`j'') (")") _tab (`2022_q2_5_`j'') (" (") (`2022_q1_5_`j'') ("-") (`2022_q3_5_`j'') (")") _tab (`2017_mode_5_`j'') _tab (`2018_mode_5_`j'') _tab (`2019_mode_5_`j'') _tab (`2020_mode_5_`j'') _tab (`2021_mode_5_`j'') _tab (`2022_mode_5_`j'') _n
}

file close tablecontent