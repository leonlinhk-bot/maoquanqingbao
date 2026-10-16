#!/usr/bin/env bash
# 港险情报站 · 增量抓取（2026-10-17 00:48 补跑，窗口起点 2026-10-16T18:08）
set -u
D=/Users/leonliang/maoquanqingbao/data/_1017_0048
mkdir -p "$D"; cd "$D"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() {
  key="$1"; url="$2"
  code=$(curl -sSL -m 40 -A "$UA" -o "$key.out" -w '%{http_code}' "$url" || echo ERR)
  echo "$key  http=$code  bytes=$(wc -c < "$key.out" 2>/dev/null | tr -d ' ')"
}
fetch ia_press    "https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch ia_circ     "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
fetch hkma        "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
fetch iaasia      "https://insuranceasia.com/rss.xml"
fetch ibm         "https://www.insurancebusinessmag.com/asia/rss/"
fetch scmp        "https://www.scmp.com/rss/92/feed"
fetch govhk       "https://www.info.gov.hk/gia/rss/general_zh.xml"
fetch hkfi        "https://www.hkfi.org.hk/en/media-centre/press-release"
fetch artemis     "https://www.artemis.bm/news/feed/"
fetch ian         "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=16"
fetch reinsnews   "https://www.reinsurancene.ws/feed/"
fetch air         "https://www.asiainsurancereview.com/rss"
fetch aia         "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/"
fetch manulife    "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
fetch prudential  "https://www.prudential.com.hk/tc/about-us/newsroom/"
fetch axa         "https://www.axa.com.hk/zh/news-room/"
fetch sunlife     "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
fetch nfra        "https://www.nfra.gov.cn/cn/view/pages/index/index.html"
fetch trustre     "https://www.trust.org/hk/en/newsroom"
echo "DONE"
