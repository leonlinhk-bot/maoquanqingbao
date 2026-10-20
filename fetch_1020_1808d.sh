#!/usr/bin/env bash
cd /Users/leonliang/maoquanqingbao/.cache1020_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
g() { curl -sL -m 40 -A "$UA" -o "$1" -w "$1 %{http_code} %{size_download}\n" "$2"; }
g rn_nms.html "https://www.reinsurancene.ws/nms-capital-launches-specialty-mga-ascendra/" &
g rn_moodys.html "https://www.reinsurancene.ws/moodys-forecasts-further-growth-in-german-insurers-private-credit-investments/" &
g rn_gal.html "https://www.reinsurancene.ws/reinsurers-must-focus-on-cedent-needs-to-attract-more-inflow-gallagher-res-deschars/" &
g art_ambest.html "https://www.artemis.bm/news/clear-exit-terms-and-liquid-collateral-key-to-lowering-casualty-sidecar-tail-risk-charges-am-best/" &
g ian_cyber.html "https://insuranceasianews.com/cybercube-adds-sompo-japan-to-growing-apac-client-base/" &
g ibm_asia.html "https://www.insurancebusinessmag.com/asia/news/breaking-news/" &
g fstb.html "https://www.fstb.gov.hk/en/" &
g scmp.xml "https://www.scmp.com/rss/92/feed" &
wait
echo done
