#!/usr/bin/env python3
"""Post-push verification: local artifacts + deployed site."""
import json, re, urllib.request, zlib

PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36')]

# local
items = json.load(open('/Users/leonliang/maoquanqingbao/data/items.json'))
core = json.load(open('/Users/leonliang/maoquanqingbao/data/core.json'))
live = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
idx = open('/Users/leonliang/maoquanqingbao/index.html', encoding='utf-8').read()
ver = re.search(r'HKII_VER\s*=\s*[\'"]([^\'"]+)', idx)
print(f"local: live={len(live['items'])} items.json={len(items['items'])}/{items.get('itemCount')} "
      f"core={len(core['items'])} | index HKII_VER={ver.group(1) if ver else '?'}")
print(f"core first ids: {[it.get('id') for it in core['items'][:3]]}")

# deployed
BASE = 'https://hkmaoquanqingbao.com'
for path in ['/index.html', '/data/items.json', '/data/core.json']:
    try:
        r = op.open(BASE + path + '?cb=20261014b', timeout=30)
        raw = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
        t = raw.decode('utf-8', 'replace')
        if path.endswith('.json'):
            j = json.loads(t)
            n = len(j['items'])
            newest = j['items'][0].get('id')
            print(f"deployed {path}: {r.status} items={n} newest={newest}")
        else:
            v = re.search(r'HKII_VER\s*=\s*[\'"]([^\'"]+)', t)
            print(f"deployed {path}: {r.status} bytes={len(t)} ver={v.group(1) if v else '?'}")
    except Exception as e:
        print(f"deployed {path}: ERR {type(e).__name__}: {str(e)[:100]}")
