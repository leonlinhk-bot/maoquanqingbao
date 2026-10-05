#!/bin/bash
# quick fetch probe for today's run
OUT=.tmp/run_1006_0156
mkdir -p $OUT
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
probe () {
  code=$(curl -s -m 20 -A "$UA" -o "$OUT/$1.html" -w "%{http_code}" "$2")
  echo "$1 -> $code  bytes=$(wc -c < $OUT/$1.html | tr -d ' ')"
}
probe ia_press "https://www.ia.org.hk/en/infocenter/press_releases.html"
probe ia_circ "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
probe hkma "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
probe insuranceasia "https://insuranceasia.com/rss.xml"
probe insbiz "https://www.insurancebusinessmag.com/asia/news/breaking-news/"
probe scmp "https://www.scmp.com/rss/92/feed"
probe hkfi "https://www.hkfi.org.hk/en/media-centre/press-release"
