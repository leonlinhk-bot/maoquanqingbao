#!/usr/bin/env python3
"""Fetch extra sources for the 2026-10-14 18:08 run and print new-window candidates."""
import json, re, sys, urllib.request, urllib.error, zlib
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 14, 2, 11, tzinfo=HKT)  # last check
PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36')]


def get(url, timeout=25):
    try:
        r = op.open(url, timeout=timeout)
        raw = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
        return raw.decode('utf-8', 'replace')
    except Exception as e:
        return f'__ERR__ {type(e).__name__}: {str(e)[:120]}'


FEEDS = {
    'hkma_api': 'https://api.hkma.gov.hk/public/press-releases?segment=all&sortby=date_desc&pagesize=30',
    'insurancebusinessmag': 'https://www.insurancebusinessmag.com/asia/rss/',
    'scmp_business': 'https://www.scmp.com/rss/92/feed',
    'insuranceasia': 'https://insuranceasia.com/rss.xml',
    'govhk': 'https://www.info.gov.hk/gia/rss/general_zh.xml',
}
out = {}
for k, u in FEEDS.items():
    t = get(u)
    out[k] = t
    print(f'=== {k} len={len(t)} ===')
    if t.startswith('__ERR__'):
        print(t)
    else:
        open(f'data/_1014/{k}.raw', 'w', encoding='utf-8').write(t)
json.dump(out, open('data/_1014/_all.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('done')
