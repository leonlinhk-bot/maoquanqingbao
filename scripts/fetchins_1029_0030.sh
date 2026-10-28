#!/usr/bin/env bash
set -u
D=~/maoquanqingbao/.cache1029_0030/ins
mkdir -p "$D"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
get() {
  local name="$1" url="$2"
  local code
  code=$(curl -sS -L -m 35 -A "$UA" -o "$D/$name.html" -w '%{http_code}' "$url" 2>/dev/null)
  echo "$name	$code	$(wc -c < "$D/$name.html" 2>/dev/null | tr -d ' ')"
}
get aia "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/"
get manulife "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
get prudential "https://www.prudential.com.hk/tc/about-us/newsroom/"
get axa "https://www.axa.com.hk/zh/news-room/"
get sunlife "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
get nfra "https://www.nfra.gov.cn/cn/view/pages/index/index.html"
get hkfi_home "https://www.hkfi.org.hk/en/"
echo "--- done ---"
