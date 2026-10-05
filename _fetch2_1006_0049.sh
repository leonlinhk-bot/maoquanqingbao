#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1006_0049
t() { printf '%-34s ' "$1"; curl -sL -m 30 -A "$UA" -o "$OUT/$1" -w "%{http_code} %{size_download}\n" "$2"; }
t p_ibm_howden.html "https://www.insurancebusinessmag.com/asia/news/breaking-news/dominic-collins-to-step-down-as-howdens-executive-chairman-592300.aspx"
t p_ibm_mas_who.html "https://www.insurancebusinessmag.com/asia/news/breaking-news/mas-moves-to-approve-who-chairs-insurer-nominating-committees-592336.aspx"
t p_ibm_lifesci.html "https://www.insurancebusinessmag.com/asia/news/breaking-news/life-sciences-risk-is-shifting-and-coverage-may-not-follow-592256.aspx"
t p_hkma_bakai.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261005-4/"
t p_sunlife_cuhk.html "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-partners-with-cuhk-medical-centre/"
t p_fstb_tax.html "https://www.info.gov.hk/gia/general/202610/05/P2026100500301.htm"
t nfra_api1.json "https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectByConditionPage_1.json"
t nfra_api3.json "https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=953&itemId=954"
echo DONE
