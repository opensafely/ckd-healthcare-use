
/****Can use this code to obtain standardised population counts
total weight
local baseline_ckd_2020 = r(table)[1,1]
local baseline_ckd_2020_ll = r(table)[5,1]
local baseline_ckd_2020_ul = r(table)[6,1]
*/

sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/standardised_ckd_progression.log, replace t

cap file close tablecontent
file open tablecontent using ./output/standardised_ckd_progression.csv, write text replace

file write tablecontent ("stratum") _tab ("start_status") _tab ("end_status") _tab ("count_2017") _tab ("count_2018") _tab ("count_2019") _tab ("count_2020") _tab ("count_2021") _tab ("count_2022") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete

**Overall
qui total weight
local baseline_ckd_`x' = r(table)[1,1]
*Total number of people in group who do not progress by the end of the year
qui total weight if ckd_progression==0
local none_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_progression==1
local ckd3_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_progression==2
local ckd4_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_progression==3
local dialysis_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_progression==4
local kt_ckd_`x' = r(table)[1,1]
*Total number of people in group who die by the end of the year
qui total weight if ckd_progression==6
local deceased_ckd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1
local cardio_ckd_`x' = r(table)[1,1]

**No CKD
*Number of people without CKD at the beginning of each year
qui total weight if ckd_group==0
local baseline_nockd_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==0 & ckd_progression==0
local none_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==0 & ckd_progression==1
local ckd3_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==0 & ckd_progression==2
local ckd4_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==0 & ckd_progression==3
local dialysis_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==0 & ckd_progression==4
local kt_nockd_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==0 & ckd_progression==6
local deceased_nockd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==0
local cardio_nockd_`x' = r(table)[1,1]

