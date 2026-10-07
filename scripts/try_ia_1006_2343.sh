#!/bin/bash
cd /Users/leonliang/maoquanqingbao
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
try() {
  curl -sSL --max-time 25 -A "$UA" -o "/tmp/ia_try_$1" -w "%{http_code} %{size_download} %{url_effective}\n" "$2"
}
try press.html  "https://www.ia.org.hk/en/infocenter/press_releases.html"
try y2026.html  "https://www.ia.org.hk/en/infocenter/press_releases/2026.html"
try whatsnew.html "https://www.ia.org.hk/en/infocenter/whats_new.html"
try rss.xml     "https://www.ia.org.hk/en/infocenter/press_releases.rss"
try news.html   "https://www.ia.org.hk/en/infocenter/index.html"
echo "--- done"
head -c 260 /tmp/ia_try_press.html
