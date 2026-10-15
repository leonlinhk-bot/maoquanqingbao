#!/usr/bin/env bash
# round 2: insurers + media topic pages
set -u
D=/Users/leonliang/maoquanqingbao/data/_1016_0029
cd "$D"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() {
  key="$1"; url="$2"
  code=$(curl -sSL -m 30 -A "$UA" -o "r2_$key.out" -w '%{http_code}' "$url" || echo ERR)
  echo "$key  http=$code  bytes=$(wc -c < "r2_$key.out" 2>/dev/null | tr -d ' ')"
}
fetch aia        "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/"
fetch prudential "https://www.prudential.com.hk/tc/about-us/newsroom/"
fetch manulife   "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
fetch axa        "https://www.axa.com.hk/zh/news-room/"
fetch sunlife    "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
fetch gia        "https://www.gia.org.hk/en/media_centre/press_releases.php"
fetch boclife    "https://www.boclife.com.hk/tc/about-us/press-release.html"
fetch fwd        "https://www.fwd.com.hk/zh-hk/about-fwd/media-centre/"
fetch hsbc       "https://www.hsbc.com.hk/insurance/about-us/media/"
fetch scmp_topic "https://www.scmp.com/topics/insurance"
fetch iaasia_web "https://insuranceasia.com/insurance/news"
fetch hkfi_med   "https://www.hkfi.org.hk/en/media-centre/press-release/"
echo DONE-2
