#!/usr/bin/env bash
# Resolve GNews redirect URLs to canonical article URLs
set -u
cd /Users/leonliang/maoquanqingbao
resolve() {
  local url="$1" label="$2"
  local final
  final=$(curl -sL --max-time 20 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36" -o /dev/null -w '%{url_effective}' "$url")
  echo "$label | $final"
}
# Manulife AI (Insurance Asia)
resolve "https://news.google.com/rss/articles/CBMinAFBVV95cUxQbXlsZjRKMXdoZXhtendxa3Q5YjBrWnByYXdkU" "manulife-ai"
# Taiwan spillover 152%
resolve "https://news.google.com/rss/articles/CBMiiwFBVV95cUxPNGZFYVBtYklwVkxoTktPal82VTJJM2JVbDZFe" "taiwan-spillover"
# Sun Life Wilton Re (Insurance Business)
resolve "https://news.google.com/rss/articles/CBMi0wFBVV95cUxOdERqTEtPdE1YcjBpbXhCbGNjM3FveEZqX0NaT" "sunlife-wilton"
# Steadfast (IBM)
resolve "https://news.google.com/rss/articles/CBMi0AFBVV95cUxNWUtfVVR5a0hhMWxrdkpVMUhHX1V2SDVTa1p4c" "steadfast"
# Evergrande Life (Re)in Asia
resolve "https://news.google.com/rss/articles/CBMijwFBVV95cUxOZmFhQ1ZMRVk2d2JmTFlqMjV2WEhyaVFyZU1CV" "evergrande-life"
# NFRA 5yr plan (Re)in Asia
resolve "https://news.google.com/rss/articles/CBMiqgFBVV95cUxNOXJlcHVDQWFTcWp5RzZ0RzVkTV83LVhGNnRQQ" "nfra-plan"
# FWD record profit (Globe and Mail)
resolve "https://news.google.com/rss/articles/CBMiyAFBVV95cUxNOVNfTFpuTTVObjExcU1CTWlaZ0pjbG5pUlZuQ" "fwd-h1"
# AIR wealth demand
resolve "https://news.google.com/rss/articles/CBMi0gFBVV95cUxOaGpuMEI0aE1QWlh3bXplZVBLUTQ4VnJXWXBae" "air-wealth"
# India life premiums July
resolve "https://news.google.com/rss/articles/CBMikAFBVV95cUxPYWhCM2ZMeDA0NVBmWjBFUkY4OTRwTjdFTEVid" "india-july"
# Taiwan FX life premiums
resolve "https://news.google.com/rss/articles/CBMioAFBVV95cUxPRXJ1QTJZcGU1eWlRWkU5dmQwSm1LcUJEdXNra" "taiwan-fx"
# Trade losses BI
resolve "https://news.google.com/rss/articles/CBMimAFBVV95cUxNWWtxOHB2NmxTR3pYOU9wQ3VYakxHUEFlS1ZqT" "trade-bi"
# Storms southern China ports
resolve "https://news.google.com/rss/articles/CBMingFBVV95cUxQdVN4WUxVcW5ZdEhZXzlMRk5PY0k3cERhUGR0O" "storms-ports"
echo DONE
