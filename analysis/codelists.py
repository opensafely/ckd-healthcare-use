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

#Cardiovascular admissions
cardiovascular_codes = codelist_from_csv(
    "codelists/user-viyaasan-cardiovascular-disease-icd-10.csv",
    system="icd10",
    column="code",
)

icd1_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-i.csv",
    system="icd10",
    column="code",
)

icd2_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-ii.csv",
    system="icd10",
    column="code",
)

icd3_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-iii.csv",
    system="icd10",
    column="code",
)

icd4_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-iv.csv",
    system="icd10",
    column="code",
)

icd5_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-v.csv",
    system="icd10",
    column="code",
)

icd6_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-vi.csv",
    system="icd10",
    column="code",
)

icd7_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-vii.csv",
    system="icd10",
    column="code",
)

icd8_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-viii.csv",
    system="icd10",
    column="code",
)

icd9_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-ix.csv",
    system="icd10",
    column="code",
)

icd10_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-x.csv",
    system="icd10",
    column="code",
)

icd11_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xi.csv",
    system="icd10",
    column="code",
)

icd12_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xii.csv",
    system="icd10",
    column="code",
)

icd13_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xiii.csv",
    system="icd10",
    column="code",
)

icd14_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xiv.csv",
    system="icd10",
    column="code",
)

icd15_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xv.csv",
    system="icd10",
    column="code",
)

icd16_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xvi.csv",
    system="icd10",
    column="code",
)

icd17_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xvii.csv",
    system="icd10",
    column="code",
)

icd18_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xviii.csv",
    system="icd10",
    column="code",
)

icd19_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xix.csv",
    system="icd10",
    column="code",
)

icd20_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xx.csv",
    system="icd10",
    column="code",
)

icd21_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xxi.csv",
    system="icd10",
    column="code",
)

icd22_codes = codelist_from_csv(
    "codelists/opensafely-icd-10-chapter-xxii.csv",
    system="icd10",
    column="code",
)


hrg_AA22 = codelists_from_csv(
    "local_codelists/hrg_AA22.csv",
    system="icd10",
    columnn="code",
)

hrg_AA23 = codelists_from_csv(
    "local_codelists/hrg_AA23.csv",
    system="icd10",
    columnn="code",
)

hrg_AA24 = codelists_from_csv(
    "local_codelists/hrg_AA24.csv",
    system="icd10",
    columnn="code",
)

hrg_AA25 = codelists_from_csv(
    "local_codelists/hrg_AA25.csv",
    system="icd10",
    columnn="code",
)

hrg_AA26 = codelists_from_csv(
    "local_codelists/hrg_AA26.csv",
    system="icd10",
    columnn="code",
)

hrg_AA28 = codelists_from_csv(
    "local_codelists/hrg_AA28.csv",
    system="icd10",
    columnn="code",
)

hrg_AA29 = codelists_from_csv(
    "local_codelists/hrg_AA29.csv",
    system="icd10",
    columnn="code",
)

hrg_AA30 = codelists_from_csv(
    "local_codelists/hrg_AA30.csv",
    system="icd10",
    columnn="code",
)

hrg_AA31 = codelists_from_csv(
    "local_codelists/hrg_AA31.csv",
    system="icd10",
    columnn="code",
)

hrg_AA35 = codelists_from_csv(
    "local_codelists/hrg_AA35.csv",
    system="icd10",
    columnn="code",
)

hrg_AA43 = codelists_from_csv(
    "local_codelists/hrg_AA43.csv",
    system="icd10",
    columnn="code",
)

hrg_BZ24 = codelists_from_csv(
    "local_codelists/hrg_BZ24.csv",
    system="icd10",
    columnn="code",
)

hrg_CB01 = codelists_from_csv(
    "local_codelists/hrg_CB01.csv",
    system="icd10",
    columnn="code",
)

hrg_CB02 = codelists_from_csv(
    "local_codelists/hrg_CB02.csv",
    system="icd10",
    columnn="code",
)

hrg_DX21 = codelists_from_csv(
    "local_codelists/hrg_DX21.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ09 = codelists_from_csv(
    "local_codelists/hrg_DZ09.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ10 = codelists_from_csv(
    "local_codelists/hrg_DZ10.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ11 = codelists_from_csv(
    "local_codelists/hrg_DZ11.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ12 = codelists_from_csv(
    "local_codelists/hrg_DZ12.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ13 = codelists_from_csv(
    "local_codelists/hrg_DZ13.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ14 = codelists_from_csv(
    "local_codelists/hrg_DZ14.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ15 = codelists_from_csv(
    "local_codelists/hrg_DZ15.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ16 = codelists_from_csv(
    "local_codelists/hrg_DZ16.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ17 = codelists_from_csv(
    "local_codelists/hrg_DZ17.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ18 = codelists_from_csv(
    "local_codelists/hrg_DZ18.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ19 = codelists_from_csv(
    "local_codelists/hrg_DZ19.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ20 = codelists_from_csv(
    "local_codelists/hrg_DZ20.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ22 = codelists_from_csv(
    "local_codelists/hrg_DZ22.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ23 = codelists_from_csv(
    "local_codelists/hrg_DZ23.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ24 = codelists_from_csv(
    "local_codelists/hrg_DZ24.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ25 = codelists_from_csv(
    "local_codelists/hrg_DZ25.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ26 = codelists_from_csv(
    "local_codelists/hrg_DZ26.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ27 = codelists_from_csv(
    "local_codelists/hrg_DZ27.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ28 = codelists_from_csv(
    "local_codelists/hrg_DZ28.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ29 = codelists_from_csv(
    "local_codelists/hrg_DZ29.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ51 = codelists_from_csv(
    "local_codelists/hrg_DZ51.csv",
    system="icd10",
    columnn="code",
)

hrg_DZ65 = codelists_from_csv(
    "local_codelists/hrg_DZ65.csv",
    system="icd10",
    columnn="code",
)

hrg_EB02 = codelists_from_csv(
    "local_codelists/hrg_EB02.csv",
    system="icd10",
    columnn="code",
)

hrg_EB03 = codelists_from_csv(
    "local_codelists/hrg_EB03.csv",
    system="icd10",
    columnn="code",
)

hrg_EB04 = codelists_from_csv(
    "local_codelists/hrg_EB04.csv",
    system="icd10",
    columnn="code",
)

hrg_EB05 = codelists_from_csv(
    "local_codelists/hrg_EB05.csv",
    system="icd10",
    columnn="code",
)

hrg_EB06 = codelists_from_csv(
    "local_codelists/hrg_EB06.csv",
    system="icd10",
    columnn="code",
)

hrg_EB07 = codelists_from_csv(
    "local_codelists/hrg_EB07.csv",
    system="icd10",
    columnn="code",
)

hrg_EB08 = codelists_from_csv(
    "local_codelists/hrg_EB08.csv",
    system="icd10",
    columnn="code",
)

hrg_EB09 = codelists_from_csv(
    "local_codelists/hrg_EB09.csv",
    system="icd10",
    columnn="code",
)

hrg_EB10 = codelists_from_csv(
    "local_codelists/hrg_EB10.csv",
    system="icd10",
    columnn="code",
)

hrg_EB12 = codelists_from_csv(
    "local_codelists/hrg_EB12.csv",
    system="icd10",
    columnn="code",
)

hrg_EB13 = codelists_from_csv(
    "local_codelists/hrg_EB13.csv",
    system="icd10",
    columnn="code",
)

hrg_EB14 = codelists_from_csv(
    "local_codelists/hrg_EB14.csv",
    system="icd10",
    columnn="code",
)

hrg_EB15 = codelists_from_csv(
    "local_codelists/hrg_EB15.csv",
    system="icd10",
    columnn="code",
)

hrg_FD01 = codelists_from_csv(
    "local_codelists/hrg_FD01.csv",
    system="icd10",
    columnn="code",
)

hrg_FD02 = codelists_from_csv(
    "local_codelists/hrg_FD02.csv",
    system="icd10",
    columnn="code",
)

hrg_FD03 = codelists_from_csv(
    "local_codelists/hrg_FD03.csv",
    system="icd10",
    columnn="code",
)

hrg_FD04 = codelists_from_csv(
    "local_codelists/hrg_FD04.csv",
    system="icd10",
    columnn="code",
)

hrg_FD05 = codelists_from_csv(
    "local_codelists/hrg_FD05.csv",
    system="icd10",
    columnn="code",
)

hrg_FD10 = codelists_from_csv(
    "local_codelists/hrg_FD10.csv",
    system="icd10",
    columnn="code",
)

hrg_FD11 = codelists_from_csv(
    "local_codelists/hrg_FD11.csv",
    system="icd10",
    columnn="code",
)

hrg_GC01 = codelists_from_csv(
    "local_codelists/hrg_GC01.csv",
    system="icd10",
    columnn="code",
)

hrg_GC12 = codelists_from_csv(
    "local_codelists/hrg_GC12.csv",
    system="icd10",
    columnn="code",
)

hrg_GC17 = codelists_from_csv(
    "local_codelists/hrg_GC17.csv",
    system="icd10",
    columnn="code",
)

hrg_GC18 = codelists_from_csv(
    "local_codelists/hrg_GC18.csv",
    system="icd10",
    columnn="code",
)

hrg_HC20 = codelists_from_csv(
    "local_codelists/hrg_HC20.csv",
    system="icd10",
    columnn="code",
)

hrg_HC21 = codelists_from_csv(
    "local_codelists/hrg_HC21.csv",
    system="icd10",
    columnn="code",
)

hrg_HC26 = codelists_from_csv(
    "local_codelists/hrg_HC26.csv",
    system="icd10",
    columnn="code",
)

hrg_HC27 = codelists_from_csv(
    "local_codelists/hrg_HC27.csv",
    system="icd10",
    columnn="code",
)

hrg_HC28 = codelists_from_csv(
    "local_codelists/hrg_HC28.csv",
    system="icd10",
    columnn="code",
)

hrg_HC29 = codelists_from_csv(
    "local_codelists/hrg_HC29.csv",
    system="icd10",
    columnn="code",
)

hrg_HC30 = codelists_from_csv(
    "local_codelists/hrg_HC30.csv",
    system="icd10",
    columnn="code",
)

hrg_HC31 = codelists_from_csv(
    "local_codelists/hrg_HC31.csv",
    system="icd10",
    columnn="code",
)

hrg_HC32 = codelists_from_csv(
    "local_codelists/hrg_HC32.csv",
    system="icd10",
    columnn="code",
)

hrg_HD21 = codelists_from_csv(
    "local_codelists/hrg_HD21.csv",
    system="icd10",
    columnn="code",
)

hrg_HD23 = codelists_from_csv(
    "local_codelists/hrg_HD23.csv",
    system="icd10",
    columnn="code",
)

hrg_HD24 = codelists_from_csv(
    "local_codelists/hrg_HD24.csv",
    system="icd10",
    columnn="code",
)

hrg_HD25 = codelists_from_csv(
    "local_codelists/hrg_HD25.csv",
    system="icd10",
    columnn="code",
)

hrg_HD26 = codelists_from_csv(
    "local_codelists/hrg_HD26.csv",
    system="icd10",
    columnn="code",
)

