sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_ckd_complete, replace t
clear

*Merge `dataset'_ckd with `dataset'_ckd_complete
capture noisily import delimited ./output/`dataset'_ckd.csv, clear
tempfile `dataset'_ckd
save ``dataset'_ckd', replace
capture noisily import delimited ./output/input_`dataset'_ckd_complete.csv, clear
merge 1:1 patient_id using ``dataset'_ckd'
keep if _merge==3
drop _merge
tempfile `dataset'_ckd_complete
save ``dataset'_ckd_complete', replace

/*Generate dummy data
cd ckd-healthcare-use
capture noisily import delimited ./output/2017_ckd.csv, clear
tempfile 2017_ckd
save ./output/2017_ckd, replace
capture noisily import delimited ./output/input_2017_ckd_complete.csv, clear
merge 1:1 patient_id using ./output/2017_ckd
keep if _merge==3
drop _merge
tempfile 2017_ckd_complete
save ./output/2017_ckd_complete, replace
*/

*CKD stage classification
foreach var of varlist 	dialysis_baseline_primary_care	///
						dialysis_baseline_icd_10		///
						dialysis_baseline_opcs_4		///
						dialysis_baseline_date			///
						kt_baseline_primary_care		///
						kt_baseline_icd_10				///
						kt_baseline_opcs_4				{
	drop `var'
	}
tab modality_baseline, m
*To reduce misclassification of dialysis, anyone with eGFR >15 with modality_baseline=="Dialysis" will be reclassified as non-dialysis (e.g. they may have received acute dialysis and recovered)
*For modality_baseline="Modality unclear" (i.e. whose dialysis and kidney transplant baseline dates are identical), those with eGFR <15 will be assumed to be on dialysis and those >15 as kidney transplant
egen esrd_egfr = cut(baseline_egfr), at (0, 15, 5000)
recode esrd_egfr 0=1 15=0
tab esrd_egfr, m
gen dialysis = 0
replace dialysis = 1 if modality_baseline=="Dialysis"
replace dialysis = 1 if modality_baseline=="Modality unclear" & esrd_egfr!=.
replace dialysis = 0 if esrd_egfr==0
gen kidney_transplant = 0
replace kidney_transplant = 1 if kidney_transplant_baseline_date!=""
replace kidney_transplant = 0 if dialysis==1
gen modality_unclear = 0
replace modality_unclear = 1 if modality_baseline=="Modality unclear"
replace modality_unclear = 0 if dialysis==1
replace modality_unclear = 0 if kidney_transplant==1
tab modality_baseline dialysis
tab modality_baseline kidney_transplant
tab modality_baseline modality_unclear
tab dialysis kidney_transplant
egen ckd_group = cut(baseline_egfr), at(0, 30, 60, 5000)
recode ckd_group 0=3 30=2 60=1
replace ckd_group = 4 if dialysis==1
replace ckd_group = 5 if kidney_transplant==1
replace ckd_group = 6 if modality_unclear==1
*ckd_group==. are those with albuminuria without available eGFR measurement or code for KRT
replace ckd_group = 1 if ckd_group==.
label define ckd_group 1 "Albuminuria" 2 "CKD stage 3" 3 "CKD stage 4/5" 4 "Dialysis" 5 "Transplant" 6 "KRT unclear modality"
label values ckd_group ckd_group
label var ckd_group "CKD group"
tab ckd_group, m
drop if ckd_group==.
tab ckd_group modality_baseline

*Dialysis & kidney transplant outcome classification
foreach var of varlist 	dialysis_outcome_primary_care	///
						dialysis_outcome_icd_10			///
						dialysis_outcome_opcs_4			///
						dialysis_outcome_date			///
						kt_outcome_primary_care			///
						kt_outcome_icd_10				///
						kt_outcome_opcs_4				///
						kidney_transplant_outcome_date 	///
						died							{
	drop `var'
	}
tab ckd_group modality_outcome, m

