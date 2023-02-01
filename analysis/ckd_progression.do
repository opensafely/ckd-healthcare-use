sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/ckd_progression.log, replace t

cap file close tablecontent
file open tablecontent using ./output/ckd_progression.csv, write text replace

**Column headings
*There are three column headings for each year 2017-2022:
*Column 1 = the number of people in each CKD group as of the beginning of each year (i.e. in April)
*Column 2 = the number of people who remain within the same CKD group, progress to a more advanced CKD group, or die by the end of the year (i.e. by the subsequent April)
*Column 3 = Column 2 as a percentage of Column 1
file write tablecontent _tab _tab ("April_2017_N") _tab ("End_2017-2018_N") _tab ("End_2017-2018_pc") _tab ("April_2018_N") _tab ("End_2018-2019_N") _tab ("End_2018-2019_pc") _tab ("April_2019_N") _tab ("End_2019-2020_N") _tab ("End_2019-2020_pc") _tab ("April_2020_N") _tab ("End_2020-2021_N") _tab ("End_2020-2021_pc") _tab ("April_2021_N") _tab ("End_2021-2022_N") _tab ("End_2021-2022_pc") _tab ("April_2022_N") _tab ("End_2022-2023_N") _tab ("End_2022-2023_pc") _n(2)

**Loops through datasets for each year `x' 2017-2022
local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
use ./output/`x'_ckd_complete.dta, clear

**Disclosure minimisation
*safecount provides a count with any counts <=5 returned at "<=5"
*round(r(N),5) rounds counts to the nearest 5 with any counts <=5 returned as "."

