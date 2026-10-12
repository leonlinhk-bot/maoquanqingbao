#!/usr/bin/env bash
mkdir -p .cache1012_1818
cd .cache1012_1818
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  code=$(curl -sL -m 25 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null)
  echo "$1 $code $(wc -c < "$1" | tr -d ' ')"
}
fetch govhk.xml "https://www.info.gov.hk/gia/rss/general_zh.xml" &
fetch nfra.html "https://www.nfra.gov.cn/cn/view/pages/index/index.html" &
fetch aia.html "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/" &
fetch pru.html "https://www.prudential.com.hk/tc/about-us/newsroom/" &
fetch axa.html "https://www.axa.com.hk/zh/news-room/" &
fetch sunlife.html "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/" &
fetch manulife.html "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html" &
fetch hkfi.html "https://www.hkfi.org.hk/en/media-centre/press-release" &
fetch ibm.xml "https://www.insurancebusinessmag.com/asia/rss/" &
fetch fstb.html "https://www.fstb.gov.hk/en/" &
wait
echo done
