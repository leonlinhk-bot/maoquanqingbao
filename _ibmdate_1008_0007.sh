#!/bin/bash
cd /Users/leonliang/maoquanqingbao/.tmp/1008_0007
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"

fetchibm(){
  slug="$1"
  f="ibm_${slug##*/}.html"
  curl -sL -m 25 -A "$UA" -o "$f" "https://www.insurancebusinessmag.com/asia/news/${slug}.aspx"
  echo "== $slug  size=$(wc -c < "$f" | tr -d ' ')"
  grep -oE '"(datePublished|dateModified)": *"[^"]+"' "$f" | head -4
  grep -oE '[0-9]{1,2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) 2026' "$f" | head -3
}

fetchibm "life-insurance/the-fraud-window-in-south-koreas-nhis-opens-the-moment-a-foreign-worker-leaves-592689"
fetchibm "catastrophe/philippines-locks-in-disaster-risk-deal-as-domestic-catastrophe-pool-struggles-for-traction-592676"
fetchibm "sme/south-koreas-free-sme-cover-what-the-limits-leave-exposed-592667"
