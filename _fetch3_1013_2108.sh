#!/usr/bin/env bash
cd .cache1013_2108
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() { code=$(curl -sL -m 30 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null); echo "$1 $code $(wc -c < "$1" | tr -d ' ')"; }
fetch iaa_manulife.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97199/Type/eDaily/Asia-Manulife-Asia-appoints-new-Chief-Information-Officer" &
fetch iaa_utmost.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97200/Type/eDaily/Asia-Utmost-appoints-new-Head-of-High-Net-Worth-Underwriting" &
fetch iaa_zhibao.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/96992/Type/eDaily/Zhibao-Labuan-Re-expands-into-Hong-Kong-and-Southeast-Asia" &
fetch iaa_tanker.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97196/Type/eDaily/Japan-Government-to-expand-tanker-reinsurance-equivalent-coverage-for-non-Iranian-crude-oil" &
fetch ian_barcelona.html "https://insuranceasianews.com/barcelona-floods-are-a-wake-up-call-on-urban-flood-risk/" &
fetch ian_howden.html "https://insuranceasianews.com/howden-australia-drafts-marsh-team-for-sport-and-entertainment-practice-build-out/" &
wait
echo done
