#!/bin/bash
cd /tmp || exit 1
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
# Bing web search (returns direct hket URLs in organic results)
curl -s --max-time 25 -A "$UA" --get "https://www.bing.com/search" \
  --data-urlencode "q=\"宏利\" \"蔡尚琴\" 亞洲股市" -o bingweb_manu.html
echo "bingweb_manu $(wc -c < bingweb_manu.html | tr -d ' ')"
curl -s --max-time 25 -A "$UA" --get "https://www.bing.com/search" \
  --data-urlencode "q=\"友邦業績強勁\" \"翹楚地位\"" -o bingweb_aia.html
echo "bingweb_aia $(wc -c < bingweb_aia.html | tr -d ' ')"
curl -s --max-time 25 -A "$UA" --get "https://www.bing.com/search" \
  --data-urlencode "q=宏利 蔡尚琴 亞洲股市風險回報 site:inews.hket.com OR site:hket.com" -o bingweb_manu2.html
echo "bingweb_manu2 $(wc -c < bingweb_manu2.html | tr -d ' ')"
