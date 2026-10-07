#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1007_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  curl -sSL --noproxy '*' --max-time 40 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
fetch art_pru_japan.html "https://insuranceasianews.com/japan-watchdog-moves-to-suspend-prudential-life-insurance-over-fraud-scandal/"
fetch art_asic.html "https://insuranceasianews.com/australian-regulator-flags-disaster-chasers-code-of-practice-overhaul-as-2026-27-insurance-priorities/"
fetch art_india_div.html "https://insuranceasianews.com/indian-regulator-eases-dividend-distribution-rules-for-foreign-owned-brokers/"
fetch art_iag.html "https://insuranceasianews.com/iag-to-seek-public-benefits-approval-after-accc-halts-rac-insurance-acquisition/"
fetch art_hdiasia.html "https://insuranceasianews.com/asia-emerges-as-international-programs-hub-as-regional-firms-centralise-risk-management-hdi-global/"
echo DONE