**eGFR >60 with albuminuria
*Number of people in group (baseline_ckd2_`x') at the beginning of each year
qui total weight if ckd_group==1
local baseline_ckd2_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==1 & ckd_progression==0
local none_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==1 & ckd_progression==1
local ckd3_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==1 & ckd_progression==2
local ckd4_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==1 & ckd_progression==3
local dialysis_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==1 & ckd_progression==4
local kt_ckd2_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==1 & ckd_progression==6
local deceased_ckd2_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==1
local cardio_ckd2_`x' = r(table)[1,1]

**CKD stage 3
*Number of people in group (baseline_ckd3_`x') at the beginning of each year
qui total weight if ckd_group==2
local baseline_ckd3_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==2 & ckd_progression==0
local none_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==2 & ckd_progression==2
local ckd4_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==2 & ckd_progression==3
local dialysis_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==2 & ckd_progression==4
local kt_ckd3_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==2 & ckd_progression==6
local deceased_ckd3_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==2
local cardio_ckd3_`x' = r(table)[1,1]

**CKD stage 4/5 without KRT
*Number of people in group (baseline_ckd4_`x') at the beginning of each year
qui total weight if ckd_group==3
local baseline_ckd4_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==3 & ckd_progression==0
local none_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==3 & ckd_progression==3
local dialysis_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==3 & ckd_progression==6
local deceased_ckd4_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==3
local cardio_ckd4_`x' = r(table)[1,1]

**Dialysis
*Number of people in group (baseline_dialysis_`x') at the beginning of each year
qui total weight if ckd_group==4
local baseline_dialysis_`x' = r(table)[1,1]
*Number of people in group remaining on dialysis by the end of the year
qui total weight if ckd_group==4 & ckd_progression==0
local none_dialysis_`x' = r(table)[1,1]
*Number of people in group with kidney transplant by the end of the year
qui total weight if ckd_group==4 & ckd_progression==4
local kt_dialysis_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==4 & ckd_progression==6
local deceased_dialysis_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==4
local cardio_dialysis_`x' = r(table)[1,1]

**Kidney transplant
*Number of people in group (baseline_kt_`x') at the beginning of each year
qui total weight if ckd_group==5
local baseline_kt_`x' = r(table)[1,1]
*Number of people in group remaining with kidney transplant by the end of the year
qui total weight if ckd_group==5 & ckd_progression==0
local none_kt_`x' = r(table)[1,1]
*Number of people in group on dialysis by the end of the year
qui total weight if ckd_group==5 & ckd_progression==3
local dialysis_kt_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==5
local cardio_kt_`x' = r(table)[1,1]
}

**Populate table with redacted counts
*Overall
file write tablecontent ("All") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2022') _n
file write tablecontent ("All") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2022') _n
file write tablecontent ("All") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2022') _n
file write tablecontent ("All") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2022') _n
file write tablecontent ("All") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2022') _n
file write tablecontent ("All") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2022') _n
file write tablecontent ("All") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2022') _n
file write tablecontent ("All") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2022') _n

*No CKD
file write tablecontent ("All") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2022') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2022') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2022') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2022') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2022') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("Transplant") _tab %10.2f (`kt_nockd_2017') _tab %10.2f (`kt_nockd_2018') _tab %10.2f (`kt_nockd_2019') _tab %10.2f (`kt_nockd_2020') _tab %10.2f (`kt_nockd_2021') _tab %10.2f (`kt_nockd_2022') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2022') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2022') _n

*eGFR >60 with albuminuria
file write tablecontent ("All") _tab ("Albuminuria") _tab ("N/A") _tab %10.2f (`baseline_ckd2_2017') _tab %10.2f (`baseline_ckd2_2018') _tab %10.2f (`baseline_ckd2_2019') _tab %10.2f (`baseline_ckd2_2020') _tab %10.2f (`baseline_ckd2_2021') _tab %10.2f (`baseline_ckd2_2022') _n
file write tablecontent ("All") _tab ("Albuminuria") _tab ("No progression") _tab %10.2f (`none_ckd2_2017') _tab %10.2f (`none_ckd2_2018') _tab %10.2f (`none_ckd2_2019') _tab %10.2f (`none_ckd2_2020') _tab %10.2f (`none_ckd2_2021') _tab %10.2f (`none_ckd2_2022') _n
file write tablecontent ("All") _tab ("Albuminuria") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd2_2017') _tab %10.2f (`ckd3_ckd2_2018') _tab %10.2f (`ckd3_ckd2_2019') _tab %10.2f (`ckd3_ckd2_2020') _tab %10.2f (`ckd3_ckd2_2021') _tab %10.2f (`ckd3_ckd2_2022') _n
file write tablecontent ("All") _tab ("Albuminuria") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd2_2017') _tab %10.2f (`ckd4_ckd2_2018') _tab %10.2f (`ckd4_ckd2_2019') _tab %10.2f (`ckd4_ckd2_2020') _tab %10.2f (`ckd4_ckd2_2021') _tab %10.2f (`ckd4_ckd2_2022') _n
file write tablecontent ("All") _tab ("Albuminuria") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd2_2017') _tab %10.2f (`dialysis_ckd2_2018') _tab %10.2f (`dialysis_ckd2_2019') _tab %10.2f (`dialysis_ckd2_2020') _tab %10.2f (`dialysis_ckd2_2021') _tab %10.2f (`dialysis_ckd2_2022') _n
file write tablecontent ("All") _tab ("Albuminuria") _tab ("Transplant") _tab %10.2f (`kt_ckd2_2017') _tab %10.2f (`kt_ckd2_2018') _tab %10.2f (`kt_ckd2_2019') _tab %10.2f (`kt_ckd2_2020') _tab %10.2f (`kt_ckd2_2021') _tab %10.2f (`kt_ckd2_2022') _n
file write tablecontent ("All") _tab ("Albuminuria") _tab ("Deceased") _tab %10.2f (`deceased_ckd2_2017') _tab %10.2f (`deceased_ckd2_2018') _tab %10.2f (`deceased_ckd2_2019') _tab %10.2f (`deceased_ckd2_2020') _tab %10.2f (`deceased_ckd2_2021') _tab %10.2f (`deceased_ckd2_2022') _n
file write tablecontent ("All") _tab ("Albuminuria") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd2_2017') _tab %10.2f (`cardio_ckd2_2018') _tab %10.2f (`cardio_ckd2_2019') _tab %10.2f (`cardio_ckd2_2020') _tab %10.2f (`cardio_ckd2_2021') _tab %10.2f (`cardio_ckd2_2022') _n

*CKD stage 3
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2022') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2022') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2022') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2022') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("Transplant") _tab %10.2f (`kt_ckd3_2017') _tab %10.2f (`kt_ckd3_2018') _tab %10.2f (`kt_ckd3_2019') _tab %10.2f (`kt_ckd3_2020') _tab %10.2f (`kt_ckd3_2021') _tab %10.2f (`kt_ckd3_2022') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2022') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2022') _n

*CKD stage 4/5 without KRT
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2022') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2022') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2022') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2022') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2022') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2022') _n

*Dialysis
file write tablecontent ("All") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2022') _n
file write tablecontent ("All") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2022') _n
file write tablecontent ("All") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2022') _n
file write tablecontent ("All") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2022') _n
file write tablecontent ("All") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2022') _n

*Kidney Transplant
file write tablecontent ("All") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2022') _n
file write tablecontent ("All") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2022') _n
file write tablecontent ("All") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2022') _n
file write tablecontent ("All") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2022') _n
file write tablecontent ("All") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2022') _n