*eGFR outcome classification based on updated mean eGFR over previous 18 months by the end of year
gen sex = 1 if male == "Male"
replace sex = 0 if male == "Female"
label define sex 0"Female" 1"Male"
label values sex sex
replace creatinine_outcome = . if !inrange(creatinine_outcome, 20, 3000)
gen mgdl_creatinine_outcome = creatinine_outcome/88.4
gen min_creatinine_outcome=.
replace min_creatinine_outcome = mgdl_creatinine_outcome/0.7 if sex==0
replace min_creatinine_outcome = mgdl_creatinine_outcome/0.9 if sex==1
replace min_creatinine_outcome = min_creatinine_outcome^-0.329  if sex==0
replace min_creatinine_outcome = min_creatinine_outcome^-0.411  if sex==1
replace min_creatinine_outcome = 1 if min_creatinine_outcome<1
gen max_creatinine_outcome=.
replace max_creatinine_outcome = mgdl_creatinine_outcome/0.7 if sex==0
replace max_creatinine_outcome = mgdl_creatinine_outcome/0.9 if sex==1
replace max_creatinine_outcome = max_creatinine_outcome^-1.209
replace max_creatinine_outcome = 1 if max_creatinine_outcome>1
gen egfr_outcome = min_creatinine_outcome*max_creatinine_outcome*141
replace egfr_outcome = egfr_outcome*(0.993^age)
replace egfr_outcome = egfr_outcome*1.018 if sex==0
drop creatinine_outcome
drop mgdl_creatinine_outcome
drop min_creatinine_outcome
drop max_creatinine_outcome
egen egfr_end = cut(egfr_outcome), at(0, 30, 60, 5000)
recode egfr_end 0=3 30=2 60=1
label define egfr_end 1 "≥60" 2 "30-59" 3 "<30"
label values egfr_end egfr_end
label var egfr_end "Final eGFR"
gen ckd_progression = 0
replace ckd_progression = 1 if egfr_end==2 & ckd_group==1
replace ckd_progression = 2 if egfr_end==3 & ckd_group==1
replace ckd_progression = 2 if egfr_end==3 & ckd_group==2
egen esrd_egfr_end = cut(egfr_outcome), at (0, 15, 5000)
recode esrd_egfr_end 0=1 15=0
tab esrd_egfr_end, m
gen dialysis_outcome = 0
replace dialysis_outcome = 1 if modality_outcome=="Dialysis"
replace dialysis_outcome = 1 if modality_outcome=="Modality unclear" & esrd_egfr_end==1
gen kidney_transplant_outcome = 0
replace kidney_transplant_outcome = 1 if modality_outcome=="Kidney transplant"
replace kidney_transplant_outcome = 1 if modality_outcome=="Modality unclear" & esrd_egfr_end==0
replace ckd_progression = 5 if modality_outcome=="Modality unclear"
replace ckd_progression = 3 if dialysis_outcome==1
replace ckd_progression = 4 if kidney_transplant_outcome==1
replace ckd_progression = 6 if modality_outcome=="Deceased"
label define ckd_progression 0 "No progression" 1 "CKD 3" 2 "CKD 4/5 pre-KRT" 3 "Dialysis" 4 "Kidney transplant" 5 "KRT unclear modality" 6 "Deceased"
label values ckd_progression ckd_progression
label var ckd_progression "CKD progression"
tab ckd_progression, m

*eGFR cut-offs to investigate timing of access formation
egen access_egfr = cut(baseline_egfr), at (0, 15, 5000)
recode access_egfr 0=1 15=2
replace access_egfr=0 if ckd_group==4
replace access_egfr=3 if access_egfr==.
label define access_egfr 0 "Dialysis" 1 "eGFR 0-14" 2 "eGFR >= 15" 3 "Unknown"
label values access_egfr access_egfr

