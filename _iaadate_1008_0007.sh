#!/bin/bash
cd /Users/leonliang/maoquanqingbao/.tmp/1008_0007
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
mkdir -p iaa
slugs="
insurance/news/aon-strengthens-japan-network-two-leadership-appointments
insurance/news/zurich-completes-beazley-deal-build-specialty-giant
insurance/news/msig-extends-fire-cover-over-300-orang-asli-homes
insurance/news/allianz-reshuffles-ceos-after-kunzmann-board-move
insurance/news/markel-moves-energy-underwriter-singapore
"
for s in $slugs; do
  n=$(echo "$s" | tr '/' '_')
  f="iaa/${n}.html"
  code=$(curl -sL -m 25 -A "$UA" -o "$f" -w "%{http_code}" "https://insuranceasia.com/$s")
  echo "== $s code=$code size=$(wc -c < "$f" | tr -d ' ')"
  grep -oE '"(datePublished|dateModified)": *"[^"]+"' "$f" | head -3
  grep -oE '(2026-10-[0-9]{2}T[0-9]{2}:[0-9]{2})' "$f" | head -3
done