forvalues i=1/6 {
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
local label`i': label ethnicity `i'
drop if ethnicity!=`i'

**Disclosure minimisation
*safecount provides a count with any counts <=5 returned at "<=5"
*r(table)[1,1] rounds counts to the nearest 5 with any counts <=5 returned as "."

**Overall
qui total weight
local baseline_ckd_`x' = r(table)[1,1]
*Total number of people in group who do not progress by the end of the year
qui total weight if ckd_progression==0
local none_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_progression==1
local ckd3_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_progression==2
local ckd4_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_progression==3
local dialysis_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_progression==4
local kt_ckd_`x' = r(table)[1,1]
*Total number of people in group who die by the end of the year
qui total weight if ckd_progression==6
local deceased_ckd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1
local cardio_ckd_`x' = r(table)[1,1]

**No CKD
*Number of people without CKD at the beginning of each year
qui total weight if ckd_group==0
local baseline_nockd_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==0 & ckd_progression==0
local none_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==0 & ckd_progression==1
local ckd3_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==0 & ckd_progression==2
local ckd4_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==0 & ckd_progression==3
local dialysis_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==0 & ckd_progression==4
local kt_nockd_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==0 & ckd_progression==6
local deceased_nockd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==0
local cardio_nockd_`x' = r(table)[1,1]

**eGFR >60 with albuminuria
*Number of people in group (baseline_ckd2_`x') at the beginning of each year
qui total weight if ckd_group==1
local baseline_ckd2_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==1 & ckd_progression==0
local none_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==1 & ckd_progression==1
local ckd3_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==1 & ckd_progression==2
local ckd4_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==1 & ckd_progression==3
local dialysis_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==1 & ckd_progression==4
local kt_ckd2_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==1 & ckd_progression==6
local deceased_ckd2_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==1
local cardio_ckd2_`x' = r(table)[1,1]

**CKD stage 3
*Number of people in group (baseline_ckd3_`x') at the beginning of each year
qui total weight if ckd_group==2
local baseline_ckd3_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==2 & ckd_progression==0
local none_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==2 & ckd_progression==2
local ckd4_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==2 & ckd_progression==3
local dialysis_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==2 & ckd_progression==4
local kt_ckd3_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==2 & ckd_progression==6
local deceased_ckd3_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==2
local cardio_ckd3_`x' = r(table)[1,1]

**CKD stage 4/5 without KRT
*Number of people in group (baseline_ckd4_`x') at the beginning of each year
qui total weight if ckd_group==3
local baseline_ckd4_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==3 & ckd_progression==0
local none_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==3 & ckd_progression==3
local dialysis_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==3 & ckd_progression==6
local deceased_ckd4_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==3
local cardio_ckd4_`x' = r(table)[1,1]

**Dialysis
*Number of people in group (baseline_dialysis_`x') at the beginning of each year
qui total weight if ckd_group==4
local baseline_dialysis_`x' = r(table)[1,1]
*Number of people in group remaining on dialysis by the end of the year
qui total weight if ckd_group==4 & ckd_progression==0
local none_dialysis_`x' = r(table)[1,1]
*Number of people in group with kidney transplant by the end of the year
qui total weight if ckd_group==4 & ckd_progression==4
local kt_dialysis_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==4 & ckd_progression==6
local deceased_dialysis_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==4
local cardio_dialysis_`x' = r(table)[1,1]

**Kidney transplant
*Number of people in group (baseline_kt_`x') at the beginning of each year
qui total weight if ckd_group==5
local baseline_kt_`x' = r(table)[1,1]
*Number of people in group remaining with kidney transplant by the end of the year
qui total weight if ckd_group==5 & ckd_progression==0
local none_kt_`x' = r(table)[1,1]
*Number of people in group on dialysis by the end of the year
qui total weight if ckd_group==5 & ckd_progression==3
local dialysis_kt_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==5
local cardio_kt_`x' = r(table)[1,1]
}

**Populate table with redacted counts
*Overall
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2022') _n

*No CKD
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Transplant") _tab %10.2f (`kt_nockd_2017') _tab %10.2f (`kt_nockd_2018') _tab %10.2f (`kt_nockd_2019') _tab %10.2f (`kt_nockd_2020') _tab %10.2f (`kt_nockd_2021') _tab %10.2f (`kt_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2022') _n

*eGFR >60 with albuminuria
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("N/A") _tab %10.2f (`baseline_ckd2_2017') _tab %10.2f (`baseline_ckd2_2018') _tab %10.2f (`baseline_ckd2_2019') _tab %10.2f (`baseline_ckd2_2020') _tab %10.2f (`baseline_ckd2_2021') _tab %10.2f (`baseline_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("No progression") _tab %10.2f (`none_ckd2_2017') _tab %10.2f (`none_ckd2_2018') _tab %10.2f (`none_ckd2_2019') _tab %10.2f (`none_ckd2_2020') _tab %10.2f (`none_ckd2_2021') _tab %10.2f (`none_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd2_2017') _tab %10.2f (`ckd3_ckd2_2018') _tab %10.2f (`ckd3_ckd2_2019') _tab %10.2f (`ckd3_ckd2_2020') _tab %10.2f (`ckd3_ckd2_2021') _tab %10.2f (`ckd3_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd2_2017') _tab %10.2f (`ckd4_ckd2_2018') _tab %10.2f (`ckd4_ckd2_2019') _tab %10.2f (`ckd4_ckd2_2020') _tab %10.2f (`ckd4_ckd2_2021') _tab %10.2f (`ckd4_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd2_2017') _tab %10.2f (`dialysis_ckd2_2018') _tab %10.2f (`dialysis_ckd2_2019') _tab %10.2f (`dialysis_ckd2_2020') _tab %10.2f (`dialysis_ckd2_2021') _tab %10.2f (`dialysis_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Transplant") _tab %10.2f (`kt_ckd2_2017') _tab %10.2f (`kt_ckd2_2018') _tab %10.2f (`kt_ckd2_2019') _tab %10.2f (`kt_ckd2_2020') _tab %10.2f (`kt_ckd2_2021') _tab %10.2f (`kt_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Deceased") _tab %10.2f (`deceased_ckd2_2017') _tab %10.2f (`deceased_ckd2_2018') _tab %10.2f (`deceased_ckd2_2019') _tab %10.2f (`deceased_ckd2_2020') _tab %10.2f (`deceased_ckd2_2021') _tab %10.2f (`deceased_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd2_2017') _tab %10.2f (`cardio_ckd2_2018') _tab %10.2f (`cardio_ckd2_2019') _tab %10.2f (`cardio_ckd2_2020') _tab %10.2f (`cardio_ckd2_2021') _tab %10.2f (`cardio_ckd2_2022') _n

