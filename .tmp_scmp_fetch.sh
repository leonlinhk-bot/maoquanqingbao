#!/usr/bin/env bash
# Fetch SCMP articles + IA sitemap pieces
set -u
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
cd /Users/leonliang/maoquanqingbao
mkdir -p .tmp/scmp0826
for id in 3364844 3364710 3364620 3364575 3364040 3363969 3363951; do
  curl -sL --max-time 25 -A "$UA" "https://www.scmp.com/business/article/$id" -o ".tmp/scmp0826/$id.html" &
done
wait
echo "SCMP fetched:"
for id in 3364844 3364710 3364620 3364575 3364040 3363969 3363951; do echo "$id $(wc -c < .tmp/scmp0826/$id.html)"; done
# insuranceasia sitemap index
curl -sL --max-time 25 -A "$UA" "https://insuranceasia.com/sitemap.xml" -o .tmp/iaa_sitemap.xml
grep -o '<loc>[^<]*</loc>' .tmp/iaa_sitemap.xml | head -20
