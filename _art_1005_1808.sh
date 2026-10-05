#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
f() { printf '%-24s ' "$1"; curl -sL -m 30 -A "$UA" -o "$OUT/a_$1" -w "%{http_code} %{size_download}\n" "$2"; }
f art_ucits   "https://www.artemis.bm/news/ucits-cat-bond-funds-average-6-67-return-ytd-fourth-highest-annual-figure-on-record-plenum-index/"
f art_eaton   "https://www.artemis.bm/news/eaton-vance-mutual-fund-ils-holdings-hit-777m-new-swiss-re-and-jaffa-capital-investments/"
f art_marshre "https://www.artemis.bm/news/apac-ils-and-parametric-markets-poised-for-growth-as-capital-needs-shift-marsh-res-gallagher/"
f ibm_lifesci "https://www.insurancebusinessmag.com/asia/news/breaking-news/life-sciences-risk-is-shifting-and-coverage-may-not-follow-592256.aspx"
f ian_koreanre "https://insuranceasianews.com/south-koreas-nat-cat-claims-under-public-insurance-schemes-top-us1bn-in-2025-korean-re/"
f iaasia_dc   "https://insuranceasia.com/insurance/expert-opinion/can-asias-data-centre-boom-reverse-falling-insurance-rates"
f doc_aia_mpf "https://news.mingpao.com/pns/%E7%B6%93%E6%BF%9F/article/20261005/s00004/1759593000000"
echo DONE
