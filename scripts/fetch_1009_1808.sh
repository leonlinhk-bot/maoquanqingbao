#!/usr/bin/env bash
# 港险情报站 · 直连抓取（2026-10-09 18:08）
set -u
cd "$(dirname "$0")/../data/_raw_1009_1808" 2>/dev/null || { mkdir -p /Users/leonliang/maoquanqingbao/data/_raw_1009_1808; cd /Users/leonliang/maoquanqingbao/data/_raw_1009_1808; }
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'

fetch() {
  key="$1"; url="$2"
  code=$(curl -sSL -m 35 -A "$UA" -o "$key.out" -w '%{http_code}' "$url")
  echo "$key  http=$code  bytes=$(wc -c < "$key.out" | tr -d ' ')"
}

fetch ia_press       "https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch ia_press2      "https://www.ia.org.hk/en/infocenter/press_releases_2.html"
fetch ia_press_zh    "https://www.ia.org.hk/tc/infocenter/press_releases.html"
fetch ia_circ        "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
fetch hkma           "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
fetch hkma_rss       "https://www.hkma.gov.hk/eng/rss/press-release.xml"
fetch iaasia         "https://insuranceasia.com/rss.xml"
fetch ibm            "https://www.insurancebusinessmag.com/asia/rss/"
fetch scmp           "https://www.scmp.com/rss/92/feed"
fetch govhk          "https://www.info.gov.hk/gia/rss/general_zh.xml"
fetch hkfi           "https://www.hkfi.org.hk/en/media-centre/press-release"
fetch artemis        "https://www.artemis.bm/news/feed/"
fetch ian_hk         "https://insuranceasianews.com/country/hong-kong/feed/"
echo "DONE"