*CKD stage 3
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Transplant") _tab %10.2f (`kt_ckd3_2017') _tab %10.2f (`kt_ckd3_2018') _tab %10.2f (`kt_ckd3_2019') _tab %10.2f (`kt_ckd3_2020') _tab %10.2f (`kt_ckd3_2021') _tab %10.2f (`kt_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2022') _n

*CKD stage 4/5 without KRT
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2022') _n

*Dialysis
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2022') _n

*Kidney Transplant
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2022') _n
}

forvalues i=1/5 {
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
local label`i': label imd `i'
drop if imd!=`i'

**Disclosure minimisation
*safecount provides a count with any counts <=5 returned at "<=5"
*r(table)[1,1] rounds counts to the nearest 5 with any counts <=5 returned as "."

**Overall
qui total weight
local baseline_ckd_`x' = r(table)[1,1]
*Total number of people in group who do not progress by the end of the year
qui total weight if ckd_progression==0
local none_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_progression==1
local ckd3_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_progression==2
local ckd4_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_progression==3
local dialysis_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_progression==4
local kt_ckd_`x' = r(table)[1,1]
*Total number of people in group who die by the end of the year
qui total weight if ckd_progression==6
local deceased_ckd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1
local cardio_ckd_`x' = r(table)[1,1]

**No CKD
*Number of people without CKD at the beginning of each year
qui total weight if ckd_group==0
local baseline_nockd_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==0 & ckd_progression==0
local none_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==0 & ckd_progression==1
local ckd3_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==0 & ckd_progression==2
local ckd4_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==0 & ckd_progression==3
local dialysis_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==0 & ckd_progression==4
local kt_nockd_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==0 & ckd_progression==6
local deceased_nockd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==0
local cardio_nockd_`x' = r(table)[1,1]

**eGFR >60 with albuminuria
*Number of people in group (baseline_ckd2_`x') at the beginning of each year
qui total weight if ckd_group==1
local baseline_ckd2_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==1 & ckd_progression==0
local none_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==1 & ckd_progression==1
local ckd3_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==1 & ckd_progression==2
local ckd4_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==1 & ckd_progression==3
local dialysis_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==1 & ckd_progression==4
local kt_ckd2_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==1 & ckd_progression==6
local deceased_ckd2_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==1
local cardio_ckd2_`x' = r(table)[1,1]

**CKD stage 3
*Number of people in group (baseline_ckd3_`x') at the beginning of each year
qui total weight if ckd_group==2
local baseline_ckd3_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==2 & ckd_progression==0
local none_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==2 & ckd_progression==2
local ckd4_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==2 & ckd_progression==3
local dialysis_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==2 & ckd_progression==4
local kt_ckd3_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==2 & ckd_progression==6
local deceased_ckd3_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==2
local cardio_ckd3_`x' = r(table)[1,1]

**CKD stage 4/5 without KRT
*Number of people in group (baseline_ckd4_`x') at the beginning of each year
qui total weight if ckd_group==3
local baseline_ckd4_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==3 & ckd_progression==0
local none_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==3 & ckd_progression==3
local dialysis_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==3 & ckd_progression==6
local deceased_ckd4_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==3
local cardio_ckd4_`x' = r(table)[1,1]

**Dialysis
*Number of people in group (baseline_dialysis_`x') at the beginning of each year
qui total weight if ckd_group==4
local baseline_dialysis_`x' = r(table)[1,1]
*Number of people in group remaining on dialysis by the end of the year
qui total weight if ckd_group==4 & ckd_progression==0
local none_dialysis_`x' = r(table)[1,1]
*Number of people in group with kidney transplant by the end of the year
qui total weight if ckd_group==4 & ckd_progression==4
local kt_dialysis_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==4 & ckd_progression==6
local deceased_dialysis_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==4
local cardio_dialysis_`x' = r(table)[1,1]

**Kidney transplant
*Number of people in group (baseline_kt_`x') at the beginning of each year
qui total weight if ckd_group==5
local baseline_kt_`x' = r(table)[1,1]
*Number of people in group remaining with kidney transplant by the end of the year
qui total weight if ckd_group==5 & ckd_progression==0
local none_kt_`x' = r(table)[1,1]
*Number of people in group on dialysis by the end of the year
qui total weight if ckd_group==5 & ckd_progression==3
local dialysis_kt_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==5
local cardio_kt_`x' = r(table)[1,1]
}

**Populate table with redacted counts
*Overall
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2022') _n

*No CKD
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Transplant") _tab %10.2f (`kt_nockd_2017') _tab %10.2f (`kt_nockd_2018') _tab %10.2f (`kt_nockd_2019') _tab %10.2f (`kt_nockd_2020') _tab %10.2f (`kt_nockd_2021') _tab %10.2f (`kt_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2022') _n

*eGFR >60 with albuminuria
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("N/A") _tab %10.2f (`baseline_ckd2_2017') _tab %10.2f (`baseline_ckd2_2018') _tab %10.2f (`baseline_ckd2_2019') _tab %10.2f (`baseline_ckd2_2020') _tab %10.2f (`baseline_ckd2_2021') _tab %10.2f (`baseline_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("No progression") _tab %10.2f (`none_ckd2_2017') _tab %10.2f (`none_ckd2_2018') _tab %10.2f (`none_ckd2_2019') _tab %10.2f (`none_ckd2_2020') _tab %10.2f (`none_ckd2_2021') _tab %10.2f (`none_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd2_2017') _tab %10.2f (`ckd3_ckd2_2018') _tab %10.2f (`ckd3_ckd2_2019') _tab %10.2f (`ckd3_ckd2_2020') _tab %10.2f (`ckd3_ckd2_2021') _tab %10.2f (`ckd3_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd2_2017') _tab %10.2f (`ckd4_ckd2_2018') _tab %10.2f (`ckd4_ckd2_2019') _tab %10.2f (`ckd4_ckd2_2020') _tab %10.2f (`ckd4_ckd2_2021') _tab %10.2f (`ckd4_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd2_2017') _tab %10.2f (`dialysis_ckd2_2018') _tab %10.2f (`dialysis_ckd2_2019') _tab %10.2f (`dialysis_ckd2_2020') _tab %10.2f (`dialysis_ckd2_2021') _tab %10.2f (`dialysis_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Transplant") _tab %10.2f (`kt_ckd2_2017') _tab %10.2f (`kt_ckd2_2018') _tab %10.2f (`kt_ckd2_2019') _tab %10.2f (`kt_ckd2_2020') _tab %10.2f (`kt_ckd2_2021') _tab %10.2f (`kt_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Deceased") _tab %10.2f (`deceased_ckd2_2017') _tab %10.2f (`deceased_ckd2_2018') _tab %10.2f (`deceased_ckd2_2019') _tab %10.2f (`deceased_ckd2_2020') _tab %10.2f (`deceased_ckd2_2021') _tab %10.2f (`deceased_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd2_2017') _tab %10.2f (`cardio_ckd2_2018') _tab %10.2f (`cardio_ckd2_2019') _tab %10.2f (`cardio_ckd2_2020') _tab %10.2f (`cardio_ckd2_2021') _tab %10.2f (`cardio_ckd2_2022') _n

