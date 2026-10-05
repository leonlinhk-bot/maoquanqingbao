#!/usr/bin/env bash
# 1005 18:08 — jina proxy for 403 sources
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
jfetch() { # name url
  code=$(curl -sL -m 60 -A "$UA" -o "$OUT/$1" -w "%{http_code}" "https://r.jina.ai/$2")
  echo "$1 $code $(wc -c < "$OUT/$1" | tr -d ' ')"
}
jfetch j_ia_press.txt   "https://www.ia.org.hk/en/infocenter/press_releases.html"
jfetch j_ia_circ.txt    "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
jfetch j_manulife.txt   "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
jfetch j_hkfi.txt       "https://www.hkfi.org.hk/en/media-centre/press-release/"
echo DONE
