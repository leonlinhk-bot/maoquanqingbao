#!/usr/bin/env bash
set -u
D=/Users/leonliang/maoquanqingbao/data/_1016_0029
cd "$D"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'
fetch() {
  key="$1"; url="$2"
  code=$(curl -sSL -m 30 -A "$UA" -o "a_$key.html" -w '%{http_code}' "$url" || echo ERR)
  echo "$key  http=$code  bytes=$(wc -c < "a_$key.html" 2>/dev/null | tr -d ' ')"
}
fetch stand   "https://www.artemis.bm/news/stand-hires-former-nephila-exec-landi-as-cfo-raises-70-million-series-c/"
fetch sidecar "https://www.artemis.bm/news/marsh-ceo-flags-client-interest-in-casualty-sidecars-notes-reinsurance-market-softening/"
fetch rn_ai   "https://www.reinsurancene.ws/marsh-leans-into-ai-growth-but-warns-of-systemic-cyber-exposure-ceo-doyle/"
fetch rn_aces "https://www.reinsurancene.ws/acics-aces-specialty-insurance-company-gets-approval-to-underwrite-es-insurance/"
fetch rn_ant  "https://www.reinsurancene.ws/antares-global-names-meera-raju-oakley-as-chief-actuary-of-commercial/"
fetch rn_brit "https://www.reinsurancene.ws/james-winn-appointed-cuo-and-head-of-office-brit-re-bermuda/"
fetch ian_marsh "https://insuranceasianews.com/marsh-to-pay-largest-share-of-us800m-credit-suisse-greensill-settlement-ft/"
fetch ibm_marsh "https://www.insurancebusinessmag.com/asia/news/breaking-news/marsh-revenue-rises-8-as-consulting-growth-offsets-reinsurance-decline-593667.aspx"
echo DONE-3
