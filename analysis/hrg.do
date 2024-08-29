sysdir set PLUS ./analysis/adofiles
sysdir set PERSONAL ./analysis/adofiles
pwd

local dataset `1'

cap log close
macro drop hr
log using ./logs/hrg_`dataset'.log, replace t

use ./output/`dataset'_ckd_complete.dta, clear
drop _merge
merge 1:1 patient_id using ./output/`dataset'_nockd_complete
replace ckd_group = 1 if ckd_group==0

cap file close tablecontent
file open tablecontent using ./output/hrg_`dataset'.csv, write text replace

file write tablecontent ("hrg") _tab ("nockd_count") _tab ("nockd_admissions") _tab ("nockd_days") _tab ("ckd3_count") _tab ("ckd3_admissions") _tab ("ckd3_days") _tab ("ckd4_count") _tab ("ckd4_admissions") _tab ("ckd4_days") _tab ("dialysis_count") _tab ("dialysis_admissions") _tab ("dialysis_days") _tab ("kt_count") _tab ("kt_admissions") _tab ("kt_days") _n

file write tablecontent ("n")
forvalues i=1/5 {
qui safecount if ckd_group==`i'
local group_`i' = round(r(N),5)
if `group_`i'' > 5 & `group_`i''!=. {
file write tablecontent _tab (`group_`i'') _tab ("N/A") _tab ("N/A")
}
else {
file write tablecontent _tab ("REDACTED") _tab ("N/A") _tab ("N/A")
}
}
file write tablecontent _n

global hrg "aa22 aa23 aa24 aa25 aa26 aa28 aa29 aa30 aa31 aa32 aa33 aa35 aa43 aa50 aa51 aa52 aa53 aa54 aa55 aa57 aa60 aa61 aa71 aa81 aa83 ab11 ab15 ab16 ab18 ab20 ab21 ab22 ab23 ab24 ab26 bz24 bz31 bz32 bz33 bz41 bz42 bz44 bz45 bz46 bz51 bz53 bz54 bz56 bz57 bz60 bz61 bz62 bz63 bz64 bz65 bz72 bz73 bz74 bz80 bz81 bz83 bz84 bz86 bz87 bz88 bz89 bz91 bz92 bz93 bz94 bz95 ca01 ca02 ca03 ca04 ca05 ca10 ca11 ca12 ca13 ca14 ca15 ca16 ca20 ca21 ca22 ca23 ca24 ca25 ca26 ca27 ca28 ca29 ca30 ca31 ca32 ca33 ca34 ca35 ca36 ca37 ca38 ca39 ca40 ca42 ca43 ca50 ca51 ca52 ca53 ca54 ca55 ca60 ca62 ca63 ca64 ca65 ca66 ca67 ca68 ca69 ca70 ca71 ca80 ca81 ca82 ca83 ca84 ca85 ca86 ca91 ca92 ca93 ca94 ca95 ca96 ca97 ca98 cb01 cb02 cd01 cd02 cd03 cd04 cd05 cd06 cd07 cd08 cd09 cd10 cd11 cd12 dx21 dz01 dz02 dz09 dz10 dz11 dz12 dz13 dz14 dz15 dz16 dz17 dz18 dz19 dz20 dz22 dz23 dz24 dz25 dz26 dz27 dz28 dz29 dz30 dz31 dz32 dz33 dz36 dz37 dz38 dz42 dz45 dz46 dz49 dz50 dz51 dz55 dz56 dz57 dz58 dz59 dz60 dz63 dz64 dz65 dz67 dz68 dz69 dz70 dz71 eb02 eb03 eb04 eb05 eb06 eb07 eb08 eb09 eb10 eb12 eb13 eb14 eb15 ec11 ec12 ec13 ec14 ec15 ec21 ed01 ed05 ed08 ed09 ed11 ed12 ed13 ed14 ed15 ed18 ed24 ed25 ed26 ed27 ed28 ed30 ed31 ey01 ey02 ey04 ey06 ey08 ey11 ey12 ey13 ey17 ey22 ey23 ey30 ey31 ey32 ey40 ey41 ey42 ey43 ey50 ey51 fd01 fd02 fd03 fd04 fd05 fd10 fd11 fe01 fe02 fe03 fe10 fe11 fe12 fe13 fe20 fe21 fe22 fe30 fe31 fe32 fe33 fe34 fe35 fe36 fe50 ff01 ff02 ff04 ff05 ff12 ff13 ff14 ff20 ff21 ff22 ff30 ff31 ff32 ff33 ff34 ff36 ff37 ff40 ff41 ff42 ff43 ff50 ff51 ff52 ff53 ff60 ff61 ff62 ff63 ga03 ga04 ga05 ga06 ga07 ga10 ga11 ga13 ga15 ga16 gb05 gb06 gb09 gb10 gb11 gb12 gb13 gc01 gc12 gc17 gc18 hc20 hc21 hc26 hc27 hc28 hc29 hc30 hc31 hc32 hc50 hc53 hc54 hc60 hc61 hc62 hc63 hc64 hc65 hc70 hc71 hc72 hd21 hd23 hd24 hd25 hd26 hd39 hd40 he11 he12 he21 he22 he31 he32 he41 he42 he51 he52 he71 he72 he81 he82 he83 hn12 hn13 hn14 hn15 hn22 hn23 hn24 hn25 hn32 hn33 hn34 hn35 hn42 hn43 hn44 hn45 hn46 hn52 hn53 hn54 hn55 hn62 hn63 hn64 hn65 hn81 hn86 hn93 ja12 ja13 ja20 ja30 ja34 ja38 ja43 ja45 jb70 jb71 jb91 jc40 jc41 jc42 jc43 jc44 jc45 jc46 jc47 jd07 ka03 ka04 ka05 ka06 ka07 ka08 ka09 kb02 kb03 kb04 kc04 kc05 la01 la02 la03 la04 la05 la07 la08 la09 la10 la11 la12 la13 la14 lb06 lb09 lb10 lb12 lb13 lb14 lb15 lb16 lb17 lb18 lb19 lb20 lb21 lb25 lb26 lb28 lb29 lb33 lb35 lb36 lb37 lb38 lb39 lb40 lb42 lb43 lb46 lb47 lb48 lb50 lb51 lb52 lb53 lb54 lb55 lb56 lb57 lb58 lb59 lb60 lb61 lb64 lb65 lb67 lb68 lb70 lb71 lb72 lb74 lb75 lb76 lb77 lb78 le01 le02 ma01 ma02 ma03 ma04 ma07 ma09 ma10 ma11 ma12 ma22 ma23 ma24 ma25 ma29 ma30 ma31 ma32 ma35 ma36 ma38 ma44 ma48 ma52 ma53 ma56 mb05 mb08 mb09 mc07 mc08 mc09 mc10 mc11 mc12 mc20 mc21 nz16 nz17 nz18 nz19 nz20 nz21 nz22 nz24 nz25 nz26 nz27 nz30 nz40 nz50 nz51 nz71 nz72 rd01 rd08 rd20 rd30 rd40 rd47 rd48 rd50 rd51 rd60 rd61 rn01 rn04 rn07 rn08 rn09 rn13 rn14 rn15 rn16 rn17 rn18 rn19 rn20 rn21 rn22 rn23 rn24 rn25 rn26 rn27 rn28 rn29 rn30 rn31 rn32 rn33 rn34 rn50 rn51 rn52 sa01 sa02 sa03 sa04 sa05 sa06 sa07 sa08 sa09 sa11 sa12 sa14 sa15 sa16 sa17 sa18 sa19 sa20 sa21 sa22 sa23 sa24 sa25 sa26 sa27 sa30 sa31 sa32 sa33 sa35 sa36 sa37 sa40 sa42 sa43 sa44 sa45 sb01 sb02 sb03 sb04 sb05 sb06 sb07 sb08 sb09 sb10 sb11 sb12 sb13 sb14 sb15 sb16 sb17 sc25 sc26 sc28 sc29 sc30 sc40 sc42 sc44 sc45 sc47 sc49 sc51 sc53 sc54 sc55 sc56 sc57 uz01 uz02 uz03 uz04 uz05 uz06 uz15 va10 vc01 vc02 vc03 vc04 vc06 vc08 vc10 vc12 vc14 vc16 vc18 vc20 vc22 vc24 vc26 vc28 vc30 vc32 vc34 vc36 vc38 vc40 vc42 wd01 wd02 wd03 wd04 wd05 wd06 wd07 wd08 wd09 wf01 wf02 wh01 wh02 wh03 wh04 wh05 wh06 wh07 wh08 wh09 wh10 wh11 wh12 wh13 wh14 wh15 wh16 wh17 wh18 wh19 wh20 wh21 wh22 wh23 wh50 wh51 wh52 wh53 wh54 wh99 wj01 wj02 wj03 wj04 wj06 wj07 wj10 wj11 xd01 xd02 xd03 xd04 xd05 xd06 xd07 xd08 xd09 xd10 xd11 xd12 xd13 xd14 xd15 xd16 xd17 xd18 xd19 xd20 xd21 xd22 xd23 xd24 xd25 xd26 xd27 xd28 xd29 xd30 xd31 xd32 xd33 xd34 xd37 xd38 xd39 xd40 xd41 xd42 xd43 xd44 xd45 xd46 xd47 xd48 xd49 xd50 xd51 xd52 xd53 xd54 xd55 xd56 xd57 xd58 xd90 xd91 ya03 ya04 ya10 ya11 ya12 ya13 yc01 yc10 yd01 yd02 yd03 yd04 yd05 yf01 yf04 yg01 yg02 yg05 yg06 yg07 yg10 yg11 yg12 yh02 yh03 yh10 yh20 yh30 yh31 yh32 yj09 yj11 yj13 yj15 yl02 yl11 yl12 yl20 yl21 yl30 yq05 yq07 yq08 yq09 yq12 yq13 yq15 yq16 yq22 yq26 yq31 yq32 yq40 yq41 yq42 yq50 yq51 yr11 yr12 yr15 yr16 yr22 yr23 yr24 yr25 yr26 yr31 yr33 yr40 yr41 yr42 yr43 yr44 yr45 yr48 yr50 yr51 yr52 yr53 yr54 yr56 yr57 yr63 yr65 yr66 yr67"

foreach hrg of global hrg {
file write tablecontent ("`hrg'")
foreach var of varlist `hrg'_admissions `hrg'_days {
egen total_`var' = total(`var')
forvalues i=1/5 {
qui safecount if ckd_group==`i' & `hrg'_count==1
local `hrg'_count_`i' = round(r(N),5)
qui su total_`var' if ckd_group==`i'
local `var'_`i' = r(mean)
if ``hrg'_count_`i'' >5 & ``hrg'_count_`i''!=. {
file write tablecontent _tab (``hrg'_count_`i'') _tab (``hrg'_admissions_`i'') _tab (``hrg'_days_`i'')
}
else {
file write tablecontent _tab ("REDACTED") _tab ("REDACTED") _tab ("REDACTED")
}
}
}
file write tablecontent _n
}

file close tablecontent