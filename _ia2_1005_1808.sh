#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
echo "--- sitemap: press-ish locs ---"
grep -oE '<loc>[^<]*(press|media|news|release)[^<]*</loc>' "$OUT/ia_sitemap.xml" | sort -u | head -40
echo "--- last 10 locs in sitemap (order) ---"
grep -oE '<loc>[^<]*</loc>' "$OUT/ia_sitemap.xml" | tail -10
echo "--- fetch function.js ---"
curl -sL -m 30 --noproxy '*' -A "$UA" -o "$OUT/ia_function.js" -w "%{http_code} %{size_download}\n" "https://www.ia.org.hk/en/infocenter/js/function.js"
echo "--- grep press/ajax in function.js ---"
grep -noE '"[^"]*\.(json|xml|html)[^"]*"' "$OUT/ia_function.js" | head -30
echo "--- try media centre pages ---"
for u in "https://www.ia.org.hk/en/infocenter/media_centre.html" "https://www.ia.org.hk/en/infocenter/press_releases_2026.html" "https://www.ia.org.hk/en/infocenter/press_releases/index.html"; do
  printf '%-70s ' "$u"; curl -sL -m 20 --noproxy '*' -A "$UA" -o /dev/null -w "%{http_code}\n" "$u"
done
echo DONE
