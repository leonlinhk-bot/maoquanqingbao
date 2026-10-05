#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
probe() { # label url
  printf '%-22s ' "$1"
  curl -sL -m 40 -A "$UA" -o "$OUT/x_$1" -w "%{http_code} %{size_download}\n" "$2"
}
IA="https://www.ia.org.hk/en/infocenter/press_releases.html"
MANU="https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
probe codetabs_ia  "https://api.codetabs.com/v1/proxy?quest=$IA"
probe allorig_ia   "https://api.allorigins.win/raw?url=$IA"
probe corsproxy_ia "https://corsproxy.io/?$IA"
probe thingproxy_ia "https://thingproxy.freeboard.io/fetch/$IA"
probe textance_ia  "https://api.codetabs.com/v1/proxy?quest=$MANU"
echo "--- content sniff ---"
for f in codetabs_ia allorig_ia corsproxy_ia; do
  echo "## $f"; head -c 300 "$OUT/x_$f"; echo; done
