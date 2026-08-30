#!/bin/bash
cd /tmp || exit 1
bfetch() {
  local q="$1" out="$2"
  curl -s --max-time 25 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36" \
    --get "https://www.bing.com/news/search" --data-urlencode "q=$q" --data-urlencode "format=rss" --data-urlencode "mkt=zh-HK" -o "$out"
  echo "$out $(wc -c < "$out" | tr -d ' ')"
}
bfetch "\"友邦業績強勁\" 翹楚地位" bing_aia2.xml
bfetch "\"蔡尚琴\"" bing_manu2.xml
bfetch "\"友邦長期收息之選\"" bing_aia3.xml
