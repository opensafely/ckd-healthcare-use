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
							m4_admitted_patients		///
							m5_admitted_patients		///
							m6_admitted_patients		///							
							m7_admitted_patients		///
							m8_admitted_patients		///
							m9_admitted_patients		///
							m10_admitted_patients		///
							m11_admitted_patients		///
							m12_admitted_patients		///
							m1_admitted_patients		///
							m2_admitted_patients		///																											
							m3_admitted_patients		///
							m4_fistula_formation		///
							m5_fistula_formation		///
							m6_fistula_formation		///							
							m7_fistula_formation		///
							m8_fistula_formation		///
							m9_fistula_formation		///
							m10_fistula_formation		///
							m11_fistula_formation		///
							m12_fistula_formation		///
							m1_fistula_formation		///
							m2_fistula_formation		///																											
							m3_fistula_formation		///
							m4_pd_insertion				///
							m5_pd_insertion				///
							m6_pd_insertion				///							
							m7_pd_insertion				///
							m8_pd_insertion				///
							m9_pd_insertion				///
							m10_pd_insertion			///
							m11_pd_insertion			///
							m12_pd_insertion			///
							m1_pd_insertion				///
							m2_pd_insertion				///																											
							m3_pd_insertion				///
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
							m4_critical_care_patients	///
							m5_critical_care_patients	///
							m6_critical_care_patients	///							
							m7_critical_care_patients	///
							m8_critical_care_patients	///
							m9_critical_care_patients	///
							m10_critical_care_patients	///
							m11_critical_care_patients	///
							m12_critical_care_patients	///
							m1_critical_care_patients	///
							m2_critical_care_patients	///																											
							m3_critical_care_patients	///
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
							m4_emergency_patients		///
							m5_emergency_patients		///
							m6_emergency_patients		///							
							m7_emergency_patients		///
							m8_emergency_patients		///
							m9_emergency_patients		///
							m10_emergency_patients		///
							m11_emergency_patients		///
							m12_emergency_patients		///
							m1_emergency_patients		///
							m2_emergency_patients		///																											
							m3_emergency_patients		///
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