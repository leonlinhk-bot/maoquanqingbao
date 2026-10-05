#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
for y in 2026 2025; do
  printf 'year=%s ' "$y"
  curl -sL -m 30 --noproxy '*' -A "$UA" -o "$OUT/ia_pr_$y.html" -w "%{http_code} %{size_download}\n" "https://www.ia.org.hk/en/infocenter/press_releases.html?year=$y"
done
echo "--- rows in 2026 ---"
grep -oE '<tr>.{0,400}' "$OUT/ia_pr_2026.html" | head -5
echo DONE