hrg_HD39 = codelists_from_csv(
    "local_codelists/hrg_HD39.csv",
    system="icd10",
    columnn="code",
)

hrg_HD40 = codelists_from_csv(
    "local_codelists/hrg_HD40.csv",
    system="icd10",
    columnn="code",
)

hrg_HE11 = codelists_from_csv(
    "local_codelists/hrg_HE11.csv",
    system="icd10",
    columnn="code",
)

hrg_HE12 = codelists_from_csv(
    "local_codelists/hrg_HE12.csv",
    system="icd10",
    columnn="code",
)

hrg_HE21 = codelists_from_csv(
    "local_codelists/hrg_HE21.csv",
    system="icd10",
    columnn="code",
)

hrg_HE22 = codelists_from_csv(
    "local_codelists/hrg_HE22.csv",
    system="icd10",
    columnn="code",
)

hrg_HE31 = codelists_from_csv(
    "local_codelists/hrg_HE31.csv",
    system="icd10",
    columnn="code",
)

hrg_HE32 = codelists_from_csv(
    "local_codelists/hrg_HE32.csv",
    system="icd10",
    columnn="code",
)

hrg_HE41 = codelists_from_csv(
    "local_codelists/hrg_HE41.csv",
    system="icd10",
    columnn="code",
)

hrg_HE42 = codelists_from_csv(
    "local_codelists/hrg_HE42.csv",
    system="icd10",
    columnn="code",
)

hrg_HE51 = codelists_from_csv(
    "local_codelists/hrg_HE51.csv",
    system="icd10",
    columnn="code",
)

hrg_HE52 = codelists_from_csv(
    "local_codelists/hrg_HE52.csv",
    system="icd10",
    columnn="code",
)

hrg_HE71 = codelists_from_csv(
    "local_codelists/hrg_HE71.csv",
    system="icd10",
    columnn="code",
)

hrg_HE72 = codelists_from_csv(
    "local_codelists/hrg_HE72.csv",
    system="icd10",
    columnn="code",
)

hrg_HE81 = codelists_from_csv(
    "local_codelists/hrg_HE81.csv",
    system="icd10",
    columnn="code",
)

hrg_HE82 = codelists_from_csv(
    "local_codelists/hrg_HE82.csv",
    system="icd10",
    columnn="code",
)

hrg_HE83 = codelists_from_csv(
    "local_codelists/hrg_HE83.csv",
    system="icd10",
    columnn="code",
)

hrg_JA12 = codelists_from_csv(
    "local_codelists/hrg_JA12.csv",
    system="icd10",
    columnn="code",
)

hrg_JA13 = codelists_from_csv(
    "local_codelists/hrg_JA13.csv",
    system="icd10",
    columnn="code",
)

hrg_JB91 = codelists_from_csv(
    "local_codelists/hrg_JB91.csv",
    system="icd10",
    columnn="code",
)

hrg_JD07 = codelists_from_csv(
    "local_codelists/hrg_JD07.csv",
    system="icd10",
    columnn="code",
)

hrg_KA05 = codelists_from_csv(
    "local_codelists/hrg_KA05.csv",
    system="icd10",
    columnn="code",
)

hrg_KA06 = codelists_from_csv(
    "local_codelists/hrg_KA06.csv",
    system="icd10",
    columnn="code",
)

hrg_KA07 = codelists_from_csv(
    "local_codelists/hrg_KA07.csv",
    system="icd10",
    columnn="code",
)

hrg_KA08 = codelists_from_csv(
    "local_codelists/hrg_KA08.csv",
    system="icd10",
    columnn="code",
)

hrg_KB02 = codelists_from_csv(
    "local_codelists/hrg_KB02.csv",
    system="icd10",
    columnn="code",
)

hrg_KB03 = codelists_from_csv(
    "local_codelists/hrg_KB03.csv",
    system="icd10",
    columnn="code",
)

hrg_KC04 = codelists_from_csv(
    "local_codelists/hrg_KC04.csv",
    system="icd10",
    columnn="code",
)

hrg_KC05 = codelists_from_csv(
    "local_codelists/hrg_KC05.csv",
    system="icd10",
    columnn="code",
)

hrg_LA04 = codelists_from_csv(
    "local_codelists/hrg_LA04.csv",
    system="icd10",
    columnn="code",
)

hrg_LA07 = codelists_from_csv(
    "local_codelists/hrg_LA07.csv",
    system="icd10",
    columnn="code",
)

hrg_LA08 = codelists_from_csv(
    "local_codelists/hrg_LA08.csv",
    system="icd10",
    columnn="code",
)

hrg_LA09 = codelists_from_csv(
    "local_codelists/hrg_LA09.csv",
    system="icd10",
    columnn="code",
)

hrg_LB06 = codelists_from_csv(
    "local_codelists/hrg_LB06.csv",
    system="icd10",
    columnn="code",
)

hrg_LB16 = codelists_from_csv(
    "local_codelists/hrg_LB16.csv",
    system="icd10",
    columnn="code",
)

hrg_LB19 = codelists_from_csv(
    "local_codelists/hrg_LB19.csv",
    system="icd10",
    columnn="code",
)

hrg_LB20 = codelists_from_csv(
    "local_codelists/hrg_LB20.csv",
    system="icd10",
    columnn="code",
)

hrg_LB28 = codelists_from_csv(
    "local_codelists/hrg_LB28.csv",
    system="icd10",
    columnn="code",
)

hrg_LB35 = codelists_from_csv(
    "local_codelists/hrg_LB35.csv",
    system="icd10",
    columnn="code",
)

hrg_LB37 = codelists_from_csv(
    "local_codelists/hrg_LB37.csv",
    system="icd10",
    columnn="code",
)

hrg_LB38 = codelists_from_csv(
    "local_codelists/hrg_LB38.csv",
    system="icd10",
    columnn="code",
)

hrg_LB40 = codelists_from_csv(
    "local_codelists/hrg_LB40.csv",
    system="icd10",
    columnn="code",
)

hrg_LB57 = codelists_from_csv(
    "local_codelists/hrg_LB57.csv",
    system="icd10",
    columnn="code",
)

hrg_LB58 = codelists_from_csv(
    "local_codelists/hrg_LB58.csv",
    system="icd10",
    columnn="code",
)

hrg_MB05 = codelists_from_csv(
    "local_codelists/hrg_MB05.csv",
    system="icd10",
    columnn="code",
)

hrg_MB08 = codelists_from_csv(
    "local_codelists/hrg_MB08.csv",
    system="icd10",
    columnn="code",
)

hrg_MB09 = codelists_from_csv(
    "local_codelists/hrg_MB09.csv",
    system="icd10",
    columnn="code",
)

hrg_NZ16 = codelists_from_csv(
    "local_codelists/hrg_NZ16.csv",
    system="icd10",
    columnn="code",
)

hrg_NZ17 = codelists_from_csv(
    "local_codelists/hrg_NZ17.csv",
    system="icd10",
    columnn="code",
)

hrg_NZ18 = codelists_from_csv(
    "local_codelists/hrg_NZ18.csv",
    system="icd10",
    columnn="code",
)

hrg_NZ19 = codelists_from_csv(
    "local_codelists/hrg_NZ19.csv",
    system="icd10",
    columnn="code",
)

hrg_NZ20 = codelists_from_csv(
    "local_codelists/hrg_NZ20.csv",
    system="icd10",
    columnn="code",
)

hrg_NZ25 = codelists_from_csv(
    "local_codelists/hrg_NZ25.csv",
    system="icd10",
    columnn="code",
)

hrg_NZ26 = codelists_from_csv(
    "local_codelists/hrg_NZ26.csv",
    system="icd10",
    columnn="code",
)

hrg_SA01 = codelists_from_csv(
    "local_codelists/hrg_SA01.csv",
    system="icd10",
    columnn="code",
)

hrg_SA02 = codelists_from_csv(
    "local_codelists/hrg_SA02.csv",
    system="icd10",
    columnn="code",
)

hrg_SA03 = codelists_from_csv(
    "local_codelists/hrg_SA03.csv",
    system="icd10",
    columnn="code",
)

hrg_SA04 = codelists_from_csv(
    "local_codelists/hrg_SA04.csv",
    system="icd10",
    columnn="code",
)

hrg_SA05 = codelists_from_csv(
    "local_codelists/hrg_SA05.csv",
    system="icd10",
    columnn="code",
)

hrg_SA06 = codelists_from_csv(
    "local_codelists/hrg_SA06.csv",
    system="icd10",
    columnn="code",
)

hrg_SA07 = codelists_from_csv(
    "local_codelists/hrg_SA07.csv",
    system="icd10",
    columnn="code",
)

hrg_SA08 = codelists_from_csv(
    "local_codelists/hrg_SA08.csv",
    system="icd10",
    columnn="code",
)

hrg_SA09 = codelists_from_csv(
    "local_codelists/hrg_SA09.csv",
    system="icd10",
    columnn="code",
)

hrg_SA11 = codelists_from_csv(
    "local_codelists/hrg_SA11.csv",
    system="icd10",
    columnn="code",
)

hrg_SA12 = codelists_from_csv(
    "local_codelists/hrg_SA12.csv",
    system="icd10",
    columnn="code",
)

hrg_SA17 = codelists_from_csv(
    "local_codelists/hrg_SA17.csv",
    system="icd10",
    columnn="code",
)

hrg_SA24 = codelists_from_csv(
    "local_codelists/hrg_SA24.csv",
    system="icd10",
    columnn="code",
)

hrg_SA25 = codelists_from_csv(
    "local_codelists/hrg_SA25.csv",
    system="icd10",
    columnn="code",
)

hrg_SA30 = codelists_from_csv(
    "local_codelists/hrg_SA30.csv",
    system="icd10",
    columnn="code",
)

hrg_SA31 = codelists_from_csv(
    "local_codelists/hrg_SA31.csv",
    system="icd10",
    columnn="code",
)

hrg_SA32 = codelists_from_csv(
    "local_codelists/hrg_SA32.csv",
    system="icd10",
    columnn="code",
)

hrg_SA35 = codelists_from_csv(
    "local_codelists/hrg_SA35.csv",
    system="icd10",
    columnn="code",
)

hrg_SA36 = codelists_from_csv(
    "local_codelists/hrg_SA36.csv",
    system="icd10",
    columnn="code",
)

hrg_SA37 = codelists_from_csv(
    "local_codelists/hrg_SA37.csv",
    system="icd10",
    columnn="code",
)

hrg_UZ01 = codelists_from_csv(
    "local_codelists/hrg_UZ01.csv",
    system="icd10",
    columnn="code",
)

hrg_UZ02 = codelists_from_csv(
    "local_codelists/hrg_UZ02.csv",
    system="icd10",
    columnn="code",
)

hrg_UZ03 = codelists_from_csv(
    "local_codelists/hrg_UZ03.csv",
    system="icd10",
    columnn="code",
)

hrg_UZ04 = codelists_from_csv(
    "local_codelists/hrg_UZ04.csv",
    system="icd10",
    columnn="code",
)

