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

foreach days of varlist aa22_days aa23_days aa24_days aa25_days aa26_days aa28_days aa29_days aa30_days aa31_days aa32_days aa33_days aa35_days aa43_days aa50_days aa51_days aa52_days aa53_days aa54_days aa55_days aa57_days aa60_days aa61_days aa71_days aa81_days aa83_days ab11_days ab15_days ab16_days ab18_days ab20_days ab21_days ab22_days ab23_days ab24_days ab26_days bz24_days bz31_days bz32_days bz33_days bz41_days bz42_days bz44_days bz45_days bz46_days bz51_days bz53_days bz54_days bz56_days bz57_days bz60_days bz61_days bz62_days bz63_days bz64_days bz65_days bz72_days bz73_days bz74_days bz80_days bz81_days bz83_days bz84_days bz86_days bz87_days bz88_days bz89_days bz91_days bz92_days bz93_days bz94_days bz95_days ca01_days ca02_days ca03_days ca04_days ca05_days ca10_days ca11_days ca12_days ca13_days ca14_days ca15_days ca16_days ca20_days ca21_days ca22_days ca23_days ca24_days ca25_days ca26_days ca27_days ca28_days ca29_days ca30_days ca31_days ca32_days ca33_days ca34_days ca35_days ca36_days ca37_days ca38_days ca39_days ca40_days ca42_days ca43_days ca50_days ca51_days ca52_days ca53_days ca54_days ca55_days ca60_days ca62_days ca63_days ca64_days ca65_days ca66_days ca67_days ca68_days ca69_days ca70_days ca71_days ca80_days ca81_days ca82_days ca83_days ca84_days ca85_days ca86_days ca91_days ca92_days ca93_days ca94_days ca95_days ca96_days ca97_days ca98_days cb01_days cb02_days cd01_days cd02_days cd03_days cd04_days cd05_days cd06_days cd07_days cd08_days cd09_days cd10_days cd11_days cd12_days dx21_days dz01_days dz02_days dz09_days dz10_days dz11_days dz12_days dz13_days dz14_days dz15_days dz16_days dz17_days dz18_days dz19_days dz20_days dz22_days dz23_days dz24_days dz25_days dz26_days dz27_days dz28_days dz29_days dz30_days dz31_days dz32_days dz33_days dz36_days dz37_days dz38_days dz42_days dz45_days dz46_days dz49_days dz50_days dz51_days dz55_days dz56_days dz57_days dz58_days dz59_days dz60_days dz63_days dz64_days dz65_days dz67_days dz68_days dz69_days dz70_days dz71_days eb02_days eb03_days eb04_days eb05_days eb06_days eb07_days eb08_days eb09_days eb10_days eb12_days eb13_days eb14_days eb15_days ec11_days ec12_days ec13_days ec14_days ec15_days ec21_days ed01_days ed05_days ed08_days ed09_days ed11_days ed12_days ed13_days ed14_days ed15_days ed18_days ed24_days ed25_days ed26_days ed27_days ed28_days ed30_days ed31_days ey01_days ey02_days ey04_days ey06_days ey08_days ey11_days ey12_days ey13_days ey17_days ey22_days ey23_days ey30_days ey31_days ey32_days ey40_days ey41_days ey42_days ey43_days ey50_days ey51_days fd01_days fd02_days fd03_days fd04_days fd05_days fd10_days fd11_days fe01_days fe02_days fe03_days fe10_days fe11_days fe12_days fe13_days fe20_days fe21_days fe22_days fe30_days fe31_days fe32_days fe33_days fe34_days fe35_days fe36_days fe50_days ff01_days ff02_days ff04_days ff05_days ff12_days ff13_days ff14_days ff20_days ff21_days ff22_days ff30_days ff31_days ff32_days ff33_days ff34_days ff36_days ff37_days ff40_days ff41_days ff42_days ff43_days ff50_days ff51_days ff52_days ff53_days ff60_days ff61_days ff62_days ff63_days ga03_days ga04_days ga05_days ga06_days ga07_days ga10_days ga11_days ga13_days ga15_days ga16_days gb05_days gb06_days gb09_days gb10_days gb11_days gb12_days gb13_days gc01_days gc12_days gc17_days gc18_days hc20_days hc21_days hc26_days hc27_days hc28_days hc29_days hc30_days hc31_days hc32_days hc50_days hc53_days hc54_days hc60_days hc61_days hc62_days hc63_days hc64_days hc65_days hc70_days hc71_days hc72_days hd21_days hd23_days hd24_days hd25_days hd26_days hd39_days hd40_days he11_days he12_days he21_days he22_days he31_days he32_days he41_days he42_days he51_days he52_days he71_days he72_days he81_days he82_days he83_days hn12_days hn13_days hn14_days hn15_days hn22_days hn23_days hn24_days hn25_days hn32_days hn33_days hn34_days hn35_days hn42_days hn43_days hn44_days hn45_days hn46_days hn52_days hn53_days hn54_days hn55_days hn62_days hn63_days hn64_days hn65_days hn81_days hn86_days hn93_days ja12_days ja13_days ja20_days ja30_days ja34_days ja38_days ja43_days ja45_days jb70_days jb71_days jb91_days jc40_days jc41_days jc42_days jc43_days jc44_days jc45_days jc46_days jc47_days jd07_days ka03_days ka04_days ka05_days ka06_days ka07_days ka08_days ka09_days kb02_days kb03_days kb04_days kc04_days kc05_days la01_days la02_days la03_days la04_days la05_days la07_days la08_days la09_days la10_days la11_days la12_days la13_days la14_days lb06_days lb09_days lb10_days lb12_days lb13_days lb14_days lb15_days lb16_days lb17_days lb18_days lb19_days lb20_days lb21_days lb25_days lb26_days lb28_days lb29_days lb33_days lb35_days lb36_days lb37_days lb38_days lb39_days lb40_days lb42_days lb43_days lb46_days lb47_days lb48_days lb50_days lb51_days lb52_days lb53_days lb54_days lb55_days lb56_days lb57_days lb58_days lb59_days lb60_days lb61_days lb64_days lb65_days lb67_days lb68_days lb70_days lb71_days lb72_days lb74_days lb75_days lb76_days lb77_days lb78_days le01_days le02_days ma01_days ma02_days ma03_days ma04_days ma07_days ma09_days ma10_days ma11_days ma12_days ma22_days ma23_days ma24_days ma25_days ma29_days ma30_days ma31_days ma32_days ma35_days ma36_days ma38_days ma44_days ma48_days ma52_days ma53_days ma56_days mb05_days mb08_days mb09_days mc07_days mc08_days mc09_days mc10_days mc11_days mc12_days mc20_days mc21_days nz16_days nz17_days nz18_days nz19_days nz20_days nz21_days nz22_days nz24_days nz25_days nz26_days nz27_days nz30_days nz40_days nz50_days nz51_days nz71_days nz72_days rd01_days rd08_days rd20_days rd30_days rd40_days rd47_days rd48_days rd50_days rd51_days rd60_days rd61_days rn01_days rn04_days rn07_days rn08_days rn09_days rn13_days rn14_days rn15_days rn16_days rn17_days rn18_days rn19_days rn20_days rn21_days rn22_days rn23_days rn24_days rn25_days rn26_days rn27_days rn28_days rn29_days rn30_days rn31_days rn32_days rn33_days rn34_days rn50_days rn51_days rn52_days sa01_days sa02_days sa03_days sa04_days sa05_days sa06_days sa07_days sa08_days sa09_days sa11_days sa12_days sa14_days sa15_days sa16_days sa17_days sa18_days sa19_days sa20_days sa21_days sa22_days sa23_days sa24_days sa25_days sa26_days sa27_days sa30_days sa31_days sa32_days sa33_days sa35_days sa36_days sa37_days sa40_days sa42_days sa43_days sa44_days sa45_days sb01_days sb02_days sb03_days sb04_days sb05_days sb06_days sb07_days sb08_days sb09_days sb10_days sb11_days sb12_days sb13_days sb14_days sb15_days sb16_days sb17_days sc25_days sc26_days sc28_days sc29_days sc30_days sc40_days sc42_days sc44_days sc45_days sc47_days sc49_days sc51_days sc53_days sc54_days sc55_days sc56_days sc57_days uz01_days uz02_days uz03_days uz04_days uz05_days uz06_days uz15_days va10_days vc01_days vc02_days vc03_days vc04_days vc06_days vc08_days vc10_days vc12_days vc14_days vc16_days vc18_days vc20_days vc22_days vc24_days vc26_days vc28_days vc30_days vc32_days vc34_days vc36_days vc38_days vc40_days vc42_days wd01_days wd02_days wd03_days wd04_days wd05_days wd06_days wd07_days wd08_days wd09_days wf01_days wf02_days wh01_days wh02_days wh03_days wh04_days wh05_days wh06_days wh07_days wh08_days wh09_days wh10_days wh11_days wh12_days wh13_days wh14_days wh15_days wh16_days wh17_days wh18_days wh19_days wh20_days wh21_days wh22_days wh23_days wh50_days wh51_days wh52_days wh53_days wh54_days wh99_days wj01_days wj02_days wj03_days wj04_days wj06_days wj07_days wj10_days wj11_days xd01_days xd02_days xd03_days xd04_days xd05_days xd06_days xd07_days xd08_days xd09_days xd10_days xd11_days xd12_days xd13_days xd14_days xd15_days xd16_days xd17_days xd18_days xd19_days xd20_days xd21_days xd22_days xd23_days xd24_days xd25_days xd26_days xd27_days xd28_days xd29_days xd30_days xd31_days xd32_days xd33_days xd34_days xd37_days xd38_days xd39_days xd40_days xd41_days xd42_days xd43_days xd44_days xd45_days xd46_days xd47_days xd48_days xd49_days xd50_days xd51_days xd52_days xd53_days xd54_days xd55_days xd56_days xd57_days xd58_days xd90_days xd91_days ya03_days ya04_days ya10_days ya11_days ya12_days ya13_days yc01_days yc10_days yd01_days yd02_days yd03_days yd04_days yd05_days yf01_days yf04_days yg01_days yg02_days yg05_days yg06_days yg07_days yg10_days yg11_days yg12_days yh02_days yh03_days yh10_days yh20_days yh30_days yh31_days yh32_days yj09_days yj11_days yj13_days yj15_days yl02_days yl11_days yl12_days yl20_days yl21_days yl30_days yq05_days yq07_days yq08_days yq09_days yq12_days yq13_days yq15_days yq16_days yq22_days yq26_days yq31_days yq32_days yq40_days yq41_days yq42_days yq50_days yq51_days yr11_days yr12_days yr15_days yr16_days yr22_days yr23_days yr24_days yr25_days yr26_days yr31_days yr33_days yr40_days yr41_days yr42_days yr43_days yr44_days yr45_days yr48_days yr50_days yr51_days yr52_days yr53_days yr54_days yr56_days yr57_days yr63_days yr65_days yr66_days yr67_days {
bysort ckd_group: egen total_`days' = total(`days')
}


