#!/bin/bash
# Bing News RSS search for canonical URLs
cd /tmp || exit 1
bfetch() {
  local q="$1" out="$2"
  curl -s --max-time 25 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36" \
    --get "https://www.bing.com/news/search" --data-urlencode "q=$q" --data-urlencode "format=rss" --data-urlencode "mkt=zh-HK" -o "$out"
  echo "$out $(wc -c < "$out" | tr -d ' ')"
}
bfetch "宏利 蔡尚琴 亞洲股市" bing_manu.xml
bfetch "友邦業績強勁 翹楚地位不變" bing_aia.xml
bfetch "許正宇 黃金交易中心 貨銀兩訖" bing_gold.xml
bfetch "永明 AI 工具 顧問" bing_sun.xml
bfetch "保險業監管局 香港" bing_ia.xml
