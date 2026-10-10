#!/usr/bin/env bash
set -u
D=/Users/leonliang/maoquanqingbao/data/_raw_1011_0023
mkdir -p "$D"; cd "$D"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() {
  key="$1"; url="$2"; shift 2
  code=$(curl -sSL -m 40 -A "$UA" "$@" -o "$key.out" -w '%{http_code}' "$url" || echo ERR)
  echo "$key  http=$code  bytes=$(wc -c < "$key.out" 2>/dev/null | tr -d ' ')"
}
# IA via jina reader
fetch ia_jina_press "https://r.jina.ai/https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch ia_jina_circ  "https://r.jina.ai/https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
# HKMA open API
fetch hkma_api "https://apidocs.hkma.gov.hk/api/press-release?lang=en"
# IBM breaking news page + regional feed
fetch ibm_break "https://www.insurancebusinessmag.com/asia/news/breaking-news/"
fetch ibm_life  "https://www.insurancebusinessmag.com/asia/news/life-insurance/"
fetch ibm_all   "https://www.insurancebusinessmag.com/asia/rss/"
# govhk english rss
fetch govhk_en "https://www.info.gov.hk/gia/rss/general_en.xml"
echo DONE-2
