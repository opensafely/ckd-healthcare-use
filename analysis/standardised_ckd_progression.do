sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/standardised_ckd_progression.log, replace t

cap file close tablecontent
file open tablecontent using ./output/standardised_ckd_progression.csv, write text replace

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

forvalues i=1/2 {
local label`i': label ethnicity `i'
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if ethnicity!=`i'

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

*Overall
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2017_ll') _tab %10.2f (`baseline_ckd_2017_ul') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2018_ll') _tab %10.2f (`baseline_ckd_2018_ul') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2019_ll') _tab %10.2f (`baseline_ckd_2019_ul') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2020_ll') _tab %10.2f (`baseline_ckd_2020_ul') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2021_ll') _tab %10.2f (`baseline_ckd_2021_ul') _tab %10.2f (`baseline_ckd_2022') _tab %10.2f (`baseline_ckd_2022_ll') _tab %10.2f (`baseline_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2017_ll') _tab %10.2f (`none_ckd_2017_ul') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2018_ll') _tab %10.2f (`none_ckd_2018_ul') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2019_ll') _tab %10.2f (`none_ckd_2019_ul') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2020_ll') _tab %10.2f (`none_ckd_2020_ul') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2021_ll') _tab %10.2f (`none_ckd_2021_ul') _tab %10.2f (`none_ckd_2022') _tab %10.2f (`none_ckd_2022_ll') _tab %10.2f (`none_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2017_ll') _tab %10.2f (`ckd3_ckd_2017_ul') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2018_ll') _tab %10.2f (`ckd3_ckd_2018_ul') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2019_ll') _tab %10.2f (`ckd3_ckd_2019_ul') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2020_ll') _tab %10.2f (`ckd3_ckd_2020_ul') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2021_ll') _tab %10.2f (`ckd3_ckd_2021_ul') _tab %10.2f (`ckd3_ckd_2022') _tab %10.2f (`ckd3_ckd_2022_ll') _tab %10.2f (`ckd3_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2017_ll') _tab %10.2f (`ckd4_ckd_2017_ul') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2018_ll') _tab %10.2f (`ckd4_ckd_2018_ul') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2019_ll') _tab %10.2f (`ckd4_ckd_2019_ul') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2020_ll') _tab %10.2f (`ckd4_ckd_2020_ul') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2021_ll') _tab %10.2f (`ckd4_ckd_2021_ul') _tab %10.2f (`ckd4_ckd_2022') _tab %10.2f (`ckd4_ckd_2022_ll') _tab %10.2f (`ckd4_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2017_ll') _tab %10.2f (`dialysis_ckd_2017_ul') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2018_ll') _tab %10.2f (`dialysis_ckd_2018_ul') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2019_ll') _tab %10.2f (`dialysis_ckd_2019_ul') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2020_ll') _tab %10.2f (`dialysis_ckd_2020_ul') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2021_ll') _tab %10.2f (`dialysis_ckd_2021_ul') _tab %10.2f (`dialysis_ckd_2022') _tab %10.2f (`dialysis_ckd_2022_ll') _tab %10.2f (`dialysis_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2017_ll') _tab %10.2f (`kt_ckd_2017_ul') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2018_ll') _tab %10.2f (`kt_ckd_2018_ul') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2019_ll') _tab %10.2f (`kt_ckd_2019_ul') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2020_ll') _tab %10.2f (`kt_ckd_2020_ul') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2021_ll') _tab %10.2f (`kt_ckd_2021_ul') _tab %10.2f (`kt_ckd_2022') _tab %10.2f (`kt_ckd_2022_ll') _tab %10.2f (`kt_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2017_ll') _tab %10.2f (`deceased_ckd_2017_ul') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2018_ll') _tab %10.2f (`deceased_ckd_2018_ul') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2019_ll') _tab %10.2f (`deceased_ckd_2019_ul') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2020_ll') _tab %10.2f (`deceased_ckd_2020_ul') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2021_ll') _tab %10.2f (`deceased_ckd_2021_ul') _tab %10.2f (`deceased_ckd_2022') _tab %10.2f (`deceased_ckd_2022_ll') _tab %10.2f (`deceased_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2017_ll') _tab %10.2f (`cardio_ckd_2017_ul') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2018_ll') _tab %10.2f (`cardio_ckd_2018_ul') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2019_ll') _tab %10.2f (`cardio_ckd_2019_ul') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2020_ll') _tab %10.2f (`cardio_ckd_2020_ul') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2021_ll') _tab %10.2f (`cardio_ckd_2021_ul') _tab %10.2f (`cardio_ckd_2022') _tab %10.2f (`cardio_ckd_2022_ll') _tab %10.2f (`cardio_ckd_2022_ul') _n

*No CKD
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2017_ll') _tab %10.2f (`baseline_nockd_2017_ul') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2018_ll') _tab %10.2f (`baseline_nockd_2018_ul') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2019_ll') _tab %10.2f (`baseline_nockd_2019_ul') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2020_ll') _tab %10.2f (`baseline_nockd_2020_ul') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2021_ll') _tab %10.2f (`baseline_nockd_2021_ul') _tab %10.2f (`baseline_nockd_2022') _tab %10.2f (`baseline_nockd_2022_ll') _tab %10.2f (`baseline_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2017_ll') _tab %10.2f (`none_nockd_2017_ul') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2018_ll') _tab %10.2f (`none_nockd_2018_ul') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2019_ll') _tab %10.2f (`none_nockd_2019_ul') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2020_ll') _tab %10.2f (`none_nockd_2020_ul') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2021_ll') _tab %10.2f (`none_nockd_2021_ul') _tab %10.2f (`none_nockd_2022') _tab %10.2f (`none_nockd_2022_ll') _tab %10.2f (`none_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2017_ll') _tab %10.2f (`ckd3_nockd_2017_ul') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2018_ll') _tab %10.2f (`ckd3_nockd_2018_ul') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2019_ll') _tab %10.2f (`ckd3_nockd_2019_ul') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2020_ll') _tab %10.2f (`ckd3_nockd_2020_ul') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2021_ll') _tab %10.2f (`ckd3_nockd_2021_ul') _tab %10.2f (`ckd3_nockd_2022') _tab %10.2f (`ckd3_nockd_2022_ll') _tab %10.2f (`ckd3_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2017_ll') _tab %10.2f (`ckd4_nockd_2017_ul') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2018_ll') _tab %10.2f (`ckd4_nockd_2018_ul') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2019_ll') _tab %10.2f (`ckd4_nockd_2019_ul') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2020_ll') _tab %10.2f (`ckd4_nockd_2020_ul') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2021_ll') _tab %10.2f (`ckd4_nockd_2021_ul') _tab %10.2f (`ckd4_nockd_2022') _tab %10.2f (`ckd4_nockd_2022_ll') _tab %10.2f (`ckd4_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2017_ll') _tab %10.2f (`dialysis_nockd_2017_ul') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2018_ll') _tab %10.2f (`dialysis_nockd_2018_ul') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2019_ll') _tab %10.2f (`dialysis_nockd_2019_ul') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2020_ll') _tab %10.2f (`dialysis_nockd_2020_ul') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2021_ll') _tab %10.2f (`dialysis_nockd_2021_ul') _tab %10.2f (`dialysis_nockd_2022') _tab %10.2f (`dialysis_nockd_2022_ll') _tab %10.2f (`dialysis_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2017_ll') _tab %10.2f (`deceased_ckd3_2017_ul') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2018_ll') _tab %10.2f (`deceased_ckd3_2018_ul') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2019_ll') _tab %10.2f (`deceased_ckd3_2019_ul') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2020_ll') _tab %10.2f (`deceased_ckd3_2020_ul') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2021_ll') _tab %10.2f (`deceased_ckd3_2021_ul') _tab %10.2f (`deceased_ckd3_2022') _tab %10.2f (`deceased_ckd3_2022_ll') _tab %10.2f (`deceased_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2017_ll') _tab %10.2f (`cardio_ckd3_2017_ul') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2018_ll') _tab %10.2f (`cardio_ckd3_2018_ul') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2019_ll') _tab %10.2f (`cardio_ckd3_2019_ul') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2020_ll') _tab %10.2f (`cardio_ckd3_2020_ul') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2021_ll') _tab %10.2f (`cardio_ckd3_2021_ul') _tab %10.2f (`cardio_ckd3_2022') _tab %10.2f (`cardio_ckd3_2022_ll') _tab %10.2f (`cardio_ckd3_2022_ul') _n

*CKD stage 4/5 without RRT
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2017_ll') _tab %10.2f (`baseline_ckd4_2017_ul') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2018_ll') _tab %10.2f (`baseline_ckd4_2018_ul') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2019_ll') _tab %10.2f (`baseline_ckd4_2019_ul') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2020_ll') _tab %10.2f (`baseline_ckd4_2020_ul') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2021_ll') _tab %10.2f (`baseline_ckd4_2021_ul') _tab %10.2f (`baseline_ckd4_2022') _tab %10.2f (`baseline_ckd4_2022_ll') _tab %10.2f (`baseline_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2017_ll') _tab %10.2f (`none_ckd4_2017_ul') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2018_ll') _tab %10.2f (`none_ckd4_2018_ul') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2019_ll') _tab %10.2f (`none_ckd4_2019_ul') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2020_ll') _tab %10.2f (`none_ckd4_2020_ul') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2021_ll') _tab %10.2f (`none_ckd4_2021_ul') _tab %10.2f (`none_ckd4_2022') _tab %10.2f (`none_ckd4_2022_ll') _tab %10.2f (`none_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2017_ll') _tab %10.2f (`dialysis_ckd4_2017_ul') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2018_ll') _tab %10.2f (`dialysis_ckd4_2018_ul') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2019_ll') _tab %10.2f (`dialysis_ckd4_2019_ul') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2020_ll') _tab %10.2f (`dialysis_ckd4_2020_ul') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2021_ll') _tab %10.2f (`dialysis_ckd4_2021_ul') _tab %10.2f (`dialysis_ckd4_2022') _tab %10.2f (`dialysis_ckd4_2022_ll') _tab %10.2f (`dialysis_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2017_ll') _tab %10.2f (`kt_ckd4_2017_ul') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2018_ll') _tab %10.2f (`kt_ckd4_2018_ul') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2019_ll') _tab %10.2f (`kt_ckd4_2019_ul') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2020_ll') _tab %10.2f (`kt_ckd4_2020_ul') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2021_ll') _tab %10.2f (`kt_ckd4_2021_ul') _tab %10.2f (`kt_ckd4_2022') _tab %10.2f (`kt_ckd4_2022_ll') _tab %10.2f (`kt_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2017_ll') _tab %10.2f (`deceased_ckd4_2017_ul') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2018_ll') _tab %10.2f (`deceased_ckd4_2018_ul') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2019_ll') _tab %10.2f (`deceased_ckd4_2019_ul') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2020_ll') _tab %10.2f (`deceased_ckd4_2020_ul') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2021_ll') _tab %10.2f (`deceased_ckd4_2021_ul') _tab %10.2f (`deceased_ckd4_2022') _tab %10.2f (`deceased_ckd4_2022_ll') _tab %10.2f (`deceased_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2017_ll') _tab %10.2f (`cardio_ckd4_2017_ul') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2018_ll') _tab %10.2f (`cardio_ckd4_2018_ul') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2019_ll') _tab %10.2f (`cardio_ckd4_2019_ul') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2020_ll') _tab %10.2f (`cardio_ckd4_2020_ul') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2021_ll') _tab %10.2f (`cardio_ckd4_2021_ul') _tab %10.2f (`cardio_ckd4_2022') _tab %10.2f (`cardio_ckd4_2022_ll') _tab %10.2f (`cardio_ckd4_2022_ul') _n

*Dialysis
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2017_ll') _tab %10.2f (`baseline_dialysis_2017_ul') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2018_ll') _tab %10.2f (`baseline_dialysis_2018_ul') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2019_ll') _tab %10.2f (`baseline_dialysis_2019_ul') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2020_ll') _tab %10.2f (`baseline_dialysis_2020_ul') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2021_ll') _tab %10.2f (`baseline_dialysis_2021_ul') _tab %10.2f (`baseline_dialysis_2022') _tab %10.2f (`baseline_dialysis_2022_ll') _tab %10.2f (`baseline_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2017_ll') _tab %10.2f (`none_dialysis_2017_ul') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2018_ll') _tab %10.2f (`none_dialysis_2018_ul') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2019_ll') _tab %10.2f (`none_dialysis_2019_ul') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2020_ll') _tab %10.2f (`none_dialysis_2020_ul') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2021_ll') _tab %10.2f (`none_dialysis_2021_ul') _tab %10.2f (`none_dialysis_2022') _tab %10.2f (`none_dialysis_2022_ll') _tab %10.2f (`none_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2017_ll') _tab %10.2f (`kt_dialysis_2017_ul') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2018_ll') _tab %10.2f (`kt_dialysis_2018_ul') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2019_ll') _tab %10.2f (`kt_dialysis_2019_ul') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2020_ll') _tab %10.2f (`kt_dialysis_2020_ul') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2021_ll') _tab %10.2f (`kt_dialysis_2021_ul') _tab %10.2f (`kt_dialysis_2022') _tab %10.2f (`kt_dialysis_2022_ll') _tab %10.2f (`kt_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2017_ll') _tab %10.2f (`deceased_dialysis_2017_ul') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2018_ll') _tab %10.2f (`deceased_dialysis_2018_ul') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2019_ll') _tab %10.2f (`deceased_dialysis_2019_ul') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2020_ll') _tab %10.2f (`deceased_dialysis_2020_ul') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2021_ll') _tab %10.2f (`deceased_dialysis_2021_ul') _tab %10.2f (`deceased_dialysis_2022') _tab %10.2f (`deceased_dialysis_2022_ll') _tab %10.2f (`deceased_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2017_ll') _tab %10.2f (`cardio_dialysis_2017_ul') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2018_ll') _tab %10.2f (`cardio_dialysis_2018_ul') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2019_ll') _tab %10.2f (`cardio_dialysis_2019_ul') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2020_ll') _tab %10.2f (`cardio_dialysis_2020_ul') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2021_ll') _tab %10.2f (`cardio_dialysis_2021_ul') _tab %10.2f (`cardio_dialysis_2022') _tab %10.2f (`cardio_dialysis_2022_ll') _tab %10.2f (`cardio_dialysis_2022_ul') _n

*Kidney transplant
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2017_ll') _tab %10.2f (`baseline_kt_2017_ul') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2018_ll') _tab %10.2f (`baseline_kt_2018_ul') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2019_ll') _tab %10.2f (`baseline_kt_2019_ul') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2020_ll') _tab %10.2f (`baseline_kt_2020_ul') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2021_ll') _tab %10.2f (`baseline_kt_2021_ul') _tab %10.2f (`baseline_kt_2022') _tab %10.2f (`baseline_kt_2022_ll') _tab %10.2f (`baseline_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2017_ll') _tab %10.2f (`none_kt_2017_ul') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2018_ll') _tab %10.2f (`none_kt_2018_ul') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2019_ll') _tab %10.2f (`none_kt_2019_ul') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2020_ll') _tab %10.2f (`none_kt_2020_ul') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2021_ll') _tab %10.2f (`none_kt_2021_ul') _tab %10.2f (`none_kt_2022') _tab %10.2f (`none_kt_2022_ll') _tab %10.2f (`none_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2017_ll') _tab %10.2f (`dialysis_kt_2017_ul') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2018_ll') _tab %10.2f (`dialysis_kt_2018_ul') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2019_ll') _tab %10.2f (`dialysis_kt_2019_ul') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2020_ll') _tab %10.2f (`dialysis_kt_2020_ul') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2021_ll') _tab %10.2f (`dialysis_kt_2021_ul') _tab %10.2f (`dialysis_kt_2022') _tab %10.2f (`dialysis_kt_2022_ll') _tab %10.2f (`dialysis_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2017_ll') _tab %10.2f (`deceased_kt_2017_ul') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2018_ll') _tab %10.2f (`deceased_kt_2018_ul') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2019_ll') _tab %10.2f (`deceased_kt_2019_ul') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2020_ll') _tab %10.2f (`deceased_kt_2020_ul') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2021_ll') _tab %10.2f (`deceased_kt_2021_ul') _tab %10.2f (`deceased_kt_2022') _tab %10.2f (`deceased_kt_2022_ll') _tab %10.2f (`deceased_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2017_ll') _tab %10.2f (`cardio_kt_2017_ul') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2018_ll') _tab %10.2f (`cardio_kt_2018_ul') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2019_ll') _tab %10.2f (`cardio_kt_2019_ul') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2020_ll') _tab %10.2f (`cardio_kt_2020_ul') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2021_ll') _tab %10.2f (`cardio_kt_2021_ul') _tab %10.2f (`cardio_kt_2022') _tab %10.2f (`cardio_kt_2022_ll') _tab %10.2f (`cardio_kt_2022_ul') _n
}


*Black ethnicity
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if ethnicity!=3

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

total weight if cardiovascular==1 & ckd_group==5
local cardio_kt_`x' = r(table)[1,1]
local cardio_kt_`x'_ll = r(table)[5,1]
local cardio_kt_`x'_ul = r(table)[6,1]
}

local year "2018 2020 2021 2022"

foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if ethnicity!=3

total weight if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = r(table)[1,1]
local deceased_kt_`x'_ll = r(table)[5,1]
local deceased_kt_`x'_ul = r(table)[6,1]
}


*Overall
file write tablecontent ("Black") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2017_ll') _tab %10.2f (`baseline_ckd_2017_ul') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2018_ll') _tab %10.2f (`baseline_ckd_2018_ul') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2019_ll') _tab %10.2f (`baseline_ckd_2019_ul') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2020_ll') _tab %10.2f (`baseline_ckd_2020_ul') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2021_ll') _tab %10.2f (`baseline_ckd_2021_ul') _tab %10.2f (`baseline_ckd_2022') _tab %10.2f (`baseline_ckd_2022_ll') _tab %10.2f (`baseline_ckd_2022_ul') _n
file write tablecontent ("Black") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2017_ll') _tab %10.2f (`none_ckd_2017_ul') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2018_ll') _tab %10.2f (`none_ckd_2018_ul') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2019_ll') _tab %10.2f (`none_ckd_2019_ul') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2020_ll') _tab %10.2f (`none_ckd_2020_ul') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2021_ll') _tab %10.2f (`none_ckd_2021_ul') _tab %10.2f (`none_ckd_2022') _tab %10.2f (`none_ckd_2022_ll') _tab %10.2f (`none_ckd_2022_ul') _n
file write tablecontent ("Black") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2017_ll') _tab %10.2f (`ckd3_ckd_2017_ul') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2018_ll') _tab %10.2f (`ckd3_ckd_2018_ul') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2019_ll') _tab %10.2f (`ckd3_ckd_2019_ul') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2020_ll') _tab %10.2f (`ckd3_ckd_2020_ul') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2021_ll') _tab %10.2f (`ckd3_ckd_2021_ul') _tab %10.2f (`ckd3_ckd_2022') _tab %10.2f (`ckd3_ckd_2022_ll') _tab %10.2f (`ckd3_ckd_2022_ul') _n
file write tablecontent ("Black") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2017_ll') _tab %10.2f (`ckd4_ckd_2017_ul') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2018_ll') _tab %10.2f (`ckd4_ckd_2018_ul') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2019_ll') _tab %10.2f (`ckd4_ckd_2019_ul') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2020_ll') _tab %10.2f (`ckd4_ckd_2020_ul') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2021_ll') _tab %10.2f (`ckd4_ckd_2021_ul') _tab %10.2f (`ckd4_ckd_2022') _tab %10.2f (`ckd4_ckd_2022_ll') _tab %10.2f (`ckd4_ckd_2022_ul') _n
file write tablecontent ("Black") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2017_ll') _tab %10.2f (`dialysis_ckd_2017_ul') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2018_ll') _tab %10.2f (`dialysis_ckd_2018_ul') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2019_ll') _tab %10.2f (`dialysis_ckd_2019_ul') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2020_ll') _tab %10.2f (`dialysis_ckd_2020_ul') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2021_ll') _tab %10.2f (`dialysis_ckd_2021_ul') _tab %10.2f (`dialysis_ckd_2022') _tab %10.2f (`dialysis_ckd_2022_ll') _tab %10.2f (`dialysis_ckd_2022_ul') _n
file write tablecontent ("Black") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2017_ll') _tab %10.2f (`kt_ckd_2017_ul') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2018_ll') _tab %10.2f (`kt_ckd_2018_ul') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2019_ll') _tab %10.2f (`kt_ckd_2019_ul') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2020_ll') _tab %10.2f (`kt_ckd_2020_ul') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2021_ll') _tab %10.2f (`kt_ckd_2021_ul') _tab %10.2f (`kt_ckd_2022') _tab %10.2f (`kt_ckd_2022_ll') _tab %10.2f (`kt_ckd_2022_ul') _n
file write tablecontent ("Black") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2017_ll') _tab %10.2f (`deceased_ckd_2017_ul') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2018_ll') _tab %10.2f (`deceased_ckd_2018_ul') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2019_ll') _tab %10.2f (`deceased_ckd_2019_ul') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2020_ll') _tab %10.2f (`deceased_ckd_2020_ul') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2021_ll') _tab %10.2f (`deceased_ckd_2021_ul') _tab %10.2f (`deceased_ckd_2022') _tab %10.2f (`deceased_ckd_2022_ll') _tab %10.2f (`deceased_ckd_2022_ul') _n
file write tablecontent ("Black") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2017_ll') _tab %10.2f (`cardio_ckd_2017_ul') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2018_ll') _tab %10.2f (`cardio_ckd_2018_ul') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2019_ll') _tab %10.2f (`cardio_ckd_2019_ul') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2020_ll') _tab %10.2f (`cardio_ckd_2020_ul') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2021_ll') _tab %10.2f (`cardio_ckd_2021_ul') _tab %10.2f (`cardio_ckd_2022') _tab %10.2f (`cardio_ckd_2022_ll') _tab %10.2f (`cardio_ckd_2022_ul') _n

