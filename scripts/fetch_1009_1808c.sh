#!/usr/bin/env bash
set -u
cd /Users/leonliang/maoquanqingbao/data/_raw_1009_1808
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() { key="$1"; url="$2"; code=$(curl -sSL -m 40 -A "$UA" -o "$key.out" -w '%{http_code}' "$url"); echo "$key http=$code bytes=$(wc -c < "$key.out" | tr -d ' ')"; }
fetch nfra_news "https://www.nfra.gov.cn/cn/view/pages/xinwenzixun/xinwenzixun.html"
fetch fstb_other "https://www.fstb.gov.hk/fsb/tc/business/other_matters/index.html"
fetch ian_blkswan "https://insuranceasianews.com/insurers-urged-to-step-up-as-risk-managers-confront-flock-of-black-swans/"
echo DONE3
