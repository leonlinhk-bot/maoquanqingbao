#!/usr/bin/env bash
mkdir -p .cache1014_0058
cd .cache1014_0058
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  code=$(curl -sL -m 40 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null)
  echo "$1 $code $(wc -c < "$1" | tr -d ' ')"
}
fetch art_verisk.html "https://www.artemis.bm/news/verisk-estimates-hurricane-isaias-insured-onshore-property-losses-in-1bn-to-2bn-range/" &
fetch ia_pr_zh.html "https://www.ia.org.hk/tc/infocenter/press_releases.html" &
fetch ia_pr_json.json "https://www.ia.org.hk/api/press_releases?lang=en" &
fetch ia_sitemap.xml "https://www.ia.org.hk/sitemap.xml" &
fetch ins_business_asia.html "https://www.insurancebusinessmag.com/asia/news/" &
fetch hkma_rss.xml "https://www.hkma.gov.hk/eng/news-and-media/press-releases/rss/" &
fetch lifehk.html "https://www.hklife.org.hk/" &
fetch mpfa.html "https://www.mpfa.org.hk/en/" &
wait
echo done
