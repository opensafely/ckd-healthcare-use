sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/ckd_progression.log, replace t

cap file close tablecontent
file open tablecontent using ./output/ckd_progression.csv, write text replace

file write tablecontent _tab _tab _tab ("April 2017 (N)") _tab ("End 2017-2018 (N)") _tab ("End 2017-2018 (%)") _tab ("April 2018 (N)") _tab ("End 2018-2019 (N)") _tab ("End 2018-2019 (%)") _tab ("April 2019 (N)") _tab ("End 2019-2020 (N)") _tab ("End 2019-2020 (%)") _tab ("April 2020 (N)") _tab ("End 2020-2021 (N)") _tab ("End 2020-2021 (%)") _tab ("April 2021 (N)") _tab ("End 2021-2022 (N)") _tab ("End 2021-2022 (%)") _tab ("April 2022 (N)") _tab ("End 2022-2023 (N)") _tab ("End 2022-2023 (%)") _n(2)


local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear

*eGFR >60 with baseline_ckd2
qui count if ckd_group==1
local baseline_ckd2_`x' = r(N)
local r_baseline_ckd2_`x' = round(`baseline_ckd2_`x'',5)
qui count if ckd_group==1 & ckd_progression==0
local none_`x' = r(N)
local r_none_`x' = round(`none_`x'',5)
local percent_none_`x' = (`r_none_`x''/`r_baseline_ckd2_`x'')*100
qui count if ckd_group==1 & ckd_progression==1
local ckd3_`x' = r(N)
local r_ckd3_`x' = round(`ckd3_`x'',5)
local percent_ckd3_`x' = (`r_ckd3_`x''/`r_baseline_ckd2_`x'')*100
qui count if ckd_group==1 & ckd_progression==2
local ckd4_`x' = r(N)
local r_ckd4_`x' = round(`ckd4_`x'',5)
local percent_ckd4_`x' = (`r_ckd4_`x''/`r_baseline_ckd2_`x'')*100
qui count if ckd_group==1 & ckd_progression==3
local dialysis_`x' = r(N)
local r_dialysis_`x' = round(`dialysis_`x'',5)
local percent_dialysis_`x' = (`r_dialysis_`x''/`r_baseline_ckd2_`x'')*100
qui count if ckd_group==1 & ckd_progression==4
local transplant_`x' = r(N)
local r_transplant_`x' = round(`transplant_`x'',5)
local percent_transplant_`x' = (`r_transplant_`x''/`r_baseline_ckd2_`x'')*100
qui count if ckd_group==1 & ckd_progression==5
local unclear_`x' = r(N)
local r_unclear_`x' = round(`unclear_`x'',5)
local percent_unclear_`x' = (`r_unclear_`x''/`r_baseline_ckd2_`x'')*100
qui count if ckd_group==1 & ckd_progression==6
local deceased_`x' = r(N)
local r_deceased_`x' = round(`deceased_`x'',5)
local percent_deceased_`x' = (`r_deceased_`x''/`r_baseline_ckd2_`x'')*100

*CKD stage 3
qui count if ckd_group==2
local baseline_ckd3_`x' = r(N)
local r_baseline_ckd3_`x' = round(`baseline_ckd3_`x'',5)
qui count if ckd_group==2 & ckd_progression==0
local none_`x' = r(N)
local r_none_`x' = round(`none_`x'',5)
local percent_none_`x' = (`r_none_`x''/`r_baseline_ckd3_`x'')*100
qui count if ckd_group==2 & ckd_progression==2
local ckd4_`x' = r(N)
local r_ckd4_`x' = round(`ckd4_`x'',5)
local percent_ckd4_`x' = (`r_ckd4_`x''/`r_baseline_ckd3_`x'')*100
qui count if ckd_group==2 & ckd_progression==3
local dialysis_`x' = r(N)
local r_dialysis_`x' = round(`dialysis_`x'',5)
local percent_dialysis_`x' = (`r_dialysis_`x''/`r_baseline_ckd3_`x'')*100
qui count if ckd_group==2 & ckd_progression==4
local transplant_`x' = r(N)
local r_transplant_`x' = round(`transplant_`x'',5)
local percent_transplant_`x' = (`r_transplant_`x''/`r_baseline_ckd3_`x'')*100
qui count if ckd_group==2 & ckd_progression==5
local unclear_`x' = r(N)
local r_unclear_`x' = round(`unclear_`x'',5)
local percent_unclear_`x' = (`r_unclear_`x''/`r_baseline_ckd3_`x'')*100
qui count if ckd_group==2 & ckd_progression==6
local deceased_`x' = r(N)
local r_deceased_`x' = round(`deceased_`x'',5)
local percent_deceased_`x' = (`r_deceased_`x''/`r_baseline_ckd3_`x'')*100

*CKD stage 4/5 without KRT
qui count if ckd_group==3
local baseline_ckd4_`x' = r(N)
local r_baseline_ckd4_`x' = round(`baseline_ckd4_`x'',5)
qui count if ckd_group==3 & ckd_progression==0
local none_`x' = r(N)
local r_none_`x' = round(`none_`x'',5)
local percent_none_`x' = (`r_none_`x''/`r_baseline_ckd4_`x'')*100
qui count if ckd_group==3 & ckd_progression==3
local dialysis_`x' = r(N)
local r_dialysis_`x' = round(`dialysis_`x'',5)
local percent_dialysis_`x' = (`r_dialysis_`x''/`r_baseline_ckd4_`x'')*100
qui count if ckd_group==3 & ckd_progression==4
local transplant_`x' = r(N)
local r_transplant_`x' = round(`transplant_`x'',5)
local percent_transplant_`x' = (`r_transplant_`x''/`r_baseline_ckd4_`x'')*100
qui count if ckd_group==3 & ckd_progression==5
local unclear_`x' = r(N)
local r_unclear_`x' = round(`unclear_`x'',5)
local percent_unclear_`x' = (`r_unclear_`x''/`r_baseline_ckd4_`x'')*100
qui count if ckd_group==3 & ckd_progression==6
local deceased_`x' = r(N)
local r_deceased_`x' = round(`deceased_`x'',5)
local percent_deceased_`x' = (`r_deceased_`x''/`r_baseline_ckd4_`x'')*100

