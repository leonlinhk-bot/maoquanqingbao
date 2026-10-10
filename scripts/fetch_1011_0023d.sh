#!/usr/bin/env bash
set -u
D=/Users/leonliang/maoquanqingbao/data/_raw_1011_0023
cd "$D"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() { key="$1"; url="$2"; code=$(curl -sSL -m 40 -A "$UA" -o "$key.out" -w '%{http_code}' "$url" || echo ERR); echo "$key  http=$code  bytes=$(wc -c < "$key.out" 2>/dev/null | tr -d ' ')"; }
fetch ian_home    "https://insuranceasianews.com/"
fetch iaasia_home "https://insuranceasia.com/"
fetch scmp_ins    "https://www.scmp.com/topics/insurance"
fetch scmp_biz_rss "https://www.scmp.com/rss/92/feed"
fetch manulife_alt "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
echo DONE-4
