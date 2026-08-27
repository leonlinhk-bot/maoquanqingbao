#!/usr/bin/env bash
set -u
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
cd /Users/leonliang/maoquanqingbao
mkdir -p .tmp/scmp0826b
fetch() {
  local url="$1" out="$2"
  curl -sL --max-time 25 -A "$UA" "$url" -o "$out"
  echo "$(wc -c < "$out") $out"
}
fetch "https://www.scmp.com/business/article/3364040/hong-kongs-insurance-authority-aims-broaden-regional-clientele-base-reappointed-ceo" .tmp/scmp0826b/3364040.html &
fetch "https://www.scmp.com/business/article/3364575/prudential-hong-kong-expands-headquarters-amid-beijings-intensified-wealth-oversight" .tmp/scmp0826b/3364575.html &
fetch "https://www.scmp.com/business/companies/article/3364620/aia-first-half-profit-11-driven-strong-growth-hong-kong-and-asia-sales" .tmp/scmp0826b/3364620.html &
fetch "https://www.scmp.com/business/banking-finance/article/3364844/chinese-insurer-ping-eyes-hong-kong-etfs-beijing-greenlights-cross-border-investment" .tmp/scmp0826b/3364844.html &
fetch "https://www.scmp.com/business/banking-finance/article/3363969/hong-kong-insurers-weather-beijings-tax-shift-8-10-premium-growth-sp" .tmp/scmp0826b/3363969.html &
fetch "https://www.scmp.com/business/banking-finance/article/3363951/hong-kong-reappoint-insurance-regulator-industry-braces-tough-period-sources" .tmp/scmp0826b/3363951.html &
fetch "https://www.scmp.com/business/banking-finance/article/3364710/chinese-insurance-giant-ping-ans-profit-climbs-36-policy-sales-investment-gains" .tmp/scmp0826b/3364710.html &
wait
echo DONE
