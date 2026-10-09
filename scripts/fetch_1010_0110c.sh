#!/usr/bin/env bash
set -u
D=/Users/leonliang/maoquanqingbao/data/_raw_1010_0110
cd "$D"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() { key="$1"; url="$2"; code=$(curl -sSL -m 45 -A "$UA" -o "$key.out" -w '%{http_code}' "$url" || echo ERR); echo "$key  http=$code  bytes=$(wc -c < "$key.out" 2>/dev/null | tr -d ' ')"; }
fetch aia2026      "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2026"
fetch sunlife2026  "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/"
fetch hkfi_news    "https://www.hkfi.org.hk/en/media-centre/news"
fetch hkfi_pr      "https://www.hkfi.org.hk/en/media-centre/press-releases"
fetch nfra_list    "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=925&itemUrl=ItemListRightList.html&itemName=%E7%9B%91%E7%AE%A1%E5%8A%A8%E6%80%81"
fetch ia_alert     "https://www.ia.org.hk/en/infocenter/alert_list.html"
echo DONE3
