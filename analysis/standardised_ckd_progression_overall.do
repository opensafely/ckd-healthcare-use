sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/standardised_ckd_progression_overall.log, replace t

cap file close tablecontent
file open tablecontent using ./output/standardised_ckd_progression_overall.csv, write text replace

file write tablecontent ("stratum") _tab ("start_status") _tab ("end_status") _tab ("2017") _tab ("2017_ll") _tab ("2017_ul") _tab ("2018") _tab ("2018_ll") _tab ("2018_ul")  _tab ("2019") _tab ("2019_ll") _tab ("2019_ul") _tab ("2020") _tab ("2020_ll") _tab ("2020_ul") _tab ("2021") _tab ("2021_ll") _tab ("2021_ul") _tab ("2022") _tab ("2022_ll") _tab ("2022_ul") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete

replace ckd_group = 0 if ckd_group==1

**Overall
total weight
local baseline_ckd_`x' = r(table)[1,1]
local baseline_ckd_`x'_ll = r(table)[5,1]
local baseline_ckd_`x'_ul = r(table)[6,1]

total weight if ckd_progression==0
local none_ckd_`x' = r(table)[1,1]
local none_ckd_`x'_ll = r(table)[5,1]
local none_ckd_`x'_ul = r(table)[6,1]

total weight if ckd_progression==1
local ckd3_ckd_`x' = r(table)[1,1]
local ckd3_ckd_`x'_ll = r(table)[5,1]
local ckd3_ckd_`x'_ul = r(table)[6,1]

total weight if ckd_progression==2
local ckd4_ckd_`x' = r(table)[1,1]
local ckd4_ckd_`x'_ll = r(table)[5,1]
local ckd4_ckd_`x'_ul = r(table)[6,1]

total weight if ckd_progression==3
local dialysis_ckd_`x' = r(table)[1,1]
local dialysis_ckd_`x'_ll = r(table)[5,1]
local dialysis_ckd_`x'_ul = r(table)[6,1]

total weight if ckd_progression==4
local kt_ckd_`x' = r(table)[1,1]
local kt_ckd_`x'_ll = r(table)[5,1]
local kt_ckd_`x'_ul = r(table)[6,1]

total weight if ckd_progression==6
local deceased_ckd_`x' = r(table)[1,1]
local deceased_ckd_`x'_ll = r(table)[5,1]
local deceased_ckd_`x'_ul = r(table)[6,1]

total weight if cardiovascular==1
local cardio_ckd_`x' = r(table)[1,1]
local cardio_ckd_`x'_ll = r(table)[5,1]
local cardio_ckd_`x'_ul = r(table)[6,1]

**No CKD
total weight if ckd_group==0
local baseline_nockd_`x' = r(table)[1,1]
local baseline_nockd_`x'_ll = r(table)[5,1]
local baseline_nockd_`x'_ul = r(table)[6,1]

total weight if ckd_group==0 & ckd_progression==0
local none_nockd_`x' = r(table)[1,1]
local none_nockd_`x'_ll = r(table)[5,1]
local none_nockd_`x'_ul = r(table)[6,1]

total weight if ckd_group==0 & ckd_progression==1
local ckd3_nockd_`x' = r(table)[1,1]
local ckd3_nockd_`x'_ll = r(table)[5,1]
local ckd3_nockd_`x'_ul = r(table)[6,1]

total weight if ckd_group==0 & ckd_progression==2
local ckd4_nockd_`x' = r(table)[1,1]
local ckd4_nockd_`x'_ll = r(table)[5,1]
local ckd4_nockd_`x'_ul = r(table)[6,1]

total weight if ckd_group==0 & ckd_progression==3
local dialysis_nockd_`x' = r(table)[1,1]
local dialysis_nockd_`x'_ll = r(table)[5,1]
local dialysis_nockd_`x'_ul = r(table)[6,1]

total weight if ckd_group==0 & ckd_progression==4
local kt_nockd_`x' = r(table)[1,1]
local kt_nockd_`x'_ll = r(table)[5,1]
local kt_nockd_`x'_ul = r(table)[6,1]

total weight if ckd_group==0 & ckd_progression==6
local deceased_nockd_`x' = r(table)[1,1]
local deceased_nockd_`x'_ll = r(table)[5,1]
local deceased_nockd_`x'_ul = r(table)[6,1]

total weight if cardiovascular==1 & ckd_group==0
local cardio_nockd_`x' = r(table)[1,1]
local cardio_nockd_`x'_ll = r(table)[5,1]
local cardio_nockd_`x'_ul = r(table)[6,1]