cap file close tablecontent
file open tablecontent using ./output/hrg_`dataset'.csv, write text replace

file write tablecontent ("hrg") _tab ("nockd_count") _tab ("nockd_days") _tab ("ckd3_count") _tab ("ckd3_days") _tab ("ckd4_count") _tab ("ckd4_days") _tab ("dialysis_count") _tab ("dialysis_days") _tab ("kt_count") _tab ("kt_days") _n

global hrg "aa22 aa23 aa24 aa25 aa26 aa28 aa29 aa30 aa31 aa32 aa33 aa35 aa43 aa50 aa51 aa52 aa53 aa54 aa55 aa57 aa60 aa61 aa71 aa81 aa83 ab11 ab15 ab16 ab18 ab20 ab21 ab22 ab23 ab24 ab26 bz24 bz31 bz32 bz33 bz41 bz42 bz44 bz45 bz46 bz51 bz53 bz54 bz56 bz57 bz60 bz61 bz62 bz63 bz64 bz65 bz72 bz73 bz74 bz80 bz81 bz83 bz84 bz86 bz87 bz88 bz89 bz91 bz92 bz93 bz94 bz95 ca01 ca02 ca03 ca04 ca05 ca10 ca11 ca12 ca13 ca14 ca15 ca16 ca20 ca21 ca22 ca23 ca24 ca25 ca26 ca27 ca28 ca29 ca30 ca31 ca32 ca33 ca34 ca35 ca36 ca37 ca38 ca39 ca40 ca42 ca43 ca50 ca51 ca52 ca53 ca54 ca55 ca60 ca62 ca63 ca64 ca65 ca66 ca67 ca68 ca69 ca70 ca71 ca80 ca81 ca82 ca83 ca84 ca85 ca86 ca91 ca92 ca93 ca94 ca95 ca96 ca97 ca98 cb01 cb02 cd01 cd02 cd03 cd04 cd05 cd06 cd07 cd08 cd09 cd10 cd11 cd12 dx21 dz01 dz02 dz09 dz10 dz11 dz12 dz13 dz14 dz15 dz16 dz17 dz18 dz19 dz20 dz22 dz23 dz24 dz25 dz26 dz27 dz28 dz29 dz30 dz31 dz32 dz33 dz36 dz37 dz38 dz42 dz45 dz46 dz49 dz50 dz51 dz55 dz56 dz57 dz58 dz59 dz60 dz63 dz64 dz65 dz67 dz68 dz69 dz70 dz71 eb02 eb03 eb04 eb05 eb06 eb07 eb08 eb09 eb10 eb12 eb13 eb14 eb15 ec11 ec12 ec13 ec14 ec15 ec21 ed01 ed05 ed08 ed09 ed11 ed12 ed13 ed14 ed15 ed18 ed24 ed25 ed26 ed27 ed28 ed30 ed31 ey01 ey02 ey04 ey06 ey08 ey11 ey12 ey13 ey17 ey22 ey23 ey30 ey31 ey32 ey40 ey41 ey42 ey43 ey50 ey51 fd01 fd02 fd03 fd04 fd05 fd10 fd11 fe01 fe02 fe03 fe10 fe11 fe12 fe13 fe20 fe21 fe22 fe30 fe31 fe32 fe33 fe34 fe35 fe36 fe50 ff01 ff02 ff04 ff05 ff12 ff13 ff14 ff20 ff21 ff22 ff30 ff31 ff32 ff33 ff34 ff36 ff37 ff40 ff41 ff42 ff43 ff50 ff51 ff52 ff53 ff60 ff61 ff62 ff63 ga03 ga04 ga05 ga06 ga07 ga10 ga11 ga13 ga15 ga16 gb05 gb06 gb09 gb10 gb11 gb12 gb13 gc01 gc12 gc17 gc18 hc20 hc21 hc26 hc27 hc28 hc29 hc30 hc31 hc32 hc50 hc53 hc54 hc60 hc61 hc62 hc63 hc64 hc65 hc70 hc71 hc72 hd21 hd23 hd24 hd25 hd26 hd39 hd40 he11 he12 he21 he22 he31 he32 he41 he42 he51 he52 he71 he72 he81 he82 he83 hn12 hn13 hn14 hn15 hn22 hn23 hn24 hn25 hn32 hn33 hn34 hn35 hn42 hn43 hn44 hn45 hn46 hn52 hn53 hn54 hn55 hn62 hn63 hn64 hn65 hn81 hn86 hn93 ja12 ja13 ja20 ja30 ja34 ja38 ja43 ja45 jb70 jb71 jb91 jc40 jc41 jc42 jc43 jc44 jc45 jc46 jc47 jd07 ka03 ka04 ka05 ka06 ka07 ka08 ka09 kb02 kb03 kb04 kc04 kc05 la01 la02 la03 la04 la05 la07 la08 la09 la10 la11 la12 la13 la14 lb06 lb09 lb10 lb12 lb13 lb14 lb15 lb16 lb17 lb18 lb19 lb20 lb21 lb25 lb26 lb28 lb29 lb33 lb35 lb36 lb37 lb38 lb39 lb40 lb42 lb43 lb46 lb47 lb48 lb50 lb51 lb52 lb53 lb54 lb55 lb56 lb57 lb58 lb59 lb60 lb61 lb64 lb65 lb67 lb68 lb70 lb71 lb72 lb74 lb75 lb76 lb77 lb78 le01 le02 ma01 ma02 ma03 ma04 ma07 ma09 ma10 ma11 ma12 ma22 ma23 ma24 ma25 ma29 ma30 ma31 ma32 ma35 ma36 ma38 ma44 ma48 ma52 ma53 ma56 mb05 mb08 mb09 mc07 mc08 mc09 mc10 mc11 mc12 mc20 mc21 nz16 nz17 nz18 nz19 nz20 nz21 nz22 nz24 nz25 nz26 nz27 nz30 nz40 nz50 nz51 nz71 nz72 rd01 rd08 rd20 rd30 rd40 rd47 rd48 rd50 rd51 rd60 rd61 rn01 rn04 rn07 rn08 rn09 rn13 rn14 rn15 rn16 rn17 rn18 rn19 rn20 rn21 rn22 rn23 rn24 rn25 rn26 rn27 rn28 rn29 rn30 rn31 rn32 rn33 rn34 rn50 rn51 rn52 sa01 sa02 sa03 sa04 sa05 sa06 sa07 sa08 sa09 sa11 sa12 sa14 sa15 sa16 sa17 sa18 sa19 sa20 sa21 sa22 sa23 sa24 sa25 sa26 sa27 sa30 sa31 sa32 sa33 sa35 sa36 sa37 sa40 sa42 sa43 sa44 sa45 sb01 sb02 sb03 sb04 sb05 sb06 sb07 sb08 sb09 sb10 sb11 sb12 sb13 sb14 sb15 sb16 sb17 sc25 sc26 sc28 sc29 sc30 sc40 sc42 sc44 sc45 sc47 sc49 sc51 sc53 sc54 sc55 sc56 sc57 uz01 uz02 uz03 uz04 uz05 uz06 uz15 va10 vc01 vc02 vc03 vc04 vc06 vc08 vc10 vc12 vc14 vc16 vc18 vc20 vc22 vc24 vc26 vc28 vc30 vc32 vc34 vc36 vc38 vc40 vc42 wd01 wd02 wd03 wd04 wd05 wd06 wd07 wd08 wd09 wf01 wf02 wh01 wh02 wh03 wh04 wh05 wh06 wh07 wh08 wh09 wh10 wh11 wh12 wh13 wh14 wh15 wh16 wh17 wh18 wh19 wh20 wh21 wh22 wh23 wh50 wh51 wh52 wh53 wh54 wh99 wj01 wj02 wj03 wj04 wj06 wj07 wj10 wj11 xd01 xd02 xd03 xd04 xd05 xd06 xd07 xd08 xd09 xd10 xd11 xd12 xd13 xd14 xd15 xd16 xd17 xd18 xd19 xd20 xd21 xd22 xd23 xd24 xd25 xd26 xd27 xd28 xd29 xd30 xd31 xd32 xd33 xd34 xd37 xd38 xd39 xd40 xd41 xd42 xd43 xd44 xd45 xd46 xd47 xd48 xd49 xd50 xd51 xd52 xd53 xd54 xd55 xd56 xd57 xd58 xd90 xd91 ya03 ya04 ya10 ya11 ya12 ya13 yc01 yc10 yd01 yd02 yd03 yd04 yd05 yf01 yf04 yg01 yg02 yg05 yg06 yg07 yg10 yg11 yg12 yh02 yh03 yh10 yh20 yh30 yh31 yh32 yj09 yj11 yj13 yj15 yl02 yl11 yl12 yl20 yl21 yl30 yq05 yq07 yq08 yq09 yq12 yq13 yq15 yq16 yq22 yq26 yq31 yq32 yq40 yq41 yq42 yq50 yq51 yr11 yr12 yr15 yr16 yr22 yr23 yr24 yr25 yr26 yr31 yr33 yr40 yr41 yr42 yr43 yr44 yr45 yr48 yr50 yr51 yr52 yr53 yr54 yr56 yr57 yr63 yr65 yr66 yr67"

foreach hrg of global hrg {
file write tablecontent ("`hrg'")
forvalues i=1/5 {
qui safecount if ckd_group==`i' & `hrg'_count==1
local `hrg'_count_`i' = round(r(N),5)
qui su total_`hrg'_days if ckd_group==`i'
local `hrg'_days_`i' = r(mean)
if ``hrg'_count_`i'' >5 & ``hrg'_count_`i''!=. {
file write tablecontent _tab (``hrg'_count_`i'') _tab (``hrg'_days_`i'')
}
else {
file write tablecontent _tab ("REDACTED") _tab ("REDACTED")
}
}
file write tablecontent _n
}

file close tablecontent