*Totals for non-binary healthcare resource outcomes (including by month)
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions icd1_days icd2_days icd3_days icd4_days icd5_days icd6_days icd7_days icd8_days icd9_days icd10_days icd11_days icd12_days icd13_days icd14_days icd15_days icd16_days icd17_days icd18_days icd19_days icd20_days icd21_days icd22_days AA22_days AA23_days AA24_days AA25_days AA26_days AA28_days AA29_days AA30_days AA31_days AA32_days AA33_days AA35_days AA43_days AA50_days AA51_days AA52_days AA53_days AA54_days AA55_days AA57_days AA60_days AA61_days AA71_days AA81_days AA83_days AB11_days AB15_days AB16_days AB18_days AB20_days AB21_days AB22_days AB23_days AB24_days AB26_days BZ24_days BZ31_days BZ32_days BZ33_days BZ41_days BZ42_days BZ44_days BZ45_days BZ46_days BZ51_days BZ53_days BZ54_days BZ56_days BZ57_days BZ60_days BZ61_days BZ62_days BZ63_days BZ64_days BZ65_days BZ72_days BZ73_days BZ74_days BZ80_days BZ81_days BZ83_days BZ84_days BZ86_days BZ87_days BZ88_days BZ89_days BZ91_days BZ92_days BZ93_days BZ94_days BZ95_days CA01_days CA02_days CA03_days CA04_days CA05_days CA10_days CA11_days CA12_days CA13_days CA14_days CA15_days CA16_days CA20_days CA21_days CA22_days CA23_days CA24_days CA25_days CA26_days CA27_days CA28_days CA29_days CA30_days CA31_days CA32_days CA33_days CA34_days CA35_days CA36_days CA37_days CA38_days CA39_days CA40_days CA42_days CA43_days CA50_days CA51_days CA52_days CA53_days CA54_days CA55_days CA60_days CA62_days CA63_days CA64_days CA65_days CA66_days CA67_days CA68_days CA69_days CA70_days CA71_days CA80_days CA81_days CA82_days CA83_days CA84_days CA85_days CA86_days CA91_days CA92_days CA93_days CA94_days CA95_days CA96_days CA97_days CA98_days CB01_days CB02_days CD01_days CD02_days CD03_days CD04_days CD05_days CD06_days CD07_days CD08_days CD09_days CD10_days CD11_days CD12_days DX21_days DZ01_days DZ02_days DZ09_days DZ10_days DZ11_days DZ12_days DZ13_days DZ14_days DZ15_days DZ16_days DZ17_days DZ18_days DZ19_days DZ20_days DZ22_days DZ23_days DZ24_days DZ25_days DZ26_days DZ27_days DZ28_days DZ29_days DZ30_days DZ31_days DZ32_days DZ33_days DZ36_days DZ37_days DZ38_days DZ42_days DZ45_days DZ46_days DZ49_days DZ50_days DZ51_days DZ55_days DZ56_days DZ57_days DZ58_days DZ59_days DZ60_days DZ63_days DZ64_days DZ65_days DZ67_days DZ68_days DZ69_days DZ70_days DZ71_days EB02_days EB03_days EB04_days EB05_days EB06_days EB07_days EB08_days EB09_days EB10_days EB12_days EB13_days EB14_days EB15_days EC11_days EC12_days EC13_days EC14_days EC15_days EC21_days ED01_days ED05_days ED08_days ED09_days ED11_days ED12_days ED13_days ED14_days ED15_days ED18_days ED24_days ED25_days ED26_days ED27_days ED28_days ED30_days ED31_days EY01_days EY02_days EY04_days EY06_days EY08_days EY11_days EY12_days EY13_days EY17_days EY22_days EY23_days EY30_days EY31_days EY32_days EY40_days EY41_days EY42_days EY43_days EY50_days EY51_days FD01_days FD02_days FD03_days FD04_days FD05_days FD10_days FD11_days FE01_days FE02_days FE03_days FE10_days FE11_days FE12_days FE13_days FE20_days FE21_days FE22_days FE30_days FE31_days FE32_days FE33_days FE34_days FE35_days FE36_days FE50_days FF01_days FF02_days FF04_days FF05_days FF12_days FF13_days FF14_days FF20_days FF21_days FF22_days FF30_days FF31_days FF32_days FF33_days FF34_days FF36_days FF37_days FF40_days FF41_days FF42_days FF43_days FF50_days FF51_days FF52_days FF53_days FF60_days FF61_days FF62_days FF63_days GA03_days GA04_days GA05_days GA06_days GA07_days GA10_days GA11_days GA13_days GA15_days GA16_days GB05_days GB06_days GB09_days GB10_days GB11_days GB12_days GB13_days GC01_days GC12_days GC17_days GC18_days HC20_days HC21_days HC26_days HC27_days HC28_days HC29_days HC30_days HC31_days HC32_days HC50_days HC53_days HC54_days HC60_days HC61_days HC62_days HC63_days HC64_days HC65_days HC70_days HC71_days HC72_days HD21_days HD23_days HD24_days HD25_days HD26_days HD39_days HD40_days HE11_days HE12_days HE21_days HE22_days HE31_days HE32_days HE41_days HE42_days HE51_days HE52_days HE71_days HE72_days HE81_days HE82_days HE83_days HN12_days HN13_days HN14_days HN15_days HN22_days HN23_days HN24_days HN25_days HN32_days HN33_days HN34_days HN35_days HN42_days HN43_days HN44_days HN45_days HN46_days HN52_days HN53_days HN54_days HN55_days HN62_days HN63_days HN64_days HN65_days HN81_days HN86_days HN93_days JA12_days JA13_days JA20_days JA30_days JA34_days JA38_days JA43_days JA45_days JB70_days JB71_days JB91_days JC40_days JC41_days JC42_days JC43_days JC44_days JC45_days JC46_days JC47_days JD07_days KA03_days KA04_days KA05_days KA06_days KA07_days KA08_days KA09_days KB02_days KB03_days KB04_days KC04_days KC05_days LA01_days LA02_days LA03_days LA04_days LA05_days LA07_days LA08_days LA09_days LA10_days LA11_days LA12_days LA13_days LA14_days LB06_days LB09_days LB10_days LB12_days LB13_days LB14_days LB15_days LB16_days LB17_days LB18_days LB19_days LB20_days LB21_days LB25_days LB26_days LB28_days LB29_days LB33_days LB35_days LB36_days LB37_days LB38_days LB39_days LB40_days LB42_days LB43_days LB46_days LB47_days LB48_days LB50_days LB51_days LB52_days LB53_days LB54_days LB55_days LB56_days LB57_days LB58_days LB59_days LB60_days LB61_days LB64_days LB65_days LB67_days LB68_days LB70_days LB71_days LB72_days LB74_days LB75_days LB76_days LB77_days LB78_days LE01_days LE02_days MA01_days MA02_days MA03_days MA04_days MA07_days MA09_days MA10_days MA11_days MA12_days MA22_days MA23_days MA24_days MA25_days MA29_days MA30_days MA31_days MA32_days MA35_days MA36_days MA38_days MA44_days MA48_days MA52_days MA53_days MA56_days MB05_days MB08_days MB09_days MC07_days MC08_days MC09_days MC10_days MC11_days MC12_days MC20_days MC21_days NZ16_days NZ17_days NZ18_days NZ19_days NZ20_days NZ21_days NZ22_days NZ24_days NZ25_days NZ26_days NZ27_days NZ30_days NZ40_days NZ50_days NZ51_days NZ71_days NZ72_days RD01_days RD08_days RD20_days RD30_days RD40_days RD47_days RD48_days RD50_days RD51_days RD60_days RD61_days RN01_days RN04_days RN07_days RN08_days RN09_days RN13_days RN14_days RN15_days RN16_days RN17_days RN18_days RN19_days RN20_days RN21_days RN22_days RN23_days RN24_days RN25_days RN26_days RN27_days RN28_days RN29_days RN30_days RN31_days RN32_days RN33_days RN34_days RN50_days RN51_days RN52_days SA01_days SA02_days SA03_days SA04_days SA05_days SA06_days SA07_days SA08_days SA09_days SA11_days SA12_days SA14_days SA15_days SA16_days SA17_days SA18_days SA19_days SA20_days SA21_days SA22_days SA23_days SA24_days SA25_days SA26_days SA27_days SA30_days SA31_days SA32_days SA33_days SA35_days SA36_days SA37_days SA40_days SA42_days SA43_days SA44_days SA45_days SB01_days SB02_days SB03_days SB04_days SB05_days SB06_days SB07_days SB08_days SB09_days SB10_days SB11_days SB12_days SB13_days SB14_days SB15_days SB16_days SB17_days SC25_days SC26_days SC28_days SC29_days SC30_days SC40_days SC42_days SC44_days SC45_days SC47_days SC49_days SC51_days SC53_days SC54_days SC55_days SC56_days SC57_days UZ01_days UZ02_days UZ03_days UZ04_days UZ05_days UZ06_days UZ15_days VA10_days VC01_days VC02_days VC03_days VC04_days VC06_days VC08_days VC10_days VC12_days VC14_days VC16_days VC18_days VC20_days VC22_days VC24_days VC26_days VC28_days VC30_days VC32_days VC34_days VC36_days VC38_days VC40_days VC42_days WD01_days WD02_days WD03_days WD04_days WD05_days WD06_days WD07_days WD08_days WD09_days WF01_days WF02_days WH01_days WH02_days WH03_days WH04_days WH05_days WH06_days WH07_days WH08_days WH09_days WH10_days WH11_days WH12_days WH13_days WH14_days WH15_days WH16_days WH17_days WH18_days WH19_days WH20_days WH21_days WH22_days WH23_days WH50_days WH51_days WH52_days WH53_days WH54_days WH99_days WJ01_days WJ02_days WJ03_days WJ04_days WJ06_days WJ07_days WJ10_days WJ11_days XD01_days XD02_days XD03_days XD04_days XD05_days XD06_days XD07_days XD08_days XD09_days XD10_days XD11_days XD12_days XD13_days XD14_days XD15_days XD16_days XD17_days XD18_days XD19_days XD20_days XD21_days XD22_days XD23_days XD24_days XD25_days XD26_days XD27_days XD28_days XD29_days XD30_days XD31_days XD32_days XD33_days XD34_days XD37_days XD38_days XD39_days XD40_days XD41_days XD42_days XD43_days XD44_days XD45_days XD46_days XD47_days XD48_days XD49_days XD50_days XD51_days XD52_days XD53_days XD54_days XD55_days XD56_days XD57_days XD58_days XD90_days XD91_days YA03_days YA04_days YA10_days YA11_days YA12_days YA13_days YC01_days YC10_days YD01_days YD02_days YD03_days YD04_days YD05_days YF01_days YF04_days YG01_days YG02_days YG05_days YG06_days YG07_days YG10_days YG11_days YG12_days YH02_days YH03_days YH10_days YH20_days YH30_days YH31_days YH32_days YJ09_days YJ11_days YJ13_days YJ15_days YL02_days YL11_days YL12_days YL20_days YL21_days YL30_days YQ05_days YQ07_days YQ08_days YQ09_days YQ12_days YQ13_days YQ15_days YQ16_days YQ22_days YQ26_days YQ31_days YQ32_days YQ40_days YQ41_days YQ42_days YQ50_days YQ51_days YR11_days YR12_days YR15_days YR16_days YR22_days YR23_days YR24_days YR25_days YR26_days YR31_days YR33_days YR40_days YR41_days YR42_days YR43_days YR44_days YR45_days YR48_days YR50_days YR51_days YR52_days YR53_days YR54_days YR56_days YR57_days YR63_days YR65_days YR66_days YR67_days {
bysort ckd_group: egen total_`aggregate' = total(`aggregate')
egen overall_`aggregate' = total(`aggregate')
tab ckd_group, sum(total_`aggregate')
sum overall_`aggregate'
}



**Potential effect modifiers
* Ethnicity
* 1 = White ethnicities (white British, white Irish, with other)
* 2 = Mixed ethnicities (white & black Caribbean, white & black African, white & Asian, other mixed ethnicities)
* 3 = South Asian ethnicities (Indian, Pakistani, Bangladeshi, other South Asian)
* 4 = Black ethnicities (black Caribbean, black African, other black)
* 5 = Other ethnicities (Chinese, all other ethnicities)
* . = Unknown ethnicity
replace ethnicity = . if ethnicity==.
replace ethnicity=6 if ethnicity==2
replace ethnicity=2 if ethnicity==3
replace ethnicity=3 if ethnicity==4
replace ethnicity=4 if ethnicity==6
replace ethnicity=6 if ethnicity==.
label define ethnicity	1 "White"  					///
						2 "South Asian"				///						
						3 "Black"  					///
						4 "Mixed"					///
						5 "Other"					///
						6 "Unknown"	
label values ethnicity ethnicity

* Index of multiple deprivation
* Ordered 1-5 from most deprived to least deprived
label define imd 1 "1 Most deprived" 2 "2" 3 "3" 4 "4" 5 "5 Least deprived"
label values imd imd

* Region
rename region region_string
gen region = 1 if region_string=="East Midlands"
replace region = 2 if region_string=="East"
replace region = 3 if region_string=="London"
replace region = 4 if region_string=="North East"
replace region = 5 if region_string=="North West"
replace region = 6 if region_string=="South East"
replace region = 7 if region_string=="South West"
replace region = 8 if region_string=="West Midlands"
replace region = 9 if region_string=="Yorkshire and The Humber"
label define region 	1 "East Midlands" 					///
						2 "East"   							///
						3 "London" 							///
						4 "North East" 						///
						5 "North West" 						///
						6 "South East" 						///
						7 "South West"						///
						8 "West Midlands" 					///
						9 "Yorkshire and The Humber"		
label values region region
label var region "Region"

* Urban/rural
replace rural_urban=. if rural_urban<1|rural_urban>8
label define rural_urban 1 "Urban major conurbation" 						///
						 2 "Urban minor conurbation" 						///
						 3 "Urban city and town" 							///
						 4 "Urban city and town in a sparse setting" 		///
						 5 "Rural town and fringe" 							///
						 6 "Rural town and fringe in a sparse setting" 		///
						 7 "Rural village and dispersed" 					///
						 8 "Rural village and dispersed in a sparse setting"
label values rural_urban rural_urban
* Urban (binary)
* Urban = 1-4 + missing, Rural = 5-8
generate urban=.
replace urban=1 if rural_urban<=4|rural_urban==.
replace urban=0 if rural_urban>4 & rural_urban!=.
label var urban "Urban/rural"
label define urban 0 "Rural" 1 "Urban"
label values urban urban
drop rural_urban

*Age bands for standardisation
egen agecat = cut(age), at(0,18,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,200)
drop if agecat==0

*Age-standardisation weights (European Standard Population 2013)
gen weight = .
replace weight = 0.027261 if agecat==18
replace weight = 0.074349 if agecat==20
replace weight = 0.074349 if agecat==25
replace weight = 0.080545 if agecat==30
replace weight = 0.086741 if agecat==35
replace weight = 0.086741 if agecat==40
replace weight = 0.086741 if agecat==45
replace weight = 0.086741 if agecat==50
replace weight = 0.080545 if agecat==55
replace weight = 0.074349 if agecat==60
replace weight = 0.068154 if agecat==65
replace weight = 0.061958 if agecat==70
replace weight = 0.049566 if agecat==75
replace weight = 0.030979 if agecat==80
replace weight = 0.018587 if agecat==85
replace weight = 0.012392 if agecat==90


*Age standardised counts for each non-binary healthcare resource outcomes
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions icd1_days icd2_days icd3_days icd4_days icd5_days icd6_days icd7_days icd8_days icd9_days icd10_days icd11_days icd12_days icd13_days icd14_days icd15_days icd16_days icd17_days icd18_days icd19_days icd20_days icd21_days icd22_days {
replace `aggregate' = `aggregate' * weight
}

* Create variable for age-standardised total # of each aggregated outcome
* `var'_`aggregate' = age-standardised total # of each aggregated outcome overall stratified by ethnicity/imd/region/urban
* `var'_`aggregate'_ckd = age-standardised total # of each aggregated outcome in each CKD group stratified by ethnicity/imd/region/urban
foreach aggregate of varlist hospital_days critical_care_days emergency_days op_appts neph_appts tx_appts gp_interactions icd1_days icd2_days icd3_days icd4_days icd5_days icd6_days icd7_days icd8_days icd9_days icd10_days icd11_days icd12_days icd13_days icd14_days icd15_days icd16_days icd17_days icd18_days icd19_days icd20_days icd21_days icd22_days {
egen overall_std_`aggregate' = total(`aggregate')
bysort ckd_group: egen std_`aggregate' = total(`aggregate')
foreach var of varlist ethnicity imd region urban {
bysort `var': egen `var'_`aggregate' = total(`aggregate')
bysort `var' ckd_group: egen `var'_`aggregate'_ckd = total(`aggregate')
}
}

foreach binary of varlist fistula_formation pd_insertion blood_pressure albuminuria creatinine icd1 icd2 icd3 icd4 icd5 icd6 icd7 icd8 icd9 icd10 icd11 icd12 icd13 icd14 icd15 icd16 icd17 icd18 icd19 icd20 icd21 icd22 {
gen esp_`binary' = `binary' * weight
egen overall_std_`binary' = total(esp_`binary')
bysort ckd_group: egen std_`binary' = total(esp_`binary')
foreach var of varlist ethnicity imd region urban {
bysort `var': egen `var'_`binary' = total(esp_`binary')
bysort `var' ckd_group: egen `var'_`binary'_ckd = total(esp_`binary')
}
}

*Merge cost data
save "./output/`dataset'_ckd_complete.dta", replace
capture noisily import delimited ./output/costs_`dataset'.csv, clear
keep patient_id apcs_cost ec_cost opa_cost
merge 1:1 patient_id using ./output/`dataset'_ckd_complete
drop if _merge==1
foreach cost of varlist apcs_cost ec_cost opa_cost {
sum `cost', d
bysort ckd_group: egen total_`cost' = total(`cost')
egen overall_`cost' = total(`cost')
tab ckd_group, sum(total_`cost')
sum overall_`cost'
foreach var of varlist ethnicity imd region urban {
bysort `var': egen `var'_`cost' = total(`cost')
bysort `var' ckd_group: egen `var'_`cost'_ckd = total(`cost')
}
}
save "./output/`dataset'_ckd_complete.dta", replace

log close

/*
save "./output/2017_ckd_complete.dta", replace
capture noisily import delimited ./output/costs_2017.csv, clear
keep patient_id apcs_cost ec_cost opa_cost
merge 1:1 patient_id using ./output/2017_ckd_complete
drop if _merge==1
drop _merge
save "./output/2017_ckd_complete.dta", replace
*/


