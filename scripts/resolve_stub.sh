#!/bin/bash
# Try to resolve Google News stub redirect to canonical URL
STUB="https://news.google.com/rss/articles/CBMimANBVV95cUxPbWZoNndFTXlmTzRENFhDMnptMkYtZ2xDNmN3aV9DZHhiODJ1SVlHdFhJU285SEpFXy1pZW1GUEZ6TkduY0phTGxLYkd2V0RjRDVhaFA5TVB"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
echo "== HEAD =="
curl -s -o /dev/null -w "code=%{http_code} redirect=%{redirect_url}\n" --max-time 20 -A "$UA" "$STUB"
echo "== FOLLOW =="
curl -s -L --max-time 25 -A "$UA" "$STUB" -o /tmp/stub_follow.html
echo "size=$(wc -c < /tmp/stub_follow.html | tr -d ' ')"
grep -o 'https://[a-z0-9.]*hket[^"< ]*' /tmp/stub_follow.html | head -3
grep -o '<title>[^<]*' /tmp/stub_follow.html | head -2