*CKD stage 3
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Transplant") _tab %10.2f (`kt_ckd3_2017') _tab %10.2f (`kt_ckd3_2018') _tab %10.2f (`kt_ckd3_2019') _tab %10.2f (`kt_ckd3_2020') _tab %10.2f (`kt_ckd3_2021') _tab %10.2f (`kt_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2022') _n

*CKD stage 4/5 without KRT
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2022') _n

*Dialysis
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2022') _n

*Kidney Transplant
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2022') _n
}

forvalues i=1/9 {
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
local label`i': label region `i'
drop if region!=`i'

**Disclosure minimisation
*safecount provides a count with any counts <=5 returned at "<=5"
*r(table)[1,1] rounds counts to the nearest 5 with any counts <=5 returned as "."

**Overall
qui total weight
local baseline_ckd_`x' = r(table)[1,1]
*Total number of people in group who do not progress by the end of the year
qui total weight if ckd_progression==0
local none_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_progression==1
local ckd3_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_progression==2
local ckd4_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_progression==3
local dialysis_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_progression==4
local kt_ckd_`x' = r(table)[1,1]
*Total number of people in group who die by the end of the year
qui total weight if ckd_progression==6
local deceased_ckd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1
local cardio_ckd_`x' = r(table)[1,1]

**No CKD
*Number of people without CKD at the beginning of each year
qui total weight if ckd_group==0
local baseline_nockd_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==0 & ckd_progression==0
local none_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==0 & ckd_progression==1
local ckd3_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==0 & ckd_progression==2
local ckd4_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==0 & ckd_progression==3
local dialysis_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==0 & ckd_progression==4
local kt_nockd_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==0 & ckd_progression==6
local deceased_nockd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==0
local cardio_nockd_`x' = r(table)[1,1]

**eGFR >60 with albuminuria
*Number of people in group (baseline_ckd2_`x') at the beginning of each year
qui total weight if ckd_group==1
local baseline_ckd2_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==1 & ckd_progression==0
local none_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==1 & ckd_progression==1
local ckd3_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==1 & ckd_progression==2
local ckd4_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==1 & ckd_progression==3
local dialysis_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==1 & ckd_progression==4
local kt_ckd2_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==1 & ckd_progression==6
local deceased_ckd2_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==1
local cardio_ckd2_`x' = r(table)[1,1]

**CKD stage 3
*Number of people in group (baseline_ckd3_`x') at the beginning of each year
qui total weight if ckd_group==2
local baseline_ckd3_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==2 & ckd_progression==0
local none_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==2 & ckd_progression==2
local ckd4_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==2 & ckd_progression==3
local dialysis_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==2 & ckd_progression==4
local kt_ckd3_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==2 & ckd_progression==6
local deceased_ckd3_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==2
local cardio_ckd3_`x' = r(table)[1,1]

**CKD stage 4/5 without KRT
*Number of people in group (baseline_ckd4_`x') at the beginning of each year
qui total weight if ckd_group==3
local baseline_ckd4_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==3 & ckd_progression==0
local none_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==3 & ckd_progression==3
local dialysis_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==3 & ckd_progression==6
local deceased_ckd4_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==3
local cardio_ckd4_`x' = r(table)[1,1]

**Dialysis
*Number of people in group (baseline_dialysis_`x') at the beginning of each year
qui total weight if ckd_group==4
local baseline_dialysis_`x' = r(table)[1,1]
*Number of people in group remaining on dialysis by the end of the year
qui total weight if ckd_group==4 & ckd_progression==0
local none_dialysis_`x' = r(table)[1,1]
*Number of people in group with kidney transplant by the end of the year
qui total weight if ckd_group==4 & ckd_progression==4
local kt_dialysis_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==4 & ckd_progression==6
local deceased_dialysis_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==4
local cardio_dialysis_`x' = r(table)[1,1]

**Kidney transplant
*Number of people in group (baseline_kt_`x') at the beginning of each year
qui total weight if ckd_group==5
local baseline_kt_`x' = r(table)[1,1]
*Number of people in group remaining with kidney transplant by the end of the year
qui total weight if ckd_group==5 & ckd_progression==0
local none_kt_`x' = r(table)[1,1]
*Number of people in group on dialysis by the end of the year
qui total weight if ckd_group==5 & ckd_progression==3
local dialysis_kt_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==5
local cardio_kt_`x' = r(table)[1,1]
}

**Populate table with redacted counts
*Overall
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2022') _n

*No CKD
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Transplant") _tab %10.2f (`kt_nockd_2017') _tab %10.2f (`kt_nockd_2018') _tab %10.2f (`kt_nockd_2019') _tab %10.2f (`kt_nockd_2020') _tab %10.2f (`kt_nockd_2021') _tab %10.2f (`kt_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2022') _n

*eGFR >60 with albuminuria
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("N/A") _tab %10.2f (`baseline_ckd2_2017') _tab %10.2f (`baseline_ckd2_2018') _tab %10.2f (`baseline_ckd2_2019') _tab %10.2f (`baseline_ckd2_2020') _tab %10.2f (`baseline_ckd2_2021') _tab %10.2f (`baseline_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("No progression") _tab %10.2f (`none_ckd2_2017') _tab %10.2f (`none_ckd2_2018') _tab %10.2f (`none_ckd2_2019') _tab %10.2f (`none_ckd2_2020') _tab %10.2f (`none_ckd2_2021') _tab %10.2f (`none_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd2_2017') _tab %10.2f (`ckd3_ckd2_2018') _tab %10.2f (`ckd3_ckd2_2019') _tab %10.2f (`ckd3_ckd2_2020') _tab %10.2f (`ckd3_ckd2_2021') _tab %10.2f (`ckd3_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd2_2017') _tab %10.2f (`ckd4_ckd2_2018') _tab %10.2f (`ckd4_ckd2_2019') _tab %10.2f (`ckd4_ckd2_2020') _tab %10.2f (`ckd4_ckd2_2021') _tab %10.2f (`ckd4_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd2_2017') _tab %10.2f (`dialysis_ckd2_2018') _tab %10.2f (`dialysis_ckd2_2019') _tab %10.2f (`dialysis_ckd2_2020') _tab %10.2f (`dialysis_ckd2_2021') _tab %10.2f (`dialysis_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Transplant") _tab %10.2f (`kt_ckd2_2017') _tab %10.2f (`kt_ckd2_2018') _tab %10.2f (`kt_ckd2_2019') _tab %10.2f (`kt_ckd2_2020') _tab %10.2f (`kt_ckd2_2021') _tab %10.2f (`kt_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Deceased") _tab %10.2f (`deceased_ckd2_2017') _tab %10.2f (`deceased_ckd2_2018') _tab %10.2f (`deceased_ckd2_2019') _tab %10.2f (`deceased_ckd2_2020') _tab %10.2f (`deceased_ckd2_2021') _tab %10.2f (`deceased_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd2_2017') _tab %10.2f (`cardio_ckd2_2018') _tab %10.2f (`cardio_ckd2_2019') _tab %10.2f (`cardio_ckd2_2020') _tab %10.2f (`cardio_ckd2_2021') _tab %10.2f (`cardio_ckd2_2022') _n