*No CKD
file write tablecontent ("Black") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2017_ll') _tab %10.2f (`baseline_nockd_2017_ul') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2018_ll') _tab %10.2f (`baseline_nockd_2018_ul') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2019_ll') _tab %10.2f (`baseline_nockd_2019_ul') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2020_ll') _tab %10.2f (`baseline_nockd_2020_ul') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2021_ll') _tab %10.2f (`baseline_nockd_2021_ul') _tab %10.2f (`baseline_nockd_2022') _tab %10.2f (`baseline_nockd_2022_ll') _tab %10.2f (`baseline_nockd_2022_ul') _n
file write tablecontent ("Black") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2017_ll') _tab %10.2f (`none_nockd_2017_ul') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2018_ll') _tab %10.2f (`none_nockd_2018_ul') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2019_ll') _tab %10.2f (`none_nockd_2019_ul') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2020_ll') _tab %10.2f (`none_nockd_2020_ul') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2021_ll') _tab %10.2f (`none_nockd_2021_ul') _tab %10.2f (`none_nockd_2022') _tab %10.2f (`none_nockd_2022_ll') _tab %10.2f (`none_nockd_2022_ul') _n
file write tablecontent ("Black") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2017_ll') _tab %10.2f (`ckd3_nockd_2017_ul') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2018_ll') _tab %10.2f (`ckd3_nockd_2018_ul') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2019_ll') _tab %10.2f (`ckd3_nockd_2019_ul') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2020_ll') _tab %10.2f (`ckd3_nockd_2020_ul') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2021_ll') _tab %10.2f (`ckd3_nockd_2021_ul') _tab %10.2f (`ckd3_nockd_2022') _tab %10.2f (`ckd3_nockd_2022_ll') _tab %10.2f (`ckd3_nockd_2022_ul') _n
file write tablecontent ("Black") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2017_ll') _tab %10.2f (`ckd4_nockd_2017_ul') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2018_ll') _tab %10.2f (`ckd4_nockd_2018_ul') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2019_ll') _tab %10.2f (`ckd4_nockd_2019_ul') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2020_ll') _tab %10.2f (`ckd4_nockd_2020_ul') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2021_ll') _tab %10.2f (`ckd4_nockd_2021_ul') _tab %10.2f (`ckd4_nockd_2022') _tab %10.2f (`ckd4_nockd_2022_ll') _tab %10.2f (`ckd4_nockd_2022_ul') _n
file write tablecontent ("Black") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2017_ll') _tab %10.2f (`dialysis_nockd_2017_ul') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2018_ll') _tab %10.2f (`dialysis_nockd_2018_ul') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2019_ll') _tab %10.2f (`dialysis_nockd_2019_ul') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2020_ll') _tab %10.2f (`dialysis_nockd_2020_ul') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2021_ll') _tab %10.2f (`dialysis_nockd_2021_ul') _tab %10.2f (`dialysis_nockd_2022') _tab %10.2f (`dialysis_nockd_2022_ll') _tab %10.2f (`dialysis_nockd_2022_ul') _n
file write tablecontent ("Black") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("Black") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("Black") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2017_ll') _tab %10.2f (`deceased_ckd3_2017_ul') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2018_ll') _tab %10.2f (`deceased_ckd3_2018_ul') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2019_ll') _tab %10.2f (`deceased_ckd3_2019_ul') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2020_ll') _tab %10.2f (`deceased_ckd3_2020_ul') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2021_ll') _tab %10.2f (`deceased_ckd3_2021_ul') _tab %10.2f (`deceased_ckd3_2022') _tab %10.2f (`deceased_ckd3_2022_ll') _tab %10.2f (`deceased_ckd3_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2017_ll') _tab %10.2f (`cardio_ckd3_2017_ul') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2018_ll') _tab %10.2f (`cardio_ckd3_2018_ul') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2019_ll') _tab %10.2f (`cardio_ckd3_2019_ul') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2020_ll') _tab %10.2f (`cardio_ckd3_2020_ul') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2021_ll') _tab %10.2f (`cardio_ckd3_2021_ul') _tab %10.2f (`cardio_ckd3_2022') _tab %10.2f (`cardio_ckd3_2022_ll') _tab %10.2f (`cardio_ckd3_2022_ul') _n

*CKD stage 4/5 without RRT
file write tablecontent ("Black") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2017_ll') _tab %10.2f (`baseline_ckd4_2017_ul') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2018_ll') _tab %10.2f (`baseline_ckd4_2018_ul') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2019_ll') _tab %10.2f (`baseline_ckd4_2019_ul') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2020_ll') _tab %10.2f (`baseline_ckd4_2020_ul') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2021_ll') _tab %10.2f (`baseline_ckd4_2021_ul') _tab %10.2f (`baseline_ckd4_2022') _tab %10.2f (`baseline_ckd4_2022_ll') _tab %10.2f (`baseline_ckd4_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2017_ll') _tab %10.2f (`none_ckd4_2017_ul') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2018_ll') _tab %10.2f (`none_ckd4_2018_ul') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2019_ll') _tab %10.2f (`none_ckd4_2019_ul') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2020_ll') _tab %10.2f (`none_ckd4_2020_ul') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2021_ll') _tab %10.2f (`none_ckd4_2021_ul') _tab %10.2f (`none_ckd4_2022') _tab %10.2f (`none_ckd4_2022_ll') _tab %10.2f (`none_ckd4_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2017_ll') _tab %10.2f (`dialysis_ckd4_2017_ul') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2018_ll') _tab %10.2f (`dialysis_ckd4_2018_ul') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2019_ll') _tab %10.2f (`dialysis_ckd4_2019_ul') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2020_ll') _tab %10.2f (`dialysis_ckd4_2020_ul') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2021_ll') _tab %10.2f (`dialysis_ckd4_2021_ul') _tab %10.2f (`dialysis_ckd4_2022') _tab %10.2f (`dialysis_ckd4_2022_ll') _tab %10.2f (`dialysis_ckd4_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2017_ll') _tab %10.2f (`kt_ckd4_2017_ul') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2018_ll') _tab %10.2f (`kt_ckd4_2018_ul') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2019_ll') _tab %10.2f (`kt_ckd4_2019_ul') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2020_ll') _tab %10.2f (`kt_ckd4_2020_ul') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2021_ll') _tab %10.2f (`kt_ckd4_2021_ul') _tab %10.2f (`kt_ckd4_2022') _tab %10.2f (`kt_ckd4_2022_ll') _tab %10.2f (`kt_ckd4_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2017_ll') _tab %10.2f (`deceased_ckd4_2017_ul') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2018_ll') _tab %10.2f (`deceased_ckd4_2018_ul') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2019_ll') _tab %10.2f (`deceased_ckd4_2019_ul') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2020_ll') _tab %10.2f (`deceased_ckd4_2020_ul') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2021_ll') _tab %10.2f (`deceased_ckd4_2021_ul') _tab %10.2f (`deceased_ckd4_2022') _tab %10.2f (`deceased_ckd4_2022_ll') _tab %10.2f (`deceased_ckd4_2022_ul') _n
file write tablecontent ("Black") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2017_ll') _tab %10.2f (`cardio_ckd4_2017_ul') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2018_ll') _tab %10.2f (`cardio_ckd4_2018_ul') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2019_ll') _tab %10.2f (`cardio_ckd4_2019_ul') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2020_ll') _tab %10.2f (`cardio_ckd4_2020_ul') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2021_ll') _tab %10.2f (`cardio_ckd4_2021_ul') _tab %10.2f (`cardio_ckd4_2022') _tab %10.2f (`cardio_ckd4_2022_ll') _tab %10.2f (`cardio_ckd4_2022_ul') _n

*Dialysis
file write tablecontent ("Black") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2017_ll') _tab %10.2f (`baseline_dialysis_2017_ul') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2018_ll') _tab %10.2f (`baseline_dialysis_2018_ul') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2019_ll') _tab %10.2f (`baseline_dialysis_2019_ul') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2020_ll') _tab %10.2f (`baseline_dialysis_2020_ul') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2021_ll') _tab %10.2f (`baseline_dialysis_2021_ul') _tab %10.2f (`baseline_dialysis_2022') _tab %10.2f (`baseline_dialysis_2022_ll') _tab %10.2f (`baseline_dialysis_2022_ul') _n
file write tablecontent ("Black") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2017_ll') _tab %10.2f (`none_dialysis_2017_ul') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2018_ll') _tab %10.2f (`none_dialysis_2018_ul') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2019_ll') _tab %10.2f (`none_dialysis_2019_ul') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2020_ll') _tab %10.2f (`none_dialysis_2020_ul') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2021_ll') _tab %10.2f (`none_dialysis_2021_ul') _tab %10.2f (`none_dialysis_2022') _tab %10.2f (`none_dialysis_2022_ll') _tab %10.2f (`none_dialysis_2022_ul') _n
file write tablecontent ("Black") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2017_ll') _tab %10.2f (`kt_dialysis_2017_ul') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2018_ll') _tab %10.2f (`kt_dialysis_2018_ul') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2019_ll') _tab %10.2f (`kt_dialysis_2019_ul') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2020_ll') _tab %10.2f (`kt_dialysis_2020_ul') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2021_ll') _tab %10.2f (`kt_dialysis_2021_ul') _tab %10.2f (`kt_dialysis_2022') _tab %10.2f (`kt_dialysis_2022_ll') _tab %10.2f (`kt_dialysis_2022_ul') _n
file write tablecontent ("Black") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2017_ll') _tab %10.2f (`deceased_dialysis_2017_ul') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2018_ll') _tab %10.2f (`deceased_dialysis_2018_ul') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2019_ll') _tab %10.2f (`deceased_dialysis_2019_ul') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2020_ll') _tab %10.2f (`deceased_dialysis_2020_ul') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2021_ll') _tab %10.2f (`deceased_dialysis_2021_ul') _tab %10.2f (`deceased_dialysis_2022') _tab %10.2f (`deceased_dialysis_2022_ll') _tab %10.2f (`deceased_dialysis_2022_ul') _n
file write tablecontent ("Black") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2017_ll') _tab %10.2f (`cardio_dialysis_2017_ul') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2018_ll') _tab %10.2f (`cardio_dialysis_2018_ul') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2019_ll') _tab %10.2f (`cardio_dialysis_2019_ul') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2020_ll') _tab %10.2f (`cardio_dialysis_2020_ul') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2021_ll') _tab %10.2f (`cardio_dialysis_2021_ul') _tab %10.2f (`cardio_dialysis_2022') _tab %10.2f (`cardio_dialysis_2022_ll') _tab %10.2f (`cardio_dialysis_2022_ul') _n

*Kidney transplant
file write tablecontent ("Black") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2017_ll') _tab %10.2f (`baseline_kt_2017_ul') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2018_ll') _tab %10.2f (`baseline_kt_2018_ul') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2019_ll') _tab %10.2f (`baseline_kt_2019_ul') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2020_ll') _tab %10.2f (`baseline_kt_2020_ul') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2021_ll') _tab %10.2f (`baseline_kt_2021_ul') _tab %10.2f (`baseline_kt_2022') _tab %10.2f (`baseline_kt_2022_ll') _tab %10.2f (`baseline_kt_2022_ul') _n
file write tablecontent ("Black") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2017_ll') _tab %10.2f (`none_kt_2017_ul') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2018_ll') _tab %10.2f (`none_kt_2018_ul') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2019_ll') _tab %10.2f (`none_kt_2019_ul') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2020_ll') _tab %10.2f (`none_kt_2020_ul') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2021_ll') _tab %10.2f (`none_kt_2021_ul') _tab %10.2f (`none_kt_2022') _tab %10.2f (`none_kt_2022_ll') _tab %10.2f (`none_kt_2022_ul') _n
file write tablecontent ("Black") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2017_ll') _tab %10.2f (`dialysis_kt_2017_ul') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2018_ll') _tab %10.2f (`dialysis_kt_2018_ul') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2019_ll') _tab %10.2f (`dialysis_kt_2019_ul') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2020_ll') _tab %10.2f (`dialysis_kt_2020_ul') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2021_ll') _tab %10.2f (`dialysis_kt_2021_ul') _tab %10.2f (`dialysis_kt_2022') _tab %10.2f (`dialysis_kt_2022_ll') _tab %10.2f (`dialysis_kt_2022_ul') _n
file write tablecontent ("Black") _tab ("Transplant") _tab ("Deceased") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2018_ll') _tab %10.2f (`deceased_kt_2018_ul') _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2020_ll') _tab %10.2f (`deceased_kt_2020_ul') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2021_ll') _tab %10.2f (`deceased_kt_2021_ul') _tab %10.2f (`deceased_kt_2022') _tab %10.2f (`deceased_kt_2022_ll') _tab %10.2f (`deceased_kt_2022_ul') _n
file write tablecontent ("Black") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2017_ll') _tab %10.2f (`cardio_kt_2017_ul') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2018_ll') _tab %10.2f (`cardio_kt_2018_ul') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2019_ll') _tab %10.2f (`cardio_kt_2019_ul') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2020_ll') _tab %10.2f (`cardio_kt_2020_ul') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2021_ll') _tab %10.2f (`cardio_kt_2021_ul') _tab %10.2f (`cardio_kt_2022') _tab %10.2f (`cardio_kt_2022_ll') _tab %10.2f (`cardio_kt_2022_ul') _n


local year "2017 2018 2019 2020 2021 2022"
forvalues i=1/5 {
local label`i': label imd `i'
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if imd!=`i'
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

*Overall
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2017_ll') _tab %10.2f (`baseline_ckd_2017_ul') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2018_ll') _tab %10.2f (`baseline_ckd_2018_ul') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2019_ll') _tab %10.2f (`baseline_ckd_2019_ul') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2020_ll') _tab %10.2f (`baseline_ckd_2020_ul') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2021_ll') _tab %10.2f (`baseline_ckd_2021_ul') _tab %10.2f (`baseline_ckd_2022') _tab %10.2f (`baseline_ckd_2022_ll') _tab %10.2f (`baseline_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2017_ll') _tab %10.2f (`none_ckd_2017_ul') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2018_ll') _tab %10.2f (`none_ckd_2018_ul') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2019_ll') _tab %10.2f (`none_ckd_2019_ul') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2020_ll') _tab %10.2f (`none_ckd_2020_ul') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2021_ll') _tab %10.2f (`none_ckd_2021_ul') _tab %10.2f (`none_ckd_2022') _tab %10.2f (`none_ckd_2022_ll') _tab %10.2f (`none_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2017_ll') _tab %10.2f (`ckd3_ckd_2017_ul') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2018_ll') _tab %10.2f (`ckd3_ckd_2018_ul') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2019_ll') _tab %10.2f (`ckd3_ckd_2019_ul') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2020_ll') _tab %10.2f (`ckd3_ckd_2020_ul') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2021_ll') _tab %10.2f (`ckd3_ckd_2021_ul') _tab %10.2f (`ckd3_ckd_2022') _tab %10.2f (`ckd3_ckd_2022_ll') _tab %10.2f (`ckd3_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2017_ll') _tab %10.2f (`ckd4_ckd_2017_ul') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2018_ll') _tab %10.2f (`ckd4_ckd_2018_ul') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2019_ll') _tab %10.2f (`ckd4_ckd_2019_ul') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2020_ll') _tab %10.2f (`ckd4_ckd_2020_ul') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2021_ll') _tab %10.2f (`ckd4_ckd_2021_ul') _tab %10.2f (`ckd4_ckd_2022') _tab %10.2f (`ckd4_ckd_2022_ll') _tab %10.2f (`ckd4_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2017_ll') _tab %10.2f (`dialysis_ckd_2017_ul') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2018_ll') _tab %10.2f (`dialysis_ckd_2018_ul') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2019_ll') _tab %10.2f (`dialysis_ckd_2019_ul') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2020_ll') _tab %10.2f (`dialysis_ckd_2020_ul') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2021_ll') _tab %10.2f (`dialysis_ckd_2021_ul') _tab %10.2f (`dialysis_ckd_2022') _tab %10.2f (`dialysis_ckd_2022_ll') _tab %10.2f (`dialysis_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2017_ll') _tab %10.2f (`kt_ckd_2017_ul') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2018_ll') _tab %10.2f (`kt_ckd_2018_ul') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2019_ll') _tab %10.2f (`kt_ckd_2019_ul') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2020_ll') _tab %10.2f (`kt_ckd_2020_ul') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2021_ll') _tab %10.2f (`kt_ckd_2021_ul') _tab %10.2f (`kt_ckd_2022') _tab %10.2f (`kt_ckd_2022_ll') _tab %10.2f (`kt_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2017_ll') _tab %10.2f (`deceased_ckd_2017_ul') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2018_ll') _tab %10.2f (`deceased_ckd_2018_ul') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2019_ll') _tab %10.2f (`deceased_ckd_2019_ul') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2020_ll') _tab %10.2f (`deceased_ckd_2020_ul') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2021_ll') _tab %10.2f (`deceased_ckd_2021_ul') _tab %10.2f (`deceased_ckd_2022') _tab %10.2f (`deceased_ckd_2022_ll') _tab %10.2f (`deceased_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2017_ll') _tab %10.2f (`cardio_ckd_2017_ul') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2018_ll') _tab %10.2f (`cardio_ckd_2018_ul') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2019_ll') _tab %10.2f (`cardio_ckd_2019_ul') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2020_ll') _tab %10.2f (`cardio_ckd_2020_ul') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2021_ll') _tab %10.2f (`cardio_ckd_2021_ul') _tab %10.2f (`cardio_ckd_2022') _tab %10.2f (`cardio_ckd_2022_ll') _tab %10.2f (`cardio_ckd_2022_ul') _n

