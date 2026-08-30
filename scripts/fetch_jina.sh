#!/bin/bash
# Fetch JS-rendered source pages via r.jina.ai proxy
cd /tmp || exit 1
jfetch() {
  local url="$1" out="$2"
  curl -s --max-time 45 "https://r.jina.ai/$url" -o "$out"
  echo "$out $(wc -c < "$out" | tr -d ' ')"
}
jfetch "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html" j_manu.txt
jfetch "https://www.prudential.com.hk/tc/about-us/newsroom/" j_pru.txt
jfetch "https://www.axa.com.hk/zh/news-room/" j_axa.txt
jfetch "https://www.fstb.gov.hk/en/" j_fstb.txt
jfetch "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/" j_aia.txt
