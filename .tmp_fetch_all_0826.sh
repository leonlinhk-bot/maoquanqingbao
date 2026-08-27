#!/usr/bin/env bash
# Fetch all newsroom pages + GNews RSS sweeps into .tmp/
set -u
cd "$(dirname "$0")/.."
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
mkdir -p .tmp/scan0826

fetch() {
  local url="$1" out="$2"
  curl -sL --max-time 30 -A "$UA" "$url" -o "$out"
  echo "$(wc -c < "$out" 2>/dev/null || echo 0) $out  <-  $url"
}

# --- newsrooms ---
fetch "https://www.aia.com.hk/en/about-aia/about-us/media-centre/press-releases" .tmp/scan0826/aia.html &
fetch "https://www.prudential.com.hk/en/about-us/newsroom/" .tmp/scan0826/pru.html &
fetch "https://www.axa.com.hk/en/news-room" .tmp/scan0826/axa.html &
fetch "https://www.sunlife.com.hk/en/about-us/newsroom/news-releases/" .tmp/scan0826/sunlife.html &
fetch "https://insuranceasia.com/insurance" .tmp/scan0826/iaa.html &
fetch "https://www.insurancebusinessmag.com/asia/news/breaking-news/" .tmp/scan0826/ibm.html &
fetch "https://www.scmp.com/topics/insurance" .tmp/scan0826/scmp.html &
fetch "https://www.fstb.gov.hk/en/" .tmp/scan0826/fstb.html &
wait
echo "--- GNews RSS ---"
gnews() {
  local q="$1" out="$2"
  curl -sL --max-time 25 -A "Mozilla/5.0" "https://news.google.com/rss/search?q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&hl=en-US&gl=US&ceid=US:en" -o "$out"
  echo "$(wc -c < "$out" 2>/dev/null || echo 0) $out"
}
gnews "Hong Kong insurance when:2d" .tmp/scan0826/g_hk_ins.xml &
gnews "site:ia.org.hk when:4d" .tmp/scan0826/g_ia.xml &
gnews "site:hkma.gov.hk when:4d" .tmp/scan0826/g_hkma.xml &
gnews "site:insuranceasia.com when:4d" .tmp/scan0826/g_iaa.xml &
gnews "site:insurancebusinessmag.com when:4d" .tmp/scan0826/g_ibm.xml &
gnews "AIA OR Manulife OR Prudential OR \"Sun Life\" OR AXA insurance when:2d" .tmp/scan0826/g_insurers.xml &
gnews "香港 保險 when:2d" .tmp/scan0826/g_zh_ins.xml &
gnews "香港 保險業監管局 when:4d" .tmp/scan0826/g_ia_zh.xml &
gnews "國家金融監督管理總局 when:2d" .tmp/scan0826/g_nfra.xml &
gnews "香港 家族辦公室 when:2d" .tmp/scan0826/g_fam.xml &
gnews "insurtech Asia when:2d" .tmp/scan0826/g_insurtech.xml &
gnews "Hong Kong life insurance when:2d" .tmp/scan0826/g_hlife.xml &
wait
echo "ALL DONE"