hrg_UZ15 = codelists_from_csv(
    "local_codelists/hrg_UZ15.csv",
    system="icd10",
    columnn="code",
)

hrg_VA10 = codelists_from_csv(
    "local_codelists/hrg_VA10.csv",
    system="icd10",
    columnn="code",
)

hrg_WD01 = codelists_from_csv(
    "local_codelists/hrg_WD01.csv",
    system="icd10",
    columnn="code",
)

hrg_WD02 = codelists_from_csv(
    "local_codelists/hrg_WD02.csv",
    system="icd10",
    columnn="code",
)

hrg_WD03 = codelists_from_csv(
    "local_codelists/hrg_WD03.csv",
    system="icd10",
    columnn="code",
)

hrg_WD04 = codelists_from_csv(
    "local_codelists/hrg_WD04.csv",
    system="icd10",
    columnn="code",
)

hrg_WD05 = codelists_from_csv(
    "local_codelists/hrg_WD05.csv",
    system="icd10",
    columnn="code",
)

hrg_WD06 = codelists_from_csv(
    "local_codelists/hrg_WD06.csv",
    system="icd10",
    columnn="code",
)

hrg_WD07 = codelists_from_csv(
    "local_codelists/hrg_WD07.csv",
    system="icd10",
    columnn="code",
)

hrg_WD08 = codelists_from_csv(
    "local_codelists/hrg_WD08.csv",
    system="icd10",
    columnn="code",
)

hrg_WD09 = codelists_from_csv(
    "local_codelists/hrg_WD09.csv",
    system="icd10",
    columnn="code",
)

hrg_WH01 = codelists_from_csv(
    "local_codelists/hrg_WH01.csv",
    system="icd10",
    columnn="code",
)

hrg_WH02 = codelists_from_csv(
    "local_codelists/hrg_WH02.csv",
    system="icd10",
    columnn="code",
)

hrg_WH03 = codelists_from_csv(
    "local_codelists/hrg_WH03.csv",
    system="icd10",
    columnn="code",
)

hrg_WH04 = codelists_from_csv(
    "local_codelists/hrg_WH04.csv",
    system="icd10",
    columnn="code",
)

hrg_WH05 = codelists_from_csv(
    "local_codelists/hrg_WH05.csv",
    system="icd10",
    columnn="code",
)

hrg_WH06 = codelists_from_csv(
    "local_codelists/hrg_WH06.csv",
    system="icd10",
    columnn="code",
)

hrg_WH07 = codelists_from_csv(
    "local_codelists/hrg_WH07.csv",
    system="icd10",
    columnn="code",
)

hrg_WH08 = codelists_from_csv(
    "local_codelists/hrg_WH08.csv",
    system="icd10",
    columnn="code",
)

hrg_WH09 = codelists_from_csv(
    "local_codelists/hrg_WH09.csv",
    system="icd10",
    columnn="code",
)

hrg_WH10 = codelists_from_csv(
    "local_codelists/hrg_WH10.csv",
    system="icd10",
    columnn="code",
)

hrg_WH11 = codelists_from_csv(
    "local_codelists/hrg_WH11.csv",
    system="icd10",
    columnn="code",
)

hrg_WH12 = codelists_from_csv(
    "local_codelists/hrg_WH12.csv",
    system="icd10",
    columnn="code",
)

hrg_WH13 = codelists_from_csv(
    "local_codelists/hrg_WH13.csv",
    system="icd10",
    columnn="code",
)

hrg_WH14 = codelists_from_csv(
    "local_codelists/hrg_WH14.csv",
    system="icd10",
    columnn="code",
)

hrg_WH15 = codelists_from_csv(
    "local_codelists/hrg_WH15.csv",
    system="icd10",
    columnn="code",
)

hrg_WH16 = codelists_from_csv(
    "local_codelists/hrg_WH16.csv",
    system="icd10",
    columnn="code",
)

hrg_WH17 = codelists_from_csv(
    "local_codelists/hrg_WH17.csv",
    system="icd10",
    columnn="code",
)

hrg_WH18 = codelists_from_csv(
    "local_codelists/hrg_WH18.csv",
    system="icd10",
    columnn="code",
)

hrg_WH19 = codelists_from_csv(
    "local_codelists/hrg_WH19.csv",
    system="icd10",
    columnn="code",
)

hrg_WH20 = codelists_from_csv(
    "local_codelists/hrg_WH20.csv",
    system="icd10",
    columnn="code",
)

hrg_WH21 = codelists_from_csv(
    "local_codelists/hrg_WH21.csv",
    system="icd10",
    columnn="code",
)

hrg_WH22 = codelists_from_csv(
    "local_codelists/hrg_WH22.csv",
    system="icd10",
    columnn="code",
)

hrg_WH23 = codelists_from_csv(
    "local_codelists/hrg_WH23.csv",
    system="icd10",
    columnn="code",
)

hrg_WH50 = codelists_from_csv(
    "local_codelists/hrg_WH50.csv",
    system="icd10",
    columnn="code",
)

hrg_WH51 = codelists_from_csv(
    "local_codelists/hrg_WH51.csv",
    system="icd10",
    columnn="code",
)

hrg_WH52 = codelists_from_csv(
    "local_codelists/hrg_WH52.csv",
    system="icd10",
    columnn="code",
)

hrg_WH53 = codelists_from_csv(
    "local_codelists/hrg_WH53.csv",
    system="icd10",
    columnn="code",
)

hrg_WH99 = codelists_from_csv(
    "local_codelists/hrg_WH99.csv",
    system="icd10",
    columnn="code",
)

hrg_WJ01 = codelists_from_csv(
    "local_codelists/hrg_WJ01.csv",
    system="icd10",
    columnn="code",
)

hrg_WJ02 = codelists_from_csv(
    "local_codelists/hrg_WJ02.csv",
    system="icd10",
    columnn="code",
)

hrg_WJ03 = codelists_from_csv(
    "local_codelists/hrg_WJ03.csv",
    system="icd10",
    columnn="code",
)

hrg_WJ04 = codelists_from_csv(
    "local_codelists/hrg_WJ04.csv",
    system="icd10",
    columnn="code",
)

hrg_WJ06 = codelists_from_csv(
    "local_codelists/hrg_WJ06.csv",
    system="icd10",
    columnn="code",
)

hrg_WJ07 = codelists_from_csv(
    "local_codelists/hrg_WJ07.csv",
    system="icd10",
    columnn="code",
)

hrg_WJ10 = codelists_from_csv(
    "local_codelists/hrg_WJ10.csv",
    system="icd10",
    columnn="code",
)

hrg_WJ11 = codelists_from_csv(
    "local_codelists/hrg_WJ11.csv",
    system="icd10",
    columnn="code",
)

hrg_YQ50 = codelists_from_csv(
    "local_codelists/hrg_YQ50.csv",
    system="icd10",
    columnn="code",
)

hrg_YQ51 = codelists_from_csv(
    "local_codelists/hrg_YQ51.csv",
    system="icd10",
    columnn="code",
)

hrg_AA32 = codelists_from_csv(
    "local_codelists/hrg_AA32.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA33 = codelists_from_csv(
    "local_codelists/hrg_AA33.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA50 = codelists_from_csv(
    "local_codelists/hrg_AA50.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA51 = codelists_from_csv(
    "local_codelists/hrg_AA51.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA52 = codelists_from_csv(
    "local_codelists/hrg_AA52.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA53 = codelists_from_csv(
    "local_codelists/hrg_AA53.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA54 = codelists_from_csv(
    "local_codelists/hrg_AA54.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA55 = codelists_from_csv(
    "local_codelists/hrg_AA55.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA57 = codelists_from_csv(
    "local_codelists/hrg_AA57.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA60 = codelists_from_csv(
    "local_codelists/hrg_AA60.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA61 = codelists_from_csv(
    "local_codelists/hrg_AA61.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA71 = codelists_from_csv(
    "local_codelists/hrg_AA71.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA81 = codelists_from_csv(
    "local_codelists/hrg_AA81.csv",
    system="opcs4",
    columnn="code",
)

hrg_AA83 = codelists_from_csv(
    "local_codelists/hrg_AA83.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB11 = codelists_from_csv(
    "local_codelists/hrg_AB11.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB15 = codelists_from_csv(
    "local_codelists/hrg_AB15.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB16 = codelists_from_csv(
    "local_codelists/hrg_AB16.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB18 = codelists_from_csv(
    "local_codelists/hrg_AB18.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB20 = codelists_from_csv(
    "local_codelists/hrg_AB20.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB21 = codelists_from_csv(
    "local_codelists/hrg_AB21.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB22 = codelists_from_csv(
    "local_codelists/hrg_AB22.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB23 = codelists_from_csv(
    "local_codelists/hrg_AB23.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB24 = codelists_from_csv(
    "local_codelists/hrg_AB24.csv",
    system="opcs4",
    columnn="code",
)

hrg_AB26 = codelists_from_csv(
    "local_codelists/hrg_AB26.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ31 = codelists_from_csv(
    "local_codelists/hrg_BZ31.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ32 = codelists_from_csv(
    "local_codelists/hrg_BZ32.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ33 = codelists_from_csv(
    "local_codelists/hrg_BZ33.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ41 = codelists_from_csv(
    "local_codelists/hrg_BZ41.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ42 = codelists_from_csv(
    "local_codelists/hrg_BZ42.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ44 = codelists_from_csv(
    "local_codelists/hrg_BZ44.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ45 = codelists_from_csv(
    "local_codelists/hrg_BZ45.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ46 = codelists_from_csv(
    "local_codelists/hrg_BZ46.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ51 = codelists_from_csv(
    "local_codelists/hrg_BZ51.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ53 = codelists_from_csv(
    "local_codelists/hrg_BZ53.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ54 = codelists_from_csv(
    "local_codelists/hrg_BZ54.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ56 = codelists_from_csv(
    "local_codelists/hrg_BZ56.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ57 = codelists_from_csv(
    "local_codelists/hrg_BZ57.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ60 = codelists_from_csv(
    "local_codelists/hrg_BZ60.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ61 = codelists_from_csv(
    "local_codelists/hrg_BZ61.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ62 = codelists_from_csv(
    "local_codelists/hrg_BZ62.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ63 = codelists_from_csv(
    "local_codelists/hrg_BZ63.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ64 = codelists_from_csv(
    "local_codelists/hrg_BZ64.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ65 = codelists_from_csv(
    "local_codelists/hrg_BZ65.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ72 = codelists_from_csv(
    "local_codelists/hrg_BZ72.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ73 = codelists_from_csv(
    "local_codelists/hrg_BZ73.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ74 = codelists_from_csv(
    "local_codelists/hrg_BZ74.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ80 = codelists_from_csv(
    "local_codelists/hrg_BZ80.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ81 = codelists_from_csv(
    "local_codelists/hrg_BZ81.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ83 = codelists_from_csv(
    "local_codelists/hrg_BZ83.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ84 = codelists_from_csv(
    "local_codelists/hrg_BZ84.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ86 = codelists_from_csv(
    "local_codelists/hrg_BZ86.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ87 = codelists_from_csv(
    "local_codelists/hrg_BZ87.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ88 = codelists_from_csv(
    "local_codelists/hrg_BZ88.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ89 = codelists_from_csv(
    "local_codelists/hrg_BZ89.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ91 = codelists_from_csv(
    "local_codelists/hrg_BZ91.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ92 = codelists_from_csv(
    "local_codelists/hrg_BZ92.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ93 = codelists_from_csv(
    "local_codelists/hrg_BZ93.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ94 = codelists_from_csv(
    "local_codelists/hrg_BZ94.csv",
    system="opcs4",
    columnn="code",
)