*Dialysis
qui count if ckd_group==4
local baseline_dialysis_`x' = r(N)
local r_baseline_dialysis_`x' = round(`baseline_dialysis_`x'',5)
qui count if ckd_group==4 & ckd_progression==0
local none_`x' = r(N)
local r_none_`x' = round(`none_`x'',5)
local percent_none_`x' = (`r_none_`x''/`r_baseline_dialysis_`x'')*100
qui count if ckd_group==4 & ckd_progression==4
local transplant_`x' = r(N)
local r_transplant_`x' = round(`transplant_`x'',5)
local percent_transplant_`x' = (`r_transplant_`x''/`r_baseline_dialysis_`x'')*100
qui count if ckd_group==4 & ckd_progression==6
local deceased_`x' = r(N)
local r_deceased_`x' = round(`deceased_`x'',5)
local percent_deceased_`x' = (`r_deceased_`x''/`r_baseline_dialysis_`x'')*100

*Kidney transplant
qui count if ckd_group==5
local baseline_transplant_`x' = r(N)
local r_baseline_transplant_`x' = round(`baseline_transplant_`x'',5)
qui count if ckd_group==5 & ckd_progression==0
local none_`x' = r(N)
local r_none_`x' = round(`none_`x'',5)
local percent_none_`x' = (`r_none_`x''/`r_baseline_transplant_`x'')*100
qui count if ckd_group==5 & ckd_progression==3
local dialysis_`x' = r(N)
local r_dialysis_`x' = round(`dialysis_`x'',5)
local percent_dialysis_`x' = (`r_dialysis_`x''/`r_baseline_transplant_`x'')*100
qui count if ckd_group==5 & ckd_progression==6
local deceased_`x' = r(N)
local r_deceased_`x' = round(`deceased_`x'',5)
local percent_deceased_`x' = (`r_deceased_`x''/`r_baseline_transplant_`x'')*100