**CKD stage 3
total weight if ckd_group==2
local baseline_ckd3_`x' = r(table)[1,1]
local baseline_ckd3_`x'_ll = r(table)[5,1]
local baseline_ckd3_`x'_ul = r(table)[6,1]

total weight if ckd_group==2 & ckd_progression==0
local none_ckd3_`x' = r(table)[1,1]
local none_ckd3_`x'_ll = r(table)[5,1]
local none_ckd3_`x'_ul = r(table)[6,1]

total weight if ckd_group==2 & ckd_progression==2
local ckd4_ckd3_`x' = r(table)[1,1]
local ckd4_ckd3_`x'_ll = r(table)[5,1]
local ckd4_ckd3_`x'_ul = r(table)[6,1]

total weight if ckd_group==2 & ckd_progression==3
local dialysis_ckd3_`x' = r(table)[1,1]
local dialysis_ckd3_`x'_ll = r(table)[5,1]
local dialysis_ckd3_`x'_ul = r(table)[6,1]

total weight if ckd_group==2 & ckd_progression==4
local kt_ckd3_`x' = r(table)[1,1]
local kt_ckd3_`x'_ll = r(table)[5,1]
local kt_ckd3_`x'_ul = r(table)[6,1]

total weight if ckd_group==2 & ckd_progression==6
local deceased_ckd3_`x' = r(table)[1,1]
local deceased_ckd3_`x'_ll = r(table)[5,1]
local deceased_ckd3_`x'_ul = r(table)[6,1]

total weight if cardiovascular==1 & ckd_group==2
local cardio_ckd3_`x' = r(table)[1,1]
local cardio_ckd3_`x'_ll = r(table)[5,1]
local cardio_ckd3_`x'_ul = r(table)[6,1]

**CKD stage 4/5
total weight if ckd_group==3
local baseline_ckd4_`x' = r(table)[1,1]
local baseline_ckd4_`x'_ll = r(table)[5,1]
local baseline_ckd4_`x'_ul = r(table)[6,1]

total weight if ckd_group==3 & ckd_progression==0
local none_ckd4_`x' = r(table)[1,1]
local none_ckd4_`x'_ll = r(table)[5,1]
local none_ckd4_`x'_ul = r(table)[6,1]

total weight if ckd_group==3 & ckd_progression==3
local dialysis_ckd4_`x' = r(table)[1,1]
local dialysis_ckd4_`x'_ll = r(table)[5,1]
local dialysis_ckd4_`x'_ul = r(table)[6,1]

total weight if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = r(table)[1,1]
local kt_ckd4_`x'_ll = r(table)[5,1]
local kt_ckd4_`x'_ul = r(table)[6,1]

total weight if ckd_group==3 & ckd_progression==6
local deceased_ckd4_`x' = r(table)[1,1]
local deceased_ckd4_`x'_ll = r(table)[5,1]
local deceased_ckd4_`x'_ul = r(table)[6,1]

total weight if cardiovascular==1 & ckd_group==3
local cardio_ckd4_`x' = r(table)[1,1]
local cardio_ckd4_`x'_ll = r(table)[5,1]
local cardio_ckd4_`x'_ul = r(table)[6,1]

**Dialysis
total weight if ckd_group==4
local baseline_dialysis_`x' = r(table)[1,1]
local baseline_dialysis_`x'_ll = r(table)[5,1]
local baseline_dialysis_`x'_ul = r(table)[6,1]

total weight if ckd_group==4 & ckd_progression==0
local none_dialysis_`x' = r(table)[1,1]
local none_dialysis_`x'_ll = r(table)[5,1]
local none_dialysis_`x'_ul = r(table)[6,1]

total weight if ckd_group==4 & ckd_progression==4
local kt_dialysis_`x' = r(table)[1,1]
local kt_dialysis_`x'_ll = r(table)[5,1]
local kt_dialysis_`x'_ul = r(table)[6,1]

total weight if ckd_group==4 & ckd_progression==6
local deceased_dialysis_`x' = r(table)[1,1]
local deceased_dialysis_`x'_ll = r(table)[5,1]
local deceased_dialysis_`x'_ul = r(table)[6,1]

