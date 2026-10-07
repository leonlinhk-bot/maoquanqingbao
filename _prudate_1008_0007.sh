#!/bin/bash
cd /Users/leonliang/maoquanqingbao/.tmp/1008_0007
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
for s in "prudential-introduces-pruhealth-corechoice-and-pruhealth-flexichoice-medical-plans-and-an-integrated-digital-service-platform-in-support-of" "prudential-rolls-out-family-based-offers-for-health-insurance-plans-with-rewards-up-to-first-4-months-premium-refund"; do
  f="pru_${s:0:20}.html"
  code=$(curl -sL -m 25 -A "$UA" -o "$f" -w "%{http_code}" "https://www.prudential.com.hk/tc/about-us/newsroom/$s/")
  echo "== $s code=$code size=$(wc -c < "$f" | tr -d ' ')"
  grep -oE '(20[0-9]{2})[年/-]([0-9]{1,2})[月/-]([0-9]{1,2})' "$f" | head -5
  grep -oE '"(datePublished|dateModified)": *"[^"]+"' "$f" | head -3
done