hrg_BZ95 = codelists_from_csv(
    "local_codelists/hrg_BZ95.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA01 = codelists_from_csv(
    "local_codelists/hrg_CA01.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA02 = codelists_from_csv(
    "local_codelists/hrg_CA02.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA03 = codelists_from_csv(
    "local_codelists/hrg_CA03.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA04 = codelists_from_csv(
    "local_codelists/hrg_CA04.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA05 = codelists_from_csv(
    "local_codelists/hrg_CA05.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA10 = codelists_from_csv(
    "local_codelists/hrg_CA10.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA11 = codelists_from_csv(
    "local_codelists/hrg_CA11.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA12 = codelists_from_csv(
    "local_codelists/hrg_CA12.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA13 = codelists_from_csv(
    "local_codelists/hrg_CA13.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA14 = codelists_from_csv(
    "local_codelists/hrg_CA14.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA15 = codelists_from_csv(
    "local_codelists/hrg_CA15.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA16 = codelists_from_csv(
    "local_codelists/hrg_CA16.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA20 = codelists_from_csv(
    "local_codelists/hrg_CA20.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA21 = codelists_from_csv(
    "local_codelists/hrg_CA21.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA22 = codelists_from_csv(
    "local_codelists/hrg_CA22.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA23 = codelists_from_csv(
    "local_codelists/hrg_CA23.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA24 = codelists_from_csv(
    "local_codelists/hrg_CA24.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA25 = codelists_from_csv(
    "local_codelists/hrg_CA25.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA26 = codelists_from_csv(
    "local_codelists/hrg_CA26.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA27 = codelists_from_csv(
    "local_codelists/hrg_CA27.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA28 = codelists_from_csv(
    "local_codelists/hrg_CA28.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA29 = codelists_from_csv(
    "local_codelists/hrg_CA29.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA30 = codelists_from_csv(
    "local_codelists/hrg_CA30.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA31 = codelists_from_csv(
    "local_codelists/hrg_CA31.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA32 = codelists_from_csv(
    "local_codelists/hrg_CA32.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA33 = codelists_from_csv(
    "local_codelists/hrg_CA33.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA34 = codelists_from_csv(
    "local_codelists/hrg_CA34.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA35 = codelists_from_csv(
    "local_codelists/hrg_CA35.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA36 = codelists_from_csv(
    "local_codelists/hrg_CA36.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA37 = codelists_from_csv(
    "local_codelists/hrg_CA37.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA38 = codelists_from_csv(
    "local_codelists/hrg_CA38.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA39 = codelists_from_csv(
    "local_codelists/hrg_CA39.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA40 = codelists_from_csv(
    "local_codelists/hrg_CA40.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA42 = codelists_from_csv(
    "local_codelists/hrg_CA42.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA43 = codelists_from_csv(
    "local_codelists/hrg_CA43.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA50 = codelists_from_csv(
    "local_codelists/hrg_CA50.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA51 = codelists_from_csv(
    "local_codelists/hrg_CA51.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA52 = codelists_from_csv(
    "local_codelists/hrg_CA52.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA53 = codelists_from_csv(
    "local_codelists/hrg_CA53.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA54 = codelists_from_csv(
    "local_codelists/hrg_CA54.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA55 = codelists_from_csv(
    "local_codelists/hrg_CA55.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA60 = codelists_from_csv(
    "local_codelists/hrg_CA60.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA62 = codelists_from_csv(
    "local_codelists/hrg_CA62.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA63 = codelists_from_csv(
    "local_codelists/hrg_CA63.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA64 = codelists_from_csv(
    "local_codelists/hrg_CA64.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA65 = codelists_from_csv(
    "local_codelists/hrg_CA65.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA66 = codelists_from_csv(
    "local_codelists/hrg_CA66.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA67 = codelists_from_csv(
    "local_codelists/hrg_CA67.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA68 = codelists_from_csv(
    "local_codelists/hrg_CA68.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA69 = codelists_from_csv(
    "local_codelists/hrg_CA69.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA70 = codelists_from_csv(
    "local_codelists/hrg_CA70.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA71 = codelists_from_csv(
    "local_codelists/hrg_CA71.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA80 = codelists_from_csv(
    "local_codelists/hrg_CA80.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA81 = codelists_from_csv(
    "local_codelists/hrg_CA81.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA82 = codelists_from_csv(
    "local_codelists/hrg_CA82.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA83 = codelists_from_csv(
    "local_codelists/hrg_CA83.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA84 = codelists_from_csv(
    "local_codelists/hrg_CA84.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA85 = codelists_from_csv(
    "local_codelists/hrg_CA85.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA86 = codelists_from_csv(
    "local_codelists/hrg_CA86.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA91 = codelists_from_csv(
    "local_codelists/hrg_CA91.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA92 = codelists_from_csv(
    "local_codelists/hrg_CA92.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA93 = codelists_from_csv(
    "local_codelists/hrg_CA93.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA94 = codelists_from_csv(
    "local_codelists/hrg_CA94.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA95 = codelists_from_csv(
    "local_codelists/hrg_CA95.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA96 = codelists_from_csv(
    "local_codelists/hrg_CA96.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA97 = codelists_from_csv(
    "local_codelists/hrg_CA97.csv",
    system="opcs4",
    columnn="code",
)

hrg_CA98 = codelists_from_csv(
    "local_codelists/hrg_CA98.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD01 = codelists_from_csv(
    "local_codelists/hrg_CD01.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD02 = codelists_from_csv(
    "local_codelists/hrg_CD02.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD03 = codelists_from_csv(
    "local_codelists/hrg_CD03.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD04 = codelists_from_csv(
    "local_codelists/hrg_CD04.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD05 = codelists_from_csv(
    "local_codelists/hrg_CD05.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD06 = codelists_from_csv(
    "local_codelists/hrg_CD06.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD07 = codelists_from_csv(
    "local_codelists/hrg_CD07.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD08 = codelists_from_csv(
    "local_codelists/hrg_CD08.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD09 = codelists_from_csv(
    "local_codelists/hrg_CD09.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD10 = codelists_from_csv(
    "local_codelists/hrg_CD10.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD11 = codelists_from_csv(
    "local_codelists/hrg_CD11.csv",
    system="opcs4",
    columnn="code",
)

hrg_CD12 = codelists_from_csv(
    "local_codelists/hrg_CD12.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ01 = codelists_from_csv(
    "local_codelists/hrg_DZ01.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ02 = codelists_from_csv(
    "local_codelists/hrg_DZ02.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ30 = codelists_from_csv(
    "local_codelists/hrg_DZ30.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ31 = codelists_from_csv(
    "local_codelists/hrg_DZ31.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ32 = codelists_from_csv(
    "local_codelists/hrg_DZ32.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ33 = codelists_from_csv(
    "local_codelists/hrg_DZ33.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ36 = codelists_from_csv(
    "local_codelists/hrg_DZ36.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ37 = codelists_from_csv(
    "local_codelists/hrg_DZ37.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ38 = codelists_from_csv(
    "local_codelists/hrg_DZ38.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ42 = codelists_from_csv(
    "local_codelists/hrg_DZ42.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ45 = codelists_from_csv(
    "local_codelists/hrg_DZ45.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ46 = codelists_from_csv(
    "local_codelists/hrg_DZ46.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ49 = codelists_from_csv(
    "local_codelists/hrg_DZ49.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ50 = codelists_from_csv(
    "local_codelists/hrg_DZ50.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ55 = codelists_from_csv(
    "local_codelists/hrg_DZ55.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ56 = codelists_from_csv(
    "local_codelists/hrg_DZ56.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ57 = codelists_from_csv(
    "local_codelists/hrg_DZ57.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ58 = codelists_from_csv(
    "local_codelists/hrg_DZ58.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ59 = codelists_from_csv(
    "local_codelists/hrg_DZ59.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ60 = codelists_from_csv(
    "local_codelists/hrg_DZ60.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ63 = codelists_from_csv(
    "local_codelists/hrg_DZ63.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ64 = codelists_from_csv(
    "local_codelists/hrg_DZ64.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ67 = codelists_from_csv(
    "local_codelists/hrg_DZ67.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ68 = codelists_from_csv(
    "local_codelists/hrg_DZ68.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ69 = codelists_from_csv(
    "local_codelists/hrg_DZ69.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ70 = codelists_from_csv(
    "local_codelists/hrg_DZ70.csv",
    system="opcs4",
    columnn="code",
)

hrg_DZ71 = codelists_from_csv(
    "local_codelists/hrg_DZ71.csv",
    system="opcs4",
    columnn="code",
)

hrg_EC11 = codelists_from_csv(
    "local_codelists/hrg_EC11.csv",
    system="opcs4",
    columnn="code",
)

hrg_EC12 = codelists_from_csv(
    "local_codelists/hrg_EC12.csv",
    system="opcs4",
    columnn="code",
)

hrg_EC13 = codelists_from_csv(
    "local_codelists/hrg_EC13.csv",
    system="opcs4",
    columnn="code",
)

hrg_EC14 = codelists_from_csv(
    "local_codelists/hrg_EC14.csv",
    system="opcs4",
    columnn="code",
)

hrg_EC15 = codelists_from_csv(
    "local_codelists/hrg_EC15.csv",
    system="opcs4",
    columnn="code",
)

hrg_EC21 = codelists_from_csv(
    "local_codelists/hrg_EC21.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED01 = codelists_from_csv(
    "local_codelists/hrg_ED01.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED05 = codelists_from_csv(
    "local_codelists/hrg_ED05.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED08 = codelists_from_csv(
    "local_codelists/hrg_ED08.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED09 = codelists_from_csv(
    "local_codelists/hrg_ED09.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED11 = codelists_from_csv(
    "local_codelists/hrg_ED11.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED12 = codelists_from_csv(
    "local_codelists/hrg_ED12.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED13 = codelists_from_csv(
    "local_codelists/hrg_ED13.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED14 = codelists_from_csv(
    "local_codelists/hrg_ED14.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED15 = codelists_from_csv(
    "local_codelists/hrg_ED15.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED18 = codelists_from_csv(
    "local_codelists/hrg_ED18.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED24 = codelists_from_csv(
    "local_codelists/hrg_ED24.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED25 = codelists_from_csv(
    "local_codelists/hrg_ED25.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED26 = codelists_from_csv(
    "local_codelists/hrg_ED26.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED27 = codelists_from_csv(
    "local_codelists/hrg_ED27.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED28 = codelists_from_csv(
    "local_codelists/hrg_ED28.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED30 = codelists_from_csv(
    "local_codelists/hrg_ED30.csv",
    system="opcs4",
    columnn="code",
)

