#!/usr/bin/env bash
cd .cache1013_2108
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() { code=$(curl -sL -m 30 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null); echo "$1 $code $(wc -c < "$1" | tr -d ' ')"; }
fetch artemis.xml "https://www.artemis.bm/news/feed/" &
fetch iaa_rss.xml "https://www.asiainsurancereview.com/RSS" &
fetch ibm_pru.html "https://www.insurancebusinessmag.com/asia/news/life-insurance/japan-orders-prudentials-life-units-to-stop-soliciting-new-business-until-january-31-593252.aspx" &
fetch iaa_p1.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97223/Type/AirPlus/Taiwan-Regulator-opens-up-insurers-investments-in-health-wellness-and-long-term-care" &
fetch iaa_p2.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97222/Type/AirPlus/Mental-health-absences-are-now-considered-an-organisational-risk" &
fetch iaasia_singlife.html "https://insuranceasia.com/videos/singlife-weighs-ai-speed-against-human-oversight" &
fetch iaasia_spore.html "https://insuranceasia.com/insurance/exclusive/singapore-insurers-face-shift-coverage-adequacy" &
fetch hkma2.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/" &
wait
echo done
