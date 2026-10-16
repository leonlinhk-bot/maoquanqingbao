#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'
def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

# insuranceasia homepage cards
r = open(D + 'iaasia_hp.out', encoding='utf-8', errors='replace').read()
print('=== iaasia homepage links ===')
seen = []
for m in re.findall(r'href="(/insurance/[^"]+)"[^>]*>(.{0,200}?)</a>', r, re.S):
    if m[0] in seen:
        continue
    seen.append(m[0])
    print(' ', m[0][:120], '|', strip(m[1])[:90])
print('=== iaasia dates on page ===')
print(sorted(set(re.findall(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+20\d{2}', strip(r))))[:20])

for f in ['axa2026.out', 'sun2026.out']:
    print('=====', f)
    r = open(D + f, encoding='utf-8', errors='replace').read()
    print(' dates:', sorted(set(re.findall(r'20\d{2}\s*年\s*\d{1,2}\s*月\s*\d{1,2}\s*日', strip(r)))))
    print(' iso:', sorted(set(re.findall(r'20\d{2}-\d{2}-\d{2}', strip(r)))))
    seen = []
    for m in re.findall(r'href="([^"]+)"[^>]*>([^<]{10,120})<', r):
        if re.search(r'news|press|media|release|announce', m[0], re.I) and m[0] not in seen:
            seen.append(m[0]); print('  L', m[0][:120], '|', strip(m[1])[:80])
