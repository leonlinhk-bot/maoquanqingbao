#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse fetched pages for items dated Aug 26-27, 2026."""
import re, html, glob

def clean(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

def links_with_text(h):
    out = []
    for m in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
        u, t = m.group(1), clean(m.group(2))
        if t and len(t) > 12:
            out.append((u, t))
    return out

DATE_RE = re.compile(r'2026[-/年]?0?8[-/月]?(2[5-7]|[0-9])|(2[5-7])\s*(Aug|八月|8月)', re.I)

for name in ['aia', 'prudential', 'axa', 'sunlife', 'scmp']:
    path = f'/tmp/src/{name}.html'
    try:
        h = open(path, encoding='utf-8').read()
    except Exception as e:
        print(f'== {name}: read error {e}')
        continue
    print(f'== {name} ({len(h)} chars)')
    seen = set()
    n = 0
    for u, t in links_with_text(h):
        if DATE_RE.search(t + ' ' + u):
            key = (u, t)
            if key in seen:
                continue
            seen.add(key)
            print('  -', t[:100], '|', u[:130])
            n += 1
            if n >= 15:
                break
    print(f'  [matched {n}]')
