#!/usr/bin/env bash
mkdir -p .cache1012_1818
cd .cache1012_1818
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() { # name url
  code=$(curl -sL -m 25 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null)
  echo "$1 $code $(wc -c < "$1" | tr -d ' ')"
}
fetch iaasia.xml "https://insuranceasia.com/rss.xml" &
fetch ian.json "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=20&_fields=id,date,link,title,excerpt" &
fetch ibm.html "https://www.insurancebusinessmag.com/asia/news/breaking-news/" &
fetch hkma.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/" &
fetch ia_press.html "https://www.ia.org.hk/en/infocenter/press_releases.html" &
fetch artemis.html "https://www.artemis.bm/news/" &
fetch scmp.xml "https://www.scmp.com/rss/92/feed" &
wait
echo done