*No CKD
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2017_ll') _tab %10.2f (`baseline_nockd_2017_ul') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2018_ll') _tab %10.2f (`baseline_nockd_2018_ul') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2019_ll') _tab %10.2f (`baseline_nockd_2019_ul') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2020_ll') _tab %10.2f (`baseline_nockd_2020_ul') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2021_ll') _tab %10.2f (`baseline_nockd_2021_ul') _tab %10.2f (`baseline_nockd_2022') _tab %10.2f (`baseline_nockd_2022_ll') _tab %10.2f (`baseline_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2017_ll') _tab %10.2f (`none_nockd_2017_ul') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2018_ll') _tab %10.2f (`none_nockd_2018_ul') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2019_ll') _tab %10.2f (`none_nockd_2019_ul') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2020_ll') _tab %10.2f (`none_nockd_2020_ul') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2021_ll') _tab %10.2f (`none_nockd_2021_ul') _tab %10.2f (`none_nockd_2022') _tab %10.2f (`none_nockd_2022_ll') _tab %10.2f (`none_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2017_ll') _tab %10.2f (`ckd3_nockd_2017_ul') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2018_ll') _tab %10.2f (`ckd3_nockd_2018_ul') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2019_ll') _tab %10.2f (`ckd3_nockd_2019_ul') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2020_ll') _tab %10.2f (`ckd3_nockd_2020_ul') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2021_ll') _tab %10.2f (`ckd3_nockd_2021_ul') _tab %10.2f (`ckd3_nockd_2022') _tab %10.2f (`ckd3_nockd_2022_ll') _tab %10.2f (`ckd3_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2017_ll') _tab %10.2f (`ckd4_nockd_2017_ul') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2018_ll') _tab %10.2f (`ckd4_nockd_2018_ul') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2019_ll') _tab %10.2f (`ckd4_nockd_2019_ul') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2020_ll') _tab %10.2f (`ckd4_nockd_2020_ul') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2021_ll') _tab %10.2f (`ckd4_nockd_2021_ul') _tab %10.2f (`ckd4_nockd_2022') _tab %10.2f (`ckd4_nockd_2022_ll') _tab %10.2f (`ckd4_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2017_ll') _tab %10.2f (`dialysis_nockd_2017_ul') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2018_ll') _tab %10.2f (`dialysis_nockd_2018_ul') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2019_ll') _tab %10.2f (`dialysis_nockd_2019_ul') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2020_ll') _tab %10.2f (`dialysis_nockd_2020_ul') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2021_ll') _tab %10.2f (`dialysis_nockd_2021_ul') _tab %10.2f (`dialysis_nockd_2022') _tab %10.2f (`dialysis_nockd_2022_ll') _tab %10.2f (`dialysis_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2017_ll') _tab %10.2f (`deceased_ckd3_2017_ul') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2018_ll') _tab %10.2f (`deceased_ckd3_2018_ul') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2019_ll') _tab %10.2f (`deceased_ckd3_2019_ul') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2020_ll') _tab %10.2f (`deceased_ckd3_2020_ul') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2021_ll') _tab %10.2f (`deceased_ckd3_2021_ul') _tab %10.2f (`deceased_ckd3_2022') _tab %10.2f (`deceased_ckd3_2022_ll') _tab %10.2f (`deceased_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2017_ll') _tab %10.2f (`cardio_ckd3_2017_ul') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2018_ll') _tab %10.2f (`cardio_ckd3_2018_ul') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2019_ll') _tab %10.2f (`cardio_ckd3_2019_ul') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2020_ll') _tab %10.2f (`cardio_ckd3_2020_ul') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2021_ll') _tab %10.2f (`cardio_ckd3_2021_ul') _tab %10.2f (`cardio_ckd3_2022') _tab %10.2f (`cardio_ckd3_2022_ll') _tab %10.2f (`cardio_ckd3_2022_ul') _n

*CKD stage 4/5 without RRT
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2017_ll') _tab %10.2f (`baseline_ckd4_2017_ul') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2018_ll') _tab %10.2f (`baseline_ckd4_2018_ul') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2019_ll') _tab %10.2f (`baseline_ckd4_2019_ul') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2020_ll') _tab %10.2f (`baseline_ckd4_2020_ul') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2021_ll') _tab %10.2f (`baseline_ckd4_2021_ul') _tab %10.2f (`baseline_ckd4_2022') _tab %10.2f (`baseline_ckd4_2022_ll') _tab %10.2f (`baseline_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2017_ll') _tab %10.2f (`none_ckd4_2017_ul') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2018_ll') _tab %10.2f (`none_ckd4_2018_ul') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2019_ll') _tab %10.2f (`none_ckd4_2019_ul') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2020_ll') _tab %10.2f (`none_ckd4_2020_ul') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2021_ll') _tab %10.2f (`none_ckd4_2021_ul') _tab %10.2f (`none_ckd4_2022') _tab %10.2f (`none_ckd4_2022_ll') _tab %10.2f (`none_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2017_ll') _tab %10.2f (`dialysis_ckd4_2017_ul') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2018_ll') _tab %10.2f (`dialysis_ckd4_2018_ul') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2019_ll') _tab %10.2f (`dialysis_ckd4_2019_ul') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2020_ll') _tab %10.2f (`dialysis_ckd4_2020_ul') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2021_ll') _tab %10.2f (`dialysis_ckd4_2021_ul') _tab %10.2f (`dialysis_ckd4_2022') _tab %10.2f (`dialysis_ckd4_2022_ll') _tab %10.2f (`dialysis_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2017_ll') _tab %10.2f (`kt_ckd4_2017_ul') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2018_ll') _tab %10.2f (`kt_ckd4_2018_ul') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2019_ll') _tab %10.2f (`kt_ckd4_2019_ul') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2020_ll') _tab %10.2f (`kt_ckd4_2020_ul') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2021_ll') _tab %10.2f (`kt_ckd4_2021_ul') _tab %10.2f (`kt_ckd4_2022') _tab %10.2f (`kt_ckd4_2022_ll') _tab %10.2f (`kt_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2017_ll') _tab %10.2f (`deceased_ckd4_2017_ul') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2018_ll') _tab %10.2f (`deceased_ckd4_2018_ul') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2019_ll') _tab %10.2f (`deceased_ckd4_2019_ul') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2020_ll') _tab %10.2f (`deceased_ckd4_2020_ul') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2021_ll') _tab %10.2f (`deceased_ckd4_2021_ul') _tab %10.2f (`deceased_ckd4_2022') _tab %10.2f (`deceased_ckd4_2022_ll') _tab %10.2f (`deceased_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2017_ll') _tab %10.2f (`cardio_ckd4_2017_ul') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2018_ll') _tab %10.2f (`cardio_ckd4_2018_ul') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2019_ll') _tab %10.2f (`cardio_ckd4_2019_ul') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2020_ll') _tab %10.2f (`cardio_ckd4_2020_ul') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2021_ll') _tab %10.2f (`cardio_ckd4_2021_ul') _tab %10.2f (`cardio_ckd4_2022') _tab %10.2f (`cardio_ckd4_2022_ll') _tab %10.2f (`cardio_ckd4_2022_ul') _n

*Dialysis
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2017_ll') _tab %10.2f (`baseline_dialysis_2017_ul') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2018_ll') _tab %10.2f (`baseline_dialysis_2018_ul') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2019_ll') _tab %10.2f (`baseline_dialysis_2019_ul') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2020_ll') _tab %10.2f (`baseline_dialysis_2020_ul') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2021_ll') _tab %10.2f (`baseline_dialysis_2021_ul') _tab %10.2f (`baseline_dialysis_2022') _tab %10.2f (`baseline_dialysis_2022_ll') _tab %10.2f (`baseline_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2017_ll') _tab %10.2f (`none_dialysis_2017_ul') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2018_ll') _tab %10.2f (`none_dialysis_2018_ul') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2019_ll') _tab %10.2f (`none_dialysis_2019_ul') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2020_ll') _tab %10.2f (`none_dialysis_2020_ul') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2021_ll') _tab %10.2f (`none_dialysis_2021_ul') _tab %10.2f (`none_dialysis_2022') _tab %10.2f (`none_dialysis_2022_ll') _tab %10.2f (`none_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2017_ll') _tab %10.2f (`kt_dialysis_2017_ul') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2018_ll') _tab %10.2f (`kt_dialysis_2018_ul') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2019_ll') _tab %10.2f (`kt_dialysis_2019_ul') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2020_ll') _tab %10.2f (`kt_dialysis_2020_ul') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2021_ll') _tab %10.2f (`kt_dialysis_2021_ul') _tab %10.2f (`kt_dialysis_2022') _tab %10.2f (`kt_dialysis_2022_ll') _tab %10.2f (`kt_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2017_ll') _tab %10.2f (`deceased_dialysis_2017_ul') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2018_ll') _tab %10.2f (`deceased_dialysis_2018_ul') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2019_ll') _tab %10.2f (`deceased_dialysis_2019_ul') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2020_ll') _tab %10.2f (`deceased_dialysis_2020_ul') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2021_ll') _tab %10.2f (`deceased_dialysis_2021_ul') _tab %10.2f (`deceased_dialysis_2022') _tab %10.2f (`deceased_dialysis_2022_ll') _tab %10.2f (`deceased_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2017_ll') _tab %10.2f (`cardio_dialysis_2017_ul') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2018_ll') _tab %10.2f (`cardio_dialysis_2018_ul') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2019_ll') _tab %10.2f (`cardio_dialysis_2019_ul') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2020_ll') _tab %10.2f (`cardio_dialysis_2020_ul') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2021_ll') _tab %10.2f (`cardio_dialysis_2021_ul') _tab %10.2f (`cardio_dialysis_2022') _tab %10.2f (`cardio_dialysis_2022_ll') _tab %10.2f (`cardio_dialysis_2022_ul') _n

*Kidney transplant
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2017_ll') _tab %10.2f (`baseline_kt_2017_ul') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2018_ll') _tab %10.2f (`baseline_kt_2018_ul') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2019_ll') _tab %10.2f (`baseline_kt_2019_ul') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2020_ll') _tab %10.2f (`baseline_kt_2020_ul') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2021_ll') _tab %10.2f (`baseline_kt_2021_ul') _tab %10.2f (`baseline_kt_2022') _tab %10.2f (`baseline_kt_2022_ll') _tab %10.2f (`baseline_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2017_ll') _tab %10.2f (`none_kt_2017_ul') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2018_ll') _tab %10.2f (`none_kt_2018_ul') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2019_ll') _tab %10.2f (`none_kt_2019_ul') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2020_ll') _tab %10.2f (`none_kt_2020_ul') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2021_ll') _tab %10.2f (`none_kt_2021_ul') _tab %10.2f (`none_kt_2022') _tab %10.2f (`none_kt_2022_ll') _tab %10.2f (`none_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2017_ll') _tab %10.2f (`dialysis_kt_2017_ul') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2018_ll') _tab %10.2f (`dialysis_kt_2018_ul') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2019_ll') _tab %10.2f (`dialysis_kt_2019_ul') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2020_ll') _tab %10.2f (`dialysis_kt_2020_ul') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2021_ll') _tab %10.2f (`dialysis_kt_2021_ul') _tab %10.2f (`dialysis_kt_2022') _tab %10.2f (`dialysis_kt_2022_ll') _tab %10.2f (`dialysis_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2017_ll') _tab %10.2f (`deceased_kt_2017_ul') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2018_ll') _tab %10.2f (`deceased_kt_2018_ul') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2019_ll') _tab %10.2f (`deceased_kt_2019_ul') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2020_ll') _tab %10.2f (`deceased_kt_2020_ul') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2021_ll') _tab %10.2f (`deceased_kt_2021_ul') _tab %10.2f (`deceased_kt_2022') _tab %10.2f (`deceased_kt_2022_ll') _tab %10.2f (`deceased_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2017_ll') _tab %10.2f (`cardio_kt_2017_ul') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2018_ll') _tab %10.2f (`cardio_kt_2018_ul') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2019_ll') _tab %10.2f (`cardio_kt_2019_ul') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2020_ll') _tab %10.2f (`cardio_kt_2020_ul') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2021_ll') _tab %10.2f (`cardio_kt_2021_ul') _tab %10.2f (`cardio_kt_2022') _tab %10.2f (`cardio_kt_2022_ll') _tab %10.2f (`cardio_kt_2022_ul') _n
}

**Region
forvalues i=1/5 {
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
**Regions with sufficient counts = East Midlands, East, North West, South West, Yorkshire & Humber - so create a new category for those
gen region2=region
drop if region==3|region==4|region==6|region==8
replace region2 = 3 if region==5
replace region2 = 4 if region==7
replace region2 = 5 if region==9
label define region2 	1 "East Midlands" 					///
						2 "East"   							///
						3 "North West" 						///
						4 "South West"						///
						5 "Yorkshire and The Humber"		
label values region2 region2

local label`i': label region2 `i'
drop if region2!=`i'
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
*Overall
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2017_ll') _tab %10.2f (`baseline_ckd_2017_ul') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2018_ll') _tab %10.2f (`baseline_ckd_2018_ul') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2019_ll') _tab %10.2f (`baseline_ckd_2019_ul') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2020_ll') _tab %10.2f (`baseline_ckd_2020_ul') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2021_ll') _tab %10.2f (`baseline_ckd_2021_ul') _tab %10.2f (`baseline_ckd_2022') _tab %10.2f (`baseline_ckd_2022_ll') _tab %10.2f (`baseline_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2017_ll') _tab %10.2f (`none_ckd_2017_ul') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2018_ll') _tab %10.2f (`none_ckd_2018_ul') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2019_ll') _tab %10.2f (`none_ckd_2019_ul') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2020_ll') _tab %10.2f (`none_ckd_2020_ul') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2021_ll') _tab %10.2f (`none_ckd_2021_ul') _tab %10.2f (`none_ckd_2022') _tab %10.2f (`none_ckd_2022_ll') _tab %10.2f (`none_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2017_ll') _tab %10.2f (`ckd3_ckd_2017_ul') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2018_ll') _tab %10.2f (`ckd3_ckd_2018_ul') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2019_ll') _tab %10.2f (`ckd3_ckd_2019_ul') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2020_ll') _tab %10.2f (`ckd3_ckd_2020_ul') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2021_ll') _tab %10.2f (`ckd3_ckd_2021_ul') _tab %10.2f (`ckd3_ckd_2022') _tab %10.2f (`ckd3_ckd_2022_ll') _tab %10.2f (`ckd3_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2017_ll') _tab %10.2f (`ckd4_ckd_2017_ul') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2018_ll') _tab %10.2f (`ckd4_ckd_2018_ul') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2019_ll') _tab %10.2f (`ckd4_ckd_2019_ul') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2020_ll') _tab %10.2f (`ckd4_ckd_2020_ul') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2021_ll') _tab %10.2f (`ckd4_ckd_2021_ul') _tab %10.2f (`ckd4_ckd_2022') _tab %10.2f (`ckd4_ckd_2022_ll') _tab %10.2f (`ckd4_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2017_ll') _tab %10.2f (`dialysis_ckd_2017_ul') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2018_ll') _tab %10.2f (`dialysis_ckd_2018_ul') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2019_ll') _tab %10.2f (`dialysis_ckd_2019_ul') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2020_ll') _tab %10.2f (`dialysis_ckd_2020_ul') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2021_ll') _tab %10.2f (`dialysis_ckd_2021_ul') _tab %10.2f (`dialysis_ckd_2022') _tab %10.2f (`dialysis_ckd_2022_ll') _tab %10.2f (`dialysis_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2017_ll') _tab %10.2f (`kt_ckd_2017_ul') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2018_ll') _tab %10.2f (`kt_ckd_2018_ul') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2019_ll') _tab %10.2f (`kt_ckd_2019_ul') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2020_ll') _tab %10.2f (`kt_ckd_2020_ul') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2021_ll') _tab %10.2f (`kt_ckd_2021_ul') _tab %10.2f (`kt_ckd_2022') _tab %10.2f (`kt_ckd_2022_ll') _tab %10.2f (`kt_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2017_ll') _tab %10.2f (`deceased_ckd_2017_ul') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2018_ll') _tab %10.2f (`deceased_ckd_2018_ul') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2019_ll') _tab %10.2f (`deceased_ckd_2019_ul') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2020_ll') _tab %10.2f (`deceased_ckd_2020_ul') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2021_ll') _tab %10.2f (`deceased_ckd_2021_ul') _tab %10.2f (`deceased_ckd_2022') _tab %10.2f (`deceased_ckd_2022_ll') _tab %10.2f (`deceased_ckd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2017_ll') _tab %10.2f (`cardio_ckd_2017_ul') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2018_ll') _tab %10.2f (`cardio_ckd_2018_ul') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2019_ll') _tab %10.2f (`cardio_ckd_2019_ul') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2020_ll') _tab %10.2f (`cardio_ckd_2020_ul') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2021_ll') _tab %10.2f (`cardio_ckd_2021_ul') _tab %10.2f (`cardio_ckd_2022') _tab %10.2f (`cardio_ckd_2022_ll') _tab %10.2f (`cardio_ckd_2022_ul') _n

*No CKD
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2017_ll') _tab %10.2f (`baseline_nockd_2017_ul') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2018_ll') _tab %10.2f (`baseline_nockd_2018_ul') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2019_ll') _tab %10.2f (`baseline_nockd_2019_ul') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2020_ll') _tab %10.2f (`baseline_nockd_2020_ul') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2021_ll') _tab %10.2f (`baseline_nockd_2021_ul') _tab %10.2f (`baseline_nockd_2022') _tab %10.2f (`baseline_nockd_2022_ll') _tab %10.2f (`baseline_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2017_ll') _tab %10.2f (`none_nockd_2017_ul') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2018_ll') _tab %10.2f (`none_nockd_2018_ul') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2019_ll') _tab %10.2f (`none_nockd_2019_ul') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2020_ll') _tab %10.2f (`none_nockd_2020_ul') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2021_ll') _tab %10.2f (`none_nockd_2021_ul') _tab %10.2f (`none_nockd_2022') _tab %10.2f (`none_nockd_2022_ll') _tab %10.2f (`none_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2017_ll') _tab %10.2f (`ckd3_nockd_2017_ul') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2018_ll') _tab %10.2f (`ckd3_nockd_2018_ul') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2019_ll') _tab %10.2f (`ckd3_nockd_2019_ul') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2020_ll') _tab %10.2f (`ckd3_nockd_2020_ul') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2021_ll') _tab %10.2f (`ckd3_nockd_2021_ul') _tab %10.2f (`ckd3_nockd_2022') _tab %10.2f (`ckd3_nockd_2022_ll') _tab %10.2f (`ckd3_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2017_ll') _tab %10.2f (`ckd4_nockd_2017_ul') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2018_ll') _tab %10.2f (`ckd4_nockd_2018_ul') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2019_ll') _tab %10.2f (`ckd4_nockd_2019_ul') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2020_ll') _tab %10.2f (`ckd4_nockd_2020_ul') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2021_ll') _tab %10.2f (`ckd4_nockd_2021_ul') _tab %10.2f (`ckd4_nockd_2022') _tab %10.2f (`ckd4_nockd_2022_ll') _tab %10.2f (`ckd4_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2017_ll') _tab %10.2f (`dialysis_nockd_2017_ul') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2018_ll') _tab %10.2f (`dialysis_nockd_2018_ul') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2019_ll') _tab %10.2f (`dialysis_nockd_2019_ul') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2020_ll') _tab %10.2f (`dialysis_nockd_2020_ul') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2021_ll') _tab %10.2f (`dialysis_nockd_2021_ul') _tab %10.2f (`dialysis_nockd_2022') _tab %10.2f (`dialysis_nockd_2022_ll') _tab %10.2f (`dialysis_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2017_ll') _tab %10.2f (`deceased_ckd3_2017_ul') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2018_ll') _tab %10.2f (`deceased_ckd3_2018_ul') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2019_ll') _tab %10.2f (`deceased_ckd3_2019_ul') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2020_ll') _tab %10.2f (`deceased_ckd3_2020_ul') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2021_ll') _tab %10.2f (`deceased_ckd3_2021_ul') _tab %10.2f (`deceased_ckd3_2022') _tab %10.2f (`deceased_ckd3_2022_ll') _tab %10.2f (`deceased_ckd3_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2017_ll') _tab %10.2f (`cardio_ckd3_2017_ul') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2018_ll') _tab %10.2f (`cardio_ckd3_2018_ul') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2019_ll') _tab %10.2f (`cardio_ckd3_2019_ul') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2020_ll') _tab %10.2f (`cardio_ckd3_2020_ul') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2021_ll') _tab %10.2f (`cardio_ckd3_2021_ul') _tab %10.2f (`cardio_ckd3_2022') _tab %10.2f (`cardio_ckd3_2022_ll') _tab %10.2f (`cardio_ckd3_2022_ul') _n