hrg_ED31 = codelists_from_csv(
    "local_codelists/hrg_ED31.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY01 = codelists_from_csv(
    "local_codelists/hrg_EY01.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY02 = codelists_from_csv(
    "local_codelists/hrg_EY02.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY04 = codelists_from_csv(
    "local_codelists/hrg_EY04.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY06 = codelists_from_csv(
    "local_codelists/hrg_EY06.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY08 = codelists_from_csv(
    "local_codelists/hrg_EY08.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY11 = codelists_from_csv(
    "local_codelists/hrg_EY11.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY12 = codelists_from_csv(
    "local_codelists/hrg_EY12.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY13 = codelists_from_csv(
    "local_codelists/hrg_EY13.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY17 = codelists_from_csv(
    "local_codelists/hrg_EY17.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY22 = codelists_from_csv(
    "local_codelists/hrg_EY22.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY23 = codelists_from_csv(
    "local_codelists/hrg_EY23.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY30 = codelists_from_csv(
    "local_codelists/hrg_EY30.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY31 = codelists_from_csv(
    "local_codelists/hrg_EY31.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY32 = codelists_from_csv(
    "local_codelists/hrg_EY32.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY40 = codelists_from_csv(
    "local_codelists/hrg_EY40.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY41 = codelists_from_csv(
    "local_codelists/hrg_EY41.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY42 = codelists_from_csv(
    "local_codelists/hrg_EY42.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY43 = codelists_from_csv(
    "local_codelists/hrg_EY43.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY50 = codelists_from_csv(
    "local_codelists/hrg_EY50.csv",
    system="opcs4",
    columnn="code",
)

hrg_EY51 = codelists_from_csv(
    "local_codelists/hrg_EY51.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE01 = codelists_from_csv(
    "local_codelists/hrg_FE01.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE02 = codelists_from_csv(
    "local_codelists/hrg_FE02.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE03 = codelists_from_csv(
    "local_codelists/hrg_FE03.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE10 = codelists_from_csv(
    "local_codelists/hrg_FE10.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE11 = codelists_from_csv(
    "local_codelists/hrg_FE11.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE12 = codelists_from_csv(
    "local_codelists/hrg_FE12.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE13 = codelists_from_csv(
    "local_codelists/hrg_FE13.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE20 = codelists_from_csv(
    "local_codelists/hrg_FE20.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE21 = codelists_from_csv(
    "local_codelists/hrg_FE21.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE22 = codelists_from_csv(
    "local_codelists/hrg_FE22.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE30 = codelists_from_csv(
    "local_codelists/hrg_FE30.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE31 = codelists_from_csv(
    "local_codelists/hrg_FE31.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE32 = codelists_from_csv(
    "local_codelists/hrg_FE32.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE33 = codelists_from_csv(
    "local_codelists/hrg_FE33.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE34 = codelists_from_csv(
    "local_codelists/hrg_FE34.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE35 = codelists_from_csv(
    "local_codelists/hrg_FE35.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE36 = codelists_from_csv(
    "local_codelists/hrg_FE36.csv",
    system="opcs4",
    columnn="code",
)

hrg_FE50 = codelists_from_csv(
    "local_codelists/hrg_FE50.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF01 = codelists_from_csv(
    "local_codelists/hrg_FF01.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF02 = codelists_from_csv(
    "local_codelists/hrg_FF02.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF04 = codelists_from_csv(
    "local_codelists/hrg_FF04.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF05 = codelists_from_csv(
    "local_codelists/hrg_FF05.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF12 = codelists_from_csv(
    "local_codelists/hrg_FF12.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF13 = codelists_from_csv(
    "local_codelists/hrg_FF13.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF14 = codelists_from_csv(
    "local_codelists/hrg_FF14.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF20 = codelists_from_csv(
    "local_codelists/hrg_FF20.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF21 = codelists_from_csv(
    "local_codelists/hrg_FF21.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF22 = codelists_from_csv(
    "local_codelists/hrg_FF22.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF30 = codelists_from_csv(
    "local_codelists/hrg_FF30.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF31 = codelists_from_csv(
    "local_codelists/hrg_FF31.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF32 = codelists_from_csv(
    "local_codelists/hrg_FF32.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF33 = codelists_from_csv(
    "local_codelists/hrg_FF33.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF34 = codelists_from_csv(
    "local_codelists/hrg_FF34.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF36 = codelists_from_csv(
    "local_codelists/hrg_FF36.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF37 = codelists_from_csv(
    "local_codelists/hrg_FF37.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF40 = codelists_from_csv(
    "local_codelists/hrg_FF40.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF41 = codelists_from_csv(
    "local_codelists/hrg_FF41.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF42 = codelists_from_csv(
    "local_codelists/hrg_FF42.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF43 = codelists_from_csv(
    "local_codelists/hrg_FF43.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF50 = codelists_from_csv(
    "local_codelists/hrg_FF50.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF51 = codelists_from_csv(
    "local_codelists/hrg_FF51.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF52 = codelists_from_csv(
    "local_codelists/hrg_FF52.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF53 = codelists_from_csv(
    "local_codelists/hrg_FF53.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF60 = codelists_from_csv(
    "local_codelists/hrg_FF60.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF61 = codelists_from_csv(
    "local_codelists/hrg_FF61.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF62 = codelists_from_csv(
    "local_codelists/hrg_FF62.csv",
    system="opcs4",
    columnn="code",
)

hrg_FF63 = codelists_from_csv(
    "local_codelists/hrg_FF63.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA03 = codelists_from_csv(
    "local_codelists/hrg_GA03.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA04 = codelists_from_csv(
    "local_codelists/hrg_GA04.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA05 = codelists_from_csv(
    "local_codelists/hrg_GA05.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA06 = codelists_from_csv(
    "local_codelists/hrg_GA06.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA07 = codelists_from_csv(
    "local_codelists/hrg_GA07.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA10 = codelists_from_csv(
    "local_codelists/hrg_GA10.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA11 = codelists_from_csv(
    "local_codelists/hrg_GA11.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA13 = codelists_from_csv(
    "local_codelists/hrg_GA13.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA15 = codelists_from_csv(
    "local_codelists/hrg_GA15.csv",
    system="opcs4",
    columnn="code",
)

hrg_GA16 = codelists_from_csv(
    "local_codelists/hrg_GA16.csv",
    system="opcs4",
    columnn="code",
)

hrg_GB05 = codelists_from_csv(
    "local_codelists/hrg_GB05.csv",
    system="opcs4",
    columnn="code",
)

hrg_GB06 = codelists_from_csv(
    "local_codelists/hrg_GB06.csv",
    system="opcs4",
    columnn="code",
)

hrg_GB09 = codelists_from_csv(
    "local_codelists/hrg_GB09.csv",
    system="opcs4",
    columnn="code",
)

hrg_GB10 = codelists_from_csv(
    "local_codelists/hrg_GB10.csv",
    system="opcs4",
    columnn="code",
)

hrg_GB11 = codelists_from_csv(
    "local_codelists/hrg_GB11.csv",
    system="opcs4",
    columnn="code",
)

hrg_GB12 = codelists_from_csv(
    "local_codelists/hrg_GB12.csv",
    system="opcs4",
    columnn="code",
)

hrg_GB13 = codelists_from_csv(
    "local_codelists/hrg_GB13.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC50 = codelists_from_csv(
    "local_codelists/hrg_HC50.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC53 = codelists_from_csv(
    "local_codelists/hrg_HC53.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC54 = codelists_from_csv(
    "local_codelists/hrg_HC54.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC60 = codelists_from_csv(
    "local_codelists/hrg_HC60.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC61 = codelists_from_csv(
    "local_codelists/hrg_HC61.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC62 = codelists_from_csv(
    "local_codelists/hrg_HC62.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC63 = codelists_from_csv(
    "local_codelists/hrg_HC63.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC64 = codelists_from_csv(
    "local_codelists/hrg_HC64.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC65 = codelists_from_csv(
    "local_codelists/hrg_HC65.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC70 = codelists_from_csv(
    "local_codelists/hrg_HC70.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC71 = codelists_from_csv(
    "local_codelists/hrg_HC71.csv",
    system="opcs4",
    columnn="code",
)

hrg_HC72 = codelists_from_csv(
    "local_codelists/hrg_HC72.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN12 = codelists_from_csv(
    "local_codelists/hrg_HN12.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN13 = codelists_from_csv(
    "local_codelists/hrg_HN13.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN14 = codelists_from_csv(
    "local_codelists/hrg_HN14.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN15 = codelists_from_csv(
    "local_codelists/hrg_HN15.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN22 = codelists_from_csv(
    "local_codelists/hrg_HN22.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN23 = codelists_from_csv(
    "local_codelists/hrg_HN23.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN24 = codelists_from_csv(
    "local_codelists/hrg_HN24.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN25 = codelists_from_csv(
    "local_codelists/hrg_HN25.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN32 = codelists_from_csv(
    "local_codelists/hrg_HN32.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN33 = codelists_from_csv(
    "local_codelists/hrg_HN33.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN34 = codelists_from_csv(
    "local_codelists/hrg_HN34.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN35 = codelists_from_csv(
    "local_codelists/hrg_HN35.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN42 = codelists_from_csv(
    "local_codelists/hrg_HN42.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN43 = codelists_from_csv(
    "local_codelists/hrg_HN43.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN44 = codelists_from_csv(
    "local_codelists/hrg_HN44.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN45 = codelists_from_csv(
    "local_codelists/hrg_HN45.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN46 = codelists_from_csv(
    "local_codelists/hrg_HN46.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN52 = codelists_from_csv(
    "local_codelists/hrg_HN52.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN53 = codelists_from_csv(
    "local_codelists/hrg_HN53.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN54 = codelists_from_csv(
    "local_codelists/hrg_HN54.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN55 = codelists_from_csv(
    "local_codelists/hrg_HN55.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN62 = codelists_from_csv(
    "local_codelists/hrg_HN62.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN63 = codelists_from_csv(
    "local_codelists/hrg_HN63.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN64 = codelists_from_csv(
    "local_codelists/hrg_HN64.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN65 = codelists_from_csv(
    "local_codelists/hrg_HN65.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN81 = codelists_from_csv(
    "local_codelists/hrg_HN81.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN86 = codelists_from_csv(
    "local_codelists/hrg_HN86.csv",
    system="opcs4",
    columnn="code",
)

hrg_HN93 = codelists_from_csv(
    "local_codelists/hrg_HN93.csv",
    system="opcs4",
    columnn="code",
)

hrg_JA20 = codelists_from_csv(
    "local_codelists/hrg_JA20.csv",
    system="opcs4",
    columnn="code",
)

hrg_JA30 = codelists_from_csv(
    "local_codelists/hrg_JA30.csv",
    system="opcs4",
    columnn="code",
)

hrg_JA34 = codelists_from_csv(
    "local_codelists/hrg_JA34.csv",
    system="opcs4",
    columnn="code",
)

