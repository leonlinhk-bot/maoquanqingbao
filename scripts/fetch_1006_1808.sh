#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1006_1808
mkdir -p $OUT
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() { # name url
  curl -sSL --noproxy '*' --max-time 45 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
fetch ia_press.html "https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch ia_circ.html "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
fetch hkma_press.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
fetch insuranceasia.rss "https://insuranceasia.com/rss.xml"
fetch ian.json "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=12"
fetch ibm_asia.html "https://www.insurancebusinessmag.com/asia/news/breaking-news/"
fetch scmp_ins.rss "https://www.scmp.com/rss/92/feed"
fetch hkfi.html "https://www.hkfi.org.hk/en/media-centre/press-release"
fetch artemis.html "https://www.artemis.bm/news/"
fetch nfra_list.html "https://www.nfra.gov.cn/cn/view/pages/index/index.html"
fetch govhk_zh.xml "https://www.info.gov.hk/gia/rss/general_zh.xml"
echo "DONE"
