#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
t() { printf '%-30s ' "$1"; curl -sL -m 25 --noproxy '*' -A "$UA" -H "Referer: https://www.nfra.gov.cn/" -o "$OUT/$1" -w "%{http_code} %{size_download}\n" "$2"; }
t nfra_api1.json "https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectByConditionPage_1.json"
t nfra_api2.json "https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=923&itemId=931"
t nfra_api3.json "https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=953&itemId=954"
t nfra_live.json "https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild_1.json?itemId=931"
echo "--- sniff ---"
head -c 400 "$OUT/nfra_api1.json"; echo; head -c 400 "$OUT/nfra_api2.json"; echo
echo DONE