hrg_JA38 = codelists_from_csv(
    "local_codelists/hrg_JA38.csv",
    system="opcs4",
    columnn="code",
)

hrg_JA43 = codelists_from_csv(
    "local_codelists/hrg_JA43.csv",
    system="opcs4",
    columnn="code",
)

hrg_JA45 = codelists_from_csv(
    "local_codelists/hrg_JA45.csv",
    system="opcs4",
    columnn="code",
)

hrg_JB70 = codelists_from_csv(
    "local_codelists/hrg_JB70.csv",
    system="opcs4",
    columnn="code",
)

hrg_JB71 = codelists_from_csv(
    "local_codelists/hrg_JB71.csv",
    system="opcs4",
    columnn="code",
)

hrg_JC40 = codelists_from_csv(
    "local_codelists/hrg_JC40.csv",
    system="opcs4",
    columnn="code",
)

hrg_JC41 = codelists_from_csv(
    "local_codelists/hrg_JC41.csv",
    system="opcs4",
    columnn="code",
)

hrg_JC42 = codelists_from_csv(
    "local_codelists/hrg_JC42.csv",
    system="opcs4",
    columnn="code",
)

hrg_JC43 = codelists_from_csv(
    "local_codelists/hrg_JC43.csv",
    system="opcs4",
    columnn="code",
)

hrg_JC44 = codelists_from_csv(
    "local_codelists/hrg_JC44.csv",
    system="opcs4",
    columnn="code",
)

hrg_JC45 = codelists_from_csv(
    "local_codelists/hrg_JC45.csv",
    system="opcs4",
    columnn="code",
)

hrg_JC46 = codelists_from_csv(
    "local_codelists/hrg_JC46.csv",
    system="opcs4",
    columnn="code",
)

hrg_JC47 = codelists_from_csv(
    "local_codelists/hrg_JC47.csv",
    system="opcs4",
    columnn="code",
)

hrg_KA03 = codelists_from_csv(
    "local_codelists/hrg_KA03.csv",
    system="opcs4",
    columnn="code",
)

hrg_KA04 = codelists_from_csv(
    "local_codelists/hrg_KA04.csv",
    system="opcs4",
    columnn="code",
)

hrg_KA09 = codelists_from_csv(
    "local_codelists/hrg_KA09.csv",
    system="opcs4",
    columnn="code",
)

hrg_KB04 = codelists_from_csv(
    "local_codelists/hrg_KB04.csv",
    system="opcs4",
    columnn="code",
)

hrg_LA01 = codelists_from_csv(
    "local_codelists/hrg_LA01.csv",
    system="opcs4",
    columnn="code",
)

hrg_LA02 = codelists_from_csv(
    "local_codelists/hrg_LA02.csv",
    system="opcs4",
    columnn="code",
)

hrg_LA03 = codelists_from_csv(
    "local_codelists/hrg_LA03.csv",
    system="opcs4",
    columnn="code",
)

hrg_LA05 = codelists_from_csv(
    "local_codelists/hrg_LA05.csv",
    system="opcs4",
    columnn="code",
)

hrg_LA10 = codelists_from_csv(
    "local_codelists/hrg_LA10.csv",
    system="opcs4",
    columnn="code",
)

hrg_LA11 = codelists_from_csv(
    "local_codelists/hrg_LA11.csv",
    system="opcs4",
    columnn="code",
)

hrg_LA12 = codelists_from_csv(
    "local_codelists/hrg_LA12.csv",
    system="opcs4",
    columnn="code",
)

hrg_LA13 = codelists_from_csv(
    "local_codelists/hrg_LA13.csv",
    system="opcs4",
    columnn="code",
)

hrg_LA14 = codelists_from_csv(
    "local_codelists/hrg_LA14.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB09 = codelists_from_csv(
    "local_codelists/hrg_LB09.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB10 = codelists_from_csv(
    "local_codelists/hrg_LB10.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB12 = codelists_from_csv(
    "local_codelists/hrg_LB12.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB13 = codelists_from_csv(
    "local_codelists/hrg_LB13.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB14 = codelists_from_csv(
    "local_codelists/hrg_LB14.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB15 = codelists_from_csv(
    "local_codelists/hrg_LB15.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB17 = codelists_from_csv(
    "local_codelists/hrg_LB17.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB18 = codelists_from_csv(
    "local_codelists/hrg_LB18.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB21 = codelists_from_csv(
    "local_codelists/hrg_LB21.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB25 = codelists_from_csv(
    "local_codelists/hrg_LB25.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB26 = codelists_from_csv(
    "local_codelists/hrg_LB26.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB29 = codelists_from_csv(
    "local_codelists/hrg_LB29.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB33 = codelists_from_csv(
    "local_codelists/hrg_LB33.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB36 = codelists_from_csv(
    "local_codelists/hrg_LB36.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB39 = codelists_from_csv(
    "local_codelists/hrg_LB39.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB42 = codelists_from_csv(
    "local_codelists/hrg_LB42.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB43 = codelists_from_csv(
    "local_codelists/hrg_LB43.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB46 = codelists_from_csv(
    "local_codelists/hrg_LB46.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB47 = codelists_from_csv(
    "local_codelists/hrg_LB47.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB48 = codelists_from_csv(
    "local_codelists/hrg_LB48.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB50 = codelists_from_csv(
    "local_codelists/hrg_LB50.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB51 = codelists_from_csv(
    "local_codelists/hrg_LB51.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB52 = codelists_from_csv(
    "local_codelists/hrg_LB52.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB53 = codelists_from_csv(
    "local_codelists/hrg_LB53.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB54 = codelists_from_csv(
    "local_codelists/hrg_LB54.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB55 = codelists_from_csv(
    "local_codelists/hrg_LB55.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB56 = codelists_from_csv(
    "local_codelists/hrg_LB56.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB59 = codelists_from_csv(
    "local_codelists/hrg_LB59.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB60 = codelists_from_csv(
    "local_codelists/hrg_LB60.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB61 = codelists_from_csv(
    "local_codelists/hrg_LB61.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB64 = codelists_from_csv(
    "local_codelists/hrg_LB64.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB65 = codelists_from_csv(
    "local_codelists/hrg_LB65.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB67 = codelists_from_csv(
    "local_codelists/hrg_LB67.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB68 = codelists_from_csv(
    "local_codelists/hrg_LB68.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB70 = codelists_from_csv(
    "local_codelists/hrg_LB70.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB71 = codelists_from_csv(
    "local_codelists/hrg_LB71.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB72 = codelists_from_csv(
    "local_codelists/hrg_LB72.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB74 = codelists_from_csv(
    "local_codelists/hrg_LB74.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB75 = codelists_from_csv(
    "local_codelists/hrg_LB75.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB76 = codelists_from_csv(
    "local_codelists/hrg_LB76.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB77 = codelists_from_csv(
    "local_codelists/hrg_LB77.csv",
    system="opcs4",
    columnn="code",
)

hrg_LB78 = codelists_from_csv(
    "local_codelists/hrg_LB78.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA01 = codelists_from_csv(
    "local_codelists/hrg_MA01.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA02 = codelists_from_csv(
    "local_codelists/hrg_MA02.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA03 = codelists_from_csv(
    "local_codelists/hrg_MA03.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA04 = codelists_from_csv(
    "local_codelists/hrg_MA04.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA07 = codelists_from_csv(
    "local_codelists/hrg_MA07.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA09 = codelists_from_csv(
    "local_codelists/hrg_MA09.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA10 = codelists_from_csv(
    "local_codelists/hrg_MA10.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA11 = codelists_from_csv(
    "local_codelists/hrg_MA11.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA12 = codelists_from_csv(
    "local_codelists/hrg_MA12.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA22 = codelists_from_csv(
    "local_codelists/hrg_MA22.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA23 = codelists_from_csv(
    "local_codelists/hrg_MA23.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA24 = codelists_from_csv(
    "local_codelists/hrg_MA24.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA25 = codelists_from_csv(
    "local_codelists/hrg_MA25.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA29 = codelists_from_csv(
    "local_codelists/hrg_MA29.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA30 = codelists_from_csv(
    "local_codelists/hrg_MA30.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA31 = codelists_from_csv(
    "local_codelists/hrg_MA31.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA32 = codelists_from_csv(
    "local_codelists/hrg_MA32.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA35 = codelists_from_csv(
    "local_codelists/hrg_MA35.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA36 = codelists_from_csv(
    "local_codelists/hrg_MA36.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA38 = codelists_from_csv(
    "local_codelists/hrg_MA38.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA44 = codelists_from_csv(
    "local_codelists/hrg_MA44.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA48 = codelists_from_csv(
    "local_codelists/hrg_MA48.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA52 = codelists_from_csv(
    "local_codelists/hrg_MA52.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA53 = codelists_from_csv(
    "local_codelists/hrg_MA53.csv",
    system="opcs4",
    columnn="code",
)

hrg_MA56 = codelists_from_csv(
    "local_codelists/hrg_MA56.csv",
    system="opcs4",
    columnn="code",
)

hrg_MC07 = codelists_from_csv(
    "local_codelists/hrg_MC07.csv",
    system="opcs4",
    columnn="code",
)

hrg_MC08 = codelists_from_csv(
    "local_codelists/hrg_MC08.csv",
    system="opcs4",
    columnn="code",
)

hrg_MC09 = codelists_from_csv(
    "local_codelists/hrg_MC09.csv",
    system="opcs4",
    columnn="code",
)

hrg_MC10 = codelists_from_csv(
    "local_codelists/hrg_MC10.csv",
    system="opcs4",
    columnn="code",
)

hrg_MC11 = codelists_from_csv(
    "local_codelists/hrg_MC11.csv",
    system="opcs4",
    columnn="code",
)

hrg_MC12 = codelists_from_csv(
    "local_codelists/hrg_MC12.csv",
    system="opcs4",
    columnn="code",
)

hrg_MC20 = codelists_from_csv(
    "local_codelists/hrg_MC20.csv",
    system="opcs4",
    columnn="code",
)

hrg_MC21 = codelists_from_csv(
    "local_codelists/hrg_MC21.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ21 = codelists_from_csv(
    "local_codelists/hrg_NZ21.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ22 = codelists_from_csv(
    "local_codelists/hrg_NZ22.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ24 = codelists_from_csv(
    "local_codelists/hrg_NZ24.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ27 = codelists_from_csv(
    "local_codelists/hrg_NZ27.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ30 = codelists_from_csv(
    "local_codelists/hrg_NZ30.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ40 = codelists_from_csv(
    "local_codelists/hrg_NZ40.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ50 = codelists_from_csv(
    "local_codelists/hrg_NZ50.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ51 = codelists_from_csv(
    "local_codelists/hrg_NZ51.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ71 = codelists_from_csv(
    "local_codelists/hrg_NZ71.csv",
    system="opcs4",
    columnn="code",
)