*CKD stage 3
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Transplant") _tab %10.2f (`kt_ckd3_2017') _tab %10.2f (`kt_ckd3_2018') _tab %10.2f (`kt_ckd3_2019') _tab %10.2f (`kt_ckd3_2020') _tab %10.2f (`kt_ckd3_2021') _tab %10.2f (`kt_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2022') _n

*CKD stage 4/5 without KRT
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2022') _n

*Dialysis
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2022') _n

*Kidney Transplant
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2022') _n
}

forvalues i=0/1 {
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
local label`i': label urban `i'
drop if urban!=`i'

**Disclosure minimisation
*safecount provides a count with any counts <=5 returned at "<=5"
*r(table)[1,1] rounds counts to the nearest 5 with any counts <=5 returned as "."

**Overall
qui total weight
local baseline_ckd_`x' = r(table)[1,1]
*Total number of people in group who do not progress by the end of the year
qui total weight if ckd_progression==0
local none_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_progression==1
local ckd3_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_progression==2
local ckd4_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_progression==3
local dialysis_ckd_`x' = r(table)[1,1]
*Total number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_progression==4
local kt_ckd_`x' = r(table)[1,1]
*Total number of people in group who die by the end of the year
qui total weight if ckd_progression==6
local deceased_ckd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1
local cardio_ckd_`x' = r(table)[1,1]

**No CKD
*Number of people without CKD at the beginning of each year
qui total weight if ckd_group==0
local baseline_nockd_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==0 & ckd_progression==0
local none_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==0 & ckd_progression==1
local ckd3_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==0 & ckd_progression==2
local ckd4_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==0 & ckd_progression==3
local dialysis_nockd_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==0 & ckd_progression==4
local kt_nockd_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==0 & ckd_progression==6
local deceased_nockd_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==0
local cardio_nockd_`x' = r(table)[1,1]

**eGFR >60 with albuminuria
*Number of people in group (baseline_ckd2_`x') at the beginning of each year
qui total weight if ckd_group==1
local baseline_ckd2_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==1 & ckd_progression==0
local none_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 3 by the end of the year
qui total weight if ckd_group==1 & ckd_progression==1
local ckd3_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==1 & ckd_progression==2
local ckd4_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==1 & ckd_progression==3
local dialysis_ckd2_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==1 & ckd_progression==4
local kt_ckd2_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==1 & ckd_progression==6
local deceased_ckd2_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==1
local cardio_ckd2_`x' = r(table)[1,1]

**CKD stage 3
*Number of people in group (baseline_ckd3_`x') at the beginning of each year
qui total weight if ckd_group==2
local baseline_ckd3_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==2 & ckd_progression==0
local none_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui total weight if ckd_group==2 & ckd_progression==2
local ckd4_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==2 & ckd_progression==3
local dialysis_ckd3_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==2 & ckd_progression==4
local kt_ckd3_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==2 & ckd_progression==6
local deceased_ckd3_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==2
local cardio_ckd3_`x' = r(table)[1,1]

**CKD stage 4/5 without KRT
*Number of people in group (baseline_ckd4_`x') at the beginning of each year
qui total weight if ckd_group==3
local baseline_ckd4_`x' = r(table)[1,1]
*Number of people in group who do not progress by the end of the year
qui total weight if ckd_group==3 & ckd_progression==0
local none_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to dialysis by the end of the year
qui total weight if ckd_group==3 & ckd_progression==3
local dialysis_ckd4_`x' = r(table)[1,1]
*Number of people in group who progress to kidney transplant by the end of the year
qui total weight if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==3 & ckd_progression==6
local deceased_ckd4_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==3
local cardio_ckd4_`x' = r(table)[1,1]

**Dialysis
*Number of people in group (baseline_dialysis_`x') at the beginning of each year
qui total weight if ckd_group==4
local baseline_dialysis_`x' = r(table)[1,1]
*Number of people in group remaining on dialysis by the end of the year
qui total weight if ckd_group==4 & ckd_progression==0
local none_dialysis_`x' = r(table)[1,1]
*Number of people in group with kidney transplant by the end of the year
qui total weight if ckd_group==4 & ckd_progression==4
local kt_dialysis_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==4 & ckd_progression==6
local deceased_dialysis_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==4
local cardio_dialysis_`x' = r(table)[1,1]

**Kidney transplant
*Number of people in group (baseline_kt_`x') at the beginning of each year
qui total weight if ckd_group==5
local baseline_kt_`x' = r(table)[1,1]
*Number of people in group remaining with kidney transplant by the end of the year
qui total weight if ckd_group==5 & ckd_progression==0
local none_kt_`x' = r(table)[1,1]
*Number of people in group on dialysis by the end of the year
qui total weight if ckd_group==5 & ckd_progression==3
local dialysis_kt_`x' = r(table)[1,1]
*Number of people in group who die by the end of the year
qui total weight if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = r(table)[1,1]
*Total number of people in groupw with cardiovascular admission each year
qui total weight if cardiovascular==1 & ckd_group==5
local cardio_kt_`x' = r(table)[1,1]
}

**Populate table with redacted counts
*Overall
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2022') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2022') _n

*No CKD
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Transplant") _tab %10.2f (`kt_nockd_2017') _tab %10.2f (`kt_nockd_2018') _tab %10.2f (`kt_nockd_2019') _tab %10.2f (`kt_nockd_2020') _tab %10.2f (`kt_nockd_2021') _tab %10.2f (`kt_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2022') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2022') _n

*eGFR >60 with albuminuria
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("N/A") _tab %10.2f (`baseline_ckd2_2017') _tab %10.2f (`baseline_ckd2_2018') _tab %10.2f (`baseline_ckd2_2019') _tab %10.2f (`baseline_ckd2_2020') _tab %10.2f (`baseline_ckd2_2021') _tab %10.2f (`baseline_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("No progression") _tab %10.2f (`none_ckd2_2017') _tab %10.2f (`none_ckd2_2018') _tab %10.2f (`none_ckd2_2019') _tab %10.2f (`none_ckd2_2020') _tab %10.2f (`none_ckd2_2021') _tab %10.2f (`none_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd2_2017') _tab %10.2f (`ckd3_ckd2_2018') _tab %10.2f (`ckd3_ckd2_2019') _tab %10.2f (`ckd3_ckd2_2020') _tab %10.2f (`ckd3_ckd2_2021') _tab %10.2f (`ckd3_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd2_2017') _tab %10.2f (`ckd4_ckd2_2018') _tab %10.2f (`ckd4_ckd2_2019') _tab %10.2f (`ckd4_ckd2_2020') _tab %10.2f (`ckd4_ckd2_2021') _tab %10.2f (`ckd4_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd2_2017') _tab %10.2f (`dialysis_ckd2_2018') _tab %10.2f (`dialysis_ckd2_2019') _tab %10.2f (`dialysis_ckd2_2020') _tab %10.2f (`dialysis_ckd2_2021') _tab %10.2f (`dialysis_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Transplant") _tab %10.2f (`kt_ckd2_2017') _tab %10.2f (`kt_ckd2_2018') _tab %10.2f (`kt_ckd2_2019') _tab %10.2f (`kt_ckd2_2020') _tab %10.2f (`kt_ckd2_2021') _tab %10.2f (`kt_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Deceased") _tab %10.2f (`deceased_ckd2_2017') _tab %10.2f (`deceased_ckd2_2018') _tab %10.2f (`deceased_ckd2_2019') _tab %10.2f (`deceased_ckd2_2020') _tab %10.2f (`deceased_ckd2_2021') _tab %10.2f (`deceased_ckd2_2022') _n
file write tablecontent ("`label`i''") _tab ("Albuminuria") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd2_2017') _tab %10.2f (`cardio_ckd2_2018') _tab %10.2f (`cardio_ckd2_2019') _tab %10.2f (`cardio_ckd2_2020') _tab %10.2f (`cardio_ckd2_2021') _tab %10.2f (`cardio_ckd2_2022') _n

*CKD stage 3
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Transplant") _tab %10.2f (`kt_ckd3_2017') _tab %10.2f (`kt_ckd3_2018') _tab %10.2f (`kt_ckd3_2019') _tab %10.2f (`kt_ckd3_2020') _tab %10.2f (`kt_ckd3_2021') _tab %10.2f (`kt_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2022') _n

*CKD stage 4/5 without KRT
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2022') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2022') _n

*Dialysis
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2022') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2022') _n

*Kidney Transplant
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2022') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2022') _n
}

file close tablecontent

export delimited "./output/ckd_progression.csv", replace