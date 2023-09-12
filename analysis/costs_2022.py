from ehrql import Dataset
import datetime
from ehrql.tables.beta.tpp import (
	opa_cost, ec_cost, apcs_cost, patients, practice_registrations
)

def age_as_of(date):
  dob =  patients.date_of_birth
  delta_age = date - dob
  return delta_age.years
 # returns an integer (rounded down)

start_date = datetime.date(2022, 4, 1)
end_date = datetime.date(2023, 3, 31)

registrations = practice_registrations \
    .except_where(practice_registrations.start_date >= start_date) \
    .except_where(practice_registrations.end_date <= end_date)

# get the number of registrations in this period to exclude anyone with >1 in the `set_population` later
registrations_number = registrations.count_for_patient()

# need to get the start and end date of last registration only
registration = registrations \
    .sort_by(practice_registrations.start_date).last_for_patient()

#Define population first
dataset = Dataset()

dataset.sex = patients.sex
dataset.age = age_as_of(start_date)
dataset.practice_nuts = registration.practice_nuts1_region_name

population = (registrations_number == 1) & (dataset.age <= 100) & (dataset.age >= 18) & (dataset.sex.contains("male"))
dataset.define_population(population)

# Cost function
# inpatient hospital costs
dataset.apcs_cost = apcs_cost \
    .where((apcs_cost.admission_date >= start_date) &
          (apcs_cost.admission_date <=  end_date)).grand_total_payment_mff.sum_for_patient() 

# A&E monthly costs
dataset.ec_cost = ec_cost \
    .where((ec_cost.ec_decision_to_admit_date >= start_date) &
          (ec_cost.ec_decision_to_admit_date <=  end_date)).grand_total_payment_mff.sum_for_patient() 

# outpatient hospital costs
dataset.opa_cost = opa_cost \
    .where((opa_cost.appointment_date >= start_date) &
          (opa_cost.appointment_date <=  end_date)).grand_total_payment_mff.sum_for_patient()