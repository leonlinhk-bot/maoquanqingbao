#!/usr/bin/env bash
set -u
cd /Users/leonliang/maoquanqingbao
mkdir -p .cache1014_0225
cd .cache1014_0225
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  code=$(curl -sL -m 35 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null)
  printf "%-24s %s %s\n" "$1" "$code" "$(wc -c < "$1" | tr -d ' ')"
}
fetch hkfi_media.html   "https://www.hkfi.org.hk/media-release"
fetch hkfi_en.html      "https://www.hkfi.org.hk/en/media-release"
fetch mpfa.html         "https://www.mpfa.org.hk/en/info-centre/press-releases"
fetch fstb.html         "https://www.fstb.gov.hk/en/"
fetch iaa.html          "https://www.asiainsurancereview.com/News/Latest-News"
fetch sunlife.html      "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
fetch pru.html          "https://www.prudential.com.hk/tc/about-us/newsroom/"
fetch aia.html          "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/"
fetch chinlife.html     "https://www.chinalife.com.hk/zh-hk/about-us/news"
fetch fwd.html          "https://www.fwd.com.hk/zh/newsroom/"
fetch boclife.html      "https://www.boclife.com.hk/tc/about-us/press-release.html"
fetch chubb.html        "https://www.chubb.com/hk-zh/about-chubb/media-center.html"
fetch hsbclife.html     "https://www.hsbc.com.hk/zh-hk/insurance/news/"
echo done
