#!/bin/bash
cd /Users/leonliang/maoquanqingbao
D=data/_jina_1004_2108
mkdir -p "$D"
jfetch() {
  local url="$1" out="$2"
  curl -s --max-time 60 "https://r.jina.ai/$url" -o "$D/$out"
  echo "$out $(wc -c < "$D/$out" | tr -d ' ')"
}
jfetch "https://www.ia.org.hk/en/infocenter/press_releases.html" ia_press.txt
jfetch "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html" ia_circ.txt
jfetch "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html" manu.txt
jfetch "https://www.hkfi.org.hk/en/media-centre/press-release" hkfi.txt