hrg_NZ72 = codelists_from_csv(
    "local_codelists/hrg_NZ72.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD01 = codelists_from_csv(
    "local_codelists/hrg_RD01.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD08 = codelists_from_csv(
    "local_codelists/hrg_RD08.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD20 = codelists_from_csv(
    "local_codelists/hrg_RD20.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD30 = codelists_from_csv(
    "local_codelists/hrg_RD30.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD40 = codelists_from_csv(
    "local_codelists/hrg_RD40.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD47 = codelists_from_csv(
    "local_codelists/hrg_RD47.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD48 = codelists_from_csv(
    "local_codelists/hrg_RD48.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD50 = codelists_from_csv(
    "local_codelists/hrg_RD50.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD51 = codelists_from_csv(
    "local_codelists/hrg_RD51.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD60 = codelists_from_csv(
    "local_codelists/hrg_RD60.csv",
    system="opcs4",
    columnn="code",
)

hrg_RD61 = codelists_from_csv(
    "local_codelists/hrg_RD61.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN01 = codelists_from_csv(
    "local_codelists/hrg_RN01.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN04 = codelists_from_csv(
    "local_codelists/hrg_RN04.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN07 = codelists_from_csv(
    "local_codelists/hrg_RN07.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN08 = codelists_from_csv(
    "local_codelists/hrg_RN08.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN09 = codelists_from_csv(
    "local_codelists/hrg_RN09.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN13 = codelists_from_csv(
    "local_codelists/hrg_RN13.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN14 = codelists_from_csv(
    "local_codelists/hrg_RN14.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN15 = codelists_from_csv(
    "local_codelists/hrg_RN15.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN16 = codelists_from_csv(
    "local_codelists/hrg_RN16.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN17 = codelists_from_csv(
    "local_codelists/hrg_RN17.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN18 = codelists_from_csv(
    "local_codelists/hrg_RN18.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN19 = codelists_from_csv(
    "local_codelists/hrg_RN19.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN20 = codelists_from_csv(
    "local_codelists/hrg_RN20.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN21 = codelists_from_csv(
    "local_codelists/hrg_RN21.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN22 = codelists_from_csv(
    "local_codelists/hrg_RN22.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN23 = codelists_from_csv(
    "local_codelists/hrg_RN23.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN24 = codelists_from_csv(
    "local_codelists/hrg_RN24.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN25 = codelists_from_csv(
    "local_codelists/hrg_RN25.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN26 = codelists_from_csv(
    "local_codelists/hrg_RN26.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN27 = codelists_from_csv(
    "local_codelists/hrg_RN27.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN28 = codelists_from_csv(
    "local_codelists/hrg_RN28.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN29 = codelists_from_csv(
    "local_codelists/hrg_RN29.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN30 = codelists_from_csv(
    "local_codelists/hrg_RN30.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN31 = codelists_from_csv(
    "local_codelists/hrg_RN31.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN32 = codelists_from_csv(
    "local_codelists/hrg_RN32.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN33 = codelists_from_csv(
    "local_codelists/hrg_RN33.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN34 = codelists_from_csv(
    "local_codelists/hrg_RN34.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN50 = codelists_from_csv(
    "local_codelists/hrg_RN50.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN51 = codelists_from_csv(
    "local_codelists/hrg_RN51.csv",
    system="opcs4",
    columnn="code",
)

hrg_RN52 = codelists_from_csv(
    "local_codelists/hrg_RN52.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA14 = codelists_from_csv(
    "local_codelists/hrg_SA14.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA15 = codelists_from_csv(
    "local_codelists/hrg_SA15.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA16 = codelists_from_csv(
    "local_codelists/hrg_SA16.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA18 = codelists_from_csv(
    "local_codelists/hrg_SA18.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA19 = codelists_from_csv(
    "local_codelists/hrg_SA19.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA20 = codelists_from_csv(
    "local_codelists/hrg_SA20.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA21 = codelists_from_csv(
    "local_codelists/hrg_SA21.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA22 = codelists_from_csv(
    "local_codelists/hrg_SA22.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA23 = codelists_from_csv(
    "local_codelists/hrg_SA23.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA26 = codelists_from_csv(
    "local_codelists/hrg_SA26.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA27 = codelists_from_csv(
    "local_codelists/hrg_SA27.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA33 = codelists_from_csv(
    "local_codelists/hrg_SA33.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA40 = codelists_from_csv(
    "local_codelists/hrg_SA40.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA42 = codelists_from_csv(
    "local_codelists/hrg_SA42.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA43 = codelists_from_csv(
    "local_codelists/hrg_SA43.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA44 = codelists_from_csv(
    "local_codelists/hrg_SA44.csv",
    system="opcs4",
    columnn="code",
)

hrg_SA45 = codelists_from_csv(
    "local_codelists/hrg_SA45.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB01 = codelists_from_csv(
    "local_codelists/hrg_SB01.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB02 = codelists_from_csv(
    "local_codelists/hrg_SB02.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB03 = codelists_from_csv(
    "local_codelists/hrg_SB03.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB04 = codelists_from_csv(
    "local_codelists/hrg_SB04.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB05 = codelists_from_csv(
    "local_codelists/hrg_SB05.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB06 = codelists_from_csv(
    "local_codelists/hrg_SB06.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB07 = codelists_from_csv(
    "local_codelists/hrg_SB07.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB08 = codelists_from_csv(
    "local_codelists/hrg_SB08.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB09 = codelists_from_csv(
    "local_codelists/hrg_SB09.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB10 = codelists_from_csv(
    "local_codelists/hrg_SB10.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB11 = codelists_from_csv(
    "local_codelists/hrg_SB11.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB12 = codelists_from_csv(
    "local_codelists/hrg_SB12.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB13 = codelists_from_csv(
    "local_codelists/hrg_SB13.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB14 = codelists_from_csv(
    "local_codelists/hrg_SB14.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB15 = codelists_from_csv(
    "local_codelists/hrg_SB15.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB16 = codelists_from_csv(
    "local_codelists/hrg_SB16.csv",
    system="opcs4",
    columnn="code",
)

hrg_SB17 = codelists_from_csv(
    "local_codelists/hrg_SB17.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC25 = codelists_from_csv(
    "local_codelists/hrg_SC25.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC26 = codelists_from_csv(
    "local_codelists/hrg_SC26.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC28 = codelists_from_csv(
    "local_codelists/hrg_SC28.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC29 = codelists_from_csv(
    "local_codelists/hrg_SC29.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC30 = codelists_from_csv(
    "local_codelists/hrg_SC30.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC40 = codelists_from_csv(
    "local_codelists/hrg_SC40.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC42 = codelists_from_csv(
    "local_codelists/hrg_SC42.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC44 = codelists_from_csv(
    "local_codelists/hrg_SC44.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC45 = codelists_from_csv(
    "local_codelists/hrg_SC45.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC47 = codelists_from_csv(
    "local_codelists/hrg_SC47.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC49 = codelists_from_csv(
    "local_codelists/hrg_SC49.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC51 = codelists_from_csv(
    "local_codelists/hrg_SC51.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC53 = codelists_from_csv(
    "local_codelists/hrg_SC53.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC54 = codelists_from_csv(
    "local_codelists/hrg_SC54.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC55 = codelists_from_csv(
    "local_codelists/hrg_SC55.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC56 = codelists_from_csv(
    "local_codelists/hrg_SC56.csv",
    system="opcs4",
    columnn="code",
)

hrg_SC57 = codelists_from_csv(
    "local_codelists/hrg_SC57.csv",
    system="opcs4",
    columnn="code",
)

hrg_UZ05 = codelists_from_csv(
    "local_codelists/hrg_UZ05.csv",
    system="opcs4",
    columnn="code",
)

hrg_UZ06 = codelists_from_csv(
    "local_codelists/hrg_UZ06.csv",
    system="opcs4",
    columnn="code",
)

hrg_VC01 = codelists_from_csv(
    "local_codelists/hrg_VC01.csv",
    system="opcs4",
    columnn="code",
)

hrg_VC02 = codelists_from_csv(
    "local_codelists/hrg_VC02.csv",
    system="opcs4",
    columnn="code",
)

hrg_VC03 = codelists_from_csv(
    "local_codelists/hrg_VC03.csv",
    system="opcs4",
    columnn="code",
)

hrg_WF01 = codelists_from_csv(
    "local_codelists/hrg_WF01.csv",
    system="opcs4",
    columnn="code",
)

hrg_WF02 = codelists_from_csv(
    "local_codelists/hrg_WF02.csv",
    system="opcs4",
    columnn="code",
)

hrg_WH54 = codelists_from_csv(
    "local_codelists/hrg_WH54.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD01 = codelists_from_csv(
    "local_codelists/hrg_XD01.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD02 = codelists_from_csv(
    "local_codelists/hrg_XD02.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD03 = codelists_from_csv(
    "local_codelists/hrg_XD03.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD04 = codelists_from_csv(
    "local_codelists/hrg_XD04.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD05 = codelists_from_csv(
    "local_codelists/hrg_XD05.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD06 = codelists_from_csv(
    "local_codelists/hrg_XD06.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD07 = codelists_from_csv(
    "local_codelists/hrg_XD07.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD08 = codelists_from_csv(
    "local_codelists/hrg_XD08.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD09 = codelists_from_csv(
    "local_codelists/hrg_XD09.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD10 = codelists_from_csv(
    "local_codelists/hrg_XD10.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD11 = codelists_from_csv(
    "local_codelists/hrg_XD11.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD12 = codelists_from_csv(
    "local_codelists/hrg_XD12.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD13 = codelists_from_csv(
    "local_codelists/hrg_XD13.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD14 = codelists_from_csv(
    "local_codelists/hrg_XD14.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD15 = codelists_from_csv(
    "local_codelists/hrg_XD15.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD16 = codelists_from_csv(
    "local_codelists/hrg_XD16.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD17 = codelists_from_csv(
    "local_codelists/hrg_XD17.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD18 = codelists_from_csv(
    "local_codelists/hrg_XD18.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD19 = codelists_from_csv(
    "local_codelists/hrg_XD19.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD20 = codelists_from_csv(
    "local_codelists/hrg_XD20.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD21 = codelists_from_csv(
    "local_codelists/hrg_XD21.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD22 = codelists_from_csv(
    "local_codelists/hrg_XD22.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD23 = codelists_from_csv(
    "local_codelists/hrg_XD23.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD24 = codelists_from_csv(
    "local_codelists/hrg_XD24.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD25 = codelists_from_csv(
    "local_codelists/hrg_XD25.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD26 = codelists_from_csv(
    "local_codelists/hrg_XD26.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD27 = codelists_from_csv(
    "local_codelists/hrg_XD27.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD28 = codelists_from_csv(
    "local_codelists/hrg_XD28.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD29 = codelists_from_csv(
    "local_codelists/hrg_XD29.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD30 = codelists_from_csv(
    "local_codelists/hrg_XD30.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD31 = codelists_from_csv(
    "local_codelists/hrg_XD31.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD32 = codelists_from_csv(
    "local_codelists/hrg_XD32.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD33 = codelists_from_csv(
    "local_codelists/hrg_XD33.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD34 = codelists_from_csv(
    "local_codelists/hrg_XD34.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD37 = codelists_from_csv(
    "local_codelists/hrg_XD37.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD38 = codelists_from_csv(
    "local_codelists/hrg_XD38.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD39 = codelists_from_csv(
    "local_codelists/hrg_XD39.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD40 = codelists_from_csv(
    "local_codelists/hrg_XD40.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD41 = codelists_from_csv(
    "local_codelists/hrg_XD41.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD42 = codelists_from_csv(
    "local_codelists/hrg_XD42.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD43 = codelists_from_csv(
    "local_codelists/hrg_XD43.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD44 = codelists_from_csv(
    "local_codelists/hrg_XD44.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD45 = codelists_from_csv(
    "local_codelists/hrg_XD45.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD46 = codelists_from_csv(
    "local_codelists/hrg_XD46.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD47 = codelists_from_csv(
    "local_codelists/hrg_XD47.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD48 = codelists_from_csv(
    "local_codelists/hrg_XD48.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD49 = codelists_from_csv(
    "local_codelists/hrg_XD49.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD50 = codelists_from_csv(
    "local_codelists/hrg_XD50.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD51 = codelists_from_csv(
    "local_codelists/hrg_XD51.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD52 = codelists_from_csv(
    "local_codelists/hrg_XD52.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD53 = codelists_from_csv(
    "local_codelists/hrg_XD53.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD54 = codelists_from_csv(
    "local_codelists/hrg_XD54.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD55 = codelists_from_csv(
    "local_codelists/hrg_XD55.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD56 = codelists_from_csv(
    "local_codelists/hrg_XD56.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD57 = codelists_from_csv(
    "local_codelists/hrg_XD57.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD58 = codelists_from_csv(
    "local_codelists/hrg_XD58.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD90 = codelists_from_csv(
    "local_codelists/hrg_XD90.csv",
    system="opcs4",
    columnn="code",
)

