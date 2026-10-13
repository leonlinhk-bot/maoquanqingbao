#!/usr/bin/env bash
mkdir -p .cache1014_0058
cd .cache1014_0058
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
curl -sL -m 40 -A "$UA" -o hkfi_zh.html "https://www.hkfi.org.hk/zh/media-release" 2>/dev/null
echo "hkfi_zh.html $(wc -c < hkfi_zh.html | tr -d ' ')"
curl -sL -m 40 -A "$UA" -o hkma2.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/?page=1" 2>/dev/null
echo "hkma2.html $(wc -c < hkma2.html | tr -d ' ')"
curl -sL -m 40 -A "$UA" -o ia_statistics.html "https://www.ia.org.hk/en/infocenter/statistics/market.html" 2>/dev/null
echo "ia_statistics.html $(wc -c < ia_statistics.html | tr -d ' ')"
echo done
