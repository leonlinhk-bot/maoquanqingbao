#!/usr/bin/env bash
cd /Users/leonliang/maoquanqingbao/.cache1020_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
curl -sL -m 45 -A "$UA" -o hkma_api.json -w "hkma_api %{http_code} %{size_download}\n" "https://api.hkma.gov.hk/public/press-releases?lang=en&offset=0"
curl -sL -m 45 -A "$UA" -o hkma_api_zh.json -w "hkma_api_zh %{http_code} %{size_download}\n" "https://api.hkma.gov.hk/public/press-releases?lang=zh-hk&offset=0"
curl -sL -m 45 -A "$UA" -o ia_api.json -w "ia_api %{http_code} %{size_download}\n" "https://www.ia.org.hk/en/infocenter/press_releases.html"