*KRT unclear modality
qui count if ckd_group==6
local baseline_unclear_`x' = r(N)
local r_baseline_unclear_`x' = round(`baseline_unclear_`x'',5)
qui count if ckd_group==6 & ckd_progression==0
local none_`x' = r(N)
local r_none_`x' = round(`none_`x'',5)
local percent_none_`x' = (`r_none_`x''/`r_baseline_unclear_`x'')*100
qui count if ckd_group==6 & ckd_progression==3
local dialysis_`x' = r(N)
local r_dialysis_`x' = round(`dialysis_`x'',5)
local percent_dialysis_`x' = (`r_dialysis_`x''/`r_baseline_unclear_`x'')*100
qui count if ckd_group==6 & ckd_progression==4
local transplant_`x' = r(N)
local r_transplant_`x' = round(`transplant_`x'',5)
local percent_transplant_`x' = (`r_transplant_`x''/`r_baseline_unclear_`x'')*100
qui count if ckd_group==6 & ckd_progression==5
local unclear_`x' = r(N)
local r_unclear_`x' = round(`unclear_`x'',5)
local percent_unclear_`x' = (`r_unclear_`x''/`r_baseline_unclear_`x'')*100
qui count if ckd_group==6 & ckd_progression==6
local deceased_`x' = r(N)
local r_deceased_`x' = round(`deceased_`x'',5)
local percent_deceased_`x' = (`r_deceased_`x''/`r_baseline_unclear_`x'')*100

}

*eGFR >60 with albuminuria
file write tablecontent ("Albuminuria") _tab _tab _tab (`r_baseline_ckd2_2017') _tab _tab _tab (`r_baseline_ckd2_2018') _tab _tab _tab (`r_baseline_ckd2_2019') _tab _tab _tab (`r_baseline_ckd2_2020') _tab _tab _tab (`r_baseline_ckd2_2021') _tab _tab _tab (`r_baseline_ckd2_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab _tab (`r_none_2017') _tab _tab _tab (`r_none_2018') _tab _tab _tab (`r_none_2019') _tab _tab _tab (`r_none_2020') _tab _tab _tab (`r_none_2021') _tab _tab _tab (`r_none_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_2017') _tab _tab _tab %3.1f (`percent_none_2018') _tab _tab _tab %3.1f (`percent_none_2019') _tab _tab _tab %3.1f (`percent_none_2020') _tab _tab _tab %3.1f (`percent_none_2021') _tab _tab _tab %3.1f (`percent_none_2022') _n(2)
file write tablecontent _tab ("CKD stage 3") _tab _tab _tab (`r_ckd3_2017') _tab _tab _tab (`r_ckd3_2018') _tab _tab _tab (`r_ckd3_2019') _tab _tab _tab (`r_ckd3_2020') _tab _tab _tab (`r_ckd3_2021') _tab _tab _tab (`r_ckd3_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_ckd3_2017') _tab _tab _tab %3.1f (`percent_ckd3_2018') _tab _tab _tab %3.1f (`percent_ckd3_2019') _tab _tab _tab %3.1f (`percent_ckd3_2020') _tab _tab _tab %3.1f (`percent_ckd3_2021') _tab _tab _tab %3.1f (`percent_ckd3_2022') _n(2)
file write tablecontent _tab ("CKD stage 4/5") _tab _tab _tab (`r_ckd4_2017') _tab _tab _tab (`r_ckd4_2018') _tab _tab _tab (`r_ckd4_2019') _tab _tab _tab (`r_ckd4_2020') _tab _tab _tab (`r_ckd4_2021') _tab _tab _tab (`r_ckd4_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_ckd4_2017') _tab _tab _tab %3.1f (`percent_ckd4_2018') _tab _tab _tab %3.1f (`percent_ckd4_2019') _tab _tab _tab %3.1f (`percent_ckd4_2020') _tab _tab _tab %3.1f (`percent_ckd4_2021') _tab _tab _tab %3.1f (`percent_ckd4_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab _tab (`r_dialysis_2017') _tab _tab _tab (`r_dialysis_2018') _tab _tab _tab (`r_dialysis_2019') _tab _tab _tab (`r_dialysis_2020') _tab _tab _tab (`r_dialysis_2021') _tab _tab _tab (`r_dialysis_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_2017') _tab _tab _tab %3.1f (`percent_dialysis_2018') _tab _tab _tab %3.1f (`percent_dialysis_2019') _tab _tab _tab %3.1f (`percent_dialysis_2020') _tab _tab _tab %3.1f (`percent_dialysis_2021') _tab _tab _tab %3.1f (`percent_dialysis_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab _tab (`r_transplant_2017') _tab _tab _tab (`r_transplant_2018') _tab _tab _tab (`r_transplant_2019') _tab _tab _tab (`r_transplant_2020') _tab _tab _tab (`r_transplant_2021') _tab _tab _tab (`r_transplant_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_transplant_2017') _tab _tab _tab %3.1f (`percent_transplant_2018') _tab _tab _tab %3.1f (`percent_transplant_2019') _tab _tab _tab %3.1f (`percent_transplant_2020') _tab _tab _tab %3.1f (`percent_transplant_2021') _tab _tab _tab %3.1f (`percent_transplant_2022') _n(2)
file write tablecontent _tab ("KRT unclear") _tab _tab _tab (`r_unclear_2017') _tab _tab _tab (`r_unclear_2018') _tab _tab _tab (`r_unclear_2019') _tab _tab _tab (`r_unclear_2020') _tab _tab _tab (`r_unclear_2021') _tab _tab _tab (`r_unclear_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_unclear_2017') _tab _tab _tab %3.1f (`percent_unclear_2018') _tab _tab _tab %3.1f (`percent_unclear_2019') _tab _tab _tab %3.1f (`percent_unclear_2020') _tab _tab _tab %3.1f (`percent_unclear_2021') _tab _tab _tab %3.1f (`percent_unclear_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab _tab (`r_deceased_2017') _tab _tab _tab (`r_deceased_2018') _tab _tab _tab (`r_deceased_2019') _tab _tab _tab (`r_deceased_2020') _tab _tab _tab (`r_deceased_2021') _tab _tab _tab (`r_deceased_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_2017') _tab _tab _tab %3.1f (`percent_deceased_2018') _tab _tab _tab %3.1f (`percent_deceased_2019') _tab _tab _tab %3.1f (`percent_deceased_2020') _tab _tab _tab %3.1f (`percent_deceased_2021') _tab _tab _tab %3.1f (`percent_deceased_2022') _n(2)

*CKD stage 3
file write tablecontent ("CKD stage 3") _tab _tab _tab (`baseline_ckd3_2017') _tab _tab _tab (`baseline_ckd3_2018') _tab _tab _tab (`baseline_ckd3_2019') _tab _tab _tab (`baseline_ckd3_2020') _tab _tab _tab (`baseline_ckd3_2021') _tab _tab _tab (`baseline_ckd3_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab _tab (`none_2017') _tab _tab _tab (`none_2018') _tab _tab _tab (`none_2019') _tab _tab _tab (`none_2020') _tab _tab _tab (`none_2021') _tab _tab _tab (`none_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_2017') _tab _tab _tab %3.1f (`percent_none_2018') _tab _tab _tab %3.1f (`percent_none_2019') _tab _tab _tab %3.1f (`percent_none_2020') _tab _tab _tab %3.1f (`percent_none_2021') _tab _tab _tab %3.1f (`percent_none_2022') _n(2)
file write tablecontent _tab ("CKD stage 4/5") _tab _tab _tab (`ckd4_2017') _tab _tab _tab (`ckd4_2018') _tab _tab _tab (`ckd4_2019') _tab _tab _tab (`ckd4_2020') _tab _tab _tab (`ckd4_2021') _tab _tab _tab (`ckd4_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_ckd4_2017') _tab _tab _tab %3.1f (`percent_ckd4_2018') _tab _tab _tab %3.1f (`percent_ckd4_2019') _tab _tab _tab %3.1f (`percent_ckd4_2020') _tab _tab _tab %3.1f (`percent_ckd4_2021') _tab _tab _tab %3.1f (`percent_ckd4_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab _tab (`dialysis_2017') _tab _tab _tab (`dialysis_2018') _tab _tab _tab (`dialysis_2019') _tab _tab _tab (`dialysis_2020') _tab _tab _tab (`dialysis_2021') _tab _tab _tab (`dialysis_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_2017') _tab _tab _tab %3.1f (`percent_dialysis_2018') _tab _tab _tab %3.1f (`percent_dialysis_2019') _tab _tab _tab %3.1f (`percent_dialysis_2020') _tab _tab _tab %3.1f (`percent_dialysis_2021') _tab _tab _tab %3.1f (`percent_dialysis_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab _tab (`transplant_2017') _tab _tab _tab (`transplant_2018') _tab _tab _tab (`transplant_2019') _tab _tab _tab (`transplant_2020') _tab _tab _tab (`transplant_2021') _tab _tab _tab (`transplant_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_transplant_2017') _tab _tab _tab %3.1f (`percent_transplant_2018') _tab _tab _tab %3.1f (`percent_transplant_2019') _tab _tab _tab %3.1f (`percent_transplant_2020') _tab _tab _tab %3.1f (`percent_transplant_2021') _tab _tab _tab %3.1f (`percent_transplant_2022') _n(2)
file write tablecontent _tab ("KRT unclear") _tab _tab _tab (`unclear_2017') _tab _tab _tab (`unclear_2018') _tab _tab _tab (`unclear_2019') _tab _tab _tab (`unclear_2020') _tab _tab _tab (`unclear_2021') _tab _tab _tab (`unclear_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_unclear_2017') _tab _tab _tab %3.1f (`percent_unclear_2018') _tab _tab _tab %3.1f (`percent_unclear_2019') _tab _tab _tab %3.1f (`percent_unclear_2020') _tab _tab _tab %3.1f (`percent_unclear_2021') _tab _tab _tab %3.1f (`percent_unclear_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab _tab (`deceased_2017') _tab _tab _tab (`deceased_2018') _tab _tab _tab (`deceased_2019') _tab _tab _tab (`deceased_2020') _tab _tab _tab (`deceased_2021') _tab _tab _tab (`deceased_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_2017') _tab _tab _tab %3.1f (`percent_deceased_2018') _tab _tab _tab %3.1f (`percent_deceased_2019') _tab _tab _tab %3.1f (`percent_deceased_2020') _tab _tab _tab %3.1f (`percent_deceased_2021') _tab _tab _tab %3.1f (`percent_deceased_2022') _n(2)

*CKD stage 4/5 without KRT
file write tablecontent ("CKD stage 4/5") _tab _tab _tab (`baseline_ckd4_2017') _tab _tab _tab (`baseline_ckd4_2018') _tab _tab _tab (`baseline_ckd4_2019') _tab _tab _tab (`baseline_ckd4_2020') _tab _tab _tab (`baseline_ckd4_2021') _tab _tab _tab (`baseline_ckd4_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab _tab (`none_2017') _tab _tab _tab (`none_2018') _tab _tab _tab (`none_2019') _tab _tab _tab (`none_2020') _tab _tab _tab (`none_2021') _tab _tab _tab (`none_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_2017') _tab _tab _tab %3.1f (`percent_none_2018') _tab _tab _tab %3.1f (`percent_none_2019') _tab _tab _tab %3.1f (`percent_none_2020') _tab _tab _tab %3.1f (`percent_none_2021') _tab _tab _tab %3.1f (`percent_none_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab _tab (`dialysis_2017') _tab _tab _tab (`dialysis_2018') _tab _tab _tab (`dialysis_2019') _tab _tab _tab (`dialysis_2020') _tab _tab _tab (`dialysis_2021') _tab _tab _tab (`dialysis_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_2017') _tab _tab _tab %3.1f (`percent_dialysis_2018') _tab _tab _tab %3.1f (`percent_dialysis_2019') _tab _tab _tab %3.1f (`percent_dialysis_2020') _tab _tab _tab %3.1f (`percent_dialysis_2021') _tab _tab _tab %3.1f (`percent_dialysis_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab _tab (`transplant_2017') _tab _tab _tab (`transplant_2018') _tab _tab _tab (`transplant_2019') _tab _tab _tab (`transplant_2020') _tab _tab _tab (`transplant_2021') _tab _tab _tab (`transplant_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_transplant_2017') _tab _tab _tab %3.1f (`percent_transplant_2018') _tab _tab _tab %3.1f (`percent_transplant_2019') _tab _tab _tab %3.1f (`percent_transplant_2020') _tab _tab _tab %3.1f (`percent_transplant_2021') _tab _tab _tab %3.1f (`percent_transplant_2022') _n(2)
file write tablecontent _tab ("KRT unclear") _tab _tab _tab (`unclear_2017') _tab _tab _tab (`unclear_2018') _tab _tab _tab (`unclear_2019') _tab _tab _tab (`unclear_2020') _tab _tab _tab (`unclear_2021') _tab _tab _tab (`unclear_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_unclear_2017') _tab _tab _tab %3.1f (`percent_unclear_2018') _tab _tab _tab %3.1f (`percent_unclear_2019') _tab _tab _tab %3.1f (`percent_unclear_2020') _tab _tab _tab %3.1f (`percent_unclear_2021') _tab _tab _tab %3.1f (`percent_unclear_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab _tab (`deceased_2017') _tab _tab _tab (`deceased_2018') _tab _tab _tab (`deceased_2019') _tab _tab _tab (`deceased_2020') _tab _tab _tab (`deceased_2021') _tab _tab _tab (`deceased_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_2017') _tab _tab _tab %3.1f (`percent_deceased_2018') _tab _tab _tab %3.1f (`percent_deceased_2019') _tab _tab _tab %3.1f (`percent_deceased_2020') _tab _tab _tab %3.1f (`percent_deceased_2021') _tab _tab _tab %3.1f (`percent_deceased_2022') _n(2)

*Dialysis
file write tablecontent ("Dialysis") _tab _tab _tab (`baseline_dialysis_2017') _tab _tab _tab (`baseline_dialysis_2018') _tab _tab _tab (`baseline_dialysis_2019') _tab _tab _tab (`baseline_dialysis_2020') _tab _tab _tab (`baseline_dialysis_2021') _tab _tab _tab (`baseline_dialysis_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab _tab (`none_2017') _tab _tab _tab (`none_2018') _tab _tab _tab (`none_2019') _tab _tab _tab (`none_2020') _tab _tab _tab (`none_2021') _tab _tab _tab (`none_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_2017') _tab _tab _tab %3.1f (`percent_none_2018') _tab _tab _tab %3.1f (`percent_none_2019') _tab _tab _tab %3.1f (`percent_none_2020') _tab _tab _tab %3.1f (`percent_none_2021') _tab _tab _tab %3.1f (`percent_none_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab _tab (`transplant_2017') _tab _tab _tab (`transplant_2018') _tab _tab _tab (`transplant_2019') _tab _tab _tab (`transplant_2020') _tab _tab _tab (`transplant_2021') _tab _tab _tab (`transplant_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_transplant_2017') _tab _tab _tab %3.1f (`percent_transplant_2018') _tab _tab _tab %3.1f (`percent_transplant_2019') _tab _tab _tab %3.1f (`percent_transplant_2020') _tab _tab _tab %3.1f (`percent_transplant_2021') _tab _tab _tab %3.1f (`percent_transplant_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab _tab (`deceased_2017') _tab _tab _tab (`deceased_2018') _tab _tab _tab (`deceased_2019') _tab _tab _tab (`deceased_2020') _tab _tab _tab (`deceased_2021') _tab _tab _tab (`deceased_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_2017') _tab _tab _tab %3.1f (`percent_deceased_2018') _tab _tab _tab %3.1f (`percent_deceased_2019') _tab _tab _tab %3.1f (`percent_deceased_2020') _tab _tab _tab %3.1f (`percent_deceased_2021') _tab _tab _tab %3.1f (`percent_deceased_2022') _n(2)

*Kidney transplant
file write tablecontent ("Transplant") _tab _tab _tab (`baseline_transplant_2017') _tab _tab _tab (`baseline_transplant_2018') _tab _tab _tab (`baseline_transplant_2019') _tab _tab _tab (`baseline_transplant_2020') _tab _tab _tab (`baseline_transplant_2021') _tab _tab _tab (`baseline_transplant_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab _tab (`none_2017') _tab _tab _tab (`none_2018') _tab _tab _tab (`none_2019') _tab _tab _tab (`none_2020') _tab _tab _tab (`none_2021') _tab _tab _tab (`none_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_2017') _tab _tab _tab %3.1f (`percent_none_2018') _tab _tab _tab %3.1f (`percent_none_2019') _tab _tab _tab %3.1f (`percent_none_2020') _tab _tab _tab %3.1f (`percent_none_2021') _tab _tab _tab %3.1f (`percent_none_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab _tab (`dialysis_2017') _tab _tab _tab (`dialysis_2018') _tab _tab _tab (`dialysis_2019') _tab _tab _tab (`dialysis_2020') _tab _tab _tab (`dialysis_2021') _tab _tab _tab (`dialysis_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_2017') _tab _tab _tab %3.1f (`percent_dialysis_2018') _tab _tab _tab %3.1f (`percent_dialysis_2019') _tab _tab _tab %3.1f (`percent_dialysis_2020') _tab _tab _tab %3.1f (`percent_dialysis_2021') _tab _tab _tab %3.1f (`percent_dialysis_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab _tab (`deceased_2017') _tab _tab _tab (`deceased_2018') _tab _tab _tab (`deceased_2019') _tab _tab _tab (`deceased_2020') _tab _tab _tab (`deceased_2021') _tab _tab _tab (`deceased_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_2017') _tab _tab _tab %3.1f (`percent_deceased_2018') _tab _tab _tab %3.1f (`percent_deceased_2019') _tab _tab _tab %3.1f (`percent_deceased_2020') _tab _tab _tab %3.1f (`percent_deceased_2021') _tab _tab _tab %3.1f (`percent_deceased_2022') _n(2)

*KRT unclear modality
file write tablecontent ("KRT unclear") _tab _tab _tab (`baseline_unclear_2017') _tab _tab _tab (`baseline_unclear_2018') _tab _tab _tab (`baseline_unclear_2019') _tab _tab _tab (`baseline_unclear_2020') _tab _tab _tab (`baseline_unclear_2021') _tab _tab _tab (`baseline_unclear_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab _tab (`none_2017') _tab _tab _tab (`none_2018') _tab _tab _tab (`none_2019') _tab _tab _tab (`none_2020') _tab _tab _tab (`none_2021') _tab _tab _tab (`none_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_2017') _tab _tab _tab %3.1f (`percent_none_2018') _tab _tab _tab %3.1f (`percent_none_2019') _tab _tab _tab %3.1f (`percent_none_2020') _tab _tab _tab %3.1f (`percent_none_2021') _tab _tab _tab %3.1f (`percent_none_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab _tab (`dialysis_2017') _tab _tab _tab (`dialysis_2018') _tab _tab _tab (`dialysis_2019') _tab _tab _tab (`dialysis_2020') _tab _tab _tab (`dialysis_2021') _tab _tab _tab (`dialysis_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_2017') _tab _tab _tab %3.1f (`percent_dialysis_2018') _tab _tab _tab %3.1f (`percent_dialysis_2019') _tab _tab _tab %3.1f (`percent_dialysis_2020') _tab _tab _tab %3.1f (`percent_dialysis_2021') _tab _tab _tab %3.1f (`percent_dialysis_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab _tab (`transplant_2017') _tab _tab _tab (`transplant_2018') _tab _tab _tab (`transplant_2019') _tab _tab _tab (`transplant_2020') _tab _tab _tab (`transplant_2021') _tab _tab _tab (`transplant_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_transplant_2017') _tab _tab _tab %3.1f (`percent_transplant_2018') _tab _tab _tab %3.1f (`percent_transplant_2019') _tab _tab _tab %3.1f (`percent_transplant_2020') _tab _tab _tab %3.1f (`percent_transplant_2021') _tab _tab _tab %3.1f (`percent_transplant_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab _tab (`deceased_2017') _tab _tab _tab (`deceased_2018') _tab _tab _tab (`deceased_2019') _tab _tab _tab (`deceased_2020') _tab _tab _tab (`deceased_2021') _tab _tab _tab (`deceased_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_2017') _tab _tab _tab %3.1f (`percent_deceased_2018') _tab _tab _tab %3.1f (`percent_deceased_2019') _tab _tab _tab %3.1f (`percent_deceased_2020') _tab _tab _tab %3.1f (`percent_deceased_2021') _tab _tab _tab %3.1f (`percent_deceased_2022') _n(2)

file close tablecontent
