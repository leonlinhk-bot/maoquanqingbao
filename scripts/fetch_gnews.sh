#!/bin/bash
# Batch fetch Google News RSS for the 14-source coverage (search fallback)
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"
cd /tmp || exit 1
fetch() {
  local q="$1" out="$2"
  curl -s --max-time 25 -A "$UA" --get "https://news.google.com/rss/search" \
    --data-urlencode "q=$q" --data-urlencode "hl=zh-HK" --data-urlencode "gl=HK" --data-urlencode "ceid=HK:zh-Hant" \
    -o "$out"
  echo "$out $(wc -c < "$out" | tr -d ' ')"
}
fetch "香港保监局 when:2d" gnews_ia.txt
fetch "保險業監管局 when:2d" gnews_ia2.txt
fetch "香港保險 when:1d" gnews_hk.txt
fetch "hong kong insurance when:2d" gnews_en.txt
fetch "金融監管總局 when:1d" gnews_nfra.txt
fetch "家族辦公室 when:2d" gnews_fam.txt
fetch "AIA 友邦 when:2d" gnews_aia.txt
fetch "保誠 保險 when:2d" gnews_pru.txt
fetch "宏利 when:1d" gnews_manu.txt
fetch "AXA 安盛 when:2d" gnews_axa.txt
fetch "永明 保險 when:2d" gnews_sun.txt
fetch "insurtech asia when:2d" gnews_insurtech.txt
fetch "insurance asia news when:2d" gnews_iasia.txt
fetch "保險科技 when:2d" gnews_insurtech2.txt
