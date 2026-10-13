#!/usr/bin/env bash
cd .cache1013_2108
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
curl -sL -m 30 -A "$UA" -o iaa_storm.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97186/Type/AirPlus/Storm-losses-estimated-at-up-to-US1bn-in-Thailand-less-than-100m-in-Myanmar" 
echo "iaa_storm $(wc -c < iaa_storm.html)"