*CKD stage 4/5 without RRT
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2017_ll') _tab %10.2f (`baseline_ckd4_2017_ul') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2018_ll') _tab %10.2f (`baseline_ckd4_2018_ul') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2019_ll') _tab %10.2f (`baseline_ckd4_2019_ul') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2020_ll') _tab %10.2f (`baseline_ckd4_2020_ul') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2021_ll') _tab %10.2f (`baseline_ckd4_2021_ul') _tab %10.2f (`baseline_ckd4_2022') _tab %10.2f (`baseline_ckd4_2022_ll') _tab %10.2f (`baseline_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2017_ll') _tab %10.2f (`none_ckd4_2017_ul') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2018_ll') _tab %10.2f (`none_ckd4_2018_ul') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2019_ll') _tab %10.2f (`none_ckd4_2019_ul') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2020_ll') _tab %10.2f (`none_ckd4_2020_ul') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2021_ll') _tab %10.2f (`none_ckd4_2021_ul') _tab %10.2f (`none_ckd4_2022') _tab %10.2f (`none_ckd4_2022_ll') _tab %10.2f (`none_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2017_ll') _tab %10.2f (`dialysis_ckd4_2017_ul') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2018_ll') _tab %10.2f (`dialysis_ckd4_2018_ul') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2019_ll') _tab %10.2f (`dialysis_ckd4_2019_ul') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2020_ll') _tab %10.2f (`dialysis_ckd4_2020_ul') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2021_ll') _tab %10.2f (`dialysis_ckd4_2021_ul') _tab %10.2f (`dialysis_ckd4_2022') _tab %10.2f (`dialysis_ckd4_2022_ll') _tab %10.2f (`dialysis_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2017_ll') _tab %10.2f (`kt_ckd4_2017_ul') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2018_ll') _tab %10.2f (`kt_ckd4_2018_ul') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2019_ll') _tab %10.2f (`kt_ckd4_2019_ul') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2020_ll') _tab %10.2f (`kt_ckd4_2020_ul') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2021_ll') _tab %10.2f (`kt_ckd4_2021_ul') _tab %10.2f (`kt_ckd4_2022') _tab %10.2f (`kt_ckd4_2022_ll') _tab %10.2f (`kt_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2017_ll') _tab %10.2f (`deceased_ckd4_2017_ul') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2018_ll') _tab %10.2f (`deceased_ckd4_2018_ul') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2019_ll') _tab %10.2f (`deceased_ckd4_2019_ul') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2020_ll') _tab %10.2f (`deceased_ckd4_2020_ul') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2021_ll') _tab %10.2f (`deceased_ckd4_2021_ul') _tab %10.2f (`deceased_ckd4_2022') _tab %10.2f (`deceased_ckd4_2022_ll') _tab %10.2f (`deceased_ckd4_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2017_ll') _tab %10.2f (`cardio_ckd4_2017_ul') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2018_ll') _tab %10.2f (`cardio_ckd4_2018_ul') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2019_ll') _tab %10.2f (`cardio_ckd4_2019_ul') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2020_ll') _tab %10.2f (`cardio_ckd4_2020_ul') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2021_ll') _tab %10.2f (`cardio_ckd4_2021_ul') _tab %10.2f (`cardio_ckd4_2022') _tab %10.2f (`cardio_ckd4_2022_ll') _tab %10.2f (`cardio_ckd4_2022_ul') _n

*Dialysis
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2017_ll') _tab %10.2f (`baseline_dialysis_2017_ul') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2018_ll') _tab %10.2f (`baseline_dialysis_2018_ul') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2019_ll') _tab %10.2f (`baseline_dialysis_2019_ul') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2020_ll') _tab %10.2f (`baseline_dialysis_2020_ul') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2021_ll') _tab %10.2f (`baseline_dialysis_2021_ul') _tab %10.2f (`baseline_dialysis_2022') _tab %10.2f (`baseline_dialysis_2022_ll') _tab %10.2f (`baseline_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2017_ll') _tab %10.2f (`none_dialysis_2017_ul') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2018_ll') _tab %10.2f (`none_dialysis_2018_ul') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2019_ll') _tab %10.2f (`none_dialysis_2019_ul') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2020_ll') _tab %10.2f (`none_dialysis_2020_ul') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2021_ll') _tab %10.2f (`none_dialysis_2021_ul') _tab %10.2f (`none_dialysis_2022') _tab %10.2f (`none_dialysis_2022_ll') _tab %10.2f (`none_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2017_ll') _tab %10.2f (`kt_dialysis_2017_ul') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2018_ll') _tab %10.2f (`kt_dialysis_2018_ul') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2019_ll') _tab %10.2f (`kt_dialysis_2019_ul') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2020_ll') _tab %10.2f (`kt_dialysis_2020_ul') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2021_ll') _tab %10.2f (`kt_dialysis_2021_ul') _tab %10.2f (`kt_dialysis_2022') _tab %10.2f (`kt_dialysis_2022_ll') _tab %10.2f (`kt_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2017_ll') _tab %10.2f (`deceased_dialysis_2017_ul') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2018_ll') _tab %10.2f (`deceased_dialysis_2018_ul') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2019_ll') _tab %10.2f (`deceased_dialysis_2019_ul') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2020_ll') _tab %10.2f (`deceased_dialysis_2020_ul') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2021_ll') _tab %10.2f (`deceased_dialysis_2021_ul') _tab %10.2f (`deceased_dialysis_2022') _tab %10.2f (`deceased_dialysis_2022_ll') _tab %10.2f (`deceased_dialysis_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2017_ll') _tab %10.2f (`cardio_dialysis_2017_ul') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2018_ll') _tab %10.2f (`cardio_dialysis_2018_ul') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2019_ll') _tab %10.2f (`cardio_dialysis_2019_ul') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2020_ll') _tab %10.2f (`cardio_dialysis_2020_ul') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2021_ll') _tab %10.2f (`cardio_dialysis_2021_ul') _tab %10.2f (`cardio_dialysis_2022') _tab %10.2f (`cardio_dialysis_2022_ll') _tab %10.2f (`cardio_dialysis_2022_ul') _n

*Kidney transplant
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2017_ll') _tab %10.2f (`baseline_kt_2017_ul') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2018_ll') _tab %10.2f (`baseline_kt_2018_ul') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2019_ll') _tab %10.2f (`baseline_kt_2019_ul') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2020_ll') _tab %10.2f (`baseline_kt_2020_ul') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2021_ll') _tab %10.2f (`baseline_kt_2021_ul') _tab %10.2f (`baseline_kt_2022') _tab %10.2f (`baseline_kt_2022_ll') _tab %10.2f (`baseline_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2017_ll') _tab %10.2f (`none_kt_2017_ul') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2018_ll') _tab %10.2f (`none_kt_2018_ul') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2019_ll') _tab %10.2f (`none_kt_2019_ul') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2020_ll') _tab %10.2f (`none_kt_2020_ul') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2021_ll') _tab %10.2f (`none_kt_2021_ul') _tab %10.2f (`none_kt_2022') _tab %10.2f (`none_kt_2022_ll') _tab %10.2f (`none_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2017_ll') _tab %10.2f (`dialysis_kt_2017_ul') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2018_ll') _tab %10.2f (`dialysis_kt_2018_ul') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2019_ll') _tab %10.2f (`dialysis_kt_2019_ul') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2020_ll') _tab %10.2f (`dialysis_kt_2020_ul') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2021_ll') _tab %10.2f (`dialysis_kt_2021_ul') _tab %10.2f (`dialysis_kt_2022') _tab %10.2f (`dialysis_kt_2022_ll') _tab %10.2f (`dialysis_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2017_ll') _tab %10.2f (`deceased_kt_2017_ul') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2018_ll') _tab %10.2f (`deceased_kt_2018_ul') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2019_ll') _tab %10.2f (`deceased_kt_2019_ul') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2020_ll') _tab %10.2f (`deceased_kt_2020_ul') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2021_ll') _tab %10.2f (`deceased_kt_2021_ul') _tab %10.2f (`deceased_kt_2022') _tab %10.2f (`deceased_kt_2022_ll') _tab %10.2f (`deceased_kt_2022_ul') _n
file write tablecontent ("`label`i''") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2017_ll') _tab %10.2f (`cardio_kt_2017_ul') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2018_ll') _tab %10.2f (`cardio_kt_2018_ul') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2019_ll') _tab %10.2f (`cardio_kt_2019_ul') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2020_ll') _tab %10.2f (`cardio_kt_2020_ul') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2021_ll') _tab %10.2f (`cardio_kt_2021_ul') _tab %10.2f (`cardio_kt_2022') _tab %10.2f (`cardio_kt_2022_ll') _tab %10.2f (`cardio_kt_2022_ul') _n
}

**London
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if region!=3
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

local year "2017 2018 2019 2021 2022"

foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if region!=3

total weight if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = r(table)[1,1]
local kt_ckd4_`x'_ll = r(table)[5,1]
local kt_ckd4_`x'_ul = r(table)[6,1]
}

*Overall
file write tablecontent ("London") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2017_ll') _tab %10.2f (`baseline_ckd_2017_ul') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2018_ll') _tab %10.2f (`baseline_ckd_2018_ul') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2019_ll') _tab %10.2f (`baseline_ckd_2019_ul') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2020_ll') _tab %10.2f (`baseline_ckd_2020_ul') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2021_ll') _tab %10.2f (`baseline_ckd_2021_ul') _tab %10.2f (`baseline_ckd_2022') _tab %10.2f (`baseline_ckd_2022_ll') _tab %10.2f (`baseline_ckd_2022_ul') _n
file write tablecontent ("London") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2017_ll') _tab %10.2f (`none_ckd_2017_ul') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2018_ll') _tab %10.2f (`none_ckd_2018_ul') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2019_ll') _tab %10.2f (`none_ckd_2019_ul') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2020_ll') _tab %10.2f (`none_ckd_2020_ul') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2021_ll') _tab %10.2f (`none_ckd_2021_ul') _tab %10.2f (`none_ckd_2022') _tab %10.2f (`none_ckd_2022_ll') _tab %10.2f (`none_ckd_2022_ul') _n
file write tablecontent ("London") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2017_ll') _tab %10.2f (`ckd3_ckd_2017_ul') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2018_ll') _tab %10.2f (`ckd3_ckd_2018_ul') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2019_ll') _tab %10.2f (`ckd3_ckd_2019_ul') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2020_ll') _tab %10.2f (`ckd3_ckd_2020_ul') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2021_ll') _tab %10.2f (`ckd3_ckd_2021_ul') _tab %10.2f (`ckd3_ckd_2022') _tab %10.2f (`ckd3_ckd_2022_ll') _tab %10.2f (`ckd3_ckd_2022_ul') _n
file write tablecontent ("London") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2017_ll') _tab %10.2f (`ckd4_ckd_2017_ul') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2018_ll') _tab %10.2f (`ckd4_ckd_2018_ul') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2019_ll') _tab %10.2f (`ckd4_ckd_2019_ul') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2020_ll') _tab %10.2f (`ckd4_ckd_2020_ul') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2021_ll') _tab %10.2f (`ckd4_ckd_2021_ul') _tab %10.2f (`ckd4_ckd_2022') _tab %10.2f (`ckd4_ckd_2022_ll') _tab %10.2f (`ckd4_ckd_2022_ul') _n
file write tablecontent ("London") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2017_ll') _tab %10.2f (`dialysis_ckd_2017_ul') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2018_ll') _tab %10.2f (`dialysis_ckd_2018_ul') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2019_ll') _tab %10.2f (`dialysis_ckd_2019_ul') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2020_ll') _tab %10.2f (`dialysis_ckd_2020_ul') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2021_ll') _tab %10.2f (`dialysis_ckd_2021_ul') _tab %10.2f (`dialysis_ckd_2022') _tab %10.2f (`dialysis_ckd_2022_ll') _tab %10.2f (`dialysis_ckd_2022_ul') _n
file write tablecontent ("London") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2017_ll') _tab %10.2f (`kt_ckd_2017_ul') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2018_ll') _tab %10.2f (`kt_ckd_2018_ul') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2019_ll') _tab %10.2f (`kt_ckd_2019_ul') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2020_ll') _tab %10.2f (`kt_ckd_2020_ul') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2021_ll') _tab %10.2f (`kt_ckd_2021_ul') _tab %10.2f (`kt_ckd_2022') _tab %10.2f (`kt_ckd_2022_ll') _tab %10.2f (`kt_ckd_2022_ul') _n
file write tablecontent ("London") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2017_ll') _tab %10.2f (`deceased_ckd_2017_ul') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2018_ll') _tab %10.2f (`deceased_ckd_2018_ul') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2019_ll') _tab %10.2f (`deceased_ckd_2019_ul') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2020_ll') _tab %10.2f (`deceased_ckd_2020_ul') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2021_ll') _tab %10.2f (`deceased_ckd_2021_ul') _tab %10.2f (`deceased_ckd_2022') _tab %10.2f (`deceased_ckd_2022_ll') _tab %10.2f (`deceased_ckd_2022_ul') _n
file write tablecontent ("London") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2017_ll') _tab %10.2f (`cardio_ckd_2017_ul') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2018_ll') _tab %10.2f (`cardio_ckd_2018_ul') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2019_ll') _tab %10.2f (`cardio_ckd_2019_ul') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2020_ll') _tab %10.2f (`cardio_ckd_2020_ul') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2021_ll') _tab %10.2f (`cardio_ckd_2021_ul') _tab %10.2f (`cardio_ckd_2022') _tab %10.2f (`cardio_ckd_2022_ll') _tab %10.2f (`cardio_ckd_2022_ul') _n

*No CKD
file write tablecontent ("London") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2017_ll') _tab %10.2f (`baseline_nockd_2017_ul') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2018_ll') _tab %10.2f (`baseline_nockd_2018_ul') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2019_ll') _tab %10.2f (`baseline_nockd_2019_ul') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2020_ll') _tab %10.2f (`baseline_nockd_2020_ul') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2021_ll') _tab %10.2f (`baseline_nockd_2021_ul') _tab %10.2f (`baseline_nockd_2022') _tab %10.2f (`baseline_nockd_2022_ll') _tab %10.2f (`baseline_nockd_2022_ul') _n
file write tablecontent ("London") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2017_ll') _tab %10.2f (`none_nockd_2017_ul') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2018_ll') _tab %10.2f (`none_nockd_2018_ul') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2019_ll') _tab %10.2f (`none_nockd_2019_ul') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2020_ll') _tab %10.2f (`none_nockd_2020_ul') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2021_ll') _tab %10.2f (`none_nockd_2021_ul') _tab %10.2f (`none_nockd_2022') _tab %10.2f (`none_nockd_2022_ll') _tab %10.2f (`none_nockd_2022_ul') _n
file write tablecontent ("London") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2017_ll') _tab %10.2f (`ckd3_nockd_2017_ul') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2018_ll') _tab %10.2f (`ckd3_nockd_2018_ul') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2019_ll') _tab %10.2f (`ckd3_nockd_2019_ul') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2020_ll') _tab %10.2f (`ckd3_nockd_2020_ul') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2021_ll') _tab %10.2f (`ckd3_nockd_2021_ul') _tab %10.2f (`ckd3_nockd_2022') _tab %10.2f (`ckd3_nockd_2022_ll') _tab %10.2f (`ckd3_nockd_2022_ul') _n
file write tablecontent ("London") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2017_ll') _tab %10.2f (`ckd4_nockd_2017_ul') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2018_ll') _tab %10.2f (`ckd4_nockd_2018_ul') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2019_ll') _tab %10.2f (`ckd4_nockd_2019_ul') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2020_ll') _tab %10.2f (`ckd4_nockd_2020_ul') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2021_ll') _tab %10.2f (`ckd4_nockd_2021_ul') _tab %10.2f (`ckd4_nockd_2022') _tab %10.2f (`ckd4_nockd_2022_ll') _tab %10.2f (`ckd4_nockd_2022_ul') _n
file write tablecontent ("London") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2017_ll') _tab %10.2f (`dialysis_nockd_2017_ul') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2018_ll') _tab %10.2f (`dialysis_nockd_2018_ul') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2019_ll') _tab %10.2f (`dialysis_nockd_2019_ul') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2020_ll') _tab %10.2f (`dialysis_nockd_2020_ul') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2021_ll') _tab %10.2f (`dialysis_nockd_2021_ul') _tab %10.2f (`dialysis_nockd_2022') _tab %10.2f (`dialysis_nockd_2022_ll') _tab %10.2f (`dialysis_nockd_2022_ul') _n
file write tablecontent ("London") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("London") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("London") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2017_ll') _tab %10.2f (`deceased_ckd3_2017_ul') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2018_ll') _tab %10.2f (`deceased_ckd3_2018_ul') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2019_ll') _tab %10.2f (`deceased_ckd3_2019_ul') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2020_ll') _tab %10.2f (`deceased_ckd3_2020_ul') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2021_ll') _tab %10.2f (`deceased_ckd3_2021_ul') _tab %10.2f (`deceased_ckd3_2022') _tab %10.2f (`deceased_ckd3_2022_ll') _tab %10.2f (`deceased_ckd3_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2017_ll') _tab %10.2f (`cardio_ckd3_2017_ul') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2018_ll') _tab %10.2f (`cardio_ckd3_2018_ul') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2019_ll') _tab %10.2f (`cardio_ckd3_2019_ul') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2020_ll') _tab %10.2f (`cardio_ckd3_2020_ul') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2021_ll') _tab %10.2f (`cardio_ckd3_2021_ul') _tab %10.2f (`cardio_ckd3_2022') _tab %10.2f (`cardio_ckd3_2022_ll') _tab %10.2f (`cardio_ckd3_2022_ul') _n

*CKD stage 4/5 without RRT
file write tablecontent ("London") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2017_ll') _tab %10.2f (`baseline_ckd4_2017_ul') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2018_ll') _tab %10.2f (`baseline_ckd4_2018_ul') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2019_ll') _tab %10.2f (`baseline_ckd4_2019_ul') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2020_ll') _tab %10.2f (`baseline_ckd4_2020_ul') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2021_ll') _tab %10.2f (`baseline_ckd4_2021_ul') _tab %10.2f (`baseline_ckd4_2022') _tab %10.2f (`baseline_ckd4_2022_ll') _tab %10.2f (`baseline_ckd4_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2017_ll') _tab %10.2f (`none_ckd4_2017_ul') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2018_ll') _tab %10.2f (`none_ckd4_2018_ul') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2019_ll') _tab %10.2f (`none_ckd4_2019_ul') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2020_ll') _tab %10.2f (`none_ckd4_2020_ul') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2021_ll') _tab %10.2f (`none_ckd4_2021_ul') _tab %10.2f (`none_ckd4_2022') _tab %10.2f (`none_ckd4_2022_ll') _tab %10.2f (`none_ckd4_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2017_ll') _tab %10.2f (`dialysis_ckd4_2017_ul') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2018_ll') _tab %10.2f (`dialysis_ckd4_2018_ul') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2019_ll') _tab %10.2f (`dialysis_ckd4_2019_ul') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2020_ll') _tab %10.2f (`dialysis_ckd4_2020_ul') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2021_ll') _tab %10.2f (`dialysis_ckd4_2021_ul') _tab %10.2f (`dialysis_ckd4_2022') _tab %10.2f (`dialysis_ckd4_2022_ll') _tab %10.2f (`dialysis_ckd4_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2017_ll') _tab %10.2f (`kt_ckd4_2017_ul') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2018_ll') _tab %10.2f (`kt_ckd4_2018_ul') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2019_ll') _tab %10.2f (`kt_ckd4_2019_ul') _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2021_ll') _tab %10.2f (`kt_ckd4_2021_ul') _tab %10.2f (`kt_ckd4_2022') _tab %10.2f (`kt_ckd4_2022_ll') _tab %10.2f (`kt_ckd4_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2017_ll') _tab %10.2f (`deceased_ckd4_2017_ul') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2018_ll') _tab %10.2f (`deceased_ckd4_2018_ul') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2019_ll') _tab %10.2f (`deceased_ckd4_2019_ul') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2020_ll') _tab %10.2f (`deceased_ckd4_2020_ul') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2021_ll') _tab %10.2f (`deceased_ckd4_2021_ul') _tab %10.2f (`deceased_ckd4_2022') _tab %10.2f (`deceased_ckd4_2022_ll') _tab %10.2f (`deceased_ckd4_2022_ul') _n
file write tablecontent ("London") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2017_ll') _tab %10.2f (`cardio_ckd4_2017_ul') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2018_ll') _tab %10.2f (`cardio_ckd4_2018_ul') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2019_ll') _tab %10.2f (`cardio_ckd4_2019_ul') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2020_ll') _tab %10.2f (`cardio_ckd4_2020_ul') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2021_ll') _tab %10.2f (`cardio_ckd4_2021_ul') _tab %10.2f (`cardio_ckd4_2022') _tab %10.2f (`cardio_ckd4_2022_ll') _tab %10.2f (`cardio_ckd4_2022_ul') _n