total weight if cardiovascular==1 & ckd_group==4
local cardio_dialysis_`x' = r(table)[1,1]
local cardio_dialysis_`x'_ll = r(table)[5,1]
local cardio_dialysis_`x'_ul = r(table)[6,1]

**Kidney transplant
total weight if ckd_group==5
local baseline_kt_`x' = r(table)[1,1]
local baseline_kt_`x'_ll = r(table)[5,1]
local baseline_kt_`x'_ul = r(table)[6,1]

total weight if ckd_group==5 & ckd_progression==0
local none_kt_`x' = r(table)[1,1]
local none_kt_`x'_ll = r(table)[5,1]
local none_kt_`x'_ul = r(table)[6,1]

total weight if ckd_group==5 & ckd_progression==3
local dialysis_kt_`x' = r(table)[1,1]
local dialysis_kt_`x'_ll = r(table)[5,1]
local dialysis_kt_`x'_ul = r(table)[6,1]

total weight if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = r(table)[1,1]
local deceased_kt_`x'_ll = r(table)[5,1]
local deceased_kt_`x'_ul = r(table)[6,1]

total weight if cardiovascular==1 & ckd_group==5
local cardio_kt_`x' = r(table)[1,1]
local cardio_kt_`x'_ll = r(table)[5,1]
local cardio_kt_`x'_ul = r(table)[6,1]
}

**Populate table with redacted counts
*Overall
file write tablecontent ("All") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2017_ll') _tab %10.2f (`baseline_ckd_2017_ul') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2018_ll') _tab %10.2f (`baseline_ckd_2018_ul') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2019_ll') _tab %10.2f (`baseline_ckd_2019_ul') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2020_ll') _tab %10.2f (`baseline_ckd_2020_ul') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2021_ll') _tab %10.2f (`baseline_ckd_2021_ul') _tab %10.2f (`baseline_ckd_2022') _tab %10.2f (`baseline_ckd_2022_ll') _tab %10.2f (`baseline_ckd_2022_ul') _n
file write tablecontent ("All") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2017_ll') _tab %10.2f (`none_ckd_2017_ul') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2018_ll') _tab %10.2f (`none_ckd_2018_ul') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2019_ll') _tab %10.2f (`none_ckd_2019_ul') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2020_ll') _tab %10.2f (`none_ckd_2020_ul') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2021_ll') _tab %10.2f (`none_ckd_2021_ul') _tab %10.2f (`none_ckd_2022') _tab %10.2f (`none_ckd_2022_ll') _tab %10.2f (`none_ckd_2022_ul') _n
file write tablecontent ("All") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2017_ll') _tab %10.2f (`ckd3_ckd_2017_ul') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2018_ll') _tab %10.2f (`ckd3_ckd_2018_ul') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2019_ll') _tab %10.2f (`ckd3_ckd_2019_ul') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2020_ll') _tab %10.2f (`ckd3_ckd_2020_ul') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2021_ll') _tab %10.2f (`ckd3_ckd_2021_ul') _tab %10.2f (`ckd3_ckd_2022') _tab %10.2f (`ckd3_ckd_2022_ll') _tab %10.2f (`ckd3_ckd_2022_ul') _n
file write tablecontent ("All") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2017_ll') _tab %10.2f (`ckd4_ckd_2017_ul') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2018_ll') _tab %10.2f (`ckd4_ckd_2018_ul') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2019_ll') _tab %10.2f (`ckd4_ckd_2019_ul') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2020_ll') _tab %10.2f (`ckd4_ckd_2020_ul') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2021_ll') _tab %10.2f (`ckd4_ckd_2021_ul') _tab %10.2f (`ckd4_ckd_2022') _tab %10.2f (`ckd4_ckd_2022_ll') _tab %10.2f (`ckd4_ckd_2022_ul') _n
file write tablecontent ("All") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2017_ll') _tab %10.2f (`dialysis_ckd_2017_ul') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2018_ll') _tab %10.2f (`dialysis_ckd_2018_ul') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2019_ll') _tab %10.2f (`dialysis_ckd_2019_ul') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2020_ll') _tab %10.2f (`dialysis_ckd_2020_ul') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2021_ll') _tab %10.2f (`dialysis_ckd_2021_ul') _tab %10.2f (`dialysis_ckd_2022') _tab %10.2f (`dialysis_ckd_2022_ll') _tab %10.2f (`dialysis_ckd_2022_ul') _n
file write tablecontent ("All") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2017_ll') _tab %10.2f (`kt_ckd_2017_ul') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2018_ll') _tab %10.2f (`kt_ckd_2018_ul') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2019_ll') _tab %10.2f (`kt_ckd_2019_ul') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2020_ll') _tab %10.2f (`kt_ckd_2020_ul') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2021_ll') _tab %10.2f (`kt_ckd_2021_ul') _tab %10.2f (`kt_ckd_2022') _tab %10.2f (`kt_ckd_2022_ll') _tab %10.2f (`kt_ckd_2022_ul') _n
file write tablecontent ("All") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2017_ll') _tab %10.2f (`deceased_ckd_2017_ul') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2018_ll') _tab %10.2f (`deceased_ckd_2018_ul') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2019_ll') _tab %10.2f (`deceased_ckd_2019_ul') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2020_ll') _tab %10.2f (`deceased_ckd_2020_ul') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2021_ll') _tab %10.2f (`deceased_ckd_2021_ul') _tab %10.2f (`deceased_ckd_2022') _tab %10.2f (`deceased_ckd_2022_ll') _tab %10.2f (`deceased_ckd_2022_ul') _n
file write tablecontent ("All") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2017_ll') _tab %10.2f (`cardio_ckd_2017_ul') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2018_ll') _tab %10.2f (`cardio_ckd_2018_ul') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2019_ll') _tab %10.2f (`cardio_ckd_2019_ul') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2020_ll') _tab %10.2f (`cardio_ckd_2020_ul') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2021_ll') _tab %10.2f (`cardio_ckd_2021_ul') _tab %10.2f (`cardio_ckd_2022') _tab %10.2f (`cardio_ckd_2022_ll') _tab %10.2f (`cardio_ckd_2022_ul') _n

