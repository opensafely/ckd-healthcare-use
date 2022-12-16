sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_outcomes, replace t
use ./output/`dataset'_ckd_complete.dta

foreach outcome of varlist	q1_hospital_days			///
							q2_hospital_days			///
							q3_hospital_days			///
							q4_hospital_days			///
							q1_critical_care_days		///
							q2_critical_care_days		///
							q3_critical_care_days		///
							q4_critical_care_days		///
							q1_emergency_days			///
							q2_emergency_days			///
							q3_emergency_days			///
							q4_emergency_days			///
							q1_outpatient_appointments	///
							q2_outpatient_appointments	///
							q3_outpatient_appointments	///
							q4_outpatient_appointments	///
							q1_nephrology_appointments	///
							q2_nephrology_appointments	///
							q3_nephrology_appointments	///
							q4_nephrology_appointments	///
							q1_transplant_appointments	///
							q2_transplant_appointments	///
							q3_transplant_appointments	///
							q4_transplant_appointments	///
							q1_gp_interactions			///
							q2_gp_interactions			///
							q3_gp_interactions			///
							q4_gp_interactions			///
							q1_blood_pressure			///
							q2_blood_pressure			///
							q3_blood_pressure			///
							q4_blood_pressure			///
							q1_albuminuria				///
							q2_albuminuria				///
							q3_albuminuria				///
							q4_albuminuria				///
							q1_creatinine				///
							q2_creatinine				///
							q3_creatinine				///
							q4_creatinine {
total `outcome', over(ckd_group)
}
tab ckd_group ckd_progression

log close