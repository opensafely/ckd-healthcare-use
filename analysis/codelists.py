from cohortextractor import (codelist, codelist_from_csv, combine_codelists)

#Hospital COVID
covid_codes = codelist_from_csv(
    "codelists/opensafely-covid-identification.csv",
    system="icd10",
    column="icd10_code",
)
#Primary care COVID
covid_primary_care_positive_test = codelist_from_csv(
    "codelists/opensafely-covid-identification-in-primary-care-probable-covid-positive-test.csv",
    system="ctv3",
    column="CTV3ID",
)
covid_primary_care_code = codelist_from_csv(
    "codelists/opensafely-covid-identification-in-primary-care-probable-covid-clinical-code.csv",
    system="ctv3",
    column="CTV3ID",
)
covid_primary_care_sequalae = codelist_from_csv(
    "codelists/opensafely-covid-identification-in-primary-care-probable-covid-sequelae.csv",
    system="ctv3",
    column="CTV3ID",
)
any_covid_primary_care_code = combine_codelists(
    covid_primary_care_code,
    covid_primary_care_positive_test,
    covid_primary_care_sequalae,
)
#Creatinine
creatinine_codes = codelist_from_csv(
    "codelists/user-bangzheng-creatinine-value.csv",
    system="snomed",
    column="code",
)
#Critical care 
    #OPCS-4 procedural codes to determine people admitted to critical care
critical_care_codes = codelist_from_csv(
    "codelists/user-viyaasan-critical-care.csv",
    system="opcs4",
    column="code",
)
#Dialysis
dialysis_icd_10_codes = codelist_from_csv(
    "codelists/user-viyaasan-dialysis.csv",
    system="icd10",
    column="code",
)
dialysis_opcs_4_codes = codelist_from_csv(
    "codelists/user-viyaasan-dialysis-opcs-4.csv",
    system="opcs4",
    column="code",
)
dialysis_codes = codelist_from_csv(
    "codelists/user-viyaasan-dialysis-chronic.csv",
    system="ctv3",
    column="code"
)
#Dialysis access procedures
avf_formation_codes = codelist_from_csv(
    "codelists/user-viyaasan-haemodialysis-arteriovenous-fistula-formation-opcs-4.csv",
    system="opcs4",
    column="code",
)
pd_insertion_codes = codelist_from_csv(
    "codelists/user-viyaasan-peritoneal-dialysis-catheter-insertion-opcs-4.csv",
    system="opcs4",
    column="code",
)
#Kidney transplant
kidney_transplant_icd_10_codes = codelist_from_csv(
    "codelists/user-viyaasan-kidney-transplant.csv",
    system="icd10",
    column="code",
)
kidney_transplant_opcs_4_codes = codelist_from_csv(
    "codelists/user-viyaasan-kidney-transplant-opcs-4.csv",
    system="opcs4",
    column="code",
)
kidney_transplant_codes = codelist_from_csv(
    "codelists/opensafely-kidney-transplant.csv",
    system="ctv3",
    column="CTV3ID"
)
#Albuminuria
albuminuria_codes = codelist_from_csv(
    "codelists/ukrr-albumincreatinine-ratio-acr-tests-level.csv",
    system="snomed",
    column="code",
)
#Blood pressure measurement
blood_pressure_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-bp_cod.csv",
    system="snomed",
    column="code",
)
#Ethnicity
ethnicity_codes = codelist_from_csv(
    "codelists/opensafely-ethnicity.csv",
    system="ctv3",
    column="Code",
    category_column="Grouping_6",
)