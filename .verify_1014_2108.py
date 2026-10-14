#!/usr/bin/env python3
"""Verify govhk press-release facts + inspect score convention in live-items."""
import json, re, html, zlib
import urllib.request

PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36')]

URLS = {
    'sidecar': 'https://www.info.gov.hk/gia/general/202610/14/P2026101300435.htm',
    'cdta': 'https://www.info.gov.hk/gia/general/202610/14/P2026101400351.htm',
    'silverbond': 'https://www.info.gov.hk/gia/general/202610/14/P2026101400250.htm',
}
for k, u in URLS.items():
    try:
        r = op.open(u, timeout=25)
        raw = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
        t = raw.decode('utf-8', 'replace')
    except Exception as e:
        print(k, 'ERR', e); continue
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', t)
    body = html.unescape(re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', t))).strip()
    print(f'\n===== {k} =====')
    print(body[:1400])

print('\n===== score convention =====')
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
by = {}
for it in d['items']:
    by.setdefault(it.get('sourceTier'), []).append(it.get('score'))
for t, xs in by.items():
    xs = [x for x in xs if isinstance(x, (int, float))]
    if xs:
        print(f'  {t:10} n={len(xs):5} min={min(xs):3} p25={sorted(xs)[len(xs)//4]:3} med={sorted(xs)[len(xs)//2]:3} max={max(xs):3}')
