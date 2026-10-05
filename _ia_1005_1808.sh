#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
ia() { # name url
  printf '%-18s ' "$1"
  curl -sL -m 30 --noproxy '*' -A "$UA" -H "Accept-Language: en,zh;q=0.9" -o "$OUT/ia_$1" -w "%{http_code} %{size_download}\n" "$2"
}
ia press.html   "https://www.ia.org.hk/en/infocenter/press_releases.html"
ia sitemap.xml  "https://www.ia.org.hk/sitemap.xml"
ia circ2026.html "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
ia circ_all.html "https://www.ia.org.hk/en/legislative_framework/circulars/index.html"
ia press_list.json "https://www.ia.org.hk/en/infocenter/press_releases.json"
ia newsroom.html "https://www.ia.org.hk/en/infocenter/index.html"
echo "--- grep for json/ajax endpoints in press page ---"
grep -oE '(href|src)="[^"]*\.(json|xml|js)"' "$OUT/ia_press.html" | sort -u | head -40
echo "--- any press release links ---"
grep -oE 'href="[^"]*(press|release|news)[^"]*"' "$OUT/ia_press.html" | sort -u | head -30
echo DONE
