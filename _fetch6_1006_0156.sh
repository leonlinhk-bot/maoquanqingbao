#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
O=/Users/leonliang/maoquanqingbao/data/_cache1006_0156
g() { printf '%-16s ' "$1"; curl -sL -m 30 -A "$UA" -o "$O/$1" -w "%{http_code} %{size_download}\n" "$2"; }
g corgi1.html "https://fintech.global/2026/10/05/corgi-targets-growing-insurance-gap-around-ai-infrastructure/"
g corgi2.html "https://www.fintech.global/2026/10/05/corgi-targets-growing-insurance-gap-around-ai-infrastructure/"
g famoff.html "https://www.familyofficehk.gov.hk/en/"
g fstb.html  "https://www.fstb.gov.hk/en/"
echo "--- corgi title sniff ---"
grep -oE '<title>[^<]*' "$O/corgi1.html" 2>/dev/null | head -2
grep -oiE '(published|date)[^<]{0,40}' "$O/corgi1.html" 2>/dev/null | head -5
echo DONE
