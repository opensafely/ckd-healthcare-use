/*=========================================================================
DO FILE NAME:			exca-censor02v3-main

AUTHOR:					Kate Mansfield	
						
VERSION:				v3
DATE VERSION CREATED: 	v3 2019-Jul-17	// re-running for NHL results EXCLUDING cutaneous lymphomas
						v2 2019-Feb-20	// edited to include NHL and Hodgkins
						v1 2019-Jan-23
					
DATABASE:				CPRD July 2017 build
						HES version 14
	
DESCRIPTION OF FILE:	Run main analysis for all outcomes (any cancer and specific types)
						and put results into an excel file
					
MORE INFORMATION:		
						
DATASETS USED:		analysis-censor-`ca'_cancer

DATASETS CREATED: 	exca-censor02v3-main.xls // excel file

DO FILES NEEDED:	exca-paths.do
					
ADO FILES NEEDED: 	exca.ado

*=========================================================================*/

/*******************************************************************************
>> HOUSEKEEPING
*******************************************************************************/
version 15
clear all
capture log close

* find path file location and run it
exca paths

* create a filename global that can be used throughout the file
global filename "exca-censor02v3-main"


* open log file - no need as fast tool will create log files
log using "${pathLogs}/${filename}", text replace






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
	local cancertype `2'
	local model `3'
	
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
#2. Start loop for each cancer outcome
*******************************************************************************/
/*
local cancers " "all" "lung" "breast" "prostate" "pancreas" "melanoma" "non_melanoma" "lymphomaNonCut" "
local cancers "`cancers' "mm" "leukaemia" "haem" "meningioma" "glioma" "CNSother" "cns" "
local cancers "`cancers' "nhl" "hodgkins" "	
*/

local cancers " "nhl" "


foreach ca in `cancers' {
	display in red "***********************************************************"
	display in red "****************** `ca' cancer ****************************"
	display in red "***********************************************************"


	* open analysis dataset
	use ${pathOut}/analysis-censor-`ca'_cancer, clear

	
	* All models implicitly adjusted for sex, date at cohort entry and practice 
	* due to stratification by matched set.
	
	
	/***************************************************************************
	#3. crude model
		unadjusted
	***************************************************************************/
	* run analysis
	stcox i.exposed, strata(setid) level(99) base 	
	matrix table = r(table) // put results into a matrix so that can pull numbers out
	getstuff table `ca' unadj // get the relevant info and put it into global macros for later putexcel code
	
	
	
	
	/***************************************************************************
	#5. Model 1 (+ calendar period + IMD) - MAIN ANALYSIS
	***************************************************************************/
	* check if any missing IMD data
	assert imd_composite!=.
	
	* run analysis 
	stcox i.exposed i.cal i.imd_composite, strata(setid) level(99) base
	matrix table = r(table) // put results into a matrix so that can pull numbers out
	getstuff table `ca' mod1 // get the relevant info and put it into global macros for later putexcel code	
	

	
	
	
	/***************************************************************************
	#6. 5 (+ harmful ETOH, smoking and BMI) - MEDIATION MODEL
		includes variables that potentially lie on the causal pathway between 
		eczema and cancer
	***************************************************************************/
	* need to preserve matching
	* so need to drop cases with missing data and then any controls who are
	* no longer matched to an included case
	* Complete cases
	
	* look for missing values of smok var
	gen exposed_nm = (exposed<.)
	gen smok_nm = (smok<.)
	gen complete = (exposed_nm==1 & smok_nm==1)
	tab complete
	tab complete exposed, col
	keep if complete==1
	drop complete
	
	* look for missing values of BMI variable
	gen bmi_nm = (bmi_cat<.)
	gen complete = (exposed_nm==1 & bmi_nm==1)
	tab complete
	tab complete exposed, col
	keep if complete==1
	drop complete

	* Preserve matching, keep valid sets only
	bysort setid: egen set_exposed_mean = mean(exposed)
	gen valid_set = (set_exposed_mean>0 & set_exposed_mean<1) // if mean of exposure var is 0 then only unexposed, if 1 then only exposed
	tab valid_set, miss
	tab valid_set exposed, col
	keep if valid_set==1
	drop valid_set set_exposed_mean
	
	* run analysis 
	stcox i.exposed i.cal i.imd_composite i.stateharmfulETOH i.smok i.bmi_cat, strata(setid) level(99) base
	matrix table = r(table) // put results into a matrix so that can pull numbers out
	getstuff table `ca' mod2 // get the relevant info and put it into global macros for later putexcel code
		
	
	
	
	

/*******************************************************************************
>> HOUSEKEEPING
	- END LOOP
	- clean up by deleting interim files used
*******************************************************************************/
} /*END foreach ca in `cancers'*/
	
	
	
	
	

	
/*******************************************************************************
#10. Put results into an excel file
*******************************************************************************/
* create excel file
putexcel set "${pathResults}/${filename}.xlsx", sheet(main) replace

* set row count variable
local rowcount=1

