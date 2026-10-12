#!/usr/bin/env bash
cd /Users/leonliang/maoquanqingbao/.cache1012_1818
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() { code=$(curl -sL -m 25 -A "$UA" -o "$1" -w "%{http_code}" "$2"); echo "$1 $code $(wc -c < "$1" | tr -d ' ')"; }
fetch nfra_rl.html "https://www.nfra.gov.cn/cn/view/pages/ItemListRightList.html?itemPId=923&itemId=915"
fetch nfra_news.html "https://www.nfra.gov.cn/cn/view/pages/xinwenzixun/xinwenzixun.html"
echo done
