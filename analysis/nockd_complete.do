sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_nockd_complete, replace t
clear

*Merge `dataset'_nockd with `dataset'_nockd_complete
capture noisily import delimited ./output/`dataset'_nockd.csv, clear
tempfile `dataset'_nockd
save ``dataset'_nockd', replace
capture noisily import delimited ./output/input_`dataset'_nockd_complete.csv, clear
merge 1:1 patient_id using ``dataset'_nockd'
keep if _merge==3
drop _merge
tempfile `dataset'_nockd_complete
save ``dataset'_nockd_complete', replace

/*Generate dummy data
cd ckd-healthcare-use
capture noisily import delimited ./output/2017_nockd.csv, clear
tempfile 2017_nockd
save ./output/2017_nockd, replace
capture noisily import delimited ./output/input_2017_nockd_complete.csv, clear
merge 1:1 patient_id using ./output/2017_nockd
keep if _merge==3
drop _merge
tempfile 2017_nockd_complete
save ./output/2017_nockd_complete, replace
*/

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
replace ckd_progression = 1 if egfr_end==2
replace ckd_progression = 2 if egfr_end==3
egen esrd_egfr_end = cut(egfr_outcome), at (0, 15, 5000)
recode esrd_egfr_end 0=1 15=0
tab esrd_egfr_end, m
*NB - might need to change "" to . with dummy data
replace modality_outcome = "Unchanged" if modality_outcome_date==.
gen dialysis_outcome = 0
replace dialysis_outcome = 1 if modality_outcome=="Dialysis"
replace dialysis_outcome = 1 if modality_outcome=="Modality unclear" & esrd_egfr_end==1
gen kidney_transplant_outcome = 0
replace kidney_transplant_outcome = 1 if modality_outcome=="Kidney transplant"
replace kidney_transplant_outcome = 1 if modality_outcome=="Modality unclear" & esrd_egfr_end==0
*NB - might need to change "" to . with dummy data
replace ckd_progression = 5 if modality_outcome=="Modality unclear" & modality_outcome_date!=.
replace ckd_progression = 3 if dialysis_outcome==1
replace ckd_progression = 4 if kidney_transplant_outcome==1
replace ckd_progression = 6 if modality_outcome=="Deceased"
label define ckd_progression 0 "No progression" 1 "CKD 3" 2 "CKD 4/5 pre-KRT" 3 "Dialysis" 4 "Kidney transplant" 5 "KRT unclear modality" 6 "Deceased"
label values ckd_progression ckd_progression
label var ckd_progression "CKD progression"
tab ckd_progression, m
gen ckd_group = 0

