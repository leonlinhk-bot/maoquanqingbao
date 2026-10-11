#!/bin/bash
# fetch batch for 2026-10-12 00:22 run
cd /Users/leonliang/maoquanqingbao
D=.tmp/1012_0022
mkdir -p $D
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"

fetch(){
  name=$1; url=$2
  code=$(curl -sL -m 25 -A "$UA" -o "$D/$name" -w "%{http_code}" "$url")
  sz=$(wc -c < "$D/$name" | tr -d ' ')
  echo "$name code=$code size=$sz"
}

fetch ia_press.html      "https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch ia_circular.html   "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters.html"
fetch hkma.html          "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
fetch iaasia.xml         "https://insuranceasia.com/insurance/rss.xml"
fetch iaasia2.xml        "https://insuranceasia.com/rss.xml"
fetch ianews.json        "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=15"
fetch ibm.html           "https://www.insurancebusinessmag.com/asia/news/breaking-news/"
fetch scmp.html          "https://www.scmp.com/topics/insurance"
fetch nfra.html          "https://www.nfra.gov.cn/cn/view/pages/index/index.html"
fetch artemis.html       "https://www.artemis.bm/news/"
fetch hkfi.html          "https://www.hkfi.org.hk/en/media-centre/press-release"
fetch fstb.xml           "https://www.info.gov.hk/gia/rss/general_zh.xml"
fetch aia.html           "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases.html"
fetch manulife.html      "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
fetch prudential.html    "https://www.prudential.com.hk/tc/about-us/newsroom/"
fetch axa.html           "https://www.axa.com.hk/zh/news-room"
fetch sunlife.html       "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
fetch govhk.xml          "https://www.info.gov.hk/gia/rss/general_zh.xml"
echo "--- done ---"
