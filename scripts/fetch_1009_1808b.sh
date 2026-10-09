#!/usr/bin/env bash
set -u
cd /Users/leonliang/maoquanqingbao/data/_raw_1009_1808
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() { key="$1"; url="$2"; code=$(curl -sSL -m 45 -A "$UA" -o "$key.out" -w '%{http_code}' "$url"); echo "$key http=$code bytes=$(wc -c < "$key.out" | tr -d ' ')"; }

fetch jina_ia_press   "https://r.jina.ai/https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch jina_ia_circ    "https://r.jina.ai/https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
fetch aia             "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases.html"
fetch manulife        "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
fetch prudential      "https://www.prudential.com.hk/tc/about-us/newsroom/"
fetch axa             "https://www.axa.com.hk/zh/news-room/"
fetch sunlife         "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
fetch nfra            "https://www.nfra.gov.cn/cn/view/pages/index/index.html"
echo DONE2
