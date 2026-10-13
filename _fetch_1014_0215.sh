#!/usr/bin/env bash
set -u
cd /Users/leonliang/maoquanqingbao
mkdir -p .cache1014_0215
cd .cache1014_0215
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  code=$(curl -sL -m 35 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null)
  printf "%-22s %s %s\n" "$1" "$code" "$(wc -c < "$1" | tr -d ' ')"
}
fetch ian.json      "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=20&_fields=id,date,link,title,excerpt"
fetch ibm_rss.xml   "https://www.insurancebusinessmag.com/asia/rss/"
fetch artemis.xml   "https://www.artemis.bm/news/feed/"
fetch iaasia.xml    "https://insuranceasia.com/rss.xml"
fetch hkma.html     "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
fetch govhk.xml     "https://www.info.gov.hk/gia/rss/general_zh.xml"
fetch iaa.html      "https://www.asiainsurancereview.com/News/Latest-News"
fetch scmp.xml      "https://www.scmp.com/rss/92/feed"
fetch hkfi.html     "https://www.hkfi.org.hk/en/media-centre/press-release"
fetch mpfa.html     "https://www.mpfa.org.hk/en/info-centre/press-releases"
fetch nfra.html     "https://www.nfra.gov.cn/cn/view/pages/index/index.html"
echo done
