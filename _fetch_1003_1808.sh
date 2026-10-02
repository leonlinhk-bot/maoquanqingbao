#!/bin/bash
cd /Users/leonliang/maoquanqingbao
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
curl -s -m 30 -A "$UA" "https://www.ia.org.hk/en/infocenter/press_releases.html" -o /tmp/ia_pr.html -w "ia_pr:%{http_code}\n"
curl -s -m 30 -A "$UA" "https://www.scmp.com/rss/92/feed" -o /tmp/scmp.xml -w "scmp:%{http_code}\n"
curl -s -m 30 -A "$UA" "https://www.info.gov.hk/gia/rss/general_zh.xml" -o /tmp/govhk.xml -w "govhk:%{http_code}\n"
curl -s -m 30 -A "$UA" "https://www.fstb.gov.hk/en/rss/press.xml" -o /tmp/fstb.xml -w "fstb:%{http_code}\n"
grep -o -E "(0[1-9]|[12][0-9]|3[01]) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) 2026" /tmp/ia_pr.html | head -20
echo "--- ia_pr size ---"
wc -c /tmp/ia_pr.html /tmp/scmp.xml /tmp/govhk.xml /tmp/fstb.xml