*No CKD
file write tablecontent ("All") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2017_ll') _tab %10.2f (`baseline_nockd_2017_ul') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2018_ll') _tab %10.2f (`baseline_nockd_2018_ul') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2019_ll') _tab %10.2f (`baseline_nockd_2019_ul') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2020_ll') _tab %10.2f (`baseline_nockd_2020_ul') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2021_ll') _tab %10.2f (`baseline_nockd_2021_ul') _tab %10.2f (`baseline_nockd_2022') _tab %10.2f (`baseline_nockd_2022_ll') _tab %10.2f (`baseline_nockd_2022_ul') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2017_ll') _tab %10.2f (`none_nockd_2017_ul') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2018_ll') _tab %10.2f (`none_nockd_2018_ul') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2019_ll') _tab %10.2f (`none_nockd_2019_ul') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2020_ll') _tab %10.2f (`none_nockd_2020_ul') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2021_ll') _tab %10.2f (`none_nockd_2021_ul') _tab %10.2f (`none_nockd_2022') _tab %10.2f (`none_nockd_2022_ll') _tab %10.2f (`none_nockd_2022_ul') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2017_ll') _tab %10.2f (`ckd3_nockd_2017_ul') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2018_ll') _tab %10.2f (`ckd3_nockd_2018_ul') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2019_ll') _tab %10.2f (`ckd3_nockd_2019_ul') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2020_ll') _tab %10.2f (`ckd3_nockd_2020_ul') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2021_ll') _tab %10.2f (`ckd3_nockd_2021_ul') _tab %10.2f (`ckd3_nockd_2022') _tab %10.2f (`ckd3_nockd_2022_ll') _tab %10.2f (`ckd3_nockd_2022_ul') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2017_ll') _tab %10.2f (`ckd4_nockd_2017_ul') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2018_ll') _tab %10.2f (`ckd4_nockd_2018_ul') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2019_ll') _tab %10.2f (`ckd4_nockd_2019_ul') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2020_ll') _tab %10.2f (`ckd4_nockd_2020_ul') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2021_ll') _tab %10.2f (`ckd4_nockd_2021_ul') _tab %10.2f (`ckd4_nockd_2022') _tab %10.2f (`ckd4_nockd_2022_ll') _tab %10.2f (`ckd4_nockd_2022_ul') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2017_ll') _tab %10.2f (`dialysis_nockd_2017_ul') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2018_ll') _tab %10.2f (`dialysis_nockd_2018_ul') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2019_ll') _tab %10.2f (`dialysis_nockd_2019_ul') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2020_ll') _tab %10.2f (`dialysis_nockd_2020_ul') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2021_ll') _tab %10.2f (`dialysis_nockd_2021_ul') _tab %10.2f (`dialysis_nockd_2022') _tab %10.2f (`dialysis_nockd_2022_ll') _tab %10.2f (`dialysis_nockd_2022_ul') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("Transplant") _tab %10.2f (`kt_nockd_2017') _tab %10.2f (`kt_nockd_2017_ll') _tab %10.2f (`kt_nockd_2017_ul') _tab %10.2f (`kt_nockd_2018') _tab %10.2f (`kt_nockd_2018_ll') _tab %10.2f (`kt_nockd_2018_ul') _tab %10.2f (`kt_nockd_2019') _tab %10.2f (`kt_nockd_2019_ll') _tab %10.2f (`kt_nockd_2019_ul') _tab %10.2f (`kt_nockd_2020') _tab %10.2f (`kt_nockd_2020_ll') _tab %10.2f (`kt_nockd_2020_ul') _tab %10.2f (`kt_nockd_2021') _tab %10.2f (`kt_nockd_2021_ll') _tab %10.2f (`kt_nockd_2021_ul') _tab %10.2f (`kt_nockd_2022') _tab %10.2f (`kt_nockd_2022_ll') _tab %10.2f (`kt_nockd_2022_ul') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("Transplant") _tab %10.2f (`kt_ckd3_2017') _tab %10.2f (`kt_ckd3_2017_ll') _tab %10.2f (`kt_ckd3_2017_ul') _tab %10.2f (`kt_ckd3_2018') _tab %10.2f (`kt_ckd3_2018_ll') _tab %10.2f (`kt_ckd3_2018_ul') _tab %10.2f (`kt_ckd3_2019') _tab %10.2f (`kt_ckd3_2019_ll') _tab %10.2f (`kt_ckd3_2019_ul') _tab %10.2f (`kt_ckd3_2020') _tab %10.2f (`kt_ckd3_2020_ll') _tab %10.2f (`kt_ckd3_2020_ul') _tab %10.2f (`kt_ckd3_2021') _tab %10.2f (`kt_ckd3_2021_ll') _tab %10.2f (`kt_ckd3_2021_ul') _tab %10.2f (`kt_ckd3_2022') _tab %10.2f (`kt_ckd3_2022_ll') _tab %10.2f (`kt_ckd3_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2017_ll') _tab %10.2f (`deceased_ckd3_2017_ul') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2018_ll') _tab %10.2f (`deceased_ckd3_2018_ul') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2019_ll') _tab %10.2f (`deceased_ckd3_2019_ul') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2020_ll') _tab %10.2f (`deceased_ckd3_2020_ul') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2021_ll') _tab %10.2f (`deceased_ckd3_2021_ul') _tab %10.2f (`deceased_ckd3_2022') _tab %10.2f (`deceased_ckd3_2022_ll') _tab %10.2f (`deceased_ckd3_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2017_ll') _tab %10.2f (`cardio_ckd3_2017_ul') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2018_ll') _tab %10.2f (`cardio_ckd3_2018_ul') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2019_ll') _tab %10.2f (`cardio_ckd3_2019_ul') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2020_ll') _tab %10.2f (`cardio_ckd3_2020_ul') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2021_ll') _tab %10.2f (`cardio_ckd3_2021_ul') _tab %10.2f (`cardio_ckd3_2022') _tab %10.2f (`cardio_ckd3_2022_ll') _tab %10.2f (`cardio_ckd3_2022_ul') _n

*CKD stage 4/5 without RRT
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2017_ll') _tab %10.2f (`baseline_ckd4_2017_ul') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2018_ll') _tab %10.2f (`baseline_ckd4_2018_ul') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2019_ll') _tab %10.2f (`baseline_ckd4_2019_ul') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2020_ll') _tab %10.2f (`baseline_ckd4_2020_ul') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2021_ll') _tab %10.2f (`baseline_ckd4_2021_ul') _tab %10.2f (`baseline_ckd4_2022') _tab %10.2f (`baseline_ckd4_2022_ll') _tab %10.2f (`baseline_ckd4_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2017_ll') _tab %10.2f (`none_ckd4_2017_ul') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2018_ll') _tab %10.2f (`none_ckd4_2018_ul') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2019_ll') _tab %10.2f (`none_ckd4_2019_ul') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2020_ll') _tab %10.2f (`none_ckd4_2020_ul') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2021_ll') _tab %10.2f (`none_ckd4_2021_ul') _tab %10.2f (`none_ckd4_2022') _tab %10.2f (`none_ckd4_2022_ll') _tab %10.2f (`none_ckd4_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2017_ll') _tab %10.2f (`dialysis_ckd4_2017_ul') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2018_ll') _tab %10.2f (`dialysis_ckd4_2018_ul') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2019_ll') _tab %10.2f (`dialysis_ckd4_2019_ul') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2020_ll') _tab %10.2f (`dialysis_ckd4_2020_ul') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2021_ll') _tab %10.2f (`dialysis_ckd4_2021_ul') _tab %10.2f (`dialysis_ckd4_2022') _tab %10.2f (`dialysis_ckd4_2022_ll') _tab %10.2f (`dialysis_ckd4_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2017_ll') _tab %10.2f (`kt_ckd4_2017_ul') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2018_ll') _tab %10.2f (`kt_ckd4_2018_ul') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2019_ll') _tab %10.2f (`kt_ckd4_2019_ul') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2020_ll') _tab %10.2f (`kt_ckd4_2020_ul') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2021_ll') _tab %10.2f (`kt_ckd4_2021_ul') _tab %10.2f (`kt_ckd4_2022') _tab %10.2f (`kt_ckd4_2022_ll') _tab %10.2f (`kt_ckd4_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2017_ll') _tab %10.2f (`deceased_ckd4_2017_ul') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2018_ll') _tab %10.2f (`deceased_ckd4_2018_ul') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2019_ll') _tab %10.2f (`deceased_ckd4_2019_ul') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2020_ll') _tab %10.2f (`deceased_ckd4_2020_ul') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2021_ll') _tab %10.2f (`deceased_ckd4_2021_ul') _tab %10.2f (`deceased_ckd4_2022') _tab %10.2f (`deceased_ckd4_2022_ll') _tab %10.2f (`deceased_ckd4_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2017_ll') _tab %10.2f (`cardio_ckd4_2017_ul') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2018_ll') _tab %10.2f (`cardio_ckd4_2018_ul') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2019_ll') _tab %10.2f (`cardio_ckd4_2019_ul') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2020_ll') _tab %10.2f (`cardio_ckd4_2020_ul') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2021_ll') _tab %10.2f (`cardio_ckd4_2021_ul') _tab %10.2f (`cardio_ckd4_2022') _tab %10.2f (`cardio_ckd4_2022_ll') _tab %10.2f (`cardio_ckd4_2022_ul') _n

*Dialysis
file write tablecontent ("All") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2017_ll') _tab %10.2f (`baseline_dialysis_2017_ul') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2018_ll') _tab %10.2f (`baseline_dialysis_2018_ul') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2019_ll') _tab %10.2f (`baseline_dialysis_2019_ul') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2020_ll') _tab %10.2f (`baseline_dialysis_2020_ul') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2021_ll') _tab %10.2f (`baseline_dialysis_2021_ul') _tab %10.2f (`baseline_dialysis_2022') _tab %10.2f (`baseline_dialysis_2022_ll') _tab %10.2f (`baseline_dialysis_2022_ul') _n
file write tablecontent ("All") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2017_ll') _tab %10.2f (`none_dialysis_2017_ul') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2018_ll') _tab %10.2f (`none_dialysis_2018_ul') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2019_ll') _tab %10.2f (`none_dialysis_2019_ul') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2020_ll') _tab %10.2f (`none_dialysis_2020_ul') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2021_ll') _tab %10.2f (`none_dialysis_2021_ul') _tab %10.2f (`none_dialysis_2022') _tab %10.2f (`none_dialysis_2022_ll') _tab %10.2f (`none_dialysis_2022_ul') _n
file write tablecontent ("All") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2017_ll') _tab %10.2f (`kt_dialysis_2017_ul') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2018_ll') _tab %10.2f (`kt_dialysis_2018_ul') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2019_ll') _tab %10.2f (`kt_dialysis_2019_ul') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2020_ll') _tab %10.2f (`kt_dialysis_2020_ul') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2021_ll') _tab %10.2f (`kt_dialysis_2021_ul') _tab %10.2f (`kt_dialysis_2022') _tab %10.2f (`kt_dialysis_2022_ll') _tab %10.2f (`kt_dialysis_2022_ul') _n
file write tablecontent ("All") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2017_ll') _tab %10.2f (`deceased_dialysis_2017_ul') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2018_ll') _tab %10.2f (`deceased_dialysis_2018_ul') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2019_ll') _tab %10.2f (`deceased_dialysis_2019_ul') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2020_ll') _tab %10.2f (`deceased_dialysis_2020_ul') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2021_ll') _tab %10.2f (`deceased_dialysis_2021_ul') _tab %10.2f (`deceased_dialysis_2022') _tab %10.2f (`deceased_dialysis_2022_ll') _tab %10.2f (`deceased_dialysis_2022_ul') _n
file write tablecontent ("All") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2017_ll') _tab %10.2f (`cardio_dialysis_2017_ul') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2018_ll') _tab %10.2f (`cardio_dialysis_2018_ul') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2019_ll') _tab %10.2f (`cardio_dialysis_2019_ul') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2020_ll') _tab %10.2f (`cardio_dialysis_2020_ul') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2021_ll') _tab %10.2f (`cardio_dialysis_2021_ul') _tab %10.2f (`cardio_dialysis_2022') _tab %10.2f (`cardio_dialysis_2022_ll') _tab %10.2f (`cardio_dialysis_2022_ul') _n