**eGFR >60 with albuminuria
*Number of people in group (baseline_ckd2_`x') at the beginning of each year ckd2_`x'
qui safecount if ckd_group==1
local baseline_ckd2_`x' = round(r(N),5)
*Number/percentage of people in group who do not progress by the end of the year
qui safecount if ckd_group==1 & ckd_progression==0
local none_ckd2_`x' = round(r(N),5)
local percent_none_ckd2_`x' = (`none_ckd2_`x''/`baseline_ckd2_`x'')*100
*Number/percentage of people in group who progress to CKD stage 3 by the end of the year
qui safecount if ckd_group==1 & ckd_progression==1
local ckd3_ckd2_`x' = round(r(N),5)
local percent_ckd3_ckd2_`x' = (`ckd3_ckd2_`x''/`baseline_ckd2_`x'')*100
*Number/percentage of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui safecount if ckd_group==1 & ckd_progression==2
local ckd4_ckd2_`x' = round(r(N),5)
local percent_ckd4_ckd2_`x' = (`ckd4_ckd2_`x''/`baseline_ckd2_`x'')*100
*Number/percentage of people in group who progress to dialysis by the end of the year
qui safecount if ckd_group==1 & ckd_progression==3
local dialysis_ckd2_`x' = round(r(N),5)
local percent_dialysis_ckd2_`x' = (`dialysis_ckd2_`x''/`baseline_ckd2_`x'')*100
*Number/percentage of people in group who progress to kidney kt by the end of the year
qui safecount if ckd_group==1 & ckd_progression==4
local kt_ckd2_`x' = round(r(N),5)
local percent_kt_ckd2_`x' = (`kt_ckd2_`x''/`baseline_ckd2_`x'')*100
*Number/percentage of people in group who progress to KRT (unclear modality) by the end of the year
qui safecount if ckd_group==1 & ckd_progression==5
local unclear_ckd2_`x' = round(r(N),5)
local percent_unclear_ckd2_`x' = (`unclear_ckd2_`x''/`baseline_ckd2_`x'')*100
*Number/percentage of people in group who die by the end of the year
qui safecount if ckd_group==1 & ckd_progression==6
local deceased_ckd2_`x' = round(r(N),5)
local percent_deceased_ckd2_`x' = (`deceased_ckd2_`x''/`baseline_ckd2_`x'')*100

**CKD stage 3
*Number of people in group (baseline_ckd3_`x') at the beginning of each year ckd3_`x'
qui safecount if ckd_group==2
local baseline_ckd3_`x' = round(r(N),5)
*Number/percentage of people in group who do not progress by the end of the year
qui safecount if ckd_group==2 & ckd_progression==0
local none_ckd3_`x' = round(r(N),5)
local percent_none_ckd3_`x' = (`none_ckd3_`x''/`baseline_ckd3_`x'')*100
*Number/percentage of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui safecount if ckd_group==2 & ckd_progression==2
local ckd4_ckd3_`x' = round(r(N),5)
local percent_ckd4_ckd3_`x' = (`ckd4_ckd3_`x''/`baseline_ckd3_`x'')*100
*Number/percentage of people in group who progress to dialysis by the end of the year
qui safecount if ckd_group==2 & ckd_progression==3
local dialysis_ckd3_`x' = round(r(N),5)
local percent_dialysis_ckd3_`x' = (`dialysis_ckd3_`x''/`baseline_ckd3_`x'')*100
*Number/percentage of people in group who progress to kidney transplant by the end of the year
qui safecount if ckd_group==2 & ckd_progression==4
local kt_ckd3_`x' = round(r(N),5)
local percent_kt_ckd3_`x' = (`kt_ckd3_`x''/`baseline_ckd3_`x'')*100
*Number/percentage of people in group who progress to KRT (unclear modality) by the end of the year
qui safecount if ckd_group==2 & ckd_progression==5
local unclear_ckd3_`x' = round(r(N),5)
local percent_unclear_ckd3_`x' = (`unclear_ckd3_`x''/`baseline_ckd3_`x'')*100
*Number/percentage of people in group who die by the end of the year
qui safecount if ckd_group==2 & ckd_progression==6
local deceased_ckd3_`x' = round(r(N),5)
local percent_deceased_ckd3_`x' = (`deceased_ckd3_`x''/`baseline_ckd3_`x'')*100

**CKD stage 4/5 without KRT
*Number of people in group (baseline_ckd4_`x') at the beginning of each year ckd4_`x'
qui safecount if ckd_group==3
local baseline_ckd4_`x' = round(r(N),5)
*Number/percentage of people in group who do not progress by the end of the year
qui safecount if ckd_group==3 & ckd_progression==0
local none_ckd4_`x' = round(r(N),5)
local percent_none_ckd4_`x' = (`none_ckd4_`x''/`baseline_ckd4_`x'')*100
*Number/percentage of people in group who progress to dialysis by the end of the year
qui safecount if ckd_group==3 & ckd_progression==3
local dialysis_ckd4_`x' = round(r(N),5)
local percent_dialysis_ckd4_`x' = (`dialysis_ckd4_`x''/`baseline_ckd4_`x'')*100
*Number/percentage of people in group who progress to kidney transplant by the end of the year
qui safecount if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = round(r(N),5)
local percent_kt_ckd4_`x' = (`kt_ckd4_`x''/`baseline_ckd4_`x'')*100
*Number/percentage of people in group who progress to KRT (unclear modality) by the end of the year
qui safecount if ckd_group==3 & ckd_progression==5
local unclear_ckd4_`x' = round(r(N),5)
local percent_unclear_ckd4_`x' = (`unclear_ckd4_`x''/`baseline_ckd4_`x'')*100
*Number/percentage of people in group who die by the end of the year
qui safecount if ckd_group==3 & ckd_progression==6
local deceased_ckd4_`x' = round(r(N),5)
local percent_deceased_ckd4_`x' = (`deceased_ckd4_`x''/`baseline_ckd4_`x'')*100

**Dialysis
*Number of people in group (baseline_dialysis_`x') at the beginning of each year dialysis_`x'
qui safecount if ckd_group==4
local baseline_dialysis_`x' = round(r(N),5)
*Number/percentage of people in group remaining on dialysis by the end of the year
qui safecount if ckd_group==4 & ckd_progression==0
local none_dialysis_`x' = round(r(N),5)
local percent_none_dialysis_`x' = (`none_dialysis_`x''/`baseline_dialysis_`x'')*100
*Number/percentage of people in group with kidney transplant by the end of the year
qui safecount if ckd_group==4 & ckd_progression==4
local kt_dialysis_`x' = round(r(N),5)
local percent_kt_dialysis_`x' = (`kt_dialysis_`x''/`baseline_dialysis_`x'')*100
*Number/percentage of people in group who die by the end of the year
qui safecount if ckd_group==4 & ckd_progression==6
local deceased_dialysis_`x' = round(r(N),5)
local percent_deceased_dialysis_`x' = (`deceased_dialysis_`x''/`baseline_dialysis_`x'')*100

**Kidney transplant
*Number of people in group (baseline_kt_`x') at the beginning of each year kt_`x'
qui safecount if ckd_group==5
local baseline_kt_`x' = round(r(N),5)
*Number/percentage of people in group remaining with kidney transplant by the end of the year
qui safecount if ckd_group==5 & ckd_progression==0
local none_kt_`x' = round(r(N),5)
local percent_none_kt_`x' = (`none_kt_`x''/`baseline_kt_`x'')*100
*Number/percentage of people in group on dialysis by the end of the year
qui safecount if ckd_group==5 & ckd_progression==3
local dialysis_kt_`x' = round(r(N),5)
local percent_dialysis_kt_`x' = (`dialysis_kt_`x''/`baseline_kt_`x'')*100
*Number/percentage of people in group who die by the end of the year
qui safecount if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = round(r(N),5)
local percent_deceased_kt_`x' = (`deceased_kt_`x''/`baseline_kt_`x'')*100

**KRT unclear modality
*Number of people in group (baseline_unclear_`x') at the beginning of each year unclear_`x'
qui safecount if ckd_group==6
local baseline_unclear_`x' = round(r(N),5)
*Number/percentage of people in group remaining in group by the end of the year
qui safecount if ckd_group==6 & ckd_progression==0
local none_unclear_`x' = round(r(N),5)
local percent_none_unclear_`x' = (`none_unclear_`x''/`baseline_unclear_`x'')*100
*Number/percentage of people in group on dialysis by the end of the year
qui safecount if ckd_group==6 & ckd_progression==3
local dialysis_unclear_`x' = round(r(N),5)
local percent_dialysis_unclear_`x' = (`dialysis_unclear_`x''/`baseline_unclear_`x'')*100
*Number/percentage of people in group with kidney transplant by the end of the year
qui safecount if ckd_group==6 & ckd_progression==4
local kt_unclear_`x' = round(r(N),5)
local percent_kt_unclear_`x' = (`kt_unclear_`x''/`baseline_unclear_`x'')*100
*Number/percentage of people in group who die by the end of the year
qui safecount if ckd_group==6 & ckd_progression==6
local deceased_unclear_`x' = round(r(N),5)
local percent_deceased_unclear_`x' = (`deceased_unclear_`x''/`baseline_unclear_`x'')*100
}

**Populate table with redacted counts
*eGFR >60 with albuminuria
file write tablecontent ("Albuminuria") _tab _tab (`baseline_ckd2_2017') _tab _tab _tab (`baseline_ckd2_2018') _tab _tab _tab (`baseline_ckd2_2019') _tab _tab _tab (`baseline_ckd2_2020') _tab _tab _tab (`baseline_ckd2_2021') _tab _tab _tab (`baseline_ckd2_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_ckd2_2017') _tab _tab _tab (`none_ckd2_2018') _tab _tab _tab (`none_ckd2_2019') _tab _tab _tab (`none_ckd2_2020') _tab _tab _tab (`none_ckd2_2021') _tab _tab _tab (`none_ckd2_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_ckd2_2017') _tab _tab _tab %3.1f (`percent_none_ckd2_2018') _tab _tab _tab %3.1f (`percent_none_ckd2_2019') _tab _tab _tab %3.1f (`percent_none_ckd2_2020') _tab _tab _tab %3.1f (`percent_none_ckd2_2021') _tab _tab _tab %3.1f (`percent_none_ckd2_2022') _n(2)
file write tablecontent _tab ("CKD stage 3") _tab _tab (`ckd3_ckd2_2017') _tab _tab _tab (`ckd3_ckd2_2018') _tab _tab _tab (`ckd3_ckd2_2019') _tab _tab _tab (`ckd3_ckd2_2020') _tab _tab _tab (`ckd3_ckd2_2021') _tab _tab _tab (`ckd3_ckd2_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_ckd3_ckd2_2017') _tab _tab _tab %3.1f (`percent_ckd3_ckd2_2018') _tab _tab _tab %3.1f (`percent_ckd3_ckd2_2019') _tab _tab _tab %3.1f (`percent_ckd3_ckd2_2020') _tab _tab _tab %3.1f (`percent_ckd3_ckd2_2021') _tab _tab _tab %3.1f (`percent_ckd3_ckd2_2022') _n(2)
file write tablecontent _tab ("CKD stage 4/5") _tab _tab (`ckd4_ckd2_2017') _tab _tab _tab (`ckd4_ckd2_2018') _tab _tab _tab (`ckd4_ckd2_2019') _tab _tab _tab (`ckd4_ckd2_2020') _tab _tab _tab (`ckd4_ckd2_2021') _tab _tab _tab (`ckd4_ckd2_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_ckd4_ckd2_2017') _tab _tab _tab %3.1f (`percent_ckd4_ckd2_2018') _tab _tab _tab %3.1f (`percent_ckd4_ckd2_2019') _tab _tab _tab %3.1f (`percent_ckd4_ckd2_2020') _tab _tab _tab %3.1f (`percent_ckd4_ckd2_2021') _tab _tab _tab %3.1f (`percent_ckd4_ckd2_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_ckd2_2017') _tab _tab _tab (`dialysis_ckd2_2018') _tab _tab _tab (`dialysis_ckd2_2019') _tab _tab _tab (`dialysis_ckd2_2020') _tab _tab _tab (`dialysis_ckd2_2021') _tab _tab _tab (`dialysis_ckd2_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_ckd2_2017') _tab _tab _tab %3.1f (`percent_dialysis_ckd2_2018') _tab _tab _tab %3.1f (`percent_dialysis_ckd2_2019') _tab _tab _tab %3.1f (`percent_dialysis_ckd2_2020') _tab _tab _tab %3.1f (`percent_dialysis_ckd2_2021') _tab _tab _tab %3.1f (`percent_dialysis_ckd2_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab (`kt_ckd2_2017') _tab _tab _tab (`kt_ckd2_2018') _tab _tab _tab (`kt_ckd2_2019') _tab _tab _tab (`kt_ckd2_2020') _tab _tab _tab (`kt_ckd2_2021') _tab _tab _tab (`kt_ckd2_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_kt_ckd2_2017') _tab _tab _tab %3.1f (`percent_kt_ckd2_2018') _tab _tab _tab %3.1f (`percent_kt_ckd2_2019') _tab _tab _tab %3.1f (`percent_kt_ckd2_2020') _tab _tab _tab %3.1f (`percent_kt_ckd2_2021') _tab _tab _tab %3.1f (`percent_kt_ckd2_2022') _n(2)
file write tablecontent _tab ("KRT unclear") _tab _tab (`unclear_ckd2_2017') _tab _tab _tab (`unclear_ckd2_2018') _tab _tab _tab (`unclear_ckd2_2019') _tab _tab _tab (`unclear_ckd2_2020') _tab _tab _tab (`unclear_ckd2_2021') _tab _tab _tab (`unclear_ckd2_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_unclear_ckd2_2017') _tab _tab _tab %3.1f (`percent_unclear_ckd2_2018') _tab _tab _tab %3.1f (`percent_unclear_ckd2_2019') _tab _tab _tab %3.1f (`percent_unclear_ckd2_2020') _tab _tab _tab %3.1f (`percent_unclear_ckd2_2021') _tab _tab _tab %3.1f (`percent_unclear_ckd2_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_ckd2_2017') _tab _tab _tab (`deceased_ckd2_2018') _tab _tab _tab (`deceased_ckd2_2019') _tab _tab _tab (`deceased_ckd2_2020') _tab _tab _tab (`deceased_ckd2_2021') _tab _tab _tab (`deceased_ckd2_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_ckd2_2017') _tab _tab _tab %3.1f (`percent_deceased_ckd2_2018') _tab _tab _tab %3.1f (`percent_deceased_ckd2_2019') _tab _tab _tab %3.1f (`percent_deceased_ckd2_2020') _tab _tab _tab %3.1f (`percent_deceased_ckd2_2021') _tab _tab _tab %3.1f (`percent_deceased_ckd2_2022') _n(2)

*CKD stage 3
file write tablecontent ("CKD stage 3") _tab _tab (`baseline_ckd3_2017') _tab _tab _tab (`baseline_ckd3_2018') _tab _tab _tab (`baseline_ckd3_2019') _tab _tab _tab (`baseline_ckd3_2020') _tab _tab _tab (`baseline_ckd3_2021') _tab _tab _tab (`baseline_ckd3_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_ckd3_2017') _tab _tab _tab (`none_ckd3_2018') _tab _tab _tab (`none_ckd3_2019') _tab _tab _tab (`none_ckd3_2020') _tab _tab _tab (`none_ckd3_2021') _tab _tab _tab (`none_ckd3_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_ckd3_2017') _tab _tab _tab %3.1f (`percent_none_ckd3_2018') _tab _tab _tab %3.1f (`percent_none_ckd3_2019') _tab _tab _tab %3.1f (`percent_none_ckd3_2020') _tab _tab _tab %3.1f (`percent_none_ckd3_2021') _tab _tab _tab %3.1f (`percent_none_ckd3_2022') _n(2)
file write tablecontent _tab ("CKD stage 4/5") _tab _tab (`ckd4_ckd3_2017') _tab _tab _tab (`ckd4_ckd3_2018') _tab _tab _tab (`ckd4_ckd3_2019') _tab _tab _tab (`ckd4_ckd3_2020') _tab _tab _tab (`ckd4_ckd3_2021') _tab _tab _tab (`ckd4_ckd3_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_ckd4_ckd3_2017') _tab _tab _tab %3.1f (`percent_ckd4_ckd3_2018') _tab _tab _tab %3.1f (`percent_ckd4_ckd3_2019') _tab _tab _tab %3.1f (`percent_ckd4_ckd3_2020') _tab _tab _tab %3.1f (`percent_ckd4_ckd3_2021') _tab _tab _tab %3.1f (`percent_ckd4_ckd3_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_ckd3_2017') _tab _tab _tab (`dialysis_ckd3_2018') _tab _tab _tab (`dialysis_ckd3_2019') _tab _tab _tab (`dialysis_ckd3_2020') _tab _tab _tab (`dialysis_ckd3_2021') _tab _tab _tab (`dialysis_ckd3_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_ckd3_2017') _tab _tab _tab %3.1f (`percent_dialysis_ckd3_2018') _tab _tab _tab %3.1f (`percent_dialysis_ckd3_2019') _tab _tab _tab %3.1f (`percent_dialysis_ckd3_2020') _tab _tab _tab %3.1f (`percent_dialysis_ckd3_2021') _tab _tab _tab %3.1f (`percent_dialysis_ckd3_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab (`kt_ckd3_2017') _tab _tab _tab (`kt_ckd3_2018') _tab _tab _tab (`kt_ckd3_2019') _tab _tab _tab (`kt_ckd3_2020') _tab _tab _tab (`kt_ckd3_2021') _tab _tab _tab (`kt_ckd3_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_kt_ckd3_2017') _tab _tab _tab %3.1f (`percent_kt_ckd3_2018') _tab _tab _tab %3.1f (`percent_kt_ckd3_2019') _tab _tab _tab %3.1f (`percent_kt_ckd3_2020') _tab _tab _tab %3.1f (`percent_kt_ckd3_2021') _tab _tab _tab %3.1f (`percent_kt_ckd3_2022') _n(2)
file write tablecontent _tab ("KRT unclear") _tab _tab (`unclear_ckd3_2017') _tab _tab _tab (`unclear_ckd3_2018') _tab _tab _tab (`unclear_ckd3_2019') _tab _tab _tab (`unclear_ckd3_2020') _tab _tab _tab (`unclear_ckd3_2021') _tab _tab _tab (`unclear_ckd3_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_unclear_ckd3_2017') _tab _tab _tab %3.1f (`percent_unclear_ckd3_2018') _tab _tab _tab %3.1f (`percent_unclear_ckd3_2019') _tab _tab _tab %3.1f (`percent_unclear_ckd3_2020') _tab _tab _tab %3.1f (`percent_unclear_ckd3_2021') _tab _tab _tab %3.1f (`percent_unclear_ckd3_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_ckd3_2017') _tab _tab _tab (`deceased_ckd3_2018') _tab _tab _tab (`deceased_ckd3_2019') _tab _tab _tab (`deceased_ckd3_2020') _tab _tab _tab (`deceased_ckd3_2021') _tab _tab _tab (`deceased_ckd3_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_ckd3_2017') _tab _tab _tab %3.1f (`percent_deceased_ckd3_2018') _tab _tab _tab %3.1f (`percent_deceased_ckd3_2019') _tab _tab _tab %3.1f (`percent_deceased_ckd3_2020') _tab _tab _tab %3.1f (`percent_deceased_ckd3_2021') _tab _tab _tab %3.1f (`percent_deceased_ckd3_2022') _n(2)

*CKD stage 4/5 without KRT
file write tablecontent ("CKD stage 4/5") _tab _tab (`baseline_ckd4_2017') _tab _tab _tab (`baseline_ckd4_2018') _tab _tab _tab (`baseline_ckd4_2019') _tab _tab _tab (`baseline_ckd4_2020') _tab _tab _tab (`baseline_ckd4_2021') _tab _tab _tab (`baseline_ckd4_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_ckd4_2017') _tab _tab _tab (`none_ckd4_2018') _tab _tab _tab (`none_ckd4_2019') _tab _tab _tab (`none_ckd4_2020') _tab _tab _tab (`none_ckd4_2021') _tab _tab _tab (`none_ckd4_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_ckd4_2017') _tab _tab _tab %3.1f (`percent_none_ckd4_2018') _tab _tab _tab %3.1f (`percent_none_ckd4_2019') _tab _tab _tab %3.1f (`percent_none_ckd4_2020') _tab _tab _tab %3.1f (`percent_none_ckd4_2021') _tab _tab _tab %3.1f (`percent_none_ckd4_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_ckd4_2017') _tab _tab _tab (`dialysis_ckd4_2018') _tab _tab _tab (`dialysis_ckd4_2019') _tab _tab _tab (`dialysis_ckd4_2020') _tab _tab _tab (`dialysis_ckd4_2021') _tab _tab _tab (`dialysis_ckd4_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_ckd4_2017') _tab _tab _tab %3.1f (`percent_dialysis_ckd4_2018') _tab _tab _tab %3.1f (`percent_dialysis_ckd4_2019') _tab _tab _tab %3.1f (`percent_dialysis_ckd4_2020') _tab _tab _tab %3.1f (`percent_dialysis_ckd4_2021') _tab _tab _tab %3.1f (`percent_dialysis_ckd4_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab (`kt_ckd4_2017') _tab _tab _tab (`kt_ckd4_2018') _tab _tab _tab (`kt_ckd4_2019') _tab _tab _tab (`kt_ckd4_2020') _tab _tab _tab (`kt_ckd4_2021') _tab _tab _tab (`kt_ckd4_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_kt_ckd4_2017') _tab _tab _tab %3.1f (`percent_kt_ckd4_2018') _tab _tab _tab %3.1f (`percent_kt_ckd4_2019') _tab _tab _tab %3.1f (`percent_kt_ckd4_2020') _tab _tab _tab %3.1f (`percent_kt_ckd4_2021') _tab _tab _tab %3.1f (`percent_kt_ckd4_2022') _n(2)
file write tablecontent _tab ("KRT unclear") _tab _tab (`unclear_ckd4_2017') _tab _tab _tab (`unclear_ckd4_2018') _tab _tab _tab (`unclear_ckd4_2019') _tab _tab _tab (`unclear_ckd4_2020') _tab _tab _tab (`unclear_ckd4_2021') _tab _tab _tab (`unclear_ckd4_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_unclear_ckd4_2017') _tab _tab _tab %3.1f (`percent_unclear_ckd4_2018') _tab _tab _tab %3.1f (`percent_unclear_ckd4_2019') _tab _tab _tab %3.1f (`percent_unclear_ckd4_2020') _tab _tab _tab %3.1f (`percent_unclear_ckd4_2021') _tab _tab _tab %3.1f (`percent_unclear_ckd4_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_ckd4_2017') _tab _tab _tab (`deceased_ckd4_2018') _tab _tab _tab (`deceased_ckd4_2019') _tab _tab _tab (`deceased_ckd4_2020') _tab _tab _tab (`deceased_ckd4_2021') _tab _tab _tab (`deceased_ckd4_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_ckd4_2017') _tab _tab _tab %3.1f (`percent_deceased_ckd4_2018') _tab _tab _tab %3.1f (`percent_deceased_ckd4_2019') _tab _tab _tab %3.1f (`percent_deceased_ckd4_2020') _tab _tab _tab %3.1f (`percent_deceased_ckd4_2021') _tab _tab _tab %3.1f (`percent_deceased_ckd4_2022') _n(2)

*Dialysis
file write tablecontent ("Dialysis") _tab _tab (`baseline_dialysis_2017') _tab _tab _tab (`baseline_dialysis_2018') _tab _tab _tab (`baseline_dialysis_2019') _tab _tab _tab (`baseline_dialysis_2020') _tab _tab _tab (`baseline_dialysis_2021') _tab _tab _tab (`baseline_dialysis_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_dialysis_2017') _tab _tab _tab (`none_dialysis_2018') _tab _tab _tab (`none_dialysis_2019') _tab _tab _tab (`none_dialysis_2020') _tab _tab _tab (`none_dialysis_2021') _tab _tab _tab (`none_dialysis_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_dialysis_2017') _tab _tab _tab %3.1f (`percent_none_dialysis_2018') _tab _tab _tab %3.1f (`percent_none_dialysis_2019') _tab _tab _tab %3.1f (`percent_none_dialysis_2020') _tab _tab _tab %3.1f (`percent_none_dialysis_2021') _tab _tab _tab %3.1f (`percent_none_dialysis_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab (`kt_dialysis_2017') _tab _tab _tab (`kt_dialysis_2018') _tab _tab _tab (`kt_dialysis_2019') _tab _tab _tab (`kt_dialysis_2020') _tab _tab _tab (`kt_dialysis_2021') _tab _tab _tab (`kt_dialysis_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_kt_dialysis_2017') _tab _tab _tab %3.1f (`percent_kt_dialysis_2018') _tab _tab _tab %3.1f (`percent_kt_dialysis_2019') _tab _tab _tab %3.1f (`percent_kt_dialysis_2020') _tab _tab _tab %3.1f (`percent_kt_dialysis_2021') _tab _tab _tab %3.1f (`percent_kt_dialysis_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_dialysis_2017') _tab _tab _tab (`deceased_dialysis_2018') _tab _tab _tab (`deceased_dialysis_2019') _tab _tab _tab (`deceased_dialysis_2020') _tab _tab _tab (`deceased_dialysis_2021') _tab _tab _tab (`deceased_dialysis_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_dialysis_2017') _tab _tab _tab %3.1f (`percent_deceased_dialysis_2018') _tab _tab _tab %3.1f (`percent_deceased_dialysis_2019') _tab _tab _tab %3.1f (`percent_deceased_dialysis_2020') _tab _tab _tab %3.1f (`percent_deceased_dialysis_2021') _tab _tab _tab %3.1f (`percent_deceased_dialysis_2022') _n(2)

*Kidney Transplant
file write tablecontent ("Transplant") _tab _tab (`baseline_kt_2017') _tab _tab _tab (`baseline_kt_2018') _tab _tab _tab (`baseline_kt_2019') _tab _tab _tab (`baseline_kt_2020') _tab _tab _tab (`baseline_kt_2021') _tab _tab _tab (`baseline_kt_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_kt_2017') _tab _tab _tab (`none_kt_2018') _tab _tab _tab (`none_kt_2019') _tab _tab _tab (`none_kt_2020') _tab _tab _tab (`none_kt_2021') _tab _tab _tab (`none_kt_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_kt_2017') _tab _tab _tab %3.1f (`percent_none_kt_2018') _tab _tab _tab %3.1f (`percent_none_kt_2019') _tab _tab _tab %3.1f (`percent_none_kt_2020') _tab _tab _tab %3.1f (`percent_none_kt_2021') _tab _tab _tab %3.1f (`percent_none_kt_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_kt_2017') _tab _tab _tab (`dialysis_kt_2018') _tab _tab _tab (`dialysis_kt_2019') _tab _tab _tab (`dialysis_kt_2020') _tab _tab _tab (`dialysis_kt_2021') _tab _tab _tab (`dialysis_kt_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_kt_2017') _tab _tab _tab %3.1f (`percent_dialysis_kt_2018') _tab _tab _tab %3.1f (`percent_dialysis_kt_2019') _tab _tab _tab %3.1f (`percent_dialysis_kt_2020') _tab _tab _tab %3.1f (`percent_dialysis_kt_2021') _tab _tab _tab %3.1f (`percent_dialysis_kt_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_kt_2017') _tab _tab _tab (`deceased_kt_2018') _tab _tab _tab (`deceased_kt_2019') _tab _tab _tab (`deceased_kt_2020') _tab _tab _tab (`deceased_kt_2021') _tab _tab _tab (`deceased_kt_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_kt_2017') _tab _tab _tab %3.1f (`percent_deceased_kt_2018') _tab _tab _tab %3.1f (`percent_deceased_kt_2019') _tab _tab _tab %3.1f (`percent_deceased_kt_2020') _tab _tab _tab %3.1f (`percent_deceased_kt_2021') _tab _tab _tab %3.1f (`percent_deceased_kt_2022') _n(2)

*KRT unclear modality
file write tablecontent ("KRT unclear") _tab _tab (`baseline_unclear_2017') _tab _tab _tab (`baseline_unclear_2018') _tab _tab _tab (`baseline_unclear_2019') _tab _tab _tab (`baseline_unclear_2020') _tab _tab _tab (`baseline_unclear_2021') _tab _tab _tab (`baseline_unclear_2022') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_unclear_2017') _tab _tab _tab (`none_unclear_2018') _tab _tab _tab (`none_unclear_2019') _tab _tab _tab (`none_unclear_2020') _tab _tab _tab (`none_unclear_2021') _tab _tab _tab (`none_unclear_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_none_unclear_2017') _tab _tab _tab %3.1f (`percent_none_unclear_2018') _tab _tab _tab %3.1f (`percent_none_unclear_2019') _tab _tab _tab %3.1f (`percent_none_unclear_2020') _tab _tab _tab %3.1f (`percent_none_unclear_2021') _tab _tab _tab %3.1f (`percent_none_unclear_2022') _n(2)
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_unclear_2017') _tab _tab _tab (`dialysis_unclear_2018') _tab _tab _tab (`dialysis_unclear_2019') _tab _tab _tab (`dialysis_unclear_2020') _tab _tab _tab (`dialysis_unclear_2021') _tab _tab _tab (`dialysis_unclear_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_dialysis_unclear_2017') _tab _tab _tab %3.1f (`percent_dialysis_unclear_2018') _tab _tab _tab %3.1f (`percent_dialysis_unclear_2019') _tab _tab _tab %3.1f (`percent_dialysis_unclear_2020') _tab _tab _tab %3.1f (`percent_dialysis_unclear_2021') _tab _tab _tab %3.1f (`percent_dialysis_unclear_2022') _n(2)
file write tablecontent _tab ("Transplant") _tab _tab (`kt_unclear_2017') _tab _tab _tab (`kt_unclear_2018') _tab _tab _tab (`kt_unclear_2019') _tab _tab _tab (`kt_unclear_2020') _tab _tab _tab (`kt_unclear_2021') _tab _tab _tab (`kt_unclear_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_kt_unclear_2017') _tab _tab _tab %3.1f (`percent_kt_unclear_2018') _tab _tab _tab %3.1f (`percent_kt_unclear_2019') _tab _tab _tab %3.1f (`percent_kt_unclear_2020') _tab _tab _tab %3.1f (`percent_kt_unclear_2021') _tab _tab _tab %3.1f (`percent_kt_unclear_2022') _n(2)
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_unclear_2017') _tab _tab _tab (`deceased_unclear_2018') _tab _tab _tab (`deceased_unclear_2019') _tab _tab _tab (`deceased_unclear_2020') _tab _tab _tab (`deceased_unclear_2021') _tab _tab _tab (`deceased_unclear_2022') _n
file write tablecontent _tab ("%") _tab _tab _tab %3.1f (`percent_deceased_unclear_2017') _tab _tab _tab %3.1f (`percent_deceased_unclear_2018') _tab _tab _tab %3.1f (`percent_deceased_unclear_2019') _tab _tab _tab %3.1f (`percent_deceased_unclear_2020') _tab _tab _tab %3.1f (`percent_deceased_unclear_2021') _tab _tab _tab %3.1f (`percent_deceased_unclear_2022') _n(2)

file close tablecontent

**Redact counts of 0 from each column in table (adapted from code by Emily Herrett)
clear
import delimited ./output/ckd_progression.csv
local columns " "april_2017" "end_20172018" "april_2018" "end_20182019" "april_2019" "end_20192020" "april_2020" "end_20202021" "april_2021" "end_20212022" "april_2022" "end_20222023" "
foreach col in `columns' {
replace `col'_n=. if `col'_n==0
}
local columns " "end_20172018" "end_20182019" "end_20192020" "end_20202021" "end_20212022" "end_20222023" "
foreach col in `columns' {
replace `col'_pc=. if `col'_pc==0
}
	
export delimited "./output/ckd_progression.csv", replace