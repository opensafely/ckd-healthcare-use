clear all
capture log close

* create a filename global that can be used throughout the file
global filename "healthcare_needs"

* open log file - no need as fast tool will create log files
log using "./logs/${filename}", text replace

/*******************************************************************************
#1. Utility program
*******************************************************************************/
* prog to get the N's, pyar, number of failures, and HR (99% CIs) out in the appropriate format as 
* local macros from the r(table) returned by a regression command
* called by giving: 
* 	- matrix name containing r(table) contents
* 	- the type of cancer - to be used in the name of the global macros containing the output
*	- the name of the model - to be used in name of global macros containing the output
* e.g. to call:
* 	getstuff matrixname cancertype modelname
cap prog drop getstuff
program define getstuff
	local matrixname `1'
	local year `2'
	local outcome `3'
	
	* pull out number (number per patient)
	
	
	* pull out HR (99% CI)
	local b : display %04.2f table[1,2]
	local ll : display %04.2f table[5,2]
	local ul : display %04.2f table[6,2]
	
	global `model'_`cancertype'_hr "`b' (`ll', `ul')"	
	
	* pull out n's
	foreach grp in exp unexp {
		if "`grp'"=="exp" stdescribe if exposed==1
		if "`grp'"=="unexp" stdescribe if exposed==0
		
		global `model'_`cancertype'_`grp'_n = string(`r(N_sub)', "%12.0gc") // number of subjects
		global `model'_`cancertype'_`grp'_pyar = string(`r(tr)', "%9.0fc") // total time at risk
		global `model'_`cancertype'_`grp'_fail = string(`r(N_fail)', "%12.0gc") // total number of failures	
	} /*foreach grp in all exp unexp*/

end /*end of getstuff program*/


/*******************************************************************************
#A1. Open dataset and set up column headers in output file
*******************************************************************************/
use ./output/2017_ckd_complete.dta, clear 

* create excel file
putexcel set "results/${filename}.xlsx", sheet(Table 1) replace

* set row count variable
local rowcount=1

* Table title
putexcel A`rowcount'="Healthcare needs by CKD group 2017/2018 to 2021/2022", bold
local ++rowcount // increment row couter variable

* set up column headers
putexcel (D`rowcount':H`rowcount'), merge hcenter vcenter
putexcel (I`rowcount':M`rowcount'), merge hcenter vcenter
putexcel (N`rowcount':R`rowcount'), merge hcenter vcenter
putexcel (S`rowcount':W`rowcount'), merge hcenter vcenter
putexcel (X`rowcount':AB`rowcount'), merge hcenter vcenter
putexcel D`rowcount'="2017-2018", border(top, thin, black)
putexcel D`rowcount', border(left, thin, black)
putexcel E`rowcount', border(top, thin, black)
putexcel F`rowcount', border(top, thin, black)
putexcel G`rowcount', border(top, thin, black)
putexcel H`rowcount', border(top, thin, black)
putexcel H`rowcount', border(right, thin, black)
putexcel I`rowcount'="2018-2019", bold hcenter border(top, thin, black)
putexcel I`rowcount', border(left, thin, black)
putexcel J`rowcount', border(top, thin, black)
putexcel K`rowcount', border(top, thin, black)
putexcel L`rowcount', border(top, thin, black)
putexcel M`rowcount', border(top, thin, black)
putexcel M`rowcount', border(right, thin, black)
putexcel N`rowcount'="2019-2020", bold hcenter border(top, thin, black)
putexcel N`rowcount', border(left, thin, black)
putexcel O`rowcount', border(top, thin, black)
putexcel P`rowcount', border(top, thin, black)
putexcel Q`rowcount', border(top, thin, black)
putexcel R`rowcount', border(top, thin, black)
putexcel R`rowcount', border(right, thin, black)
putexcel S`rowcount'="2020-2021", bold hcenter border(top, thin, black)
putexcel S`rowcount', border(left, thin, black)
putexcel T`rowcount', border(top, thin, black)
putexcel U`rowcount', border(top, thin, black)
putexcel V`rowcount', border(top, thin, black)
putexcel W`rowcount', border(top, thin, black)
putexcel W`rowcount', border(right, thin, black)
putexcel X`rowcount'="2021-2022", bold hcenter border(top, thin, black)
putexcel X`rowcount', border(left, thin, black)
putexcel Y`rowcount', border(top, thin, black)
putexcel Z`rowcount', border(top, thin, black)
putexcel AA`rowcount', border(top, thin, black)
putexcel AB`rowcount', border(top, thin, black)
putexcel AB`rowcount', border(right, thin, black)

local ++rowcount
putexcel (A`rowcount':C`rowcount'), merge hcenter vcenter
putexcel D`rowcount'="April 2017", bold hcenter border(all, thin, black)
putexcel E`rowcount'="July 2017", bold hcenter border(all, thin, black)
putexcel F`rowcount'="October 2017", bold hcenter border(all, thin, black)
putexcel G`rowcount'="January 2018", bold hcenter border(all, thin, black)
putexcel H`rowcount'="April 2018", bold hcenter border(all, thin, black)
putexcel I`rowcount'="April 2018", bold hcenter border(all, thin, black)
putexcel J`rowcount'="July 2018", bold hcenter border(all, thin, black)
putexcel K`rowcount'="October 2018", bold hcenter border(all, thin, black)
putexcel L`rowcount'="January 2019", bold hcenter border(all, thin, black)
putexcel M`rowcount'="April 2019", bold hcenter border(all, thin, black)
putexcel N`rowcount'="April 2019", bold hcenter border(all, thin, black)
putexcel O`rowcount'="July 2019", bold hcenter border(all, thin, black)
putexcel P`rowcount'="October 2019", bold hcenter border(all, thin, black)
putexcel Q`rowcount'="January 2020", bold hcenter border(all, thin, black)
putexcel R`rowcount'="April 2020", bold hcenter border(all, thin, black)
putexcel S`rowcount'="April 2020", bold hcenter border(all, thin, black)
putexcel T`rowcount'="July 2020", bold hcenter border(all, thin, black)
putexcel U`rowcount'="October 2020", bold hcenter border(all, thin, black)
putexcel V`rowcount'="January 2021", bold hcenter border(all, thin, black)
putexcel W`rowcount'="April 2021", bold hcenter border(all, thin, black)
putexcel X`rowcount'="April 2021", bold hcenter border(all, thin, black)
putexcel Y`rowcount'="July 2021", bold hcenter border(all, thin, black)
putexcel Z`rowcount'="October 2021", bold hcenter border(all, thin, black)
putexcel AA`rowcount'="January 2022", bold hcenter border(all, thin, black)
putexcel AB`rowcount'="April 2022", bold hcenter border(all, thin, black)

local ++rowcount
putexcel (A`rowcount':A14), merge hcenter vcenter
putexcel A`rowcount'="eGFR >60 with proteinuria", bold hcenter vcenter border(all, thin, black)
putexcel (B`rowcount':C`rowcount'), merge
putexcel B`rowcount'="Number at April of each year", bold txtwrap border(top, thin, black) fpattern(solid, lightgray)
putexcel B`rowcount', border (left, thin, black)
putexcel C`rowcount', border(top, thin, black)
putexcel C`rowcount', border(right, thin, black)
unique patient_id if ckd_group==3
local n = string(`r(unique)', "%12.0gc")
putexcel D`rowcount'="`n'", hcenter border(all, thin, black)
putexcel (E`rowcount':H`rowcount'), merge fpattern(solid, lightgray)
putexcel E`rowcount', border(top, thin, black)
putexcel F`rowcount', border(top, thin, black)
putexcel G`rowcount', border(top, thin, black)
putexcel H`rowcount', border(top, thin, black)
use ./output/2018_ckd_complete.dta, clear 
unique patient_id if ckd_group==3
local n = string(`r(unique)', "%12.0gc")
putexcel I`rowcount'="`n'", hcenter border(all, thin, black)
putexcel (J`rowcount':M`rowcount'), merge fpattern(solid, lightgray)
putexcel J`rowcount', border(top, thin, black)
putexcel K`rowcount', border(top, thin, black)
putexcel L`rowcount', border(top, thin, black)
putexcel M`rowcount', border(top, thin, black)
use ./output/2019_ckd_complete.dta, clear 
unique patient_id if ckd_group==3
local n = string(`r(unique)', "%12.0gc")
putexcel N`rowcount'="`n'", hcenter border(all, thin, black)
putexcel (O`rowcount':R`rowcount'), merge fpattern(solid, lightgray)
putexcel O`rowcount', border(top, thin, black)
putexcel P`rowcount', border(top, thin, black)
putexcel Q`rowcount', border(top, thin, black)
putexcel R`rowcount', border(top, thin, black)
use ./output/2020_ckd_complete.dta, clear 
unique patient_id if ckd_group==3
local n = string(`r(unique)', "%12.0gc")
putexcel S`rowcount'="`n'", hcenter border(all, thin, black)
putexcel (T`rowcount':W`rowcount'), merge fpattern(solid, lightgray)
putexcel T`rowcount', border(top, thin, black)
putexcel U`rowcount', border(top, thin, black)
putexcel V`rowcount', border(top, thin, black)
putexcel W`rowcount', border(top, thin, black)
use ./output/2021_ckd_complete.dta, clear 
unique patient_id if ckd_group==3
local n = string(`r(unique)', "%12.0gc")
putexcel X`rowcount'="`n'", hcenter border(all, thin, black)
putexcel (Y`rowcount':AB`rowcount'), merge fpattern(solid, lightgray)
putexcel Y`rowcount', border(top, thin, black)
putexcel Z`rowcount', border(top, thin, black)
putexcel AA`rowcount', border(top, thin, black)
putexcel AB`rowcount', border(top, thin, black)

local ++rowcount
putexcel (B`rowcount':B14), merge hcenter vcenter
putexcel B`rowcount'="Healthcare needs by quarter", hcenter vcenter border(all, thin, black)
putexcel C`rowcount'="Inpatient days (days per patient)", left border(all, thin, black)
putexcel (D`rowcount':D14), merge fpattern(solid, lightgray)

foreach year in 2017 2018 2019 2020 2021 {
	if "`year'"=="cohort" { // whole cohort
		unique patient_id if sex==2
		local denom=$ncohort
		local col "B"
	}


* loop through cohort, exp and unexp
foreach group in cohort exp unexp {
	if "`group'"=="cohort" { // whole cohort
		unique patid if sex==2
		local denom=$ncohort
		local col "B"
	}
	if "`group'"=="exp" { // exposed
		unique patid if sex==2 & exposed==1
		local denom=$nexp
		local col "C"
	}
	if "`group'"=="unexp" { // unexp
		unique patid if sex==2 & exposed==0
		local denom=$nunexp
		local col "D"
	}
	local n=string(`r(unique)',"%12.0gc")
	local percent=string((`r(unique)'/`denom')*100, "%4.1f")
	local female "`n' (`percent'%)"
	
	putexcel `col'`rowcount'="`female'",  hcenter
} /*end foreach group in cohort exp unexp*/

local ++rowcount


/*******************************************************************************
#A2. Ns and pyar 
*******************************************************************************/
/*------------------------------------------------------------------------------
#2.1 Ns 
------------------------------------------------------------------------------*/
* border on first cell
putexcel A`rowcount'="", border(bottom, thin, black)

* whole cohort
unique patid
global ncohort=r(unique) // for percentage calc later
local n = string(`r(unique)',"%12.0gc")
putexcel B`rowcount'="n=`n'", hcenter border(bottom, thin, black) // alternative: putexcel B`rowcount'=`r(unique)', nformat(#,###)

* exposed
unique patid if exposed==1
global nexp=r(unique)
local n = string(`r(unique)',"%12.0gc")
putexcel C`rowcount'="n=`n'", hcenter border(bottom, thin, black)

* unexposed
unique patid if exposed==0
global nunexp=r(unique)
local n = string(`r(unique)',"%12.0gc")
putexcel D`rowcount'="n=`n'", hcenter border(bottom, thin, black)

local ++rowcount




/*------------------------------------------------------------------------------
#2.2 pyar 
	- total
	- median
	- mean
------------------------------------------------------------------------------*/
* fu for each observation
gen fu_time=_t-_t0 // fu time duration

* loop through whole cohort, exposed and unexposed
foreach group in cohort exp unexp {
	preserve
		* keep relevant patids
		if "`group'"=="exp" keep if exposed==1
		if "`group'"=="unexp" keep if exposed==0
		
		* collapse
		collapse (sum)fu_time, by(patid)
		summ fu_time, detail 
		
		* total
		global `group'_pyar=`r(sum)'
		
		* mean
		local meanfu=string(`r(mean)', "%4.1f")
		local sdfu=string(`r(sd)', "%4.1f")
		global `group'_meanfu "`meanfu' (`sdfu')"
		
		* median
		local p50=string(`r(p50)', "%4.1f")
		local p25=string(`r(p25)', "%4.1f")
		local p75=string(`r(p75)', "%4.1f")
		global `group'_median "`p50' (`p25'-`p75')"	
	restore
} /*end foreach group in cohort exp unexp*/


* put data in excel file
putexcel A`rowcount'="Follow-up*", bold
local ++rowcount

* total person years
putexcel A`rowcount'="Total person-years"
foreach group in cohort exp unexp {
	if "`group'"=="cohort" local col "B"
	if "`group'"=="exp" local col "C"
	if "`group'"=="unexp" local col "D"

	local pyar ${`group'_pyar}
	putexcel `col'`rowcount'=`pyar', hcenter nformat(#,###0)
} /*end foreach group in cohort exp unexp*/
local ++rowcount

* median
putexcel A`rowcount'="Median (IQR) duration of follow-up (years)"
foreach group in cohort exp unexp {
	if "`group'"=="cohort" local col "B"
	if "`group'"=="exp" local col "C"
	if "`group'"=="unexp" local col "D"

	local median "${`group'_median}"
	putexcel `col'`rowcount'="`median'", hcenter
} /*end foreach group in cohort exp unexp*/
local ++rowcount

* mean
putexcel A`rowcount'="Mean (SD) duration of follow-up (years)"
foreach group in cohort exp unexp {
	if "`group'"=="cohort" local col "B"
	if "`group'"=="exp" local col "C"
	if "`group'"=="unexp" local col "D"

	local mean "${`group'_meanfu}"
	putexcel `col'`rowcount'="`mean'", hcenter
} /*end foreach group in cohort exp unexp*/
local ++rowcount




/*******************************************************************************
#A3. Sex
*******************************************************************************/
putexcel A`rowcount'="Sex", bold
local ++rowcount

putexcel A`rowcount'="Female (%)"

* loop through cohort, exp and unexp
foreach group in cohort exp unexp {
	if "`group'"=="cohort" { // whole cohort
		unique patid if sex==2
		local denom=$ncohort
		local col "B"
	}
	if "`group'"=="exp" { // exposed
		unique patid if sex==2 & exposed==1
		local denom=$nexp
		local col "C"
	}
	if "`group'"=="unexp" { // unexp
		unique patid if sex==2 & exposed==0
		local denom=$nunexp
		local col "D"
	}
	local n=string(`r(unique)',"%12.0gc")
	local percent=string((`r(unique)'/`denom')*100, "%4.1f")
	local female "`n' (`percent'%)"
	
	putexcel `col'`rowcount'="`female'",  hcenter
} /*end foreach group in cohort exp unexp*/

local ++rowcount





/*******************************************************************************
#A4. Age
*******************************************************************************/
* make new age band var with only 3 levels for consistency with Danish 
* studies and for brevity in Table
gen ageband_new=ageband
replace ageband_new=45 if ageband>45 & ageband<64
replace ageband_new=65 if ageband>=65
label define ageband_new 17"18-44" 45"45-64" 65"65+"
label values ageband_new ageband_new
tab ageband ageband_new // check

* keep first record for each patid/indexdate combination
sort patid indexdate date
bysort patid indexdate: keep if _n==1
assert date==indexdate // check

putexcel A`rowcount'="Age (years)**", bold
local ++rowcount

* loop through each ageband
* so that we end up with the ageband covariates in vars: age_`group'_`ageband'
* where group is: cohort, exp or unexp
* and where ageband_new is 17 45 65
levelsof ageband_new, local(levels)
foreach i of local levels {
	foreach group in cohort exp unexp {
		if "`group'"=="cohort" unique patid if ageband_new==`i'
		if "`group'"=="exp" unique patid if ageband_new==`i' & exposed==1
		if "`group'"=="unexp" unique patid if ageband_new==`i' & exposed==0
		
		* use returned results
		local n=string(`r(unique)',"%12.0gc") 
		local percent=string((`r(unique)' / ${n`group'}) * 100, "%4.1f")
		
		* create string for output
		global age_`group'_`i' "`n' (`percent'%)"	
	} /*end foreach group in cohort exp unexp*/
	
	putexcel A`rowcount'="`: label (ageband_new) `i''" // use variable label for row caption
	putexcel B`rowcount'="${age_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${age_exp_`i'}",  hcenter
	putexcel D`rowcount'="${age_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/





/*******************************************************************************
#A5. IMD
*******************************************************************************/
putexcel A`rowcount'="Qunitiles of index of multiple deprivation***", bold
local ++rowcount

* loop through each quintile
forvalues x=1/5 {
	* put in row label
	if `x'==1 putexcel A`rowcount'="1 (least deprived)"
	else if `x'==5 putexcel A`rowcount'="5 (most deprived)"
	else putexcel A`rowcount'="`x'"
	
	* now loop through each quintile
	foreach group in cohort exp unexp {
		if "`group'"=="cohort" unique patid if imd_composite==`x'
		if "`group'"=="exp" unique patid if imd_composite==`x' & exposed==1
		if "`group'"=="unexp" unique patid if imd_composite==`x' & exposed==0
		
		* use returned results
		local n=string(`r(unique)',"%12.0gc") 
		local percent=string((`r(unique)' / ${n`group'}) * 100, "%4.1f")
		
		* create string for output
		global imd_`group'_`x' "`n' (`percent'%)"	
	} /*end foreach group in cohort exp unexp*/	
	
	* put output strings in excel file
	putexcel B`rowcount'="${imd_cohort_`x'}",  hcenter
	putexcel C`rowcount'="${imd_exp_`x'}",  hcenter
	putexcel D`rowcount'="${imd_unexp_`x'}",  hcenter
	
	local ++rowcount
} /*end forvalues x=1/5*/





/*******************************************************************************
#A6. BMI
*******************************************************************************/
putexcel A`rowcount'="Body mass index (kg/m2)****", bold
local ++rowcount

recode bmi_cat 1=0 0=1 2=2 3=3 .=4
label define bmicat3 0"Underweight (<20)" 1"Normal (20-24)" 2"Overweight (25-29)" 3"Obese (30+)" 4"Missing"
label values bmi_cat bmicat3

* loop through each BMI cat
levelsof bmi_cat, local(levels)
foreach i of local levels {
	foreach group in cohort exp unexp {
		if "`group'"=="cohort" unique patid if bmi_cat==`i'
		if "`group'"=="exp" unique patid if bmi_cat==`i' & exposed==1
		if "`group'"=="unexp" unique patid if bmi_cat==`i' & exposed==0
		
		* use returned results
		local n=string(`r(unique)',"%12.0gc") 
		local percent=string((`r(unique)' / ${n`group'}) * 100, "%4.1f")
		
		* create string for output
		global bmi_`group'_`i' "`n' (`percent'%)"	
	} /*end foreach group in cohort exp unexp*/
	
	putexcel A`rowcount'="`: label (bmi_cat) `i''" // use variable label for row caption
	putexcel B`rowcount'="${bmi_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${bmi_exp_`i'}",  hcenter
	putexcel D`rowcount'="${bmi_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/




/*******************************************************************************
#A7. Smoking
*******************************************************************************/
putexcel A`rowcount'="Smoking****", bold
local ++rowcount

* recode smoking status var >> assume current/ex smokers are current smokers
recode smok 0=0 1=1 .=13
label define smok2 0"Non-smoker" 1"Current or ex-smoker" 13"Missing"
label values smok smok2 

* loop through each smoking cat
levelsof smok, local(levels)
foreach i of local levels {
	foreach group in cohort exp unexp {
		if "`group'"=="cohort" unique patid if smok==`i'
		if "`group'"=="exp" unique patid if smok==`i' & exposed==1
		if "`group'"=="unexp" unique patid if smok==`i' & exposed==0
		
		* use returned results
		local n=string(`r(unique)',"%12.0gc") 
		local percent=string((`r(unique)' / ${n`group'}) * 100, "%4.1f")
		
		* create string for output
		global smok_`group'_`i' "`n' (`percent'%)"	
	} /*end foreach group in cohort exp unexp*/
	
	putexcel A`rowcount'="`: label (smok) `i''" // use variable label for row caption
	putexcel B`rowcount'="${smok_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${smok_exp_`i'}",  hcenter
	putexcel D`rowcount'="${smok_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/







/*******************************************************************************
#A8. Alcohol
*******************************************************************************/
putexcel A`rowcount'="Alcohol*****", bold
local ++rowcount


* harmful ETOH use
putexcel A`rowcount'="Harmful alcohol use (%)"

* loop through cohort, exp and unexp
foreach group in cohort exp unexp {
	if "`group'"=="cohort" { // whole cohort
		unique patid if stateharmfulETOH==1
		local denom=$ncohort
		local col "B"
	}
	if "`group'"=="exp" { // exposed
		unique patid if stateharmfulETOH==1 & exposed==1
		local denom=$nexp
		local col "C"
	}
	if "`group'"=="unexp" { // unexp
		unique patid if stateharmfulETOH==1 & exposed==0
		local denom=$nunexp
		local col "D"
	}
	local n=string(`r(unique)',"%12.0gc")
	local percent=string((`r(unique)'/`denom')*100, "%4.1f")
	local harmfulETOH "`n' (`percent'%)"
	
	putexcel `col'`rowcount'="`harmfulETOH'",  hcenter
} /*end foreach group in cohort exp unexp*/

local ++rowcount




/*******************************************************************************
#A9. Ethnicity 
*******************************************************************************/
* recode ethnicity and create new var
recode eth5_new 0=0 1=1 2=2 3=3 4=4 5=5 .=5, gen(ethnicity)
label define ethnicity 0"White" 1"South Asian" 2"Black" 3"Other" 4"Mixed" 5"Not stated or missing"
label values ethnicity ethnicity
tab ethnicity eth5_new, miss

* row caption
putexcel A`rowcount'="Ethnicity", bold
local ++rowcount

* loop through each ethnicity cat
levelsof ethnicity, local(levels)
foreach i of local levels {
	foreach group in cohort exp unexp {
		if "`group'"=="cohort" unique patid if ethnicity==`i'
		if "`group'"=="exp" unique patid if ethnicity==`i' & exposed==1
		if "`group'"=="unexp" unique patid if ethnicity==`i' & exposed==0
		
		* use returned results
		local n=string(`r(unique)',"%12.0gc") 
		local percent=string((`r(unique)' / ${n`group'}) * 100, "%4.1f")
		
		* create string for output
		global eth_`group'_`i' "`n' (`percent'%)"	
	} /*end foreach group in cohort exp unexp*/
	
	putexcel A`rowcount'="`: label (ethnicity) `i''" // use variable label for row caption
	putexcel B`rowcount'="${eth_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${eth_exp_`i'}",  hcenter
	putexcel D`rowcount'="${eth_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/





/*******************************************************************************
#A10. Comorbidities 
*******************************************************************************/

/*------------------------------------------------------------------------------
#10.1 Binary
------------------------------------------------------------------------------*/
putexcel A`rowcount'="Comorbidities*****", bold
local ++rowcount

* loop through each binary covar
foreach comorb in asthma immunosup {
	if "`comorb'"=="asthma" putexcel A`rowcount'="Asthma"
	if "`comorb'"=="immunosup" putexcel A`rowcount'="Immunosuppression"
	
	foreach group in cohort exp unexp {
		if "`group'"=="cohort" unique patid if state`comorb'==1
		if "`group'"=="exp" unique patid if state`comorb'==1 & exposed==1
		if "`group'"=="unexp" unique patid if state`comorb'==1 & exposed==0
		
		* use returned results
		local n=string(`r(unique)',"%12.0gc") 
		local percent=string((`r(unique)' / ${n`group'}) * 100, "%4.1f")
		
		* create string for output
		global `comorb'_`group' "`n' (`percent'%)"	
	} /*end foreach group in cohort exp unexp*/
	
	* put in excel file
	putexcel B`rowcount'="${`comorb'_cohort}",  hcenter
	putexcel C`rowcount'="${`comorb'_exp}",  hcenter
	putexcel D`rowcount'="${`comorb'_unexp}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach comorb in asthma immunosup*/




/*------------------------------------------------------------------------------
#A10.2 DM
------------------------------------------------------------------------------*/
* recode DM var
recode stateDMtype 0=0 1=3 3=1 2=2, gen(dm_new)
label define dm_new 0"No diabetes" 1"Type I" 2"Type II" 3"Type unspecified"
label values dm_new dm_new
tab stateDMtype dm_new, miss

* row caption
putexcel A`rowcount'="Diabetes mellitus*****", bold
local ++rowcount

* loop through each DM cat
levelsof dm_new, local(levels)
foreach i of local levels {
	foreach group in cohort exp unexp {
		if "`group'"=="cohort" unique patid if dm_new==`i'
		if "`group'"=="exp" unique patid if dm_new==`i' & exposed==1
		if "`group'"=="unexp" unique patid if dm_new==`i' & exposed==0
		
		* use returned results
		local n=string(`r(unique)',"%12.0gc") 
		local percent=string((`r(unique)' / ${n`group'}) * 100, "%4.1f")
		
		* create string for output
		global dm_`group'_`i' "`n' (`percent'%)"	
	} /*end foreach group in cohort exp unexp*/
	
	putexcel A`rowcount'="`: label (dm_new) `i''" // use variable label for row caption
	putexcel B`rowcount'="${dm_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${dm_exp_`i'}",  hcenter
	putexcel D`rowcount'="${dm_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/
	


	
	
	
/*******************************************************************************
#A11. Oral glucocorticoid or systemic therapy prescriptions
*******************************************************************************/
putexcel A`rowcount'="Prescriptions*****", bold
local ++rowcount

* loop through each drug
foreach d in statehighGC statesystemicRx {
	if "`d'"=="statehighGC" putexcel A`rowcount'="Oral glucocorticoids (20mg+ predinosolne equivalent dose)"
	if "`d'"=="statesystemicRx" putexcel A`rowcount'="Systemic drugs (azathioprine, ciclosporin, methotrexate, mycophenolate)"

	* loop through each group
	foreach group in cohort exp unexp {
		if "`group'"=="cohort" unique patid if `d'==1
		if "`group'"=="exp" unique patid if `d'==1 & exposed==1
		if "`group'"=="unexp" unique patid if `d'==1 & exposed==0
		
		* use returned results
		local n=string(`r(unique)',"%12.0gc") 
		local percent=string((`r(unique)' / ${n`group'}) * 100, "%4.1f")
		
		* create string for output
		global `d'_`group' "`n' (`percent'%)"	
	} /*end foreach group in cohort exp unexp*/
		
	* put in excel file
	putexcel B`rowcount'="${`d'_cohort}",  hcenter
	putexcel C`rowcount'="${`d'_exp}",  hcenter
	putexcel D`rowcount'="${`d'_unexp}",  hcenter
		
	local ++rowcount // increment row counter so that next iteration of loop put on next row

}/*end foreach d in highGC systemicRx {*/

	
	
* put top border on next row
foreach col in A B C D {
	putexcel `col'`rowcount'="" , border(top, thin, black)
}

local ++rowcount
	




/*******************************************************************************
#A12. Footnotes 
*******************************************************************************/
putexcel A`rowcount'="Individuals can contribute data as both eczema exposed and unexposed. Therefore, numbers of exposed/unexposed do not total the whole cohort, as individuals may be included in more than one column."
local ++rowcount

putexcel A`rowcount'="*Follow-up based on censoring at the earliest of: death, no longer registered with practice, practice no longer contributing to CPRD, or any cancer diagnosis (excluding non-melanoma skin cancer)"
local ++rowcount

putexcel A`rowcount'="IQR: Interquartile range"
local ++rowcount

putexcel A`rowcount'="** age at index date"
local ++rowcount

putexcel A`rowcount'="*** IMD based on individual-level data (from 2007) if available, supplemented with practice-level data (from 2010) if individual-level data not available."
local ++rowcount

putexcel A`rowcount'="**** Smoking and BMI based on records closest to index date."
local ++rowcount

putexcel A`rowcount'="***** Based on records before cohort entry."
local ++rowcount













/*******************************************************************************
********************************************************************************
********************************************************************************
#SECTION B - DATA AS pyar(%)
********************************************************************************
********************************************************************************
*******************************************************************************/


/*******************************************************************************
#B1. Open dataset
*******************************************************************************/
use ${pathOut}/analysis-censor-all_cancer, clear 




/*******************************************************************************
#B2. pyar 
	- total
	- median
	- mean
*******************************************************************************/
* fu for each observation
gen fu_time=_t-_t0 // fu time duration

/*
* no need to run this code as already run in SECTION A
* loop through whole cohort, exposed and unexposed
foreach group in cohort exp unexp {
	preserve
		* keep relevant patids
		if "`group'"=="exp" keep if exposed==1
		if "`group'"=="unexp" keep if exposed==0
		
		* collapse
		collapse (sum)fu_time, by(patid)
		summ fu_time, detail 
		
		* total
		global `group'_pyar=`r(sum)'
		
		* mean
		local meanfu=string(`r(mean)', "%4.1f")
		local sdfu=string(`r(sd)', "%4.1f")
		global `group'_meanfu "`meanfu' (`sdfu')"
		
		* median
		local p50=string(`r(p50)', "%4.1f")
		local p25=string(`r(p25)', "%4.1f")
		local p75=string(`r(p75)', "%4.1f")
		global `group'_median "`p50' (`p25'-`p75')"	
	restore
} /*end foreach group in cohort exp unexp*/
*/





/*******************************************************************************
#B2. recode variables for helpful categories and useful label names
*******************************************************************************/
recode stateDMtype 0=0 1=3 3=1 2=2, gen(dm_new)
label define dm_new 0"No diabetes" 1"Type I" 2"Type II" 3"Type unspecified"
label values dm_new dm_new

recode bmi_cat 1=0 0=1 2=2 3=3 .=4
label define bmicat3 0"Underweight (<20)" 1"Normal (20-24)" 2"Overweight (25-29)" 3"Obese (30+)" 4"Missing"
label values bmi_cat bmicat3

recode smok 0=0 1=1 .=13
label define smoklab2 0"Non-smoker" 1"Current or ex-smoker" 13"Missing"
label values smok smoklab2

recode eth5_new 0=0 1=1 2=2 3=3 4=4 5=5 .=5, gen(ethnicity)
label define ethnicity 0"White" 1"South Asian" 2"Black" 3"Other" 4"Mixed" 5"Not stated or missing"
label values ethnicity ethnicity

gen ageband_new=ageband
replace ageband_new=45 if ageband>45 & ageband<64
replace ageband_new=65 if ageband>=65
label define ageband_new 17"18-44" 45"45-64" 65"65+"
label values ageband_new ageband_new
drop ageband
rename ageband_new ageband



/*******************************************************************************
#B3. Loop through whole cohort, exp and unexposed 
	and identify text for each table cell
*******************************************************************************/
foreach group in cohort exp unexp {
	preserve
		* keep relevant patids
		if "`group'"=="exp" keep if exposed==1
		if "`group'"=="unexp" keep if exposed==0
		
	
		/*--------------------------------------------------------------------------
		#B3.1 Binary covariates
		--------------------------------------------------------------------------*/
		local bincv ""stateasthma" "stateimmunosup" "sex" "stateharmfulETOH" "statehighGC" "statesystemicRx" "
		foreach cv in `bincv' {
			summ fu_time if `cv'==1
			local pyar=string(`r(sum)',"%9.0fc")
			local percent=string((`r(sum)' / ${`group'_pyar}) * 100, "%4.1f" )
			
			* create string for output
			global `cv'_`group' "`pyar' (`percent'%)" 
		}/*end foreach cv in `bincv'*/
		
		
		/*--------------------------------------------------------------------------
		#B3.2 multilevel covariates
		--------------------------------------------------------------------------*/	
		local multicv ""dm_new" "bmi_cat" "smok" "ethnicity" "imd_composite" "
		local multicv "`multicv' "ageband" "calendarperiod" "
		foreach cv in `multicv' {
			levelsof `cv', local(levels)
			foreach i of local levels {
				summ fu_time if `cv'==`i'
				
				* use returned results
				local pyar=string(`r(sum)',"%9.0fc") 
				local percent=string((`r(sum)' / ${`group'_pyar}) * 100, "%4.1f")
				
				* create string for output
				global `cv'_`group'_`i' "`pyar' (`percent'%)"
			} /*end foreach i of local levels*/
		}/*end foreach cv in `multicv'*/
		
/*******************************************************************************
>> end loop and restore dataset
*******************************************************************************/
	restore
} /*end foreach group in cohort exp unexp*/





/*******************************************************************************
#B4. put data into excel
*******************************************************************************/
* add sheet to existing excel file
putexcel set "${pathResults}/${filename}.xlsx", sheet(n_pyar) modify

* set row count variable
local rowcount=1

* Table title
putexcel A`rowcount'="Table x. Person-time under follow-up broken down by patient-level characteristics and atopic eczema exposure status." 
local ++rowcount // increment row couter variable
putexcel A`rowcount'="Values are pyar (percentages) unless stated otherwise"
local ++rowcount // increment row couter variable

* set up column headers
putexcel A`rowcount'="", border(top, thin, black)
putexcel B`rowcount'="Whole cohort", bold hcenter border(top, thin, black)
putexcel C`rowcount'="With atopic eczema", bold hcenter border(top, thin, black)
putexcel D`rowcount'="Without atopic eczema", bold hcenter border(top, thin, black)

local ++rowcount

* put data in excel file
* total person years
putexcel A`rowcount'="Total person-years", border(top, thin, black)
foreach group in cohort exp unexp {
	if "`group'"=="cohort" local col "B"
	if "`group'"=="exp" local col "C"
	if "`group'"=="unexp" local col "D"

	local pyar ${`group'_pyar}
	putexcel `col'`rowcount'=`pyar', hcenter nformat(#,###0) border(top, thin, black)
} /*end foreach group in cohort exp unexp*/
local ++rowcount

* median
putexcel A`rowcount'="Median (IQR) duration of follow-up (years)"
foreach group in cohort exp unexp {
	if "`group'"=="cohort" local col "B"
	if "`group'"=="exp" local col "C"
	if "`group'"=="unexp" local col "D"

	local median "${`group'_median}"
	putexcel `col'`rowcount'="`median'", hcenter
} /*end foreach group in cohort exp unexp*/
local ++rowcount

* mean
putexcel A`rowcount'="Mean (SD) duration of follow-up (years)"
foreach group in cohort exp unexp {
	if "`group'"=="cohort" local col "B"
	if "`group'"=="exp" local col "C"
	if "`group'"=="unexp" local col "D"

	local mean "${`group'_meanfu}"
	putexcel `col'`rowcount'="`mean'", hcenter
} /*end foreach group in cohort exp unexp*/
local ++rowcount




/*----------------------------------------------------------------------------*/
* sex
putexcel A`rowcount'="Sex", bold
local ++rowcount

putexcel A`rowcount'="Female (%)"
putexcel B`rowcount'="${sex_cohort}",  hcenter
putexcel C`rowcount'="${sex_exp}",  hcenter
putexcel D`rowcount'="${sex_unexp}",  hcenter
local ++rowcount



/*----------------------------------------------------------------------------*/
* age band
putexcel A`rowcount'="Age (years)", bold
local ++rowcount

levelsof ageband, local(levels)
foreach i of local levels {
	putexcel A`rowcount'="`: label (ageband) `i''" // use variable label for row caption
	putexcel B`rowcount'="${ageband_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${ageband_exp_`i'}",  hcenter
	putexcel D`rowcount'="${ageband_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/



/*----------------------------------------------------------------------------*/
* IMD
putexcel A`rowcount'="Qunitiles of index of multiple deprivation**", bold
local ++rowcount

* loop through each quintile
forvalues x=1/5 {
	* put in row label
	if `x'==1 putexcel A`rowcount'="1 (least deprived)"
	else if `x'==5 putexcel A`rowcount'="5 (most deprived)"
	else putexcel A`rowcount'="`x'"
	
	* put output strings in excel file
	putexcel B`rowcount'="${imd_composite_cohort_`x'}",  hcenter
	putexcel C`rowcount'="${imd_composite_exp_`x'}",  hcenter
	putexcel D`rowcount'="${imd_composite_unexp_`x'}",  hcenter
	
	local ++rowcount
} /*end forvalues x=1/5*/



/*----------------------------------------------------------------------------*/
* BMI
putexcel A`rowcount'="Body mass index (kg/m2)***", bold
local ++rowcount

* loop through each BMI cat
levelsof bmi_cat, local(levels)
foreach i of local levels {
	putexcel A`rowcount'="`: label (bmi_cat) `i''" // use variable label for row caption
	putexcel B`rowcount'="${bmi_cat_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${bmi_cat_exp_`i'}",  hcenter
	putexcel D`rowcount'="${bmi_cat_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/



/*----------------------------------------------------------------------------*/
* Smoking
putexcel A`rowcount'="Smoking***", bold
local ++rowcount

* loop through each smoking cat
labelsof smok
local labels=r(labels)
local val=r(values) // values that go with value labels
local k=1 // counter variable to identify values in the `val' macro

foreach j in `labels' {
	putexcel A`rowcount'="`j'" // use variable label for row caption
	local content : word `k' of `val'
	
	putexcel B`rowcount'="${smok_cohort_`content'}",  hcenter
	putexcel C`rowcount'="${smok_exp_`content'}",  hcenter
	putexcel D`rowcount'="${smok_unexp_`content'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
	local ++k
} /*end foreach j in `labels'*/




/*----------------------------------------------------------------------------*/
* ETOH
putexcel A`rowcount'="Alcohol", bold
local ++rowcount

putexcel A`rowcount'="Harmful alcohol use (%)"
putexcel B`rowcount'="${stateharmfulETOH_cohort}",  hcenter
putexcel C`rowcount'="${stateharmfulETOH_exp}",  hcenter
putexcel D`rowcount'="${stateharmfulETOH_unexp}",  hcenter
local ++rowcount 




/*----------------------------------------------------------------------------*/
* Ethnicity
* row caption
putexcel A`rowcount'="Ethnicity", bold
local ++rowcount

* loop through each ethnicity cat
levelsof ethnicity, local(levels)
foreach i of local levels {
	putexcel A`rowcount'="`: label (ethnicity) `i''" // use variable label for row caption
	putexcel B`rowcount'="${ethnicity_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${ethnicity_exp_`i'}",  hcenter
	putexcel D`rowcount'="${ethnicity_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/




/*----------------------------------------------------------------------------*/
* Comorbidities
putexcel A`rowcount'="Comorbidities", bold
local ++rowcount

* loop through each binary covar
foreach comorb in stateasthma stateimmunosup {
	if "`comorb'"=="stateasthma" putexcel A`rowcount'="Asthma"
	if "`comorb'"=="stateimmunosup" putexcel A`rowcount'="Immunosuppression"
	
	* put in excel file
	putexcel B`rowcount'="${`comorb'_cohort}",  hcenter
	putexcel C`rowcount'="${`comorb'_exp}",  hcenter
	putexcel D`rowcount'="${`comorb'_unexp}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach comorb in asthma immunosup*/




/*----------------------------------------------------------------------------*/
* DM
* row caption
putexcel A`rowcount'="Diabetes mellitus", bold
local ++rowcount

* loop through each DM cat
levelsof dm_new, local(levels)
foreach i of local levels {
	putexcel A`rowcount'="`: label (dm_new) `i''" // use variable label for row caption
	putexcel B`rowcount'="${dm_new_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${dm_new_exp_`i'}",  hcenter
	putexcel D`rowcount'="${dm_new_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/
	
	
	
	
	
	
/*----------------------------------------------------------------------------*/
* Calendar period
* row caption
putexcel A`rowcount'="Calendar period", bold
local ++rowcount

* loop through each Calendar period cat
levelsof calendarperiod, local(levels)
foreach i of local levels {
	putexcel A`rowcount'="`: label (calendarperiod) `i''" // use variable label for row caption
	putexcel B`rowcount'="${calendarperiod_cohort_`i'}",  hcenter
	putexcel C`rowcount'="${calendarperiod_exp_`i'}",  hcenter
	putexcel D`rowcount'="${calendarperiod_unexp_`i'}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach i of local levels*/
	
	
	
	
	
	
	
/*----------------------------------------------------------------------------*/
* Prescriptions
putexcel A`rowcount'="Prescriptions (defined as ever prescribed, and time-updated as at first prescription)", bold
local ++rowcount

* loop through each binary covar
foreach d in statehighGC statesystemicRx {
	if "`d'"=="statehighGC" putexcel A`rowcount'="High-dose oral glucocorticoids (20mg+ prednisolone equivalent dose)"
	if "`d'"=="statesystemicRx" putexcel A`rowcount'="Systemic drugs (azathioprine, ciclosporin, methotrexate, mycophenolate)"
	
	* put in excel file
	putexcel B`rowcount'="${`d'_cohort}",  hcenter
	putexcel C`rowcount'="${`d'_exp}",  hcenter
	putexcel D`rowcount'="${`d'_unexp}",  hcenter
	
	local ++rowcount // increment row counter so that next iteration of loop put on next row
} /*end foreach comorb in asthma immunosup*/

	
	
	
	


	
		
* put top border on next row
foreach col in A B C D {
	putexcel `col'`rowcount'="" , border(top, thin, black)
}

local ++rowcount



/*----------------------------------------------------------------------------*/
* Footnotes 
putexcel A`rowcount'="Individuals can contribute data as both eczema exposed and unexposed. Therefore, pyar for exposed/unexposed do not total the whole cohort, as individuals may be included in more than one column."
local ++rowcount

putexcel A`rowcount'="*Follow-up based on censoring at the earliest of: death, no longer registered with practice, practice no longer contributing to CPRD, or any cancer diagnosis (excluding non-melanoma skin cancer)"
local ++rowcount

putexcel A`rowcount'="IQR: Interquartile range"
local ++rowcount

putexcel A`rowcount'="** IMD based on individual-level data (from 2007) if available, supplemented with practice-level data (from 2010) if individual-level data not available."
local ++rowcount

putexcel A`rowcount'="*** Smoking and BMI based on records closest to index date."
local ++rowcount







log close