*Kidney transplant
file write tablecontent ("All") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2017_ll') _tab %10.2f (`baseline_kt_2017_ul') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2018_ll') _tab %10.2f (`baseline_kt_2018_ul') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2019_ll') _tab %10.2f (`baseline_kt_2019_ul') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2020_ll') _tab %10.2f (`baseline_kt_2020_ul') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2021_ll') _tab %10.2f (`baseline_kt_2021_ul') _tab %10.2f (`baseline_kt_2022') _tab %10.2f (`baseline_kt_2022_ll') _tab %10.2f (`baseline_kt_2022_ul') _n
file write tablecontent ("All") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2017_ll') _tab %10.2f (`none_kt_2017_ul') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2018_ll') _tab %10.2f (`none_kt_2018_ul') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2019_ll') _tab %10.2f (`none_kt_2019_ul') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2020_ll') _tab %10.2f (`none_kt_2020_ul') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2021_ll') _tab %10.2f (`none_kt_2021_ul') _tab %10.2f (`none_kt_2022') _tab %10.2f (`none_kt_2022_ll') _tab %10.2f (`none_kt_2022_ul') _n
file write tablecontent ("All") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2017_ll') _tab %10.2f (`dialysis_kt_2017_ul') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2018_ll') _tab %10.2f (`dialysis_kt_2018_ul') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2019_ll') _tab %10.2f (`dialysis_kt_2019_ul') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2020_ll') _tab %10.2f (`dialysis_kt_2020_ul') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2021_ll') _tab %10.2f (`dialysis_kt_2021_ul') _tab %10.2f (`dialysis_kt_2022') _tab %10.2f (`dialysis_kt_2022_ll') _tab %10.2f (`dialysis_kt_2022_ul') _n
file write tablecontent ("All") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2017_ll') _tab %10.2f (`deceased_kt_2017_ul') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2018_ll') _tab %10.2f (`deceased_kt_2018_ul') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2019_ll') _tab %10.2f (`deceased_kt_2019_ul') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2020_ll') _tab %10.2f (`deceased_kt_2020_ul') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2021_ll') _tab %10.2f (`deceased_kt_2021_ul') _tab %10.2f (`deceased_kt_2022') _tab %10.2f (`deceased_kt_2022_ll') _tab %10.2f (`deceased_kt_2022_ul') _n
file write tablecontent ("All") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2017_ll') _tab %10.2f (`cardio_kt_2017_ul') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2018_ll') _tab %10.2f (`cardio_kt_2018_ul') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2019_ll') _tab %10.2f (`cardio_kt_2019_ul') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2020_ll') _tab %10.2f (`cardio_kt_2020_ul') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2021_ll') _tab %10.2f (`cardio_kt_2021_ul') _tab %10.2f (`cardio_kt_2022') _tab %10.2f (`cardio_kt_2022_ll') _tab %10.2f (`cardio_kt_2022_ul') _n

file close tablecontent