#!/usr/bin/env bash
mkdir -p .cache1013_2108
cd .cache1013_2108
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() { # name url
  code=$(curl -sL -m 30 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null)
  echo "$1 $code $(wc -c < "$1" | tr -d ' ')"
}
fetch ian.json "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=25&_fields=id,date,link,title,excerpt" &
fetch ibm.html "https://www.insurancebusinessmag.com/asia/news/breaking-news/" &
fetch artemis.html "https://www.artemis.bm/news/" &
fetch iaa.html "https://www.asiainsurancereview.com/News/Latest-News" &
fetch hkma.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/" &
fetch ia_press.html "https://www.ia.org.hk/en/infocenter/press_releases.html" &
fetch ia_circ.html "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html" &
fetch iaasia.xml "https://insuranceasia.com/rss.xml" &
fetch scmp.xml "https://www.scmp.com/rss/92/feed" &
fetch govhk.xml "https://www.info.gov.hk/gia/rss/general_zh.xml" &
wait
echo done
