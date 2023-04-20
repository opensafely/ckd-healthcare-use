sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/ckd_progression_v2_dialysis.log, replace t

cap file close tablecontent
file open tablecontent using ./output/ckd_progression_v2_dialysis.csv, write text replace

**Column headings
*There are two column headings for each year 2017-2023:
*Column 1 = the number of people in each CKD group as of the beginning of each year (i.e. in April)
*Column 2 = the number of people who remain within the same CKD group, progress to another CKD group, or die by the end of the year (i.e. by the subsequent April)
file write tablecontent _tab _tab ("N_2017") _tab ("April_2018") _tab ("N_2018") _tab ("April_2019") _tab ("N_2019") _tab ("April_2020") _tab ("N_2020") _tab ("April_2021") _tab ("N_2021") _tab ("April_2022") _tab ("N_2022") _tab ("April_2023") _tab ("N_2023") _n(2)

**Loops through datasets for each year `x' 2017-2023
local year "2017 2018 2019 2020 2021 2022 2023"
foreach x of local year {
use ./output/`x'_ckd_complete_v2.dta, clear

**Disclosure minimisation
*safecount provides a count with any counts <=5 returned at "<=5"
*round(r(N),5) rounds counts to the nearest 5 with any counts <=5 returned as "."

**CKD stage 4/5 without KRT
*Number of people in group (baseline_ckd4_`x') at the beginning of each year ckd4_`x'
qui safecount if ckd_group==3
local baseline_ckd4_`x' = round(r(N),5)
*Number of people in group who do not progress by the end of the year
qui safecount if ckd_group==3 & ckd_progression==0
local none_ckd4_`x' = round(r(N),5)
*Number of people in group who progress to dialysis by the end of the year
qui safecount if ckd_group==3 & ckd_progression==3
local dialysis_ckd4_`x' = round(r(N),5)
*Number of people in group who progress to kidney transplant by the end of the year
qui safecount if ckd_group==3 & ckd_progression==4
local kt_ckd4_`x' = round(r(N),5)
*Number of people in group who progress to KRT (unclear modality) by the end of the year
qui safecount if ckd_group==3 & ckd_progression==5
local unclear_ckd4_`x' = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==3 & ckd_progression==6
local deceased_ckd4_`x' = round(r(N),5)

**Dialysis
*Number of people in group (baseline_dialysis_`x') at the beginning of each year dialysis_`x'
qui safecount if ckd_group==4
local baseline_dialysis_`x' = round(r(N),5)
*Number of people in group remaining on dialysis by the end of the year
qui safecount if ckd_group==4 & ckd_progression==0
local none_dialysis_`x' = round(r(N),5)
*Number of people in group with kidney transplant by the end of the year
qui safecount if ckd_group==4 & ckd_progression==4
local kt_dialysis_`x' = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==4 & ckd_progression==6
local deceased_dialysis_`x' = round(r(N),5)

**Kidney transplant
*Number of people in group (baseline_kt_`x') at the beginning of each year kt_`x'
qui safecount if ckd_group==5
local baseline_kt_`x' = round(r(N),5)
*Number of people in group remaining with kidney transplant by the end of the year
qui safecount if ckd_group==5 & ckd_progression==0
local none_kt_`x' = round(r(N),5)
*Number of people in group on dialysis by the end of the year
qui safecount if ckd_group==5 & ckd_progression==3
local dialysis_kt_`x' = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==5 & ckd_progression==6
local deceased_kt_`x' = round(r(N),5)

**KRT unclear modality
*Number of people in group (baseline_unclear_`x') at the beginning of each year unclear_`x'
qui safecount if ckd_group==6
local baseline_unclear_`x' = round(r(N),5)
*Number of people in group remaining in group by the end of the year
qui safecount if ckd_group==6 & ckd_progression==0
local none_unclear_`x' = round(r(N),5)
*Number of people in group on dialysis by the end of the year
qui safecount if ckd_group==6 & ckd_progression==3
local dialysis_unclear_`x' = round(r(N),5)
*Number of people in group with kidney transplant by the end of the year
qui safecount if ckd_group==6 & ckd_progression==4
local kt_unclear_`x' = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==6 & ckd_progression==6
local deceased_unclear_`x' = round(r(N),5)
}

**Populate table with redacted counts
*CKD stage 4/5 without KRT
file write tablecontent ("CKD stage 4/5") _tab _tab (`baseline_ckd4_2017') _tab _tab (`baseline_ckd4_2018') _tab _tab (`baseline_ckd4_2019') _tab _tab (`baseline_ckd4_2020') _tab _tab (`baseline_ckd4_2021') _tab _tab (`baseline_ckd4_2022') _tab _tab (`baseline_ckd4_2023') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_ckd4_2017') _tab _tab (`none_ckd4_2018') _tab _tab (`none_ckd4_2019') _tab _tab (`none_ckd4_2020') _tab _tab (`none_ckd4_2021') _tab _tab (`none_ckd4_2022') _n
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_ckd4_2017') _tab _tab (`dialysis_ckd4_2018') _tab _tab (`dialysis_ckd4_2019') _tab _tab (`dialysis_ckd4_2020') _tab _tab (`dialysis_ckd4_2021') _tab _tab (`dialysis_ckd4_2022') _n
file write tablecontent _tab ("Transplant") _tab _tab (`kt_ckd4_2017') _tab _tab (`kt_ckd4_2018') _tab _tab (`kt_ckd4_2019') _tab _tab (`kt_ckd4_2020') _tab _tab (`kt_ckd4_2021') _tab _tab (`kt_ckd4_2022') _n
file write tablecontent _tab ("KRT unclear") _tab _tab (`unclear_ckd4_2017') _tab _tab (`unclear_ckd4_2018') _tab _tab (`unclear_ckd4_2019') _tab _tab (`unclear_ckd4_2020') _tab _tab (`unclear_ckd4_2021') _tab _tab (`unclear_ckd4_2022') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_ckd4_2017') _tab _tab (`deceased_ckd4_2018') _tab _tab (`deceased_ckd4_2019') _tab _tab (`deceased_ckd4_2020') _tab _tab (`deceased_ckd4_2021') _tab _tab (`deceased_ckd4_2022') _n(2)

*Dialysis
file write tablecontent ("Dialysis") _tab _tab (`baseline_dialysis_2017') _tab _tab (`baseline_dialysis_2018') _tab _tab (`baseline_dialysis_2019') _tab _tab (`baseline_dialysis_2020') _tab _tab (`baseline_dialysis_2021') _tab _tab (`baseline_dialysis_2022') _tab _tab (`baseline_dialysis_2023') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_dialysis_2017') _tab _tab (`none_dialysis_2018') _tab _tab (`none_dialysis_2019') _tab _tab (`none_dialysis_2020') _tab _tab (`none_dialysis_2021') _tab _tab (`none_dialysis_2022') _n
file write tablecontent _tab ("Transplant") _tab _tab (`kt_dialysis_2017') _tab _tab (`kt_dialysis_2018') _tab _tab (`kt_dialysis_2019') _tab _tab (`kt_dialysis_2020') _tab _tab (`kt_dialysis_2021') _tab _tab (`kt_dialysis_2022') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_dialysis_2017') _tab _tab (`deceased_dialysis_2018') _tab _tab (`deceased_dialysis_2019') _tab _tab (`deceased_dialysis_2020') _tab _tab (`deceased_dialysis_2021') _tab _tab (`deceased_dialysis_2022') _n(2)

*Kidney Transplant
file write tablecontent ("Transplant") _tab _tab (`baseline_kt_2017') _tab _tab (`baseline_kt_2018') _tab _tab (`baseline_kt_2019') _tab _tab (`baseline_kt_2020') _tab _tab (`baseline_kt_2021') _tab _tab (`baseline_kt_2022') _tab _tab (`baseline_kt_2023') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_kt_2017') _tab _tab (`none_kt_2018') _tab _tab (`none_kt_2019') _tab _tab (`none_kt_2020') _tab _tab (`none_kt_2021') _tab _tab (`none_kt_2022') _n
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_kt_2017') _tab _tab (`dialysis_kt_2018') _tab _tab (`dialysis_kt_2019') _tab _tab (`dialysis_kt_2020') _tab _tab (`dialysis_kt_2021') _tab _tab (`dialysis_kt_2022') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_kt_2017') _tab _tab (`deceased_kt_2018') _tab _tab (`deceased_kt_2019') _tab _tab (`deceased_kt_2020') _tab _tab (`deceased_kt_2021') _tab _tab (`deceased_kt_2022') _n(2)

*KRT unclear modality
file write tablecontent ("KRT unclear") _tab _tab (`baseline_unclear_2017') _tab _tab (`baseline_unclear_2018') _tab _tab (`baseline_unclear_2019') _tab _tab (`baseline_unclear_2020') _tab _tab (`baseline_unclear_2021') _tab _tab (`baseline_unclear_2022') _tab _tab (`baseline_unclear_2023') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_unclear_2017') _tab _tab (`none_unclear_2018') _tab _tab (`none_unclear_2019') _tab _tab (`none_unclear_2020') _tab _tab (`none_unclear_2021') _tab _tab (`none_unclear_2022') _n
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_unclear_2017') _tab _tab (`dialysis_unclear_2018') _tab _tab (`dialysis_unclear_2019') _tab _tab (`dialysis_unclear_2020') _tab _tab (`dialysis_unclear_2021') _tab _tab (`dialysis_unclear_2022') _n
file write tablecontent _tab ("Transplant") _tab _tab (`kt_unclear_2017') _tab _tab (`kt_unclear_2018') _tab _tab (`kt_unclear_2019') _tab _tab (`kt_unclear_2020') _tab _tab (`kt_unclear_2021') _tab _tab (`kt_unclear_2022') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_unclear_2017') _tab _tab (`deceased_unclear_2018') _tab _tab (`deceased_unclear_2019') _tab _tab (`deceased_unclear_2020') _tab _tab (`deceased_unclear_2021') _tab _tab (`deceased_unclear_2022')

file close tablecontent

**Redact counts of 0 from each column in table (adapted from code by Emily Herrett)
clear
import delimited ./output/ckd_progression_v2_dialysis.csv
local columns " "n_2017" "april_2018" "n_2018" "april_2019" "n_2019" "april_2020" "n_2020" "april_2021" "n_2021" "april_2022" "n_2022" "april_2023" "n_2023" "
foreach col in `columns' {
replace `col'=. if `col'<=5
}
	
export delimited "./output/ckd_progression_v2_dialysis.csv", replace