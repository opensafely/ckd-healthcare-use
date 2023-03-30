sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
cap log close
macro drop hr
log using ./logs/2020_01_ckd_progression.log, replace t

cap file close tablecontent
file open tablecontent using ./output/2020_01_ckd_progression.csv, write text replace

**Column headings
*There are three column headings for each year 2017-2022:
*Column 1 = the number of people in each CKD group as of the beginning of each year (i.e. in April)
*Column 2 = the number of people who remain within the same CKD group, progress to a more advanced CKD group, or die by the end of the year (i.e. by the subsequent April)
*Column 3 = Column 2 as a percentage of Column 1
file write tablecontent _tab _tab ("n_2020_01") _tab ("january 2021") _n(2)

use ./output/2020_01_ckd_complete.dta, clear

**Disclosure minimisation
*safecount provides a count with any counts <=5 returned at "<=5"
*round(r(N),5) rounds counts to the nearest 5 with any counts <=5 returned as "."

**Overall
qui safecount
local baseline_ckd = round(r(N),5)
*Total number of people in group who do not progress by the end of the year
qui safecount if ckd_progression==0
local none_ckd = round(r(N),5)
*Total number of people in group who progress to CKD stage 3 by the end of the year
qui safecount if ckd_progression==1
local ckd3_ckd = round(r(N),5)
*Total number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui safecount if ckd_progression==2
local ckd4_ckd = round(r(N),5)
*Total number of people in group who progress to dialysis by the end of the year
qui safecount if ckd_progression==3
local dialysis_ckd = round(r(N),5)
*Total number of people in group who progress to kidney kt by the end of the year
qui safecount if ckd_progression==4
local kt_ckd = round(r(N),5)
*Total number of people in group who progress to KRT (unclear modality) by the end of the year
qui safecount if ckd_progression==5
local unclear_ckd = round(r(N),5)
*Total number of people in group who die by the end of the year
qui safecount if ckd_progression==6
local deceased_ckd = round(r(N),5)

**eGFR >60 with albuminuria
*Number of people in group (baseline_ckd2) at the beginning of each year ckd2
qui safecount if ckd_group==1
local baseline_ckd2 = round(r(N),5)
*Number of people in group who do not progress by the end of the year
qui safecount if ckd_group==1 & ckd_progression==0
local none_ckd2 = round(r(N),5)
*Number of people in group who progress to CKD stage 3 by the end of the year
qui safecount if ckd_group==1 & ckd_progression==1
local ckd3_ckd2 = round(r(N),5)
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui safecount if ckd_group==1 & ckd_progression==2
local ckd4_ckd2 = round(r(N),5)
*Number of people in group who progress to dialysis by the end of the year
qui safecount if ckd_group==1 & ckd_progression==3
local dialysis_ckd2 = round(r(N),5)
*Number of people in group who progress to kidney kt by the end of the year
qui safecount if ckd_group==1 & ckd_progression==4
local kt_ckd2 = round(r(N),5)
*Number of people in group who progress to KRT (unclear modality) by the end of the year
qui safecount if ckd_group==1 & ckd_progression==5
local unclear_ckd2 = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==1 & ckd_progression==6
local deceased_ckd2 = round(r(N),5)

**CKD stage 3
*Number of people in group (baseline_ckd3) at the beginning of each year ckd3
qui safecount if ckd_group==2
local baseline_ckd3 = round(r(N),5)
*Number of people in group who do not progress by the end of the year
qui safecount if ckd_group==2 & ckd_progression==0
local none_ckd3 = round(r(N),5)
*Number of people in group who progress to CKD stage 4/5 (without KRT) by the end of the year
qui safecount if ckd_group==2 & ckd_progression==2
local ckd4_ckd3 = round(r(N),5)
*Number of people in group who progress to dialysis by the end of the year
qui safecount if ckd_group==2 & ckd_progression==3
local dialysis_ckd3 = round(r(N),5)
*Number of people in group who progress to kidney transplant by the end of the year
qui safecount if ckd_group==2 & ckd_progression==4
local kt_ckd3 = round(r(N),5)
*Number of people in group who progress to KRT (unclear modality) by the end of the year
qui safecount if ckd_group==2 & ckd_progression==5
local unclear_ckd3 = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==2 & ckd_progression==6
local deceased_ckd3 = round(r(N),5)

**CKD stage 4/5 without KRT
*Number of people in group (baseline_ckd4) at the beginning of each year ckd4
qui safecount if ckd_group==3
local baseline_ckd4 = round(r(N),5)
*Number of people in group who do not progress by the end of the year
qui safecount if ckd_group==3 & ckd_progression==0
local none_ckd4 = round(r(N),5)
*Number of people in group who progress to dialysis by the end of the year
qui safecount if ckd_group==3 & ckd_progression==3
local dialysis_ckd4 = round(r(N),5)
*Number of people in group who progress to kidney transplant by the end of the year
qui safecount if ckd_group==3 & ckd_progression==4
local kt_ckd4 = round(r(N),5)
*Number of people in group who progress to KRT (unclear modality) by the end of the year
qui safecount if ckd_group==3 & ckd_progression==5
local unclear_ckd4 = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==3 & ckd_progression==6
local deceased_ckd4 = round(r(N),5)

