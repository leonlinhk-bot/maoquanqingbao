#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
O=/Users/leonliang/maoquanqingbao/data/_cache1006_0156
t() { printf '%-22s ' "$1"; curl -sL -m 35 -A "$UA" -o "$O/$1" -w "%{http_code} %{size_download}\n" "$2"; }
IA="https%3A%2F%2Fwww.ia.org.hk%2Fen%2Finfocenter%2Fpress_releases.html"
t ia_allorigins.txt "https://api.allorigins.win/raw?url=$IA"
t ia_corsproxy.txt  "https://corsproxy.io/?$IA"
t ia_textance.txt   "https://api.codetabs.com/v1/proxy?quest=$IA"
t iaweb.txt         "https://api.codetabs.com/v1/proxy?quest=https%3A%2F%2Fwww.ia.org.hk%2Fen%2Flegislative_framework%2Fcirculars%2Freg_matters%2Fcirculars_on_regulatory_matters_2026.html"
t nfra_list.json    "https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectByConditionPage.json?pageNum=1&pageSize=20"
t nfra_list2.json   "https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild.json?itemId=931&pageSize=20"
echo "--- sniff sizes/content ---"
for f in ia_allorigins.txt ia_corsproxy.txt ia_textance.txt iaweb.txt nfra_list.json nfra_list2.json; do
  printf '%-20s ' "$f"; head -c 150 "$O/$f" | tr -d '\n'; echo
done
echo DONE
