#!/usr/bin/env bash
# 1029 00:40 抓候选正文
set -u
D=~/maoquanqingbao/.cache1029_0030/arts
mkdir -p "$D"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

get() {
  local name="$1" url="$2"
  local code
  code=$(curl -sS -L -m 40 -A "$UA" -o "$D/$name.html" -w '%{http_code}' "$url" 2>"$D/$name.err")
  echo "$name	$code	$(wc -c < "$D/$name.html" | tr -d ' ')"
}

get a1 "https://www.artemis.bm/news/evolving-ils-capital-landscape-an-opportunity-broker-facilities-no-threat-renre-ceo-odonnell/"
get a2 "https://www.artemis.bm/news/scale-of-client-needs-requires-us-to-connect-risk-with-capital-beyond-traditional-aon-ceo-case/"
get a3 "https://www.artemis.bm/news/vig-re-seeks-e50m-euro-wind-retro-with-debut-charles-bridge-re-cat-bond-sponsorship/"
get a4 "https://www.artemis.bm/news/morocco-targets-regulatory-framework-for-insurance-securitization-including-cat-bonds/"
get a5 "https://www.artemis.bm/news/lockton-re-names-jeremy-england-lee-as-chairman-bermuda/"
get b1 "https://www.insurancebusinessmag.com/asia/news/breaking-news/aons-debt-nearly-doubles-as-usi-close-approaches-595259.aspx"
get b2 "https://www.insurancebusinessmag.com/asia/news/breaking-news/arch-grows-primary-insurance-internationally-while-cutting-reinsurance-exposure-595250.aspx"
get b3 "https://www.insurancebusinessmag.com/asia/news/breaking-news/minings-soft-market-window-is-open-but-the-risks-arent-soft-595235.aspx"
get b4 "https://www.insurancebusinessmag.com/asia/news/marine/weak-dollar-flatters-marine-premium-growth-as-attritional-claims-build-iumi-finds-595220.aspx"
get c1 "https://insuranceasia.com/insurance/news/challenger-rejects-daiichi-lifes-82-takeover-offer"
get c5 "https://insuranceasia.com/insurance/news/allianz-partners-adds-247-support-international-students"
get c6 "https://insuranceasia.com/insurance/news/igloo-eyes-new-markets-insurers-automate-operations"
echo "--- done ---"