*Dialysis
file write tablecontent ("London") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2017_ll') _tab %10.2f (`baseline_dialysis_2017_ul') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2018_ll') _tab %10.2f (`baseline_dialysis_2018_ul') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2019_ll') _tab %10.2f (`baseline_dialysis_2019_ul') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2020_ll') _tab %10.2f (`baseline_dialysis_2020_ul') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2021_ll') _tab %10.2f (`baseline_dialysis_2021_ul') _tab %10.2f (`baseline_dialysis_2022') _tab %10.2f (`baseline_dialysis_2022_ll') _tab %10.2f (`baseline_dialysis_2022_ul') _n
file write tablecontent ("London") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2017_ll') _tab %10.2f (`none_dialysis_2017_ul') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2018_ll') _tab %10.2f (`none_dialysis_2018_ul') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2019_ll') _tab %10.2f (`none_dialysis_2019_ul') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2020_ll') _tab %10.2f (`none_dialysis_2020_ul') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2021_ll') _tab %10.2f (`none_dialysis_2021_ul') _tab %10.2f (`none_dialysis_2022') _tab %10.2f (`none_dialysis_2022_ll') _tab %10.2f (`none_dialysis_2022_ul') _n
file write tablecontent ("London") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2017_ll') _tab %10.2f (`kt_dialysis_2017_ul') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2018_ll') _tab %10.2f (`kt_dialysis_2018_ul') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2019_ll') _tab %10.2f (`kt_dialysis_2019_ul') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2020_ll') _tab %10.2f (`kt_dialysis_2020_ul') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2021_ll') _tab %10.2f (`kt_dialysis_2021_ul') _tab %10.2f (`kt_dialysis_2022') _tab %10.2f (`kt_dialysis_2022_ll') _tab %10.2f (`kt_dialysis_2022_ul') _n
file write tablecontent ("London") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2017_ll') _tab %10.2f (`deceased_dialysis_2017_ul') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2018_ll') _tab %10.2f (`deceased_dialysis_2018_ul') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2019_ll') _tab %10.2f (`deceased_dialysis_2019_ul') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2020_ll') _tab %10.2f (`deceased_dialysis_2020_ul') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2021_ll') _tab %10.2f (`deceased_dialysis_2021_ul') _tab %10.2f (`deceased_dialysis_2022') _tab %10.2f (`deceased_dialysis_2022_ll') _tab %10.2f (`deceased_dialysis_2022_ul') _n
file write tablecontent ("London") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2017_ll') _tab %10.2f (`cardio_dialysis_2017_ul') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2018_ll') _tab %10.2f (`cardio_dialysis_2018_ul') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2019_ll') _tab %10.2f (`cardio_dialysis_2019_ul') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2020_ll') _tab %10.2f (`cardio_dialysis_2020_ul') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2021_ll') _tab %10.2f (`cardio_dialysis_2021_ul') _tab %10.2f (`cardio_dialysis_2022') _tab %10.2f (`cardio_dialysis_2022_ll') _tab %10.2f (`cardio_dialysis_2022_ul') _n

*Kidney transplant
file write tablecontent ("London") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2017_ll') _tab %10.2f (`baseline_kt_2017_ul') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2018_ll') _tab %10.2f (`baseline_kt_2018_ul') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2019_ll') _tab %10.2f (`baseline_kt_2019_ul') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2020_ll') _tab %10.2f (`baseline_kt_2020_ul') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2021_ll') _tab %10.2f (`baseline_kt_2021_ul') _tab %10.2f (`baseline_kt_2022') _tab %10.2f (`baseline_kt_2022_ll') _tab %10.2f (`baseline_kt_2022_ul') _n
file write tablecontent ("London") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2017_ll') _tab %10.2f (`none_kt_2017_ul') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2018_ll') _tab %10.2f (`none_kt_2018_ul') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2019_ll') _tab %10.2f (`none_kt_2019_ul') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2020_ll') _tab %10.2f (`none_kt_2020_ul') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2021_ll') _tab %10.2f (`none_kt_2021_ul') _tab %10.2f (`none_kt_2022') _tab %10.2f (`none_kt_2022_ll') _tab %10.2f (`none_kt_2022_ul') _n
file write tablecontent ("London") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2017_ll') _tab %10.2f (`dialysis_kt_2017_ul') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2018_ll') _tab %10.2f (`dialysis_kt_2018_ul') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2019_ll') _tab %10.2f (`dialysis_kt_2019_ul') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2020_ll') _tab %10.2f (`dialysis_kt_2020_ul') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2021_ll') _tab %10.2f (`dialysis_kt_2021_ul') _tab %10.2f (`dialysis_kt_2022') _tab %10.2f (`dialysis_kt_2022_ll') _tab %10.2f (`dialysis_kt_2022_ul') _n
file write tablecontent ("London") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2017_ll') _tab %10.2f (`deceased_kt_2017_ul') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2018_ll') _tab %10.2f (`deceased_kt_2018_ul') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2019_ll') _tab %10.2f (`deceased_kt_2019_ul') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2020_ll') _tab %10.2f (`deceased_kt_2020_ul') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2021_ll') _tab %10.2f (`deceased_kt_2021_ul') _tab %10.2f (`deceased_kt_2022') _tab %10.2f (`deceased_kt_2022_ll') _tab %10.2f (`deceased_kt_2022_ul') _n
file write tablecontent ("London") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2017_ll') _tab %10.2f (`cardio_kt_2017_ul') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2018_ll') _tab %10.2f (`cardio_kt_2018_ul') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2019_ll') _tab %10.2f (`cardio_kt_2019_ul') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2020_ll') _tab %10.2f (`cardio_kt_2020_ul') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2021_ll') _tab %10.2f (`cardio_kt_2021_ul') _tab %10.2f (`cardio_kt_2022') _tab %10.2f (`cardio_kt_2022_ll') _tab %10.2f (`cardio_kt_2022_ul') _n

**North East
local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if region!=4
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

use ./output/2018_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/2018_nockd_complete
drop if region!=4

total weight if ckd_group==3 & ckd_progression==4
local kt_ckd4_2018 = r(table)[1,1]
local kt_ckd4_2018_ll = r(table)[5,1]
local kt_ckd4_2018_ul = r(table)[6,1]

*Overall
file write tablecontent ("North East") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2017_ll') _tab %10.2f (`baseline_ckd_2017_ul') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2018_ll') _tab %10.2f (`baseline_ckd_2018_ul') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2019_ll') _tab %10.2f (`baseline_ckd_2019_ul') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2020_ll') _tab %10.2f (`baseline_ckd_2020_ul') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2021_ll') _tab %10.2f (`baseline_ckd_2021_ul') _tab %10.2f (`baseline_ckd_2022') _tab %10.2f (`baseline_ckd_2022_ll') _tab %10.2f (`baseline_ckd_2022_ul') _n
file write tablecontent ("North East") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2017_ll') _tab %10.2f (`none_ckd_2017_ul') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2018_ll') _tab %10.2f (`none_ckd_2018_ul') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2019_ll') _tab %10.2f (`none_ckd_2019_ul') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2020_ll') _tab %10.2f (`none_ckd_2020_ul') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2021_ll') _tab %10.2f (`none_ckd_2021_ul') _tab %10.2f (`none_ckd_2022') _tab %10.2f (`none_ckd_2022_ll') _tab %10.2f (`none_ckd_2022_ul') _n
file write tablecontent ("North East") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2017_ll') _tab %10.2f (`ckd3_ckd_2017_ul') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2018_ll') _tab %10.2f (`ckd3_ckd_2018_ul') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2019_ll') _tab %10.2f (`ckd3_ckd_2019_ul') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2020_ll') _tab %10.2f (`ckd3_ckd_2020_ul') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2021_ll') _tab %10.2f (`ckd3_ckd_2021_ul') _tab %10.2f (`ckd3_ckd_2022') _tab %10.2f (`ckd3_ckd_2022_ll') _tab %10.2f (`ckd3_ckd_2022_ul') _n
file write tablecontent ("North East") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2017_ll') _tab %10.2f (`ckd4_ckd_2017_ul') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2018_ll') _tab %10.2f (`ckd4_ckd_2018_ul') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2019_ll') _tab %10.2f (`ckd4_ckd_2019_ul') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2020_ll') _tab %10.2f (`ckd4_ckd_2020_ul') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2021_ll') _tab %10.2f (`ckd4_ckd_2021_ul') _tab %10.2f (`ckd4_ckd_2022') _tab %10.2f (`ckd4_ckd_2022_ll') _tab %10.2f (`ckd4_ckd_2022_ul') _n
file write tablecontent ("North East") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2017_ll') _tab %10.2f (`dialysis_ckd_2017_ul') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2018_ll') _tab %10.2f (`dialysis_ckd_2018_ul') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2019_ll') _tab %10.2f (`dialysis_ckd_2019_ul') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2020_ll') _tab %10.2f (`dialysis_ckd_2020_ul') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2021_ll') _tab %10.2f (`dialysis_ckd_2021_ul') _tab %10.2f (`dialysis_ckd_2022') _tab %10.2f (`dialysis_ckd_2022_ll') _tab %10.2f (`dialysis_ckd_2022_ul') _n
file write tablecontent ("North East") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2017_ll') _tab %10.2f (`kt_ckd_2017_ul') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2018_ll') _tab %10.2f (`kt_ckd_2018_ul') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2019_ll') _tab %10.2f (`kt_ckd_2019_ul') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2020_ll') _tab %10.2f (`kt_ckd_2020_ul') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2021_ll') _tab %10.2f (`kt_ckd_2021_ul') _tab %10.2f (`kt_ckd_2022') _tab %10.2f (`kt_ckd_2022_ll') _tab %10.2f (`kt_ckd_2022_ul') _n
file write tablecontent ("North East") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2017_ll') _tab %10.2f (`deceased_ckd_2017_ul') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2018_ll') _tab %10.2f (`deceased_ckd_2018_ul') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2019_ll') _tab %10.2f (`deceased_ckd_2019_ul') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2020_ll') _tab %10.2f (`deceased_ckd_2020_ul') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2021_ll') _tab %10.2f (`deceased_ckd_2021_ul') _tab %10.2f (`deceased_ckd_2022') _tab %10.2f (`deceased_ckd_2022_ll') _tab %10.2f (`deceased_ckd_2022_ul') _n
file write tablecontent ("North East") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2017_ll') _tab %10.2f (`cardio_ckd_2017_ul') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2018_ll') _tab %10.2f (`cardio_ckd_2018_ul') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2019_ll') _tab %10.2f (`cardio_ckd_2019_ul') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2020_ll') _tab %10.2f (`cardio_ckd_2020_ul') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2021_ll') _tab %10.2f (`cardio_ckd_2021_ul') _tab %10.2f (`cardio_ckd_2022') _tab %10.2f (`cardio_ckd_2022_ll') _tab %10.2f (`cardio_ckd_2022_ul') _n

*No CKD
file write tablecontent ("North East") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2017_ll') _tab %10.2f (`baseline_nockd_2017_ul') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2018_ll') _tab %10.2f (`baseline_nockd_2018_ul') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2019_ll') _tab %10.2f (`baseline_nockd_2019_ul') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2020_ll') _tab %10.2f (`baseline_nockd_2020_ul') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2021_ll') _tab %10.2f (`baseline_nockd_2021_ul') _tab %10.2f (`baseline_nockd_2022') _tab %10.2f (`baseline_nockd_2022_ll') _tab %10.2f (`baseline_nockd_2022_ul') _n
file write tablecontent ("North East") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2017_ll') _tab %10.2f (`none_nockd_2017_ul') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2018_ll') _tab %10.2f (`none_nockd_2018_ul') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2019_ll') _tab %10.2f (`none_nockd_2019_ul') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2020_ll') _tab %10.2f (`none_nockd_2020_ul') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2021_ll') _tab %10.2f (`none_nockd_2021_ul') _tab %10.2f (`none_nockd_2022') _tab %10.2f (`none_nockd_2022_ll') _tab %10.2f (`none_nockd_2022_ul') _n
file write tablecontent ("North East") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2017_ll') _tab %10.2f (`ckd3_nockd_2017_ul') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2018_ll') _tab %10.2f (`ckd3_nockd_2018_ul') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2019_ll') _tab %10.2f (`ckd3_nockd_2019_ul') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2020_ll') _tab %10.2f (`ckd3_nockd_2020_ul') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2021_ll') _tab %10.2f (`ckd3_nockd_2021_ul') _tab %10.2f (`ckd3_nockd_2022') _tab %10.2f (`ckd3_nockd_2022_ll') _tab %10.2f (`ckd3_nockd_2022_ul') _n
file write tablecontent ("North East") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2017_ll') _tab %10.2f (`ckd4_nockd_2017_ul') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2018_ll') _tab %10.2f (`ckd4_nockd_2018_ul') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2019_ll') _tab %10.2f (`ckd4_nockd_2019_ul') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2020_ll') _tab %10.2f (`ckd4_nockd_2020_ul') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2021_ll') _tab %10.2f (`ckd4_nockd_2021_ul') _tab %10.2f (`ckd4_nockd_2022') _tab %10.2f (`ckd4_nockd_2022_ll') _tab %10.2f (`ckd4_nockd_2022_ul') _n
file write tablecontent ("North East") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2017_ll') _tab %10.2f (`dialysis_nockd_2017_ul') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2018_ll') _tab %10.2f (`dialysis_nockd_2018_ul') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2019_ll') _tab %10.2f (`dialysis_nockd_2019_ul') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2020_ll') _tab %10.2f (`dialysis_nockd_2020_ul') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2021_ll') _tab %10.2f (`dialysis_nockd_2021_ul') _tab %10.2f (`dialysis_nockd_2022') _tab %10.2f (`dialysis_nockd_2022_ll') _tab %10.2f (`dialysis_nockd_2022_ul') _n
file write tablecontent ("North East") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("North East") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("North East") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("North East") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("North East") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("North East") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
file write tablecontent ("North East") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2017_ll') _tab %10.2f (`deceased_ckd3_2017_ul') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2018_ll') _tab %10.2f (`deceased_ckd3_2018_ul') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2019_ll') _tab %10.2f (`deceased_ckd3_2019_ul') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2020_ll') _tab %10.2f (`deceased_ckd3_2020_ul') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2021_ll') _tab %10.2f (`deceased_ckd3_2021_ul') _tab %10.2f (`deceased_ckd3_2022') _tab %10.2f (`deceased_ckd3_2022_ll') _tab %10.2f (`deceased_ckd3_2022_ul') _n
file write tablecontent ("North East") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2017_ll') _tab %10.2f (`cardio_ckd3_2017_ul') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2018_ll') _tab %10.2f (`cardio_ckd3_2018_ul') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2019_ll') _tab %10.2f (`cardio_ckd3_2019_ul') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2020_ll') _tab %10.2f (`cardio_ckd3_2020_ul') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2021_ll') _tab %10.2f (`cardio_ckd3_2021_ul') _tab %10.2f (`cardio_ckd3_2022') _tab %10.2f (`cardio_ckd3_2022_ll') _tab %10.2f (`cardio_ckd3_2022_ul') _n

*CKD stage 4/5 without RRT
file write tablecontent ("North East") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2017_ll') _tab %10.2f (`baseline_ckd4_2017_ul') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2018_ll') _tab %10.2f (`baseline_ckd4_2018_ul') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2019_ll') _tab %10.2f (`baseline_ckd4_2019_ul') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2020_ll') _tab %10.2f (`baseline_ckd4_2020_ul') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2021_ll') _tab %10.2f (`baseline_ckd4_2021_ul') _tab %10.2f (`baseline_ckd4_2022') _tab %10.2f (`baseline_ckd4_2022_ll') _tab %10.2f (`baseline_ckd4_2022_ul') _n
file write tablecontent ("North East") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2017_ll') _tab %10.2f (`none_ckd4_2017_ul') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2018_ll') _tab %10.2f (`none_ckd4_2018_ul') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2019_ll') _tab %10.2f (`none_ckd4_2019_ul') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2020_ll') _tab %10.2f (`none_ckd4_2020_ul') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2021_ll') _tab %10.2f (`none_ckd4_2021_ul') _tab %10.2f (`none_ckd4_2022') _tab %10.2f (`none_ckd4_2022_ll') _tab %10.2f (`none_ckd4_2022_ul') _n
file write tablecontent ("North East") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2017_ll') _tab %10.2f (`dialysis_ckd4_2017_ul') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2018_ll') _tab %10.2f (`dialysis_ckd4_2018_ul') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2019_ll') _tab %10.2f (`dialysis_ckd4_2019_ul') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2020_ll') _tab %10.2f (`dialysis_ckd4_2020_ul') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2021_ll') _tab %10.2f (`dialysis_ckd4_2021_ul') _tab %10.2f (`dialysis_ckd4_2022') _tab %10.2f (`dialysis_ckd4_2022_ll') _tab %10.2f (`dialysis_ckd4_2022_ul') _n
file write tablecontent ("North East") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2018_ll') _tab %10.2f (`kt_ckd4_2018_ul') _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _n
file write tablecontent ("North East") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2017_ll') _tab %10.2f (`deceased_ckd4_2017_ul') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2018_ll') _tab %10.2f (`deceased_ckd4_2018_ul') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2019_ll') _tab %10.2f (`deceased_ckd4_2019_ul') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2020_ll') _tab %10.2f (`deceased_ckd4_2020_ul') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2021_ll') _tab %10.2f (`deceased_ckd4_2021_ul') _tab %10.2f (`deceased_ckd4_2022') _tab %10.2f (`deceased_ckd4_2022_ll') _tab %10.2f (`deceased_ckd4_2022_ul') _n
file write tablecontent ("North East") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2017_ll') _tab %10.2f (`cardio_ckd4_2017_ul') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2018_ll') _tab %10.2f (`cardio_ckd4_2018_ul') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2019_ll') _tab %10.2f (`cardio_ckd4_2019_ul') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2020_ll') _tab %10.2f (`cardio_ckd4_2020_ul') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2021_ll') _tab %10.2f (`cardio_ckd4_2021_ul') _tab %10.2f (`cardio_ckd4_2022') _tab %10.2f (`cardio_ckd4_2022_ll') _tab %10.2f (`cardio_ckd4_2022_ul') _n

*Dialysis
file write tablecontent ("North East") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2017_ll') _tab %10.2f (`baseline_dialysis_2017_ul') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2018_ll') _tab %10.2f (`baseline_dialysis_2018_ul') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2019_ll') _tab %10.2f (`baseline_dialysis_2019_ul') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2020_ll') _tab %10.2f (`baseline_dialysis_2020_ul') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2021_ll') _tab %10.2f (`baseline_dialysis_2021_ul') _tab %10.2f (`baseline_dialysis_2022') _tab %10.2f (`baseline_dialysis_2022_ll') _tab %10.2f (`baseline_dialysis_2022_ul') _n
file write tablecontent ("North East") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2017_ll') _tab %10.2f (`none_dialysis_2017_ul') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2018_ll') _tab %10.2f (`none_dialysis_2018_ul') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2019_ll') _tab %10.2f (`none_dialysis_2019_ul') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2020_ll') _tab %10.2f (`none_dialysis_2020_ul') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2021_ll') _tab %10.2f (`none_dialysis_2021_ul') _tab %10.2f (`none_dialysis_2022') _tab %10.2f (`none_dialysis_2022_ll') _tab %10.2f (`none_dialysis_2022_ul') _n
file write tablecontent ("North East") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2017_ll') _tab %10.2f (`kt_dialysis_2017_ul') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2018_ll') _tab %10.2f (`kt_dialysis_2018_ul') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2019_ll') _tab %10.2f (`kt_dialysis_2019_ul') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2020_ll') _tab %10.2f (`kt_dialysis_2020_ul') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2021_ll') _tab %10.2f (`kt_dialysis_2021_ul') _tab %10.2f (`kt_dialysis_2022') _tab %10.2f (`kt_dialysis_2022_ll') _tab %10.2f (`kt_dialysis_2022_ul') _n
file write tablecontent ("North East") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2017_ll') _tab %10.2f (`deceased_dialysis_2017_ul') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2018_ll') _tab %10.2f (`deceased_dialysis_2018_ul') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2019_ll') _tab %10.2f (`deceased_dialysis_2019_ul') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2020_ll') _tab %10.2f (`deceased_dialysis_2020_ul') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2021_ll') _tab %10.2f (`deceased_dialysis_2021_ul') _tab %10.2f (`deceased_dialysis_2022') _tab %10.2f (`deceased_dialysis_2022_ll') _tab %10.2f (`deceased_dialysis_2022_ul') _n
file write tablecontent ("North East") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2017_ll') _tab %10.2f (`cardio_dialysis_2017_ul') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2018_ll') _tab %10.2f (`cardio_dialysis_2018_ul') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2019_ll') _tab %10.2f (`cardio_dialysis_2019_ul') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2020_ll') _tab %10.2f (`cardio_dialysis_2020_ul') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2021_ll') _tab %10.2f (`cardio_dialysis_2021_ul') _tab %10.2f (`cardio_dialysis_2022') _tab %10.2f (`cardio_dialysis_2022_ll') _tab %10.2f (`cardio_dialysis_2022_ul') _n

