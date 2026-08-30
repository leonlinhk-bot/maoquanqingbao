#!/bin/bash
cd /tmp || exit 1
# Yahoo HK finance search for HKET reposts
curl -s --max-time 50 "https://r.jina.ai/https://hk.finance.yahoo.com/search?q=%E8%94%A1%E5%B0%9A%E7%90%B4" -o j_yahoo_manu.txt
echo "yahoo_manu $(wc -c < j_yahoo_manu.txt | tr -d ' ')"
# Baidu News
curl -s --max-time 30 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36" \
  --get "https://www.baidu.com/s" --data-urlencode "tn=news" --data-urlencode "word=蔡尚琴 宏利 亚洲股市" -o baidu_manu.html
echo "baidu_manu $(wc -c < baidu_manu.html | tr -d ' ')"
curl -s --max-time 30 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36" \
  --get "https://www.baidu.com/s" --data-urlencode "tn=news" --data-urlencode "word=友邦業績強勁 翹楚地位" -o baidu_aia.html
echo "baidu_aia $(wc -c < baidu_aia.html | tr -d ' ')"
# Sun Life AI article for timestamp
curl -s --max-time 50 "https://r.jina.ai/https://n.yam.com/Article/20260830515957" -o j_yam_sun.txt
echo "yam_sun $(wc -c < j_yam_sun.txt | tr -d ' ')"
