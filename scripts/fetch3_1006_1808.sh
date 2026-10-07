#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1006_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  curl -sSL --noproxy '*' --max-time 45 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
# Google News RSS (timeliness)
fetch gn_hk_ia.xml "https://news.google.com/rss/search?q=%E4%BF%9D%E9%9A%AA%E6%A5%AD%E7%9B%A3%E7%AE%A1%E5%B1%80+OR+%E4%BF%9D%E7%9B%A3%E5%B1%80&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
fetch gn_hk_ins.xml "https://news.google.com/rss/search?q=%E9%A6%99%E6%B8%AF+%E4%BF%9D%E9%9A%AA&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
fetch gn_hk_fo.xml "https://news.google.com/rss/search?q=%E5%AE%B6%E6%97%8F%E8%BE%A6%E5%85%AC%E5%AE%A4&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
fetch gn_hk_mpf.xml "https://news.google.com/rss/search?q=%E5%BC%B7%E7%A9%8D%E9%87%91&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
fetch gn_en_hkins.xml "https://news.google.com/rss/search?q=Hong+Kong+insurance&hl=en-HK&gl=HK&ceid=HK:en"
fetch gn_cn_ins.xml "https://news.google.com/rss/search?q=%E9%87%91%E8%9E%8D%E7%9B%91%E7%AE%A1%E6%80%BB%E5%B1%80+%E4%BF%9D%E9%99%A9&hl=zh-CN&gl=CN&ceid=CN:zh-Hans"
echo "DONE-GN"