*Kidney transplant
file write tablecontent ("North East") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2017_ll') _tab %10.2f (`baseline_kt_2017_ul') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2018_ll') _tab %10.2f (`baseline_kt_2018_ul') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2019_ll') _tab %10.2f (`baseline_kt_2019_ul') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2020_ll') _tab %10.2f (`baseline_kt_2020_ul') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2021_ll') _tab %10.2f (`baseline_kt_2021_ul') _tab %10.2f (`baseline_kt_2022') _tab %10.2f (`baseline_kt_2022_ll') _tab %10.2f (`baseline_kt_2022_ul') _n
file write tablecontent ("North East") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2017_ll') _tab %10.2f (`none_kt_2017_ul') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2018_ll') _tab %10.2f (`none_kt_2018_ul') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2019_ll') _tab %10.2f (`none_kt_2019_ul') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2020_ll') _tab %10.2f (`none_kt_2020_ul') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2021_ll') _tab %10.2f (`none_kt_2021_ul') _tab %10.2f (`none_kt_2022') _tab %10.2f (`none_kt_2022_ll') _tab %10.2f (`none_kt_2022_ul') _n
file write tablecontent ("North East") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2017_ll') _tab %10.2f (`dialysis_kt_2017_ul') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2018_ll') _tab %10.2f (`dialysis_kt_2018_ul') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2019_ll') _tab %10.2f (`dialysis_kt_2019_ul') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2020_ll') _tab %10.2f (`dialysis_kt_2020_ul') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2021_ll') _tab %10.2f (`dialysis_kt_2021_ul') _tab %10.2f (`dialysis_kt_2022') _tab %10.2f (`dialysis_kt_2022_ll') _tab %10.2f (`dialysis_kt_2022_ul') _n
file write tablecontent ("North East") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2017_ll') _tab %10.2f (`deceased_kt_2017_ul') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2018_ll') _tab %10.2f (`deceased_kt_2018_ul') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2019_ll') _tab %10.2f (`deceased_kt_2019_ul') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2020_ll') _tab %10.2f (`deceased_kt_2020_ul') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2021_ll') _tab %10.2f (`deceased_kt_2021_ul') _tab %10.2f (`deceased_kt_2022') _tab %10.2f (`deceased_kt_2022_ll') _tab %10.2f (`deceased_kt_2022_ul') _n
file write tablecontent ("North East") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2017_ll') _tab %10.2f (`cardio_kt_2017_ul') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2018_ll') _tab %10.2f (`cardio_kt_2018_ul') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2019_ll') _tab %10.2f (`cardio_kt_2019_ul') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2020_ll') _tab %10.2f (`cardio_kt_2020_ul') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2021_ll') _tab %10.2f (`cardio_kt_2021_ul') _tab %10.2f (`cardio_kt_2022') _tab %10.2f (`cardio_kt_2022_ll') _tab %10.2f (`cardio_kt_2022_ul') _n

**South East
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if region!=6
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

local year "2017 2021"

foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if region!=6

total weight if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = r(table)[1,1]
local kt_ckd4_`x'_ll = r(table)[5,1]
local kt_ckd4_`x'_ul = r(table)[6,1]
}

local year "2017 2018 2019 2021 2022"

foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if region!=6

total weight if ckd_group==4 & ckd_progression==4
local kt_dialysis_`x' = r(table)[1,1]
local kt_dialysis_`x'_ll = r(table)[5,1]
local kt_dialysis_`x'_ul = r(table)[6,1]
}

*Overall
file write tablecontent ("South East") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2017_ll') _tab %10.2f (`baseline_ckd_2017_ul') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2018_ll') _tab %10.2f (`baseline_ckd_2018_ul') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2019_ll') _tab %10.2f (`baseline_ckd_2019_ul') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2020_ll') _tab %10.2f (`baseline_ckd_2020_ul') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2021_ll') _tab %10.2f (`baseline_ckd_2021_ul') _tab %10.2f (`baseline_ckd_2022') _tab %10.2f (`baseline_ckd_2022_ll') _tab %10.2f (`baseline_ckd_2022_ul') _n
file write tablecontent ("South East") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2017_ll') _tab %10.2f (`none_ckd_2017_ul') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2018_ll') _tab %10.2f (`none_ckd_2018_ul') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2019_ll') _tab %10.2f (`none_ckd_2019_ul') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2020_ll') _tab %10.2f (`none_ckd_2020_ul') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2021_ll') _tab %10.2f (`none_ckd_2021_ul') _tab %10.2f (`none_ckd_2022') _tab %10.2f (`none_ckd_2022_ll') _tab %10.2f (`none_ckd_2022_ul') _n
file write tablecontent ("South East") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2017_ll') _tab %10.2f (`ckd3_ckd_2017_ul') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2018_ll') _tab %10.2f (`ckd3_ckd_2018_ul') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2019_ll') _tab %10.2f (`ckd3_ckd_2019_ul') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2020_ll') _tab %10.2f (`ckd3_ckd_2020_ul') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2021_ll') _tab %10.2f (`ckd3_ckd_2021_ul') _tab %10.2f (`ckd3_ckd_2022') _tab %10.2f (`ckd3_ckd_2022_ll') _tab %10.2f (`ckd3_ckd_2022_ul') _n
file write tablecontent ("South East") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2017_ll') _tab %10.2f (`ckd4_ckd_2017_ul') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2018_ll') _tab %10.2f (`ckd4_ckd_2018_ul') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2019_ll') _tab %10.2f (`ckd4_ckd_2019_ul') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2020_ll') _tab %10.2f (`ckd4_ckd_2020_ul') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2021_ll') _tab %10.2f (`ckd4_ckd_2021_ul') _tab %10.2f (`ckd4_ckd_2022') _tab %10.2f (`ckd4_ckd_2022_ll') _tab %10.2f (`ckd4_ckd_2022_ul') _n
file write tablecontent ("South East") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2017_ll') _tab %10.2f (`dialysis_ckd_2017_ul') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2018_ll') _tab %10.2f (`dialysis_ckd_2018_ul') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2019_ll') _tab %10.2f (`dialysis_ckd_2019_ul') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2020_ll') _tab %10.2f (`dialysis_ckd_2020_ul') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2021_ll') _tab %10.2f (`dialysis_ckd_2021_ul') _tab %10.2f (`dialysis_ckd_2022') _tab %10.2f (`dialysis_ckd_2022_ll') _tab %10.2f (`dialysis_ckd_2022_ul') _n
file write tablecontent ("South East") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2017_ll') _tab %10.2f (`kt_ckd_2017_ul') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2018_ll') _tab %10.2f (`kt_ckd_2018_ul') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2019_ll') _tab %10.2f (`kt_ckd_2019_ul') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2020_ll') _tab %10.2f (`kt_ckd_2020_ul') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2021_ll') _tab %10.2f (`kt_ckd_2021_ul') _tab %10.2f (`kt_ckd_2022') _tab %10.2f (`kt_ckd_2022_ll') _tab %10.2f (`kt_ckd_2022_ul') _n
file write tablecontent ("South East") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2017_ll') _tab %10.2f (`deceased_ckd_2017_ul') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2018_ll') _tab %10.2f (`deceased_ckd_2018_ul') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2019_ll') _tab %10.2f (`deceased_ckd_2019_ul') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2020_ll') _tab %10.2f (`deceased_ckd_2020_ul') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2021_ll') _tab %10.2f (`deceased_ckd_2021_ul') _tab %10.2f (`deceased_ckd_2022') _tab %10.2f (`deceased_ckd_2022_ll') _tab %10.2f (`deceased_ckd_2022_ul') _n
file write tablecontent ("South East") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2017_ll') _tab %10.2f (`cardio_ckd_2017_ul') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2018_ll') _tab %10.2f (`cardio_ckd_2018_ul') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2019_ll') _tab %10.2f (`cardio_ckd_2019_ul') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2020_ll') _tab %10.2f (`cardio_ckd_2020_ul') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2021_ll') _tab %10.2f (`cardio_ckd_2021_ul') _tab %10.2f (`cardio_ckd_2022') _tab %10.2f (`cardio_ckd_2022_ll') _tab %10.2f (`cardio_ckd_2022_ul') _n

*No CKD
file write tablecontent ("South East") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2017_ll') _tab %10.2f (`baseline_nockd_2017_ul') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2018_ll') _tab %10.2f (`baseline_nockd_2018_ul') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2019_ll') _tab %10.2f (`baseline_nockd_2019_ul') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2020_ll') _tab %10.2f (`baseline_nockd_2020_ul') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2021_ll') _tab %10.2f (`baseline_nockd_2021_ul') _tab %10.2f (`baseline_nockd_2022') _tab %10.2f (`baseline_nockd_2022_ll') _tab %10.2f (`baseline_nockd_2022_ul') _n
file write tablecontent ("South East") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2017_ll') _tab %10.2f (`none_nockd_2017_ul') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2018_ll') _tab %10.2f (`none_nockd_2018_ul') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2019_ll') _tab %10.2f (`none_nockd_2019_ul') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2020_ll') _tab %10.2f (`none_nockd_2020_ul') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2021_ll') _tab %10.2f (`none_nockd_2021_ul') _tab %10.2f (`none_nockd_2022') _tab %10.2f (`none_nockd_2022_ll') _tab %10.2f (`none_nockd_2022_ul') _n
file write tablecontent ("South East") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2017_ll') _tab %10.2f (`ckd3_nockd_2017_ul') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2018_ll') _tab %10.2f (`ckd3_nockd_2018_ul') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2019_ll') _tab %10.2f (`ckd3_nockd_2019_ul') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2020_ll') _tab %10.2f (`ckd3_nockd_2020_ul') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2021_ll') _tab %10.2f (`ckd3_nockd_2021_ul') _tab %10.2f (`ckd3_nockd_2022') _tab %10.2f (`ckd3_nockd_2022_ll') _tab %10.2f (`ckd3_nockd_2022_ul') _n
file write tablecontent ("South East") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2017_ll') _tab %10.2f (`ckd4_nockd_2017_ul') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2018_ll') _tab %10.2f (`ckd4_nockd_2018_ul') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2019_ll') _tab %10.2f (`ckd4_nockd_2019_ul') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2020_ll') _tab %10.2f (`ckd4_nockd_2020_ul') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2021_ll') _tab %10.2f (`ckd4_nockd_2021_ul') _tab %10.2f (`ckd4_nockd_2022') _tab %10.2f (`ckd4_nockd_2022_ll') _tab %10.2f (`ckd4_nockd_2022_ul') _n
file write tablecontent ("South East") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2017_ll') _tab %10.2f (`dialysis_nockd_2017_ul') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2018_ll') _tab %10.2f (`dialysis_nockd_2018_ul') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2019_ll') _tab %10.2f (`dialysis_nockd_2019_ul') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2020_ll') _tab %10.2f (`dialysis_nockd_2020_ul') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2021_ll') _tab %10.2f (`dialysis_nockd_2021_ul') _tab %10.2f (`dialysis_nockd_2022') _tab %10.2f (`dialysis_nockd_2022_ll') _tab %10.2f (`dialysis_nockd_2022_ul') _n
file write tablecontent ("South East") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("South East") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("South East") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("South East") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("South East") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("South East") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
file write tablecontent ("South East") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2017_ll') _tab %10.2f (`deceased_ckd3_2017_ul') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2018_ll') _tab %10.2f (`deceased_ckd3_2018_ul') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2019_ll') _tab %10.2f (`deceased_ckd3_2019_ul') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2020_ll') _tab %10.2f (`deceased_ckd3_2020_ul') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2021_ll') _tab %10.2f (`deceased_ckd3_2021_ul') _tab %10.2f (`deceased_ckd3_2022') _tab %10.2f (`deceased_ckd3_2022_ll') _tab %10.2f (`deceased_ckd3_2022_ul') _n
file write tablecontent ("South East") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2017_ll') _tab %10.2f (`cardio_ckd3_2017_ul') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2018_ll') _tab %10.2f (`cardio_ckd3_2018_ul') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2019_ll') _tab %10.2f (`cardio_ckd3_2019_ul') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2020_ll') _tab %10.2f (`cardio_ckd3_2020_ul') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2021_ll') _tab %10.2f (`cardio_ckd3_2021_ul') _tab %10.2f (`cardio_ckd3_2022') _tab %10.2f (`cardio_ckd3_2022_ll') _tab %10.2f (`cardio_ckd3_2022_ul') _n

*CKD stage 4/5 without RRT
file write tablecontent ("South East") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2017_ll') _tab %10.2f (`baseline_ckd4_2017_ul') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2018_ll') _tab %10.2f (`baseline_ckd4_2018_ul') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2019_ll') _tab %10.2f (`baseline_ckd4_2019_ul') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2020_ll') _tab %10.2f (`baseline_ckd4_2020_ul') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2021_ll') _tab %10.2f (`baseline_ckd4_2021_ul') _tab %10.2f (`baseline_ckd4_2022') _tab %10.2f (`baseline_ckd4_2022_ll') _tab %10.2f (`baseline_ckd4_2022_ul') _n
file write tablecontent ("South East") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2017_ll') _tab %10.2f (`none_ckd4_2017_ul') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2018_ll') _tab %10.2f (`none_ckd4_2018_ul') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2019_ll') _tab %10.2f (`none_ckd4_2019_ul') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2020_ll') _tab %10.2f (`none_ckd4_2020_ul') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2021_ll') _tab %10.2f (`none_ckd4_2021_ul') _tab %10.2f (`none_ckd4_2022') _tab %10.2f (`none_ckd4_2022_ll') _tab %10.2f (`none_ckd4_2022_ul') _n
file write tablecontent ("South East") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2017_ll') _tab %10.2f (`dialysis_ckd4_2017_ul') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2018_ll') _tab %10.2f (`dialysis_ckd4_2018_ul') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2019_ll') _tab %10.2f (`dialysis_ckd4_2019_ul') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2020_ll') _tab %10.2f (`dialysis_ckd4_2020_ul') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2021_ll') _tab %10.2f (`dialysis_ckd4_2021_ul') _tab %10.2f (`dialysis_ckd4_2022') _tab %10.2f (`dialysis_ckd4_2022_ll') _tab %10.2f (`dialysis_ckd4_2022_ul') _n
file write tablecontent ("South East") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2017_ll') _tab %10.2f (`kt_ckd4_2017_ul') _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2021_ll') _tab %10.2f (`kt_ckd4_2021_ul') _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _n
file write tablecontent ("South East") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2017_ll') _tab %10.2f (`deceased_ckd4_2017_ul') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2018_ll') _tab %10.2f (`deceased_ckd4_2018_ul') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2019_ll') _tab %10.2f (`deceased_ckd4_2019_ul') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2020_ll') _tab %10.2f (`deceased_ckd4_2020_ul') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2021_ll') _tab %10.2f (`deceased_ckd4_2021_ul') _tab %10.2f (`deceased_ckd4_2022') _tab %10.2f (`deceased_ckd4_2022_ll') _tab %10.2f (`deceased_ckd4_2022_ul') _n
file write tablecontent ("South East") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2017_ll') _tab %10.2f (`cardio_ckd4_2017_ul') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2018_ll') _tab %10.2f (`cardio_ckd4_2018_ul') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2019_ll') _tab %10.2f (`cardio_ckd4_2019_ul') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2020_ll') _tab %10.2f (`cardio_ckd4_2020_ul') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2021_ll') _tab %10.2f (`cardio_ckd4_2021_ul') _tab %10.2f (`cardio_ckd4_2022') _tab %10.2f (`cardio_ckd4_2022_ll') _tab %10.2f (`cardio_ckd4_2022_ul') _n

*Dialysis
file write tablecontent ("South East") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2017_ll') _tab %10.2f (`baseline_dialysis_2017_ul') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2018_ll') _tab %10.2f (`baseline_dialysis_2018_ul') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2019_ll') _tab %10.2f (`baseline_dialysis_2019_ul') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2020_ll') _tab %10.2f (`baseline_dialysis_2020_ul') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2021_ll') _tab %10.2f (`baseline_dialysis_2021_ul') _tab %10.2f (`baseline_dialysis_2022') _tab %10.2f (`baseline_dialysis_2022_ll') _tab %10.2f (`baseline_dialysis_2022_ul') _n
file write tablecontent ("South East") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2017_ll') _tab %10.2f (`none_dialysis_2017_ul') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2018_ll') _tab %10.2f (`none_dialysis_2018_ul') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2019_ll') _tab %10.2f (`none_dialysis_2019_ul') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2020_ll') _tab %10.2f (`none_dialysis_2020_ul') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2021_ll') _tab %10.2f (`none_dialysis_2021_ul') _tab %10.2f (`none_dialysis_2022') _tab %10.2f (`none_dialysis_2022_ll') _tab %10.2f (`none_dialysis_2022_ul') _n
file write tablecontent ("South East") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2017_ll') _tab %10.2f (`kt_dialysis_2017_ul') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2018_ll') _tab %10.2f (`kt_dialysis_2018_ul') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2019_ll') _tab %10.2f (`kt_dialysis_2019_ul') _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2021_ll') _tab %10.2f (`kt_dialysis_2021_ul') _tab %10.2f (`kt_dialysis_2022') _tab %10.2f (`kt_dialysis_2022_ll') _tab %10.2f (`kt_dialysis_2022_ul') _n
file write tablecontent ("South East") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2017_ll') _tab %10.2f (`deceased_dialysis_2017_ul') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2018_ll') _tab %10.2f (`deceased_dialysis_2018_ul') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2019_ll') _tab %10.2f (`deceased_dialysis_2019_ul') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2020_ll') _tab %10.2f (`deceased_dialysis_2020_ul') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2021_ll') _tab %10.2f (`deceased_dialysis_2021_ul') _tab %10.2f (`deceased_dialysis_2022') _tab %10.2f (`deceased_dialysis_2022_ll') _tab %10.2f (`deceased_dialysis_2022_ul') _n
file write tablecontent ("South East") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2017_ll') _tab %10.2f (`cardio_dialysis_2017_ul') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2018_ll') _tab %10.2f (`cardio_dialysis_2018_ul') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2019_ll') _tab %10.2f (`cardio_dialysis_2019_ul') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2020_ll') _tab %10.2f (`cardio_dialysis_2020_ul') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2021_ll') _tab %10.2f (`cardio_dialysis_2021_ul') _tab %10.2f (`cardio_dialysis_2022') _tab %10.2f (`cardio_dialysis_2022_ll') _tab %10.2f (`cardio_dialysis_2022_ul') _n