* Table title
putexcel A`rowcount'="Table x. Association between atopic eczema and cancer outcomes. ", bold
local ++rowcount // increment row couter variable
putexcel A`rowcount'="Fitted to patients with complete data for all variables included in each model and from valid matched sets*"
local ++rowcount
putexcel A`rowcount'="All models implicitly adjusted for sex, date at cohort entry and practice due to stratification by matched set"
local ++rowcount

* set up column headers
putexcel A`rowcount'="", border(top, thin, black)
putexcel B`rowcount'="Unadjusted", bold border(top, thin, black)
putexcel F`rowcount'="Fully adjusted (adjusted for IMD and calendar period)", bold border(top, thin, black)
putexcel J`rowcount'="Adjusted for mediating variables (harmful alcohol use, smoking and BMI)", bold border(top, thin, black)




foreach col in C D E G H I K L M {
	putexcel `col'`rowcount'="", border(top, thin, black)
} /*end foreach col in C D E G H I K L M*/
local ++rowcount

* next row of col headers - write the same four col headers for each model
putexcel A`rowcount'="Cancer outcome (ICD-10 code)", border(bottom, thin, black) bold
local unadj "B C D E"
local mod1 "F G H I"
local mod2 "J K L M"

foreach model in unadj mod1 mod2 {
	forvalues i=1/4 {
		local col`i' : word `i' of ``model''
	} /*end forvalues i=1/4*/
	putexcel `col1'`rowcount'="Number", border(bottom, thin, black)
	putexcel `col2'`rowcount'="Person years at risk", border(bottom, thin, black)
	putexcel `col3'`rowcount'="Events", border(bottom, thin, black)
	putexcel `col4'`rowcount'="Hazard ratio (99% CI)**", border(bottom, thin, black)
} /*end foreach model in unadj mod1 mod2 */
local ++rowcount




* loop through each outcome
local cancers " "nhl" "

foreach ca in `cancers' {
	* put in cancer headings
	if "`ca'"=="all" putexcel A`rowcount'="ANY CANCER", bold
	if "`ca'"=="lung" {
		putexcel A`rowcount'="SPECIFIC CANCER OUTCOMES", bold
		local ++rowcount
		putexcel A`rowcount'="Lung (C34)", italic bold
	} /*end if "`ca'"=="lung"*/
	if "`ca'"=="breast" putexcel A`rowcount'="Breast (C50)", italic bold
	if "`ca'"=="prostate" putexcel A`rowcount'="Prostate (C61)", italic bold
	if "`ca'"=="pancreas" putexcel A`rowcount'="Pancreas (C25)", italic bold
	if "`ca'"=="haem" putexcel A`rowcount'="Haematological cancers", italic bold
	if "`ca'"=="leukaemia" putexcel A`rowcount'="Leukaemia (C91-C95)", italic
	if "`ca'"=="lymphomaNonCut" putexcel A`rowcount'="Lymphoma - excluding cutaneous (C81-C86)", italic bold
	if "`ca'"=="hodgkins" putexcel A`rowcount'="Hodgkins lymphoma (C81)", italic
	if "`ca'"=="nhl" putexcel A`rowcount'="Non-Hodgkins lymphoma (C82-C86)", italic
	if "`ca'"=="mm" putexcel A`rowcount'="Multiple myeloma (C90)", italic
	if "`ca'"=="cns" putexcel A`rowcount'="Central nervous system cancers", italic bold
	if "`ca'"=="meningioma" putexcel A`rowcount'="Meningioma (C70)", italic
	if "`ca'"=="glioma" putexcel A`rowcount'="Brain neoplasm (C71)", italic
	if "`ca'"=="CNSother" putexcel A`rowcount'="Spinal cord, cranial nerve or other CNS tumours (C72)", italic
	if "`ca'"=="melanoma" putexcel A`rowcount'="Melanoma (C43)", italic bold
	if "`ca'"=="non_melanoma" putexcel A`rowcount'="Non-melanoma skin cancer (C44)", italic bold
	
	local ++rowcount
	
	* now put in data for each model - first for exp and then next line for unexposed
	foreach grp in unexp exp {
		if "`grp'"=="unexp" putexcel A`rowcount'="unexposed"
		if "`grp'"=="exp" putexcel A`rowcount'="exposed"
		foreach mod in unadj mod1 mod2 {
			forvalues i=1/4 {
				local col`i' : word `i' of ``mod''
			} /*end forvalues i=1/4*/	
			putexcel `col1'`rowcount'="${`mod'_`ca'_`grp'_n}"
			putexcel `col2'`rowcount'="${`mod'_`ca'_`grp'_pyar}"
			putexcel `col3'`rowcount'="${`mod'_`ca'_`grp'_fail}"
			if "`grp'"=="unexp" putexcel `col4'`rowcount'="1 (ref)"
			if "`grp'"=="exp" putexcel `col4'`rowcount'="${`mod'_`ca'_hr}", bold
		} /*end foreach mode in unadj mod1 mod2 */
		local ++rowcount
	} /*end foreach grp in unexp exp*/

	

} /*end foreach ca in `cancers' */




/*----------------------------------------------------------------------------*/
* Footnotes 
foreach col in A B C D E F G H I J K L M {
	putexcel `col'`rowcount'="", border(top, thin, black)
} /*end foreach col in A B C D E F G H I J K L M */
local ++rowcount

putexcel A`rowcount'="*Matched sets including one exposed patient and at least one unexposed patient"
local ++rowcount
putexcel A`rowcount'="**Estimated hazard ratios from Cox regression with current age as underlying timescale, stratified by matched set (matched on age at cohort entry, sex, general practice, and date at cohort entry)"
local ++rowcount
putexcel A`rowcount'="Specific cancer outcomes individuals censored at first diagnosis of any definite cancer outcome."
local ++rowcount




	




log close













