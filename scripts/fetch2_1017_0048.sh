#!/usr/bin/env bash
set -u
D=/Users/leonliang/maoquanqingbao/data/_1017_0048
mkdir -p "$D"; cd "$D"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() { key="$1"; url="$2"
  code=$(curl -sSL -m 40 -A "$UA" -o "$key.out" -w '%{http_code}' "$url" || echo ERR)
  echo "$key http=$code bytes=$(wc -c < "$key.out" 2>/dev/null|tr -d ' ')"; }
fetch axa2026   "https://www.axa.com.hk/zh/news-room/2026"
fetch sun2026   "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/"
fetch iaasia_hp "https://insuranceasia.com/"
fetch iaasia_lp "https://insuranceasia.com/insurance/news"
fetch ibm_hk     "https://www.insurancebusinessmag.com/asia/news/"
fetch cir_aml    "https://www.ia.org.hk/en/legislative_framework/circulars/antimoney_laundering/circulars_on_anti-money_laundering_matters.html"
fetch nfra_news  "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=931&itemUrl=ItemListRightList.html&itemName=%E7%9B%91%E7%AE%A1%E5%8A%A8%E6%80%81"
echo DONE2
