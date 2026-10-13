#!/usr/bin/env bash
set -u
cd /Users/leonliang/maoquanqingbao
mkdir -p .cache1014_0245
cd .cache1014_0245
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
U="https://www.artemis.bm/news/verisk-estimates-hurricane-isaias-insured-onshore-property-losses-in-1bn-to-2bn-range/"
code=$(curl -sL -m 35 -A "$UA" -o verisk.html -w "%{http_code}" "$U")
echo "direct: $code $(wc -c < verisk.html)"
code=$(curl -sL -m 40 -A "$UA" -o verisk_jina.txt -w "%{http_code}" "https://r.jina.ai/$U")
echo "jina: $code $(wc -c < verisk_jina.txt)"
