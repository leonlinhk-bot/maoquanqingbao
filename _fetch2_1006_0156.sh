#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
O=/Users/leonliang/maoquanqingbao/data/_cache1006_0156
g() { curl -sL -m 30 -A "$UA" -o "$O/$1" -w "$1 %{http_code} " "$2"; wc -c < "$O/$1" | tr -d ' '; }
g gn_ia.xml "https://news.google.com/rss/search?q=Insurance+Authority+Hong+Kong+when:3d&hl=en-HK&gl=HK&ceid=HK:en"
g gn_ia_zh.xml "https://news.google.com/rss/search?q=%E4%BF%9D%E7%9B%91%E5%B1%80+when:3d&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
g gn_hk_ins.xml "https://news.google.com/rss/search?q=%E9%A6%99%E6%B8%AF%E4%BF%9D%E9%99%A9+when:2d&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
g gn_manulife.xml "https://news.google.com/rss/search?q=Manulife+Hong+Kong+when:7d&hl=en-HK&gl=HK&ceid=HK:en"
g gn_fam.xml "https://news.google.com/rss/search?q=%E5%AE%B6%E6%97%8F%E8%BE%A6%E5%85%AC%E5%AE%A4+when:3d&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
g gn_insurtech.xml "https://news.google.com/rss/search?q=insurtech+when:3d&hl=en-HK&gl=HK&ceid=HK:en"
g hkfi2.html "https://www.hkfi.org.hk/en/media-centre/press-releases"
g manulife2.html "https://www.manulife.com.hk/en/individual/about/newsroom.html"
echo DONE
