sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
log using ./logs/`dataset'_nockd_random, replace t
clear

import delimited ./output/`dataset'_nockd.csv, delimiter(comma) varnames(1) case(preserve)

gen random_order = runiform()              
sort random_order                          
safecount                                   
local total_obs = r(N)                     
local drop_count = ceil(0.75 * `total_obs') 
drop in 1/`drop_count'  

export delimited using "./output/`dataset'_nockd.csv", replace

log close
