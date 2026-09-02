#!/usr/bin/env bash
# Fetch Google News RSS for a list of queries
UA="Mozilla/5.0"
declare -a QUERIES=(
  "site:ia.org.hk"
  "site:hkma.gov.hk insurance"
  "AIA Hong Kong"
  "Manulife Hong Kong"
  "Prudential Hong Kong"
  "AXA Hong Kong insurance"
  "Sun Life Hong Kong"
  "Hong Kong insurance regulator"
  "Hong Kong family office"
  "香港保险 保监局"
  "香港保险 友邦 保诚"
  "NFRA insurance China"
  "香港保险科技 insurtech"
)
for q in "${QUERIES[@]}"; do
  fn=$(printf "%s" "$q" | md5 | cut -c1-8)
  enc=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")
  curl -s -m 20 -A "$UA" "https://news.google.com/rss/search?q=${enc}&hl=en-US&gl=US&ceid=US:en" -o "/tmp/g_${fn}.xml"
  sz=$(wc -c < "/tmp/g_${fn}.xml")
  echo "$q -> $sz"
done