hrg_XD91 = codelists_from_csv(
    "local_codelists/hrg_XD91.csv",
    system="opcs4",
    columnn="code",
)

hrg_YA03 = codelists_from_csv(
    "local_codelists/hrg_YA03.csv",
    system="opcs4",
    columnn="code",
)

hrg_YA04 = codelists_from_csv(
    "local_codelists/hrg_YA04.csv",
    system="opcs4",
    columnn="code",
)

hrg_YA10 = codelists_from_csv(
    "local_codelists/hrg_YA10.csv",
    system="opcs4",
    columnn="code",
)

hrg_YA11 = codelists_from_csv(
    "local_codelists/hrg_YA11.csv",
    system="opcs4",
    columnn="code",
)

hrg_YA12 = codelists_from_csv(
    "local_codelists/hrg_YA12.csv",
    system="opcs4",
    columnn="code",
)

hrg_YA13 = codelists_from_csv(
    "local_codelists/hrg_YA13.csv",
    system="opcs4",
    columnn="code",
)

hrg_YC01 = codelists_from_csv(
    "local_codelists/hrg_YC01.csv",
    system="opcs4",
    columnn="code",
)

hrg_YC10 = codelists_from_csv(
    "local_codelists/hrg_YC10.csv",
    system="opcs4",
    columnn="code",
)

hrg_YD01 = codelists_from_csv(
    "local_codelists/hrg_YD01.csv",
    system="opcs4",
    columnn="code",
)

hrg_YD02 = codelists_from_csv(
    "local_codelists/hrg_YD02.csv",
    system="opcs4",
    columnn="code",
)

hrg_YD03 = codelists_from_csv(
    "local_codelists/hrg_YD03.csv",
    system="opcs4",
    columnn="code",
)

hrg_YD04 = codelists_from_csv(
    "local_codelists/hrg_YD04.csv",
    system="opcs4",
    columnn="code",
)

hrg_YD05 = codelists_from_csv(
    "local_codelists/hrg_YD05.csv",
    system="opcs4",
    columnn="code",
)

hrg_YF01 = codelists_from_csv(
    "local_codelists/hrg_YF01.csv",
    system="opcs4",
    columnn="code",
)

hrg_YF04 = codelists_from_csv(
    "local_codelists/hrg_YF04.csv",
    system="opcs4",
    columnn="code",
)

hrg_YG01 = codelists_from_csv(
    "local_codelists/hrg_YG01.csv",
    system="opcs4",
    columnn="code",
)

hrg_YG02 = codelists_from_csv(
    "local_codelists/hrg_YG02.csv",
    system="opcs4",
    columnn="code",
)

hrg_YG05 = codelists_from_csv(
    "local_codelists/hrg_YG05.csv",
    system="opcs4",
    columnn="code",
)

hrg_YG06 = codelists_from_csv(
    "local_codelists/hrg_YG06.csv",
    system="opcs4",
    columnn="code",
)

hrg_YG07 = codelists_from_csv(
    "local_codelists/hrg_YG07.csv",
    system="opcs4",
    columnn="code",
)

hrg_YG10 = codelists_from_csv(
    "local_codelists/hrg_YG10.csv",
    system="opcs4",
    columnn="code",
)

hrg_YG11 = codelists_from_csv(
    "local_codelists/hrg_YG11.csv",
    system="opcs4",
    columnn="code",
)

hrg_YG12 = codelists_from_csv(
    "local_codelists/hrg_YG12.csv",
    system="opcs4",
    columnn="code",
)

hrg_YH02 = codelists_from_csv(
    "local_codelists/hrg_YH02.csv",
    system="opcs4",
    columnn="code",
)

hrg_YH03 = codelists_from_csv(
    "local_codelists/hrg_YH03.csv",
    system="opcs4",
    columnn="code",
)

hrg_YH10 = codelists_from_csv(
    "local_codelists/hrg_YH10.csv",
    system="opcs4",
    columnn="code",
)

hrg_YH20 = codelists_from_csv(
    "local_codelists/hrg_YH20.csv",
    system="opcs4",
    columnn="code",
)

hrg_YH30 = codelists_from_csv(
    "local_codelists/hrg_YH30.csv",
    system="opcs4",
    columnn="code",
)

hrg_YH31 = codelists_from_csv(
    "local_codelists/hrg_YH31.csv",
    system="opcs4",
    columnn="code",
)

hrg_YH32 = codelists_from_csv(
    "local_codelists/hrg_YH32.csv",
    system="opcs4",
    columnn="code",
)

hrg_YJ09 = codelists_from_csv(
    "local_codelists/hrg_YJ09.csv",
    system="opcs4",
    columnn="code",
)

hrg_YJ11 = codelists_from_csv(
    "local_codelists/hrg_YJ11.csv",
    system="opcs4",
    columnn="code",
)

hrg_YJ13 = codelists_from_csv(
    "local_codelists/hrg_YJ13.csv",
    system="opcs4",
    columnn="code",
)

hrg_YJ15 = codelists_from_csv(
    "local_codelists/hrg_YJ15.csv",
    system="opcs4",
    columnn="code",
)

hrg_YL02 = codelists_from_csv(
    "local_codelists/hrg_YL02.csv",
    system="opcs4",
    columnn="code",
)

hrg_YL11 = codelists_from_csv(
    "local_codelists/hrg_YL11.csv",
    system="opcs4",
    columnn="code",
)

hrg_YL12 = codelists_from_csv(
    "local_codelists/hrg_YL12.csv",
    system="opcs4",
    columnn="code",
)

hrg_YL20 = codelists_from_csv(
    "local_codelists/hrg_YL20.csv",
    system="opcs4",
    columnn="code",
)

hrg_YL21 = codelists_from_csv(
    "local_codelists/hrg_YL21.csv",
    system="opcs4",
    columnn="code",
)

hrg_YL30 = codelists_from_csv(
    "local_codelists/hrg_YL30.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ05 = codelists_from_csv(
    "local_codelists/hrg_YQ05.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ07 = codelists_from_csv(
    "local_codelists/hrg_YQ07.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ08 = codelists_from_csv(
    "local_codelists/hrg_YQ08.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ09 = codelists_from_csv(
    "local_codelists/hrg_YQ09.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ12 = codelists_from_csv(
    "local_codelists/hrg_YQ12.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ13 = codelists_from_csv(
    "local_codelists/hrg_YQ13.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ15 = codelists_from_csv(
    "local_codelists/hrg_YQ15.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ16 = codelists_from_csv(
    "local_codelists/hrg_YQ16.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ22 = codelists_from_csv(
    "local_codelists/hrg_YQ22.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ26 = codelists_from_csv(
    "local_codelists/hrg_YQ26.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ31 = codelists_from_csv(
    "local_codelists/hrg_YQ31.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ32 = codelists_from_csv(
    "local_codelists/hrg_YQ32.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ40 = codelists_from_csv(
    "local_codelists/hrg_YQ40.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ41 = codelists_from_csv(
    "local_codelists/hrg_YQ41.csv",
    system="opcs4",
    columnn="code",
)

hrg_YQ42 = codelists_from_csv(
    "local_codelists/hrg_YQ42.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR11 = codelists_from_csv(
    "local_codelists/hrg_YR11.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR12 = codelists_from_csv(
    "local_codelists/hrg_YR12.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR15 = codelists_from_csv(
    "local_codelists/hrg_YR15.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR16 = codelists_from_csv(
    "local_codelists/hrg_YR16.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR22 = codelists_from_csv(
    "local_codelists/hrg_YR22.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR23 = codelists_from_csv(
    "local_codelists/hrg_YR23.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR24 = codelists_from_csv(
    "local_codelists/hrg_YR24.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR25 = codelists_from_csv(
    "local_codelists/hrg_YR25.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR26 = codelists_from_csv(
    "local_codelists/hrg_YR26.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR31 = codelists_from_csv(
    "local_codelists/hrg_YR31.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR33 = codelists_from_csv(
    "local_codelists/hrg_YR33.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR40 = codelists_from_csv(
    "local_codelists/hrg_YR40.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR41 = codelists_from_csv(
    "local_codelists/hrg_YR41.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR42 = codelists_from_csv(
    "local_codelists/hrg_YR42.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR43 = codelists_from_csv(
    "local_codelists/hrg_YR43.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR44 = codelists_from_csv(
    "local_codelists/hrg_YR44.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR45 = codelists_from_csv(
    "local_codelists/hrg_YR45.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR48 = codelists_from_csv(
    "local_codelists/hrg_YR48.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR50 = codelists_from_csv(
    "local_codelists/hrg_YR50.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR51 = codelists_from_csv(
    "local_codelists/hrg_YR51.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR52 = codelists_from_csv(
    "local_codelists/hrg_YR52.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR53 = codelists_from_csv(
    "local_codelists/hrg_YR53.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR54 = codelists_from_csv(
    "local_codelists/hrg_YR54.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR56 = codelists_from_csv(
    "local_codelists/hrg_YR56.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR57 = codelists_from_csv(
    "local_codelists/hrg_YR57.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR63 = codelists_from_csv(
    "local_codelists/hrg_YR63.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR65 = codelists_from_csv(
    "local_codelists/hrg_YR65.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR66 = codelists_from_csv(
    "local_codelists/hrg_YR66.csv",
    system="opcs4",
    columnn="code",
)

hrg_YR67 = codelists_from_csv(
    "local_codelists/hrg_YR67.csv",
    system="opcs4",
    columnn="code",
)
