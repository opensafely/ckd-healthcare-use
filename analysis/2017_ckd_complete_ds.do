sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

cap log close
log using ./logs/2017_ckd_complete_ds, replace t
clear

capture noisily import delimited ./output/input_2017_ckd_complete.csv, clear

ds

log close