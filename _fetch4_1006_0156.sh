#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
O=/Users/leonliang/maoquanqingbao/data/_cache1006_0156
g() { curl -sL -m 30 -A "$UA" -o "$O/$1" -w "$1 %{http_code} " "$2"; wc -c < "$O/$1" | tr -d ' '; }
g air_news.html   "https://www.asiainsurancereview.com/News"
g reinasia.html   "https://www.reinasia.com/"
g fintechg.html   "https://www.fintech.global/category/insurtech/"
g iaasia_home.html "https://www.insuranceasia.com/"
g nfra_api1.json  "https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectByConditionPage_1.json"
g nfra_api2.json  "https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=923&itemId=931"
echo DONE