*Kidney transplant
file write tablecontent ("South East") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2017_ll') _tab %10.2f (`baseline_kt_2017_ul') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2018_ll') _tab %10.2f (`baseline_kt_2018_ul') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2019_ll') _tab %10.2f (`baseline_kt_2019_ul') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2020_ll') _tab %10.2f (`baseline_kt_2020_ul') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2021_ll') _tab %10.2f (`baseline_kt_2021_ul') _tab %10.2f (`baseline_kt_2022') _tab %10.2f (`baseline_kt_2022_ll') _tab %10.2f (`baseline_kt_2022_ul') _n
file write tablecontent ("South East") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2017_ll') _tab %10.2f (`none_kt_2017_ul') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2018_ll') _tab %10.2f (`none_kt_2018_ul') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2019_ll') _tab %10.2f (`none_kt_2019_ul') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2020_ll') _tab %10.2f (`none_kt_2020_ul') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2021_ll') _tab %10.2f (`none_kt_2021_ul') _tab %10.2f (`none_kt_2022') _tab %10.2f (`none_kt_2022_ll') _tab %10.2f (`none_kt_2022_ul') _n
file write tablecontent ("South East") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2017_ll') _tab %10.2f (`dialysis_kt_2017_ul') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2018_ll') _tab %10.2f (`dialysis_kt_2018_ul') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2019_ll') _tab %10.2f (`dialysis_kt_2019_ul') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2020_ll') _tab %10.2f (`dialysis_kt_2020_ul') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2021_ll') _tab %10.2f (`dialysis_kt_2021_ul') _tab %10.2f (`dialysis_kt_2022') _tab %10.2f (`dialysis_kt_2022_ll') _tab %10.2f (`dialysis_kt_2022_ul') _n
file write tablecontent ("South East") _tab ("Transplant") _tab ("Deceased") _tab %10.2f (`deceased_kt_2017') _tab %10.2f (`deceased_kt_2017_ll') _tab %10.2f (`deceased_kt_2017_ul') _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2018_ll') _tab %10.2f (`deceased_kt_2018_ul') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2019_ll') _tab %10.2f (`deceased_kt_2019_ul') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2020_ll') _tab %10.2f (`deceased_kt_2020_ul') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2021_ll') _tab %10.2f (`deceased_kt_2021_ul') _tab %10.2f (`deceased_kt_2022') _tab %10.2f (`deceased_kt_2022_ll') _tab %10.2f (`deceased_kt_2022_ul') _n
file write tablecontent ("South East") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2017_ll') _tab %10.2f (`cardio_kt_2017_ul') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2018_ll') _tab %10.2f (`cardio_kt_2018_ul') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2019_ll') _tab %10.2f (`cardio_kt_2019_ul') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2020_ll') _tab %10.2f (`cardio_kt_2020_ul') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2021_ll') _tab %10.2f (`cardio_kt_2021_ul') _tab %10.2f (`cardio_kt_2022') _tab %10.2f (`cardio_kt_2022_ll') _tab %10.2f (`cardio_kt_2022_ul') _n


**West Midlands
local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if region!=8
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

