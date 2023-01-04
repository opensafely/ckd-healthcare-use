sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_outcomes, replace t
use ./output/`dataset'_ckd_complete.dta

tab ckd_group ckd_progression

foreach outcome of varlist	m4_hospital_days			///
							m5_hospital_days			///
							m6_hospital_days			///							
							m7_hospital_days			///
							m8_hospital_days			///
							m9_hospital_days			///
							m10_hospital_days			///
							m11_hospital_days			///
							m12_hospital_days			///
							m1_hospital_days			///
							m2_hospital_days			///																											
							m3_hospital_days			///
							m4_critical_care_days		///
							m5_critical_care_days		///
							m6_critical_care_days		///							
							m7_critical_care_days		///
							m8_critical_care_days		///
							m9_critical_care_days		///
							m10_critical_care_days		///
							m11_critical_care_days		///
							m12_critical_care_days		///
							m1_critical_care_days		///
							m2_critical_care_days		///																											
							m3_critical_care_days		///
							m4_emergency_days			///
							m5_emergency_days			///
							m6_emergency_days			///							
							m7_emergency_days			///
							m8_emergency_days			///
							m9_emergency_days			///
							m10_emergency_days			///
							m11_emergency_days			///
							m12_emergency_days			///
							m1_emergency_days			///
							m2_emergency_days			///																											
							m3_emergency_days			///
							m4_outpatient_appointments	///
							m5_outpatient_appointments	///
							m6_outpatient_appointments	///							
							m7_outpatient_appointments	///
							m8_outpatient_appointments	///
							m9_outpatient_appointments	///
							m10_outpatient_appointments	///
							m11_outpatient_appointments	///
							m12_outpatient_appointments	///
							m1_outpatient_appointments	///
							m2_outpatient_appointments	///																											
							m3_outpatient_appointments	///
							m4_nephrology_appointments	///
							m5_nephrology_appointments	///
							m6_nephrology_appointments	///							
							m7_nephrology_appointments	///
							m8_nephrology_appointments	///
							m9_nephrology_appointments	///
							m10_nephrology_appointments	///
							m11_nephrology_appointments	///
							m12_nephrology_appointments	///
							m1_nephrology_appointments	///
							m2_nephrology_appointments	///																											
							m3_nephrology_appointments	///
							m4_transplant_appointments	///
							m5_transplant_appointments	///
							m6_transplant_appointments	///							
							m7_transplant_appointments	///
							m8_transplant_appointments	///
							m9_transplant_appointments	///
							m10_transplant_appointments	///
							m11_transplant_appointments	///
							m12_transplant_appointments	///
							m1_transplant_appointments	///
							m2_transplant_appointments	///																											
							m3_transplant_appointments	///
							m4_gp_interactions			///
							m5_gp_interactions			///
							m6_gp_interactions			///							
							m7_gp_interactions			///
							m8_gp_interactions			///
							m9_gp_interactions			///
							m10_gp_interactions			///
							m11_gp_interactions			///
							m12_gp_interactions			///
							m1_gp_interactions			///
							m2_gp_interactions			///																											
							m3_gp_interactions			///
							m4_blood_pressure			///
							m5_blood_pressure			///
							m6_blood_pressure			///							
							m7_blood_pressure			///
							m8_blood_pressure			///
							m9_blood_pressure			///
							m10_blood_pressure			///
							m11_blood_pressure			///
							m12_blood_pressure			///
							m1_blood_pressure			///
							m2_blood_pressure			///																											
							m3_blood_pressure			///
							m4_albuminuria				///
							m5_albuminuria				///
							m6_albuminuria				///							
							m7_albuminuria				///
							m8_albuminuria				///
							m9_albuminuria				///
							m10_albuminuria				///
							m11_albuminuria				///
							m12_albuminuria				///
							m1_albuminuria				///
							m2_albuminuria				///																											
							m3_albuminuria				///
							m4_creatinine				///
							m5_creatinine				///
							m6_creatinine				///							
							m7_creatinine				///
							m8_creatinine				///
							m9_creatinine				///
							m10_creatinine				///
							m11_creatinine				///
							m12_creatinine				///
							m1_creatinine				///
							m2_creatinine				///																											
							m3_creatinine {
total `outcome', over(ckd_group)
}


log close