foreach aggregate of varlist aa22_days aa23_days aa24_days aa25_days aa26_days aa28_days aa29_days aa30_days aa31_days aa32_days aa33_days aa35_days aa43_days aa50_days aa51_days aa52_days aa53_days aa54_days aa55_days aa57_days aa60_days aa61_days aa71_days aa81_days aa83_days ab11_days ab15_days ab16_days ab18_days ab20_days ab21_days ab22_days ab23_days ab24_days ab26_days bz24_days bz31_days bz32_days bz33_days bz41_days bz42_days bz44_days bz45_days bz46_days bz51_days bz53_days bz54_days bz56_days bz57_days bz60_days bz61_days bz62_days bz63_days bz64_days bz65_days bz72_days bz73_days bz74_days bz80_days bz81_days bz83_days bz84_days bz86_days bz87_days bz88_days bz89_days bz91_days bz92_days bz93_days bz94_days bz95_days ca01_days ca02_days ca03_days ca04_days ca05_days ca10_days ca11_days ca12_days ca13_days ca14_days ca15_days ca16_days ca20_days ca21_days ca22_days ca23_days ca24_days ca25_days ca26_days ca27_days ca28_days ca29_days ca30_days ca31_days ca32_days ca33_days ca34_days ca35_days ca36_days ca37_days ca38_days ca39_days ca40_days ca42_days ca43_days ca50_days ca51_days ca52_days ca53_days ca54_days ca55_days ca60_days ca62_days ca63_days ca64_days ca65_days ca66_days ca67_days ca68_days ca69_days ca70_days ca71_days ca80_days ca81_days ca82_days ca83_days ca84_days ca85_days ca86_days ca91_days ca92_days ca93_days ca94_days ca95_days ca96_days ca97_days ca98_days cb01_days cb02_days cd01_days cd02_days cd03_days cd04_days cd05_days cd06_days cd07_days cd08_days cd09_days cd10_days cd11_days cd12_days dx21_days dz01_days dz02_days dz09_days dz10_days dz11_days dz12_days dz13_days dz14_days dz15_days dz16_days dz17_days dz18_days dz19_days dz20_days dz22_days dz23_days dz24_days dz25_days dz26_days dz27_days dz28_days dz29_days dz30_days dz31_days dz32_days dz33_days dz36_days dz37_days dz38_days dz42_days dz45_days dz46_days dz49_days dz50_days dz51_days dz55_days dz56_days dz57_days dz58_days dz59_days dz60_days dz63_days dz64_days dz65_days dz67_days dz68_days dz69_days dz70_days dz71_days eb02_days eb03_days eb04_days eb05_days eb06_days eb07_days eb08_days eb09_days eb10_days eb12_days eb13_days eb14_days eb15_days ec11_days ec12_days ec13_days ec14_days ec15_days ec21_days ed01_days ed05_days ed08_days ed09_days ed11_days ed12_days ed13_days ed14_days ed15_days ed18_days ed24_days ed25_days ed26_days ed27_days ed28_days ed30_days ed31_days ey01_days ey02_days ey04_days ey06_days ey08_days ey11_days ey12_days ey13_days ey17_days ey22_days ey23_days ey30_days ey31_days ey32_days ey40_days ey41_days ey42_days ey43_days ey50_days ey51_days fd01_days fd02_days fd03_days fd04_days fd05_days fd10_days fd11_days fe01_days fe02_days fe03_days fe10_days fe11_days fe12_days fe13_days fe20_days fe21_days fe22_days fe30_days fe31_days fe32_days fe33_days fe34_days fe35_days fe36_days fe50_days ff01_days ff02_days ff04_days ff05_days ff12_days ff13_days ff14_days ff20_days ff21_days ff22_days ff30_days ff31_days ff32_days ff33_days ff34_days ff36_days ff37_days ff40_days ff41_days ff42_days ff43_days ff50_days ff51_days ff52_days ff53_days ff60_days ff61_days ff62_days ff63_days ga03_days ga04_days ga05_days ga06_days ga07_days ga10_days ga11_days ga13_days ga15_days ga16_days gb05_days gb06_days gb09_days gb10_days gb11_days gb12_days gb13_days gc01_days gc12_days gc17_days gc18_days hc20_days hc21_days hc26_days hc27_days hc28_days hc29_days hc30_days hc31_days hc32_days hc50_days hc53_days hc54_days hc60_days hc61_days hc62_days hc63_days hc64_days hc65_days hc70_days hc71_days hc72_days hd21_days hd23_days hd24_days hd25_days hd26_days hd39_days hd40_days he11_days he12_days he21_days he22_days he31_days he32_days he41_days he42_days he51_days he52_days he71_days he72_days he81_days he82_days he83_days hn12_days hn13_days hn14_days hn15_days hn22_days hn23_days hn24_days hn25_days hn32_days hn33_days hn34_days hn35_days hn42_days hn43_days hn44_days hn45_days hn46_days hn52_days hn53_days hn54_days hn55_days hn62_days hn63_days hn64_days hn65_days hn81_days hn86_days hn93_days ja12_days ja13_days ja20_days ja30_days ja34_days ja38_days ja43_days ja45_days jb70_days jb71_days jb91_days jc40_days jc41_days jc42_days jc43_days jc44_days jc45_days jc46_days jc47_days jd07_days ka03_days ka04_days ka05_days ka06_days ka07_days ka08_days ka09_days kb02_days kb03_days kb04_days kc04_days kc05_days la01_days la02_days la03_days la04_days la05_days la07_days la08_days la09_days la10_days la11_days la12_days la13_days la14_days lb06_days lb09_days lb10_days lb12_days lb13_days lb14_days lb15_days lb16_days lb17_days lb18_days lb19_days lb20_days lb21_days lb25_days lb26_days lb28_days lb29_days lb33_days lb35_days lb36_days lb37_days lb38_days lb39_days lb40_days lb42_days lb43_days lb46_days lb47_days lb48_days lb50_days lb51_days lb52_days lb53_days lb54_days lb55_days lb56_days lb57_days lb58_days lb59_days lb60_days lb61_days lb64_days lb65_days lb67_days lb68_days lb70_days lb71_days lb72_days lb74_days lb75_days lb76_days lb77_days lb78_days le01_days le02_days ma01_days ma02_days ma03_days ma04_days ma07_days ma09_days ma10_days ma11_days ma12_days ma22_days ma23_days ma24_days ma25_days ma29_days ma30_days ma31_days ma32_days ma35_days ma36_days ma38_days ma44_days ma48_days ma52_days ma53_days ma56_days mb05_days mb08_days mb09_days mc07_days mc08_days mc09_days mc10_days mc11_days mc12_days mc20_days mc21_days nz16_days nz17_days nz18_days nz19_days nz20_days nz21_days nz22_days nz24_days nz25_days nz26_days nz27_days nz30_days nz40_days nz50_days nz51_days nz71_days nz72_days rd01_days rd08_days rd20_days rd30_days rd40_days rd47_days rd48_days rd50_days rd51_days rd60_days rd61_days rn01_days rn04_days rn07_days rn08_days rn09_days rn13_days rn14_days rn15_days rn16_days rn17_days rn18_days rn19_days rn20_days rn21_days rn22_days rn23_days rn24_days rn25_days rn26_days rn27_days rn28_days rn29_days rn30_days rn31_days rn32_days rn33_days rn34_days rn50_days rn51_days rn52_days sa01_days sa02_days sa03_days sa04_days sa05_days sa06_days sa07_days sa08_days sa09_days sa11_days sa12_days sa14_days sa15_days sa16_days sa17_days sa18_days sa19_days sa20_days sa21_days sa22_days sa23_days sa24_days sa25_days sa26_days sa27_days sa30_days sa31_days sa32_days sa33_days sa35_days sa36_days sa37_days sa40_days sa42_days sa43_days sa44_days sa45_days sb01_days sb02_days sb03_days sb04_days sb05_days sb06_days sb07_days sb08_days sb09_days sb10_days sb11_days sb12_days sb13_days sb14_days sb15_days sb16_days sb17_days sc25_days sc26_days sc28_days sc29_days sc30_days sc40_days sc42_days sc44_days sc45_days sc47_days sc49_days sc51_days sc53_days sc54_days sc55_days sc56_days sc57_days uz01_days uz02_days uz03_days uz04_days uz05_days uz06_days uz15_days va10_days vc01_days vc02_days vc03_days vc04_days vc06_days vc08_days vc10_days vc12_days vc14_days vc16_days vc18_days vc20_days vc22_days vc24_days vc26_days vc28_days vc30_days vc32_days vc34_days vc36_days vc38_days vc40_days vc42_days wd01_days wd02_days wd03_days wd04_days wd05_days wd06_days wd07_days wd08_days wd09_days wf01_days wf02_days wh01_days wh02_days wh03_days wh04_days wh05_days wh06_days wh07_days wh08_days wh09_days wh10_days wh11_days wh12_days wh13_days wh14_days wh15_days wh16_days wh17_days wh18_days wh19_days wh20_days wh21_days wh22_days wh23_days wh50_days wh51_days wh52_days wh53_days wh54_days wh99_days wj01_days wj02_days wj03_days wj04_days wj06_days wj07_days wj10_days wj11_days xd01_days xd02_days xd03_days xd04_days xd05_days xd06_days xd07_days xd08_days xd09_days xd10_days xd11_days xd12_days xd13_days xd14_days xd15_days xd16_days xd17_days xd18_days xd19_days xd20_days xd21_days xd22_days xd23_days xd24_days xd25_days xd26_days xd27_days xd28_days xd29_days xd30_days xd31_days xd32_days xd33_days xd34_days xd37_days xd38_days xd39_days xd40_days xd41_days xd42_days xd43_days xd44_days xd45_days xd46_days xd47_days xd48_days xd49_days xd50_days xd51_days xd52_days xd53_days xd54_days xd55_days xd56_days xd57_days xd58_days xd90_days xd91_days ya03_days ya04_days ya10_days ya11_days ya12_days ya13_days yc01_days yc10_days yd01_days yd02_days yd03_days yd04_days yd05_days yf01_days yf04_days yg01_days yg02_days yg05_days yg06_days yg07_days yg10_days yg11_days yg12_days yh02_days yh03_days yh10_days yh20_days yh30_days yh31_days yh32_days yj09_days yj11_days yj13_days yj15_days yl02_days yl11_days yl12_days yl20_days yl21_days yl30_days yq05_days yq07_days yq08_days yq09_days yq12_days yq13_days yq15_days yq16_days yq22_days yq26_days yq31_days yq32_days yq40_days yq41_days yq42_days yq50_days yq51_days yr11_days yr12_days yr15_days yr16_days yr22_days yr23_days yr24_days yr25_days yr26_days yr31_days yr33_days yr40_days yr41_days yr42_days yr43_days yr44_days yr45_days yr48_days yr50_days yr51_days yr52_days yr53_days yr54_days yr56_days yr57_days yr63_days yr65_days yr66_days yr67_days {
egen total_`aggregate' = total(`aggregate')
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

/*Merge cost data
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
}/*

save "./output/`dataset'_nockd_complete.dta", replace

log close