total weight if cardiovascular==1 & ckd_group==5
local cardio_kt_`x' = r(table)[1,1]
local cardio_kt_`x'_ll = r(table)[5,1]
local cardio_kt_`x'_ul = r(table)[6,1]
}

local year "2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
drop if region!=8

total weight if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = r(table)[1,1]
local deceased_kt_`x'_ll = r(table)[5,1]
local deceased_kt_`x'_ul = r(table)[6,1]
}

*Overall
file write tablecontent ("West Midlands") _tab ("Overall") _tab ("N/A") _tab %10.2f (`baseline_ckd_2017') _tab %10.2f (`baseline_ckd_2017_ll') _tab %10.2f (`baseline_ckd_2017_ul') _tab %10.2f (`baseline_ckd_2018') _tab %10.2f (`baseline_ckd_2018_ll') _tab %10.2f (`baseline_ckd_2018_ul') _tab %10.2f (`baseline_ckd_2019') _tab %10.2f (`baseline_ckd_2019_ll') _tab %10.2f (`baseline_ckd_2019_ul') _tab %10.2f (`baseline_ckd_2020') _tab %10.2f (`baseline_ckd_2020_ll') _tab %10.2f (`baseline_ckd_2020_ul') _tab %10.2f (`baseline_ckd_2021') _tab %10.2f (`baseline_ckd_2021_ll') _tab %10.2f (`baseline_ckd_2021_ul') _tab %10.2f (`baseline_ckd_2022') _tab %10.2f (`baseline_ckd_2022_ll') _tab %10.2f (`baseline_ckd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Overall") _tab ("No progression") _tab %10.2f (`none_ckd_2017') _tab %10.2f (`none_ckd_2017_ll') _tab %10.2f (`none_ckd_2017_ul') _tab %10.2f (`none_ckd_2018') _tab %10.2f (`none_ckd_2018_ll') _tab %10.2f (`none_ckd_2018_ul') _tab %10.2f (`none_ckd_2019') _tab %10.2f (`none_ckd_2019_ll') _tab %10.2f (`none_ckd_2019_ul') _tab %10.2f (`none_ckd_2020') _tab %10.2f (`none_ckd_2020_ll') _tab %10.2f (`none_ckd_2020_ul') _tab %10.2f (`none_ckd_2021') _tab %10.2f (`none_ckd_2021_ll') _tab %10.2f (`none_ckd_2021_ul') _tab %10.2f (`none_ckd_2022') _tab %10.2f (`none_ckd_2022_ll') _tab %10.2f (`none_ckd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Overall") _tab ("CKD stage 3") _tab %10.2f (`ckd3_ckd_2017') _tab %10.2f (`ckd3_ckd_2017_ll') _tab %10.2f (`ckd3_ckd_2017_ul') _tab %10.2f (`ckd3_ckd_2018') _tab %10.2f (`ckd3_ckd_2018_ll') _tab %10.2f (`ckd3_ckd_2018_ul') _tab %10.2f (`ckd3_ckd_2019') _tab %10.2f (`ckd3_ckd_2019_ll') _tab %10.2f (`ckd3_ckd_2019_ul') _tab %10.2f (`ckd3_ckd_2020') _tab %10.2f (`ckd3_ckd_2020_ll') _tab %10.2f (`ckd3_ckd_2020_ul') _tab %10.2f (`ckd3_ckd_2021') _tab %10.2f (`ckd3_ckd_2021_ll') _tab %10.2f (`ckd3_ckd_2021_ul') _tab %10.2f (`ckd3_ckd_2022') _tab %10.2f (`ckd3_ckd_2022_ll') _tab %10.2f (`ckd3_ckd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Overall") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd_2017') _tab %10.2f (`ckd4_ckd_2017_ll') _tab %10.2f (`ckd4_ckd_2017_ul') _tab %10.2f (`ckd4_ckd_2018') _tab %10.2f (`ckd4_ckd_2018_ll') _tab %10.2f (`ckd4_ckd_2018_ul') _tab %10.2f (`ckd4_ckd_2019') _tab %10.2f (`ckd4_ckd_2019_ll') _tab %10.2f (`ckd4_ckd_2019_ul') _tab %10.2f (`ckd4_ckd_2020') _tab %10.2f (`ckd4_ckd_2020_ll') _tab %10.2f (`ckd4_ckd_2020_ul') _tab %10.2f (`ckd4_ckd_2021') _tab %10.2f (`ckd4_ckd_2021_ll') _tab %10.2f (`ckd4_ckd_2021_ul') _tab %10.2f (`ckd4_ckd_2022') _tab %10.2f (`ckd4_ckd_2022_ll') _tab %10.2f (`ckd4_ckd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Overall") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd_2017') _tab %10.2f (`dialysis_ckd_2017_ll') _tab %10.2f (`dialysis_ckd_2017_ul') _tab %10.2f (`dialysis_ckd_2018') _tab %10.2f (`dialysis_ckd_2018_ll') _tab %10.2f (`dialysis_ckd_2018_ul') _tab %10.2f (`dialysis_ckd_2019') _tab %10.2f (`dialysis_ckd_2019_ll') _tab %10.2f (`dialysis_ckd_2019_ul') _tab %10.2f (`dialysis_ckd_2020') _tab %10.2f (`dialysis_ckd_2020_ll') _tab %10.2f (`dialysis_ckd_2020_ul') _tab %10.2f (`dialysis_ckd_2021') _tab %10.2f (`dialysis_ckd_2021_ll') _tab %10.2f (`dialysis_ckd_2021_ul') _tab %10.2f (`dialysis_ckd_2022') _tab %10.2f (`dialysis_ckd_2022_ll') _tab %10.2f (`dialysis_ckd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Overall") _tab ("Transplant") _tab %10.2f (`kt_ckd_2017') _tab %10.2f (`kt_ckd_2017_ll') _tab %10.2f (`kt_ckd_2017_ul') _tab %10.2f (`kt_ckd_2018') _tab %10.2f (`kt_ckd_2018_ll') _tab %10.2f (`kt_ckd_2018_ul') _tab %10.2f (`kt_ckd_2019') _tab %10.2f (`kt_ckd_2019_ll') _tab %10.2f (`kt_ckd_2019_ul') _tab %10.2f (`kt_ckd_2020') _tab %10.2f (`kt_ckd_2020_ll') _tab %10.2f (`kt_ckd_2020_ul') _tab %10.2f (`kt_ckd_2021') _tab %10.2f (`kt_ckd_2021_ll') _tab %10.2f (`kt_ckd_2021_ul') _tab %10.2f (`kt_ckd_2022') _tab %10.2f (`kt_ckd_2022_ll') _tab %10.2f (`kt_ckd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Overall") _tab ("Deceased") _tab %10.2f (`deceased_ckd_2017') _tab %10.2f (`deceased_ckd_2017_ll') _tab %10.2f (`deceased_ckd_2017_ul') _tab %10.2f (`deceased_ckd_2018') _tab %10.2f (`deceased_ckd_2018_ll') _tab %10.2f (`deceased_ckd_2018_ul') _tab %10.2f (`deceased_ckd_2019') _tab %10.2f (`deceased_ckd_2019_ll') _tab %10.2f (`deceased_ckd_2019_ul') _tab %10.2f (`deceased_ckd_2020') _tab %10.2f (`deceased_ckd_2020_ll') _tab %10.2f (`deceased_ckd_2020_ul') _tab %10.2f (`deceased_ckd_2021') _tab %10.2f (`deceased_ckd_2021_ll') _tab %10.2f (`deceased_ckd_2021_ul') _tab %10.2f (`deceased_ckd_2022') _tab %10.2f (`deceased_ckd_2022_ll') _tab %10.2f (`deceased_ckd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Overall") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd_2017') _tab %10.2f (`cardio_ckd_2017_ll') _tab %10.2f (`cardio_ckd_2017_ul') _tab %10.2f (`cardio_ckd_2018') _tab %10.2f (`cardio_ckd_2018_ll') _tab %10.2f (`cardio_ckd_2018_ul') _tab %10.2f (`cardio_ckd_2019') _tab %10.2f (`cardio_ckd_2019_ll') _tab %10.2f (`cardio_ckd_2019_ul') _tab %10.2f (`cardio_ckd_2020') _tab %10.2f (`cardio_ckd_2020_ll') _tab %10.2f (`cardio_ckd_2020_ul') _tab %10.2f (`cardio_ckd_2021') _tab %10.2f (`cardio_ckd_2021_ll') _tab %10.2f (`cardio_ckd_2021_ul') _tab %10.2f (`cardio_ckd_2022') _tab %10.2f (`cardio_ckd_2022_ll') _tab %10.2f (`cardio_ckd_2022_ul') _n

*No CKD
file write tablecontent ("West Midlands") _tab ("No CKD") _tab ("N/A") _tab %10.2f (`baseline_nockd_2017') _tab %10.2f (`baseline_nockd_2017_ll') _tab %10.2f (`baseline_nockd_2017_ul') _tab %10.2f (`baseline_nockd_2018') _tab %10.2f (`baseline_nockd_2018_ll') _tab %10.2f (`baseline_nockd_2018_ul') _tab %10.2f (`baseline_nockd_2019') _tab %10.2f (`baseline_nockd_2019_ll') _tab %10.2f (`baseline_nockd_2019_ul') _tab %10.2f (`baseline_nockd_2020') _tab %10.2f (`baseline_nockd_2020_ll') _tab %10.2f (`baseline_nockd_2020_ul') _tab %10.2f (`baseline_nockd_2021') _tab %10.2f (`baseline_nockd_2021_ll') _tab %10.2f (`baseline_nockd_2021_ul') _tab %10.2f (`baseline_nockd_2022') _tab %10.2f (`baseline_nockd_2022_ll') _tab %10.2f (`baseline_nockd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("No CKD") _tab ("No progression") _tab %10.2f (`none_nockd_2017') _tab %10.2f (`none_nockd_2017_ll') _tab %10.2f (`none_nockd_2017_ul') _tab %10.2f (`none_nockd_2018') _tab %10.2f (`none_nockd_2018_ll') _tab %10.2f (`none_nockd_2018_ul') _tab %10.2f (`none_nockd_2019') _tab %10.2f (`none_nockd_2019_ll') _tab %10.2f (`none_nockd_2019_ul') _tab %10.2f (`none_nockd_2020') _tab %10.2f (`none_nockd_2020_ll') _tab %10.2f (`none_nockd_2020_ul') _tab %10.2f (`none_nockd_2021') _tab %10.2f (`none_nockd_2021_ll') _tab %10.2f (`none_nockd_2021_ul') _tab %10.2f (`none_nockd_2022') _tab %10.2f (`none_nockd_2022_ll') _tab %10.2f (`none_nockd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("No CKD") _tab ("CKD stage 3") _tab %10.2f (`ckd3_nockd_2017') _tab %10.2f (`ckd3_nockd_2017_ll') _tab %10.2f (`ckd3_nockd_2017_ul') _tab %10.2f (`ckd3_nockd_2018') _tab %10.2f (`ckd3_nockd_2018_ll') _tab %10.2f (`ckd3_nockd_2018_ul') _tab %10.2f (`ckd3_nockd_2019') _tab %10.2f (`ckd3_nockd_2019_ll') _tab %10.2f (`ckd3_nockd_2019_ul') _tab %10.2f (`ckd3_nockd_2020') _tab %10.2f (`ckd3_nockd_2020_ll') _tab %10.2f (`ckd3_nockd_2020_ul') _tab %10.2f (`ckd3_nockd_2021') _tab %10.2f (`ckd3_nockd_2021_ll') _tab %10.2f (`ckd3_nockd_2021_ul') _tab %10.2f (`ckd3_nockd_2022') _tab %10.2f (`ckd3_nockd_2022_ll') _tab %10.2f (`ckd3_nockd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("No CKD") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_nockd_2017') _tab %10.2f (`ckd4_nockd_2017_ll') _tab %10.2f (`ckd4_nockd_2017_ul') _tab %10.2f (`ckd4_nockd_2018') _tab %10.2f (`ckd4_nockd_2018_ll') _tab %10.2f (`ckd4_nockd_2018_ul') _tab %10.2f (`ckd4_nockd_2019') _tab %10.2f (`ckd4_nockd_2019_ll') _tab %10.2f (`ckd4_nockd_2019_ul') _tab %10.2f (`ckd4_nockd_2020') _tab %10.2f (`ckd4_nockd_2020_ll') _tab %10.2f (`ckd4_nockd_2020_ul') _tab %10.2f (`ckd4_nockd_2021') _tab %10.2f (`ckd4_nockd_2021_ll') _tab %10.2f (`ckd4_nockd_2021_ul') _tab %10.2f (`ckd4_nockd_2022') _tab %10.2f (`ckd4_nockd_2022_ll') _tab %10.2f (`ckd4_nockd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("No CKD") _tab ("Dialysis") _tab %10.2f (`dialysis_nockd_2017') _tab %10.2f (`dialysis_nockd_2017_ll') _tab %10.2f (`dialysis_nockd_2017_ul') _tab %10.2f (`dialysis_nockd_2018') _tab %10.2f (`dialysis_nockd_2018_ll') _tab %10.2f (`dialysis_nockd_2018_ul') _tab %10.2f (`dialysis_nockd_2019') _tab %10.2f (`dialysis_nockd_2019_ll') _tab %10.2f (`dialysis_nockd_2019_ul') _tab %10.2f (`dialysis_nockd_2020') _tab %10.2f (`dialysis_nockd_2020_ll') _tab %10.2f (`dialysis_nockd_2020_ul') _tab %10.2f (`dialysis_nockd_2021') _tab %10.2f (`dialysis_nockd_2021_ll') _tab %10.2f (`dialysis_nockd_2021_ul') _tab %10.2f (`dialysis_nockd_2022') _tab %10.2f (`dialysis_nockd_2022_ll') _tab %10.2f (`dialysis_nockd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("West Midlands") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 3") _tab ("Deceased") _tab %10.2f (`deceased_ckd3_2017') _tab %10.2f (`deceased_ckd3_2017_ll') _tab %10.2f (`deceased_ckd3_2017_ul') _tab %10.2f (`deceased_ckd3_2018') _tab %10.2f (`deceased_ckd3_2018_ll') _tab %10.2f (`deceased_ckd3_2018_ul') _tab %10.2f (`deceased_ckd3_2019') _tab %10.2f (`deceased_ckd3_2019_ll') _tab %10.2f (`deceased_ckd3_2019_ul') _tab %10.2f (`deceased_ckd3_2020') _tab %10.2f (`deceased_ckd3_2020_ll') _tab %10.2f (`deceased_ckd3_2020_ul') _tab %10.2f (`deceased_ckd3_2021') _tab %10.2f (`deceased_ckd3_2021_ll') _tab %10.2f (`deceased_ckd3_2021_ul') _tab %10.2f (`deceased_ckd3_2022') _tab %10.2f (`deceased_ckd3_2022_ll') _tab %10.2f (`deceased_ckd3_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 3") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd3_2017') _tab %10.2f (`cardio_ckd3_2017_ll') _tab %10.2f (`cardio_ckd3_2017_ul') _tab %10.2f (`cardio_ckd3_2018') _tab %10.2f (`cardio_ckd3_2018_ll') _tab %10.2f (`cardio_ckd3_2018_ul') _tab %10.2f (`cardio_ckd3_2019') _tab %10.2f (`cardio_ckd3_2019_ll') _tab %10.2f (`cardio_ckd3_2019_ul') _tab %10.2f (`cardio_ckd3_2020') _tab %10.2f (`cardio_ckd3_2020_ll') _tab %10.2f (`cardio_ckd3_2020_ul') _tab %10.2f (`cardio_ckd3_2021') _tab %10.2f (`cardio_ckd3_2021_ll') _tab %10.2f (`cardio_ckd3_2021_ul') _tab %10.2f (`cardio_ckd3_2022') _tab %10.2f (`cardio_ckd3_2022_ll') _tab %10.2f (`cardio_ckd3_2022_ul') _n

*CKD stage 4/5 without RRT
file write tablecontent ("West Midlands") _tab ("CKD stage 4/5") _tab ("N/A") _tab %10.2f (`baseline_ckd4_2017') _tab %10.2f (`baseline_ckd4_2017_ll') _tab %10.2f (`baseline_ckd4_2017_ul') _tab %10.2f (`baseline_ckd4_2018') _tab %10.2f (`baseline_ckd4_2018_ll') _tab %10.2f (`baseline_ckd4_2018_ul') _tab %10.2f (`baseline_ckd4_2019') _tab %10.2f (`baseline_ckd4_2019_ll') _tab %10.2f (`baseline_ckd4_2019_ul') _tab %10.2f (`baseline_ckd4_2020') _tab %10.2f (`baseline_ckd4_2020_ll') _tab %10.2f (`baseline_ckd4_2020_ul') _tab %10.2f (`baseline_ckd4_2021') _tab %10.2f (`baseline_ckd4_2021_ll') _tab %10.2f (`baseline_ckd4_2021_ul') _tab %10.2f (`baseline_ckd4_2022') _tab %10.2f (`baseline_ckd4_2022_ll') _tab %10.2f (`baseline_ckd4_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 4/5") _tab ("No progression") _tab %10.2f (`none_ckd4_2017') _tab %10.2f (`none_ckd4_2017_ll') _tab %10.2f (`none_ckd4_2017_ul') _tab %10.2f (`none_ckd4_2018') _tab %10.2f (`none_ckd4_2018_ll') _tab %10.2f (`none_ckd4_2018_ul') _tab %10.2f (`none_ckd4_2019') _tab %10.2f (`none_ckd4_2019_ll') _tab %10.2f (`none_ckd4_2019_ul') _tab %10.2f (`none_ckd4_2020') _tab %10.2f (`none_ckd4_2020_ll') _tab %10.2f (`none_ckd4_2020_ul') _tab %10.2f (`none_ckd4_2021') _tab %10.2f (`none_ckd4_2021_ll') _tab %10.2f (`none_ckd4_2021_ul') _tab %10.2f (`none_ckd4_2022') _tab %10.2f (`none_ckd4_2022_ll') _tab %10.2f (`none_ckd4_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 4/5") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd4_2017') _tab %10.2f (`dialysis_ckd4_2017_ll') _tab %10.2f (`dialysis_ckd4_2017_ul') _tab %10.2f (`dialysis_ckd4_2018') _tab %10.2f (`dialysis_ckd4_2018_ll') _tab %10.2f (`dialysis_ckd4_2018_ul') _tab %10.2f (`dialysis_ckd4_2019') _tab %10.2f (`dialysis_ckd4_2019_ll') _tab %10.2f (`dialysis_ckd4_2019_ul') _tab %10.2f (`dialysis_ckd4_2020') _tab %10.2f (`dialysis_ckd4_2020_ll') _tab %10.2f (`dialysis_ckd4_2020_ul') _tab %10.2f (`dialysis_ckd4_2021') _tab %10.2f (`dialysis_ckd4_2021_ll') _tab %10.2f (`dialysis_ckd4_2021_ul') _tab %10.2f (`dialysis_ckd4_2022') _tab %10.2f (`dialysis_ckd4_2022_ll') _tab %10.2f (`dialysis_ckd4_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 4/5") _tab ("Transplant") _tab %10.2f (`kt_ckd4_2017') _tab %10.2f (`kt_ckd4_2017_ll') _tab %10.2f (`kt_ckd4_2017_ul') _tab %10.2f (`kt_ckd4_2018') _tab %10.2f (`kt_ckd4_2018_ll') _tab %10.2f (`kt_ckd4_2018_ul') _tab %10.2f (`kt_ckd4_2019') _tab %10.2f (`kt_ckd4_2019_ll') _tab %10.2f (`kt_ckd4_2019_ul') _tab %10.2f (`kt_ckd4_2020') _tab %10.2f (`kt_ckd4_2020_ll') _tab %10.2f (`kt_ckd4_2020_ul') _tab %10.2f (`kt_ckd4_2021') _tab %10.2f (`kt_ckd4_2021_ll') _tab %10.2f (`kt_ckd4_2021_ul') _tab %10.2f (`kt_ckd4_2022') _tab %10.2f (`kt_ckd4_2022_ll') _tab %10.2f (`kt_ckd4_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 4/5") _tab ("Deceased") _tab %10.2f (`deceased_ckd4_2017') _tab %10.2f (`deceased_ckd4_2017_ll') _tab %10.2f (`deceased_ckd4_2017_ul') _tab %10.2f (`deceased_ckd4_2018') _tab %10.2f (`deceased_ckd4_2018_ll') _tab %10.2f (`deceased_ckd4_2018_ul') _tab %10.2f (`deceased_ckd4_2019') _tab %10.2f (`deceased_ckd4_2019_ll') _tab %10.2f (`deceased_ckd4_2019_ul') _tab %10.2f (`deceased_ckd4_2020') _tab %10.2f (`deceased_ckd4_2020_ll') _tab %10.2f (`deceased_ckd4_2020_ul') _tab %10.2f (`deceased_ckd4_2021') _tab %10.2f (`deceased_ckd4_2021_ll') _tab %10.2f (`deceased_ckd4_2021_ul') _tab %10.2f (`deceased_ckd4_2022') _tab %10.2f (`deceased_ckd4_2022_ll') _tab %10.2f (`deceased_ckd4_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("CKD stage 4/5") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_ckd4_2017') _tab %10.2f (`cardio_ckd4_2017_ll') _tab %10.2f (`cardio_ckd4_2017_ul') _tab %10.2f (`cardio_ckd4_2018') _tab %10.2f (`cardio_ckd4_2018_ll') _tab %10.2f (`cardio_ckd4_2018_ul') _tab %10.2f (`cardio_ckd4_2019') _tab %10.2f (`cardio_ckd4_2019_ll') _tab %10.2f (`cardio_ckd4_2019_ul') _tab %10.2f (`cardio_ckd4_2020') _tab %10.2f (`cardio_ckd4_2020_ll') _tab %10.2f (`cardio_ckd4_2020_ul') _tab %10.2f (`cardio_ckd4_2021') _tab %10.2f (`cardio_ckd4_2021_ll') _tab %10.2f (`cardio_ckd4_2021_ul') _tab %10.2f (`cardio_ckd4_2022') _tab %10.2f (`cardio_ckd4_2022_ll') _tab %10.2f (`cardio_ckd4_2022_ul') _n

*Dialysis
file write tablecontent ("West Midlands") _tab ("Dialysis") _tab ("N/A") _tab %10.2f (`baseline_dialysis_2017') _tab %10.2f (`baseline_dialysis_2017_ll') _tab %10.2f (`baseline_dialysis_2017_ul') _tab %10.2f (`baseline_dialysis_2018') _tab %10.2f (`baseline_dialysis_2018_ll') _tab %10.2f (`baseline_dialysis_2018_ul') _tab %10.2f (`baseline_dialysis_2019') _tab %10.2f (`baseline_dialysis_2019_ll') _tab %10.2f (`baseline_dialysis_2019_ul') _tab %10.2f (`baseline_dialysis_2020') _tab %10.2f (`baseline_dialysis_2020_ll') _tab %10.2f (`baseline_dialysis_2020_ul') _tab %10.2f (`baseline_dialysis_2021') _tab %10.2f (`baseline_dialysis_2021_ll') _tab %10.2f (`baseline_dialysis_2021_ul') _tab %10.2f (`baseline_dialysis_2022') _tab %10.2f (`baseline_dialysis_2022_ll') _tab %10.2f (`baseline_dialysis_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Dialysis") _tab ("No progression") _tab %10.2f (`none_dialysis_2017') _tab %10.2f (`none_dialysis_2017_ll') _tab %10.2f (`none_dialysis_2017_ul') _tab %10.2f (`none_dialysis_2018') _tab %10.2f (`none_dialysis_2018_ll') _tab %10.2f (`none_dialysis_2018_ul') _tab %10.2f (`none_dialysis_2019') _tab %10.2f (`none_dialysis_2019_ll') _tab %10.2f (`none_dialysis_2019_ul') _tab %10.2f (`none_dialysis_2020') _tab %10.2f (`none_dialysis_2020_ll') _tab %10.2f (`none_dialysis_2020_ul') _tab %10.2f (`none_dialysis_2021') _tab %10.2f (`none_dialysis_2021_ll') _tab %10.2f (`none_dialysis_2021_ul') _tab %10.2f (`none_dialysis_2022') _tab %10.2f (`none_dialysis_2022_ll') _tab %10.2f (`none_dialysis_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Dialysis") _tab ("Transplant") _tab %10.2f (`kt_dialysis_2017') _tab %10.2f (`kt_dialysis_2017_ll') _tab %10.2f (`kt_dialysis_2017_ul') _tab %10.2f (`kt_dialysis_2018') _tab %10.2f (`kt_dialysis_2018_ll') _tab %10.2f (`kt_dialysis_2018_ul') _tab %10.2f (`kt_dialysis_2019') _tab %10.2f (`kt_dialysis_2019_ll') _tab %10.2f (`kt_dialysis_2019_ul') _tab %10.2f (`kt_dialysis_2020') _tab %10.2f (`kt_dialysis_2020_ll') _tab %10.2f (`kt_dialysis_2020_ul') _tab %10.2f (`kt_dialysis_2021') _tab %10.2f (`kt_dialysis_2021_ll') _tab %10.2f (`kt_dialysis_2021_ul') _tab %10.2f (`kt_dialysis_2022') _tab %10.2f (`kt_dialysis_2022_ll') _tab %10.2f (`kt_dialysis_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Dialysis") _tab ("Deceased") _tab %10.2f (`deceased_dialysis_2017') _tab %10.2f (`deceased_dialysis_2017_ll') _tab %10.2f (`deceased_dialysis_2017_ul') _tab %10.2f (`deceased_dialysis_2018') _tab %10.2f (`deceased_dialysis_2018_ll') _tab %10.2f (`deceased_dialysis_2018_ul') _tab %10.2f (`deceased_dialysis_2019') _tab %10.2f (`deceased_dialysis_2019_ll') _tab %10.2f (`deceased_dialysis_2019_ul') _tab %10.2f (`deceased_dialysis_2020') _tab %10.2f (`deceased_dialysis_2020_ll') _tab %10.2f (`deceased_dialysis_2020_ul') _tab %10.2f (`deceased_dialysis_2021') _tab %10.2f (`deceased_dialysis_2021_ll') _tab %10.2f (`deceased_dialysis_2021_ul') _tab %10.2f (`deceased_dialysis_2022') _tab %10.2f (`deceased_dialysis_2022_ll') _tab %10.2f (`deceased_dialysis_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Dialysis") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_dialysis_2017') _tab %10.2f (`cardio_dialysis_2017_ll') _tab %10.2f (`cardio_dialysis_2017_ul') _tab %10.2f (`cardio_dialysis_2018') _tab %10.2f (`cardio_dialysis_2018_ll') _tab %10.2f (`cardio_dialysis_2018_ul') _tab %10.2f (`cardio_dialysis_2019') _tab %10.2f (`cardio_dialysis_2019_ll') _tab %10.2f (`cardio_dialysis_2019_ul') _tab %10.2f (`cardio_dialysis_2020') _tab %10.2f (`cardio_dialysis_2020_ll') _tab %10.2f (`cardio_dialysis_2020_ul') _tab %10.2f (`cardio_dialysis_2021') _tab %10.2f (`cardio_dialysis_2021_ll') _tab %10.2f (`cardio_dialysis_2021_ul') _tab %10.2f (`cardio_dialysis_2022') _tab %10.2f (`cardio_dialysis_2022_ll') _tab %10.2f (`cardio_dialysis_2022_ul') _n

*Kidney transplant
file write tablecontent ("West Midlands") _tab ("Transplant") _tab ("N/A") _tab %10.2f (`baseline_kt_2017') _tab %10.2f (`baseline_kt_2017_ll') _tab %10.2f (`baseline_kt_2017_ul') _tab %10.2f (`baseline_kt_2018') _tab %10.2f (`baseline_kt_2018_ll') _tab %10.2f (`baseline_kt_2018_ul') _tab %10.2f (`baseline_kt_2019') _tab %10.2f (`baseline_kt_2019_ll') _tab %10.2f (`baseline_kt_2019_ul') _tab %10.2f (`baseline_kt_2020') _tab %10.2f (`baseline_kt_2020_ll') _tab %10.2f (`baseline_kt_2020_ul') _tab %10.2f (`baseline_kt_2021') _tab %10.2f (`baseline_kt_2021_ll') _tab %10.2f (`baseline_kt_2021_ul') _tab %10.2f (`baseline_kt_2022') _tab %10.2f (`baseline_kt_2022_ll') _tab %10.2f (`baseline_kt_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Transplant") _tab ("No progression") _tab %10.2f (`none_kt_2017') _tab %10.2f (`none_kt_2017_ll') _tab %10.2f (`none_kt_2017_ul') _tab %10.2f (`none_kt_2018') _tab %10.2f (`none_kt_2018_ll') _tab %10.2f (`none_kt_2018_ul') _tab %10.2f (`none_kt_2019') _tab %10.2f (`none_kt_2019_ll') _tab %10.2f (`none_kt_2019_ul') _tab %10.2f (`none_kt_2020') _tab %10.2f (`none_kt_2020_ll') _tab %10.2f (`none_kt_2020_ul') _tab %10.2f (`none_kt_2021') _tab %10.2f (`none_kt_2021_ll') _tab %10.2f (`none_kt_2021_ul') _tab %10.2f (`none_kt_2022') _tab %10.2f (`none_kt_2022_ll') _tab %10.2f (`none_kt_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Transplant") _tab ("Dialysis") _tab %10.2f (`dialysis_kt_2017') _tab %10.2f (`dialysis_kt_2017_ll') _tab %10.2f (`dialysis_kt_2017_ul') _tab %10.2f (`dialysis_kt_2018') _tab %10.2f (`dialysis_kt_2018_ll') _tab %10.2f (`dialysis_kt_2018_ul') _tab %10.2f (`dialysis_kt_2019') _tab %10.2f (`dialysis_kt_2019_ll') _tab %10.2f (`dialysis_kt_2019_ul') _tab %10.2f (`dialysis_kt_2020') _tab %10.2f (`dialysis_kt_2020_ll') _tab %10.2f (`dialysis_kt_2020_ul') _tab %10.2f (`dialysis_kt_2021') _tab %10.2f (`dialysis_kt_2021_ll') _tab %10.2f (`dialysis_kt_2021_ul') _tab %10.2f (`dialysis_kt_2022') _tab %10.2f (`dialysis_kt_2022_ll') _tab %10.2f (`dialysis_kt_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Transplant") _tab ("Deceased") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f ("") _tab %10.2f (`deceased_kt_2018') _tab %10.2f (`deceased_kt_2018_ll') _tab %10.2f (`deceased_kt_2018_ul') _tab %10.2f (`deceased_kt_2019') _tab %10.2f (`deceased_kt_2019_ll') _tab %10.2f (`deceased_kt_2019_ul') _tab %10.2f (`deceased_kt_2020') _tab %10.2f (`deceased_kt_2020_ll') _tab %10.2f (`deceased_kt_2020_ul') _tab %10.2f (`deceased_kt_2021') _tab %10.2f (`deceased_kt_2021_ll') _tab %10.2f (`deceased_kt_2021_ul') _tab %10.2f (`deceased_kt_2022') _tab %10.2f (`deceased_kt_2022_ll') _tab %10.2f (`deceased_kt_2022_ul') _n
file write tablecontent ("West Midlands") _tab ("Transplant") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_kt_2017') _tab %10.2f (`cardio_kt_2017_ll') _tab %10.2f (`cardio_kt_2017_ul') _tab %10.2f (`cardio_kt_2018') _tab %10.2f (`cardio_kt_2018_ll') _tab %10.2f (`cardio_kt_2018_ul') _tab %10.2f (`cardio_kt_2019') _tab %10.2f (`cardio_kt_2019_ll') _tab %10.2f (`cardio_kt_2019_ul') _tab %10.2f (`cardio_kt_2020') _tab %10.2f (`cardio_kt_2020_ll') _tab %10.2f (`cardio_kt_2020_ul') _tab %10.2f (`cardio_kt_2021') _tab %10.2f (`cardio_kt_2021_ll') _tab %10.2f (`cardio_kt_2021_ul') _tab %10.2f (`cardio_kt_2022') _tab %10.2f (`cardio_kt_2022_ll') _tab %10.2f (`cardio_kt_2022_ul') _n

local year "2017 2018 2019 2020 2021 2022"
forvalues i=0/1 {
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`x'_nockd_complete
local label`i': label urban `i'
drop if urban!=`i'
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
file write tablecontent ("All") _tab ("No CKD") _tab ("Deceased") _tab %10.2f (`deceased_nockd_2017') _tab %10.2f (`deceased_nockd_2017_ll') _tab %10.2f (`deceased_nockd_2017_ul') _tab %10.2f (`deceased_nockd_2018') _tab %10.2f (`deceased_nockd_2018_ll') _tab %10.2f (`deceased_nockd_2018_ul') _tab %10.2f (`deceased_nockd_2019') _tab %10.2f (`deceased_nockd_2019_ll') _tab %10.2f (`deceased_nockd_2019_ul') _tab %10.2f (`deceased_nockd_2020') _tab %10.2f (`deceased_nockd_2020_ll') _tab %10.2f (`deceased_nockd_2020_ul') _tab %10.2f (`deceased_nockd_2021') _tab %10.2f (`deceased_nockd_2021_ll') _tab %10.2f (`deceased_nockd_2021_ul') _tab %10.2f (`deceased_nockd_2022') _tab %10.2f (`deceased_nockd_2022_ll') _tab %10.2f (`deceased_nockd_2022_ul') _n
file write tablecontent ("All") _tab ("No CKD") _tab ("Cardiovascular admission") _tab %10.2f (`cardio_nockd_2017') _tab %10.2f (`cardio_nockd_2017_ll') _tab %10.2f (`cardio_nockd_2017_ul') _tab %10.2f (`cardio_nockd_2018') _tab %10.2f (`cardio_nockd_2018_ll') _tab %10.2f (`cardio_nockd_2018_ul') _tab %10.2f (`cardio_nockd_2019') _tab %10.2f (`cardio_nockd_2019_ll') _tab %10.2f (`cardio_nockd_2019_ul') _tab %10.2f (`cardio_nockd_2020') _tab %10.2f (`cardio_nockd_2020_ll') _tab %10.2f (`cardio_nockd_2020_ul') _tab %10.2f (`cardio_nockd_2021') _tab %10.2f (`cardio_nockd_2021_ll') _tab %10.2f (`cardio_nockd_2021_ul') _tab %10.2f (`cardio_nockd_2022') _tab %10.2f (`cardio_nockd_2022_ll') _tab %10.2f (`cardio_nockd_2022_ul') _n

*CKD stage 3
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("N/A") _tab %10.2f (`baseline_ckd3_2017') _tab %10.2f (`baseline_ckd3_2017_ll') _tab %10.2f (`baseline_ckd3_2017_ul') _tab %10.2f (`baseline_ckd3_2018') _tab %10.2f (`baseline_ckd3_2018_ll') _tab %10.2f (`baseline_ckd3_2018_ul') _tab %10.2f (`baseline_ckd3_2019') _tab %10.2f (`baseline_ckd3_2019_ll') _tab %10.2f (`baseline_ckd3_2019_ul') _tab %10.2f (`baseline_ckd3_2020') _tab %10.2f (`baseline_ckd3_2020_ll') _tab %10.2f (`baseline_ckd3_2020_ul') _tab %10.2f (`baseline_ckd3_2021') _tab %10.2f (`baseline_ckd3_2021_ll') _tab %10.2f (`baseline_ckd3_2021_ul') _tab %10.2f (`baseline_ckd3_2022') _tab %10.2f (`baseline_ckd3_2022_ll') _tab %10.2f (`baseline_ckd3_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("No progression") _tab %10.2f (`none_ckd3_2017') _tab %10.2f (`none_ckd3_2017_ll') _tab %10.2f (`none_ckd3_2017_ul') _tab %10.2f (`none_ckd3_2018') _tab %10.2f (`none_ckd3_2018_ll') _tab %10.2f (`none_ckd3_2018_ul') _tab %10.2f (`none_ckd3_2019') _tab %10.2f (`none_ckd3_2019_ll') _tab %10.2f (`none_ckd3_2019_ul') _tab %10.2f (`none_ckd3_2020') _tab %10.2f (`none_ckd3_2020_ll') _tab %10.2f (`none_ckd3_2020_ul') _tab %10.2f (`none_ckd3_2021') _tab %10.2f (`none_ckd3_2021_ll') _tab %10.2f (`none_ckd3_2021_ul') _tab %10.2f (`none_ckd3_2022') _tab %10.2f (`none_ckd3_2022_ll') _tab %10.2f (`none_ckd3_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("CKD stage 4/5") _tab %10.2f (`ckd4_ckd3_2017') _tab %10.2f (`ckd4_ckd3_2017_ll') _tab %10.2f (`ckd4_ckd3_2017_ul') _tab %10.2f (`ckd4_ckd3_2018') _tab %10.2f (`ckd4_ckd3_2018_ll') _tab %10.2f (`ckd4_ckd3_2018_ul') _tab %10.2f (`ckd4_ckd3_2019') _tab %10.2f (`ckd4_ckd3_2019_ll') _tab %10.2f (`ckd4_ckd3_2019_ul') _tab %10.2f (`ckd4_ckd3_2020') _tab %10.2f (`ckd4_ckd3_2020_ll') _tab %10.2f (`ckd4_ckd3_2020_ul') _tab %10.2f (`ckd4_ckd3_2021') _tab %10.2f (`ckd4_ckd3_2021_ll') _tab %10.2f (`ckd4_ckd3_2021_ul') _tab %10.2f (`ckd4_ckd3_2022') _tab %10.2f (`ckd4_ckd3_2022_ll') _tab %10.2f (`ckd4_ckd3_2022_ul') _n
file write tablecontent ("All") _tab ("CKD stage 3") _tab ("Dialysis") _tab %10.2f (`dialysis_ckd3_2017') _tab %10.2f (`dialysis_ckd3_2017_ll') _tab %10.2f (`dialysis_ckd3_2017_ul') _tab %10.2f (`dialysis_ckd3_2018') _tab %10.2f (`dialysis_ckd3_2018_ll') _tab %10.2f (`dialysis_ckd3_2018_ul') _tab %10.2f (`dialysis_ckd3_2019') _tab %10.2f (`dialysis_ckd3_2019_ll') _tab %10.2f (`dialysis_ckd3_2019_ul') _tab %10.2f (`dialysis_ckd3_2020') _tab %10.2f (`dialysis_ckd3_2020_ll') _tab %10.2f (`dialysis_ckd3_2020_ul') _tab %10.2f (`dialysis_ckd3_2021') _tab %10.2f (`dialysis_ckd3_2021_ll') _tab %10.2f (`dialysis_ckd3_2021_ul') _tab %10.2f (`dialysis_ckd3_2022') _tab %10.2f (`dialysis_ckd3_2022_ll') _tab %10.2f (`dialysis_ckd3_2022_ul') _n
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
}

file close tablecontent