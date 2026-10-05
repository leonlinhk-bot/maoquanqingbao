#!/usr/bin/env bash
# 1005 18:08 fetch — direct curl with browser UA
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
mkdir -p "$OUT"
fetch() { # name url
  code=$(curl -sL -m 25 -A "$UA" -H "Accept-Language: en,zh;q=0.8" -o "$OUT/$1" -w "%{http_code}" "$2" || echo ERR)
  echo "$1 $code $(wc -c < "$OUT/$1" | tr -d ' ')"
}
fetch ia_press.html      "https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch ia_circ2026.html   "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
fetch hkma_press.html    "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
fetch insuranceasia.xml  "https://insuranceasia.com/rss.xml"
fetch ian.json           "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=20"
fetch artemis.html       "https://www.artemis.bm/news/"
fetch ibm.html           "https://www.insurancebusinessmag.com/asia/news/breaking-news/"
fetch aia.html           "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases.html"
fetch manulife.html      "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
fetch prudential.html    "https://www.prudential.com.hk/tc/about-us/newsroom/"
fetch axa.html           "https://www.axa.com.hk/zh/news-room"
fetch sunlife.html       "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
fetch govhk_zh.xml       "https://www.info.gov.hk/gia/rss/general_zh.xml"
fetch hkfi.html          "https://www.hkfi.org.hk/en/media-centre/press-release"
fetch nfra.html          "https://www.nfra.gov.cn/cn/view/pages/index/index.html"
echo "DONE $OUT"
