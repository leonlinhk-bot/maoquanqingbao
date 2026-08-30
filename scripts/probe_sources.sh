#!/bin/bash
# Probe accessibility of insurer/news sources via curl
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
cd /tmp || exit 1
while IFS= read -r u; do
  [ -z "$u" ] && continue
  name=$(echo "$u" | md5 -q | cut -c1-6)
  curl -sL --max-time 20 -A "$UA" "$u" -o "probe_$name.html"
  sz=$(wc -c < "probe_$name.html" | tr -d ' ')
  ti=$(grep -o '<title>[^<]*' "probe_$name.html" | head -1)
  echo "== $u"
  echo "   size=$sz title=$ti"
done <<'URLS'
https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html
https://www.prudential.com.hk/tc/about-us/newsroom/
https://www.axa.com.hk/zh/news-room/
https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/
https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/
https://www.insurancebusinessmag.com/asia/news/breaking-news/
https://www.nfra.gov.cn/
https://www.fstb.gov.hk/en/
https://www.ia.org.hk/en/infocenter/press_releases.html
URLS
