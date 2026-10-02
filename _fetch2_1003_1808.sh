#!/bin/bash
cd /Users/leonliang/maoquanqingbao
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
echo "--- SCMP rss 92 -L ---"
curl -sL -m 30 -A "$UA" "https://www.scmp.com/rss/92/feed" -o /tmp/scmp92.xml -w "%{http_code} %{size_download}\n"
echo "--- NFRA ItemList ---"
curl -s -m 30 -A "$UA" -H "Referer: https://www.nfra.gov.cn/" "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=915&itemUrl=ItemListRightList.html&itemName=%E7%9B%91%E7%AE%A1%E5%8A%A8%E6%80%81" -o /tmp/nfra_list.html -w "%{http_code} %{size_download}\n"
echo "--- NFRA docinfo json ---"
curl -s -m 30 -A "$UA" -H "Referer: https://www.nfra.gov.cn/" "https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectByConditionPage_1.json" -o /tmp/nfra_api.json -w "%{http_code} %{size_download}\n"
echo "--- IA pr ---"
curl -s -m 30 -A "$UA" -H "Accept-Language: en" "https://www.ia.org.hk/en/infocenter/press_releases.html" -o /tmp/ia_pr2.html -w "%{http_code} %{size_download}\n"
echo "--- IA 2026 pr page ---"
curl -s -m 30 -A "$UA" "https://www.ia.org.hk/en/infocenter/press_releases_2026.html" -o /tmp/ia_pr26.html -w "%{http_code} %{size_download}\n"
head -c 500 /tmp/nfra_api.json
