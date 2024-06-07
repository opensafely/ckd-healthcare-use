sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd
**Loops through datasets for each year 2017-2018 to 2022-2023
* `dataset' specifies year from project.yaml script
local dataset `1'
cap log close
macro drop hr
log using ./logs/healthcare_use_counts_overall.log, replace t
cap file close tablecontent
**Creates output file for each year (`dataset')
file open tablecontent using ./output/healthcare_use_counts_overall.csv, write text replace
**Column headings
file write tablecontent ("Date") _tab ("ip") _tab ("icu") _tab ("ed") _tab ("opd") _tab ("neph") _tab ("tx") _tab ("gp") _tab ("icd1") _tab ("icd2") _tab ("icd3") _tab ("icd4") _tab ("icd5") _tab ("icd6") _tab ("icd7") _tab ("icd8") _tab ("icd9") _tab ("icd10") _tab ("icd11") _tab ("icd12") _tab ("icd13") _tab ("icd14") _tab ("icd15") _tab ("icd16") _tab ("icd17") _tab ("icd18") _tab ("icd19") _tab ("icd20") _tab ("icd21") _tab ("icd22") _n

local year "2017 2018 2019 2020 2021 2022"
foreach x of local year {
file write tablecontent ("01/04/`x'") _tab
use ./output/`x'_ckd_complete.dta, clear
foreach binary of varlist admitted_patients critical_care_patients emergency_patients op_patients neph_patients tx_patients gp_patients icd1 icd2 icd3 icd4 icd5 icd6 icd7 icd8 icd9 icd10 icd11 icd12 icd13 icd14 icd15 icd16 icd17 icd18 icd19 icd20 icd21 icd22 {
qui safecount if `binary'==1
local `x'_`binary' = round(r(N),5)
}
file write tablecontent (``x'_admitted_patients') _tab (``x'_critical_care_patients') _tab (``x'_emergency_patients') _tab (``x'_op_patients') _tab (``x'_neph_patients') _tab (``x'_tx_patients') _tab (``x'_gp_patients') _tab (``x'_icd1') _tab (``x'_icd2') _tab (``x'_icd3') _tab (``x'_icd4') _tab (``x'_icd5') _tab (``x'_icd6') _tab (``x'_icd7') _tab (``x'_icd8') _tab (``x'_icd9') _tab (``x'_icd10') _tab (``x'_icd11') _tab (``x'_icd12') _tab (``x'_icd13') _tab (``x'_icd14') _tab (``x'_icd15') _tab (``x'_icd16') _tab (``x'_icd17') _tab (``x'_icd18') _tab (``x'_icd19') _tab (``x'_icd20') _tab (``x'_icd21') _tab (``x'_icd22') _n
}

file close tablecontent

import delimited ./output/healthcare_use_counts_overall.csv, clear
local columns ""ip" "icu" "ed" "opd" "neph" "tx" "gp" "icd1" "icd2" "icd3" "icd4" "icd5" "icd6" "icd7" "icd8" "icd9" "icd10" "icd11" "icd12" "icd13" "icd14" "icd15" "icd16" "icd17" "icd18" "icd19" "icd20" "icd21" "icd22""
foreach col of local columns {
    replace `col' = . if `col' <= 5
}


export delimited "./output/healthcare_use_counts_overall.csv", replace
