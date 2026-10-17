#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os, html
C = '/Users/leonliang/maoquanqingbao/.cache1018_0012'

def strip(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

def scan(fn, pats, label, maxn=14):
    print('='*18, label)
    p = os.path.join(C, fn)
    if not os.path.exists(p):
        print(' missing'); return
    raw = open(p, encoding='utf-8', errors='ignore').read()
    n = 0
    seen = set()
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, flags=re.S|re.I):
        href, inner = m.group(1), strip(m.group(2))
        if len(inner) < 14 or inner in seen:
            continue
        ctx = strip(raw[max(0,m.start()-200):m.start()+700])
        if any(p in ctx for p in pats):
            seen.add(inner)
            print('  %s\n     %s\n     ctx: %s' % (inner[:130], href[:150], ctx[:150]))
            n += 1
            if n >= maxn: break
    if n == 0:
        print('  (no dated anchors) text sample:', strip(raw)[:300])

for fn, label in [('aia.html','AIA'), ('prudential.html','PRUDENTIAL'), ('axa.html','AXA'), ('sunlife.html','SUNLIFE'), ('manulife.html','MANULIFE'), ('iaasia.html','ASIA INSURANCE REVIEW')]:
    scan(fn, ['2026', 'Oct', '10月'], label)
