#!/usr/bin/env bash
set -u
cd /Users/leonliang/maoquanqingbao
gnews() {
  local q="$1" out="$2"
  local enc
  enc=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")
  curl -sL --max-time 25 -A "Mozilla/5.0" "https://news.google.com/rss/search?q=${enc}&hl=en-US&gl=US&ceid=US:en" -o "$out"
  echo "$(wc -c < "$out") $out  <-  $q"
}
gnews "Sun Life Wilton Re reinsurer when:4d" .tmp/scan0826/g2_sunlife_wilton.xml &
gnews "Evergrande Life licence revoked when:5d" .tmp/scan0826/g2_evergrande.xml &
gnews "NFRA five-year governance reform non-motor when:5d" .tmp/scan0826/g2_nfra_plan.xml &
gnews "FWD Group first half 2026 profit when:5d" .tmp/scan0826/g2_fwd.xml &
gnews "family office Hong Kong when:3d" .tmp/scan0826/g2_fam.xml &
gnews "international wealth insurance Asia demand when:4d" .tmp/scan0826/g2_air_wealth.xml &
gnews "trade losses business interruption when:4d" .tmp/scan0826/g2_tradebi.xml &
wait
echo DONE
