#!/usr/bin/env bash
set -u
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
cd /Users/leonliang/maoquanqingbao
mkdir -p .tmp/art0826
fetch() {
  local url="$1" out="$2"
  curl -sL --max-time 30 -A "$UA" "$url" -o "$out" 2>/dev/null
  echo "$(wc -c < "$out" 2>/dev/null || echo 0) $out <- $url"
}
fetch "https://insuranceasia.com/insurance/exclusive/manulife-asia-pushes-ai-drive-health-wealth-growth" .tmp/art0826/manulife_ai.html &
fetch "https://insuranceasia.com/insurance/news/taiwan-spillover-effect-premiums-surge-152" .tmp/art0826/taiwan_spill.html &
fetch "https://www.insurancebusinessmag.com/asia/news/breaking-news/steadfast-lifts-profit-as-us-consortium-moves-to-take-it-private-587463.aspx" .tmp/art0826/steadfast.html &
fetch "https://www.nfra.gov.cn/" .tmp/art0826/nfra_home.html &
fetch "https://www.fwd.com/en/newsroom/" .tmp/art0826/fwd.html &
fetch "https://reinasiainstitute.com/" .tmp/art0826/reinasia.html &
fetch "https://www.asiainsurancereview.com/" .tmp/art0826/air.html &
fetch "https://insuranceasia.com/insurance/news/india-life-premiums-rise-1745-16b-in-july-2026" .tmp/art0826/india_july.html &
wait
echo DONE
