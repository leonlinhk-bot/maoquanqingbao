#!/usr/bin/env bash
# 1029 00:30 采集：批量拉取原始页面到缓存目录
set -u
D=~/maoquanqingbao/.cache1029_0030
mkdir -p "$D"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

fetch() {
  local name="$1" url="$2"
  local code
  code=$(curl -sS -L -m 45 -A "$UA" -o "$D/$name.raw" -w '%{http_code}' "$url" 2>"$D/$name.err")
  local sz
  sz=$(wc -c < "$D/$name.raw" 2>/dev/null | tr -d ' ')
  echo "$name	$code	${sz:-0}	$url"
}

fetch hkma_press     "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
fetch hkma_rss       "https://www.hkma.gov.hk/eng/rss/press-releases.xml"
fetch govhk_zh       "https://www.info.gov.hk/gia/rss/general_zh.xml"
fetch insuranceasia  "https://insuranceasia.com/insurance"
fetch ibm_asia       "https://www.insurancebusinessmag.com/asia/news/breaking-news/"
fetch ian_hk         "https://insuranceasianews.com/country/hong-kong/feed/"
fetch reinsnews      "https://www.reinsurancenewsnet.com/feed/"
fetch artemis        "https://www.artemis.bm/news/"
fetch scmp_ins       "https://www.scmp.com/topics/insurance"
fetch hkfi           "https://www.hkfi.org.hk/en/media-centre/press-release"
echo "--- done ---"
