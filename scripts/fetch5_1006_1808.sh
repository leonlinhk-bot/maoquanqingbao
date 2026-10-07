#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1006_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
bs() { # name query
  curl -sSL --noproxy '*' --max-time 40 -A "$UA" -H "Accept-Language: zh-HK,zh;q=0.9,en;q=0.8" \
    --data-urlencode "q=$2" -G "https://www.bing.com/search" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
bs bing_bochk.html "中銀香港 線上人壽保險 新造保費 七成"
bs bing_mpfa.html "積金局 股票基金 10.3% 過去12個月 回報"
bs bing_aia.html "友邦香港 Z世代 MPF 投資組合 虛擬投資比賽"
bs bing_hsbc.html "金管局 滙豐 新加坡 AI中心 質問"
bs bing_fo.html "陳德翹 家族辦公室 跨境理財 監管 三大動力"
bs bing_nfra.html "金融監管總局 科技保險 政策紅利"
echo DONE