**Dialysis
*Number of people in group (baseline_dialysis) at the beginning of each year dialysis
qui safecount if ckd_group==4
local baseline_dialysis = round(r(N),5)
*Number of people in group remaining on dialysis by the end of the year
qui safecount if ckd_group==4 & ckd_progression==0
local none_dialysis = round(r(N),5)
*Number of people in group with kidney transplant by the end of the year
qui safecount if ckd_group==4 & ckd_progression==4
local kt_dialysis = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==4 & ckd_progression==6
local deceased_dialysis = round(r(N),5)

**Kidney transplant
*Number of people in group (baseline_kt) at the beginning of each year kt
qui safecount if ckd_group==5
local baseline_kt = round(r(N),5)
*Number of people in group remaining with kidney transplant by the end of the year
qui safecount if ckd_group==5 & ckd_progression==0
local none_kt = round(r(N),5)
*Number of people in group on dialysis by the end of the year
qui safecount if ckd_group==5 & ckd_progression==3
local dialysis_kt = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==5 & ckd_progression==6
local deceased_kt = round(r(N),5)

**KRT unclear modality
*Number of people in group (baseline_unclear) at the beginning of each year unclear
qui safecount if ckd_group==6
local baseline_unclear = round(r(N),5)
*Number of people in group remaining in group by the end of the year
qui safecount if ckd_group==6 & ckd_progression==0
local none_unclear = round(r(N),5)
*Number of people in group on dialysis by the end of the year
qui safecount if ckd_group==6 & ckd_progression==3
local dialysis_unclear = round(r(N),5)
*Number of people in group with kidney transplant by the end of the year
qui safecount if ckd_group==6 & ckd_progression==4
local kt_unclear = round(r(N),5)
*Number of people in group who die by the end of the year
qui safecount if ckd_group==6 & ckd_progression==6
local deceased_unclear = round(r(N),5)

**Populate table with redacted counts
*Overall
file write tablecontent ("All CKD groups") _tab _tab (`baseline_ckd') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_ckd') _n
file write tablecontent _tab ("CKD stage 3") _tab _tab (`ckd3_ckd') _tab _n
file write tablecontent _tab ("CKD stage 4/5") _tab _tab (`ckd4_ckd') _n
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_ckd') _n
file write tablecontent _tab ("Transplant") _tab _tab (`kt_ckd') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_ckd') _n(2)

*eGFR >60 with albuminuria
file write tablecontent ("Albuminuria") _tab _tab (`baseline_ckd2') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_ckd2') _n
file write tablecontent _tab ("CKD stage 3") _tab _tab (`ckd3_ckd2') _n
file write tablecontent _tab ("CKD stage 4/5") _tab _tab (`ckd4_ckd2') _n
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_ckd2') _n
file write tablecontent _tab ("Transplant") _tab _tab (`kt_ckd2') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_ckd2') _n(2)

*CKD stage 3
file write tablecontent ("CKD stage 3") _tab _tab (`baseline_ckd3') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_ckd3') _n
file write tablecontent _tab ("CKD stage 4/5") _tab _tab (`ckd4_ckd3') _n
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_ckd3') _n
file write tablecontent _tab ("Transplant") _tab _tab (`kt_ckd3') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_ckd3') _n(2)

*CKD stage 4/5 without KRT
file write tablecontent ("CKD stage 4/5") _tab _tab (`baseline_ckd4') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_ckd4') _n
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_ckd4') _n
file write tablecontent _tab ("Transplant") _tab _tab (`kt_ckd4') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_ckd4') _n(2)

*Dialysis
file write tablecontent ("Dialysis") _tab _tab (`baseline_dialysis') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_dialysis') _n
file write tablecontent _tab ("Transplant") _tab _tab (`kt_dialysis') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_dialysis') _n(2)

*Kidney Transplant
file write tablecontent ("Transplant") _tab _tab (`baseline_kt') _n(2)
file write tablecontent _tab ("No progression") _tab _tab (`none_kt') _n
file write tablecontent _tab ("Dialysis") _tab _tab (`dialysis_kt') _n
file write tablecontent _tab ("Deceased") _tab _tab (`deceased_kt') _n(2)

file close tablecontent

**Redact counts of 0 from each column in table (adapted from code by Emily Herrett)
clear
import delimited ./output/2020_01_ckd_progression.csv
local columns " "n_2020_01" "january2021"  "
foreach col in `columns' {
replace `col'=. if `col'<=5
}
	
export delimited "./output/2020_01_ckd_progression.csv", replace