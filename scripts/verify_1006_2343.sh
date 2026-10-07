#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1006_2343
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
f(){ curl -sSL --max-time 30 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"; }
f v_mpfa.html   "https://www.mpfa.org.hk/en/info-centre/press-releases/20261006"
f v_govhk_free.html "https://www.info.gov.hk/gia/general/202610/06/P2026100600631.htm"
f v_hkma_bnm.html   "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261006-4/"
f v_ibm_life.html   "https://www.insurancebusinessmag.com/asia/news/breaking-news/life-sciences-risk-is-shifting-and-coverage-may-not-follow-592256.aspx"
f v_fo_singtao.html "https://www.singtao.ca/7646910/2026-10-05/news-%E8%B7%A8%E5%A2%83%E7%90%86%E8%B2%A1%E7%9B%A3%E7%AE%A1%E8%B6%A8%E5%9A%B4+%E9%99%B3%E5%BE%B7%E7%BF%B9%EF%BC%9A%E5%90%88%E8%A6%8F%E6%B8%A0%E9%81%93%E9%9C%80%E6%B1%82%E5%A2%9E+%E3%80%8C%E4%B8%89%E5%A4%A7%E5%8B%95%E5%8A%9B%E3%80%8D%E6%94%AF%E6%8C%81%E6%B8%AF%E5%AE%B6%E8%BE%A6%E5%B8%82%E5%A0%B4/"
echo DONE
