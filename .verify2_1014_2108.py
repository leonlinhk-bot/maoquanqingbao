#!/usr/bin/env python3
import re, html, zlib
import urllib.request
PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36')]
r = op.open('https://www.info.gov.hk/gia/general/202610/14/P2026101400250.htm', timeout=25)
t = r.read().decode('utf-8', 'replace')
t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', t)
body = html.unescape(re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', t))).strip()
for kw in ['退休入息保障', '88,422', '97,396', '100萬', '銀色財務及保障安排', '投資選項']:
    idx = body.find(kw)
    print(f'--- {kw}: {"FOUND" if idx >= 0 else "NOT FOUND"}')
    if idx >= 0:
        print('   ...', body[max(0, idx - 260):idx + 200].strip(), '...')
# tail of the answer
print('\n=== TAIL ===')
print(body[-1800:])
