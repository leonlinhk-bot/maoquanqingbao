#!/bin/bash
cd /Users/leonliang/maoquanqingbao/.tmp/1008_0007
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
f(){
 n=$1; u=$2
 c=$(curl -sL -m 25 -A "$UA" -o "$n" -w "%{http_code}" "$u")
 echo "$n code=$c size=$(wc -c < "$n" | tr -d ' ')"
}
f scmp_rss.xml "https://www.scmp.com/rss/92/feed"
f aia.html  "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/"
f pru.html  "https://www.prudential.com.hk/tc/about-us/newsroom/"
f mlife.html "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
f axa.html  "https://www.axa.com.hk/zh/news-room/"
f sun.html  "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
f hkfi_media.html "https://www.hkfi.org.hk/zh/media-release"
echo done
