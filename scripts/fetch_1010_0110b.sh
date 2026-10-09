#!/usr/bin/env bash
# 港险情报站 · 直连抓取 2（2026-10-10 01:12）
set -u
D=/Users/leonliang/maoquanqingbao/data/_raw_1010_0110
mkdir -p "$D"; cd "$D"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() {
  key="$1"; url="$2"
  code=$(curl -sSL -m 50 -A "$UA" -o "$key.out" -w '%{http_code}' "$url" || echo ERR)
  echo "$key  http=$code  bytes=$(wc -c < "$key.out" 2>/dev/null | tr -d ' ')"
}
fetch jina_ia_press  "https://r.jina.ai/https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch jina_ia_circ   "https://r.jina.ai/https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
fetch aia            "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases.html"
fetch manulife       "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
fetch prudential     "https://www.prudential.com.hk/tc/about-us/newsroom/"
fetch axa            "https://www.axa.com.hk/zh/news-room/"
fetch sunlife        "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
fetch nfra_news      "https://www.nfra.gov.cn/cn/view/pages/xinwenzixun/xinwenzixun.html"
fetch fstb_other     "https://www.fstb.gov.hk/fsb/tc/business/other_matters/index.html"
echo "DONE-2"
