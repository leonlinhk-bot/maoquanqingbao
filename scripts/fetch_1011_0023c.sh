#!/usr/bin/env bash
set -u
D=/Users/leonliang/maoquanqingbao/data/_raw_1011_0023
mkdir -p "$D"; cd "$D"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() { key="$1"; url="$2"; code=$(curl -sSL -m 40 -A "$UA" -o "$key.out" -w '%{http_code}' "$url" || echo ERR); echo "$key  http=$code  bytes=$(wc -c < "$key.out" 2>/dev/null | tr -d ' ')"; }
fetch iaasia_site "https://insuranceasia.com/insurance/news"
fetch nfra_news    "https://www.nfra.gov.cn/cn/view/pages/xinwenzixun/xinwenzixun.html"
fetch nfra_stats   "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=953&itemId=954"
fetch hkfi_zh      "https://www.hkfi.org.hk/zh/media-release"
fetch fstb_other   "https://www.fstb.gov.hk/fsb/tc/business/other_matters/index.html"
fetch hkma_circ    "https://www.hkma.gov.hk/eng/news-and-media/insight/"
fetch artemis_simon "https://www.artemis.bm/news/hurricane-simon-intensify-mexico-catastrophe-bond-watch/"
fetch ibm_ci       "https://www.insurancebusinessmag.com/asia/news/life-insurance/singapores-ci-definitions-are-moving-toward-disease--legacy-policies-arent-593083.aspx"
echo DONE-3
