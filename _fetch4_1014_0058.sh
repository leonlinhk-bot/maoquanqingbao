#!/usr/bin/env bash
mkdir -p .cache1014_0058
cd .cache1014_0058
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  code=$(curl -sL -m 40 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null)
  echo "$1 $code $(wc -c < "$1" | tr -d ' ')"
}
fetch iaasia_news.html "https://insuranceasia.com/insurance/news" &
fetch sunlife2026.html "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/" &
fetch hkfi_ml.html "https://www.hkfi.org.hk/en/media-centre/media-release" &
fetch hkfi_ml2.html "https://www.hkfi.org.hk/media-centre/media-release" &
fetch aia_zh.html "https://www.aia.com.hk/zh-hk/about-aia/media-centre/press-releases" &
wait
echo done
