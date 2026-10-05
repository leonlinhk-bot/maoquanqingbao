#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1006_0049
t() { printf '%-32s ' "$1"; curl -sL -m 30 -A "$UA" -o "$OUT/$1" -w "%{http_code} %{size_download}\n" "$2"; }
t a_dc.html "https://insuranceasia.com/insurance/expert-opinion/can-asias-data-centre-boom-reverse-falling-insurance-rates"
t a_unimed.html "https://insuranceasia.com/insurance/news/unimed-recovers-two-years-losses-premium-increases-kick-in"
t a_aero.html "https://insuranceasia.com/insurance/news/aerospace-insurers-tighten-scrutiny-despite-stable-price-and-capacity"
t a_drought.html "https://insuranceasia.com/insurance/news/australian-insurers-face-29b-drought-risk"
t a_cyber.html "https://insuranceasia.com/insurance/news/insurers-face-apac-cyber-regulatory-divergence-enforcement-tightens"
t a_picc.html "https://www.artemis.bm/news/picc-pc-appears-to-have-returned-for-its-second-great-wall-re-catastrophe-bond/"
t a_ucits.html "https://www.artemis.bm/news/ucits-cat-bond-funds-average-6-67-return-ytd-fourth-highest-annual-figure-on-record-plenum-index/"
t a_eaton.html "https://www.artemis.bm/news/eaton-vance-mutual-fund-ils-holdings-hit-777m-new-swiss-re-and-jaffa-capital-investments/"
t a_arc.html "https://www.artemis.bm/news/african-risk-capacity-ltd-promotes-muthengi-to-chief-underwriting-officer/"
t a_marshre.html "https://artemis.bm/news/apac-ils-and-parametric-markets-poised-for-growth-as-capital-needs-shift-marsh-res-gallagher/"
t ian_marsh.html "https://insuranceasianews.com/as-apac-risk-transfer-market-opens-up-marsh-re-eyes-parametric-wind-bushfire-cover/"
echo DONE
