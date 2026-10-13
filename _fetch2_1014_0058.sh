#!/usr/bin/env bash
mkdir -p .cache1014_0058
cd .cache1014_0058
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  code=$(curl -sL -m 40 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null)
  echo "$1 $code $(wc -c < "$1" | tr -d ' ')"
}
fetch artemis.xml "https://www.artemis.bm/news/feed/" &
fetch ibm_rss.xml "https://www.insurancebusinessmag.com/asia/rss/" &
fetch ibm_rss2.xml "https://www.insurancebusinessmag.com/rss/news" &
fetch iaa_latest.html "https://www.asiainsurancereview.com/News/Latest-News?page=1" &
fetch aia.html "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/" &
fetch manulife.html "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html" &
fetch prudential.html "https://www.prudential.com.hk/tc/about-us/newsroom/" &
fetch axa.html "https://www.axa.com.hk/zh/news-room/" &
fetch sunlife.html "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/" &
fetch hkfi2.html "https://www.hkfi.org.hk/media-release" &
fetch nfra.html "https://www.nfra.gov.cn/cn/view/pages/index/index.html" &
fetch fstb.html "https://www.fstb.gov.hk/en/" &
wait
echo done
