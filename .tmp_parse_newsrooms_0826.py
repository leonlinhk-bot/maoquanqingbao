#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract anchors + nearby dates from newsroom HTML files."""
import re, glob, html as H

FILES = {
    'aia': '/Users/leonliang/.tmp/scan0826/aia.html',
    'pru': '/Users/leonliang/.tmp/scan0826/pru.html',
    'axa': '/Users/leonliang/.tmp/scan0826/axa.html',
    'sunlife': '/Users/leonliang/.tmp/scan0826/sunlife.html',
    'iaa': '/Users/leonliang/.tmp/scan0826/iaa.html',
    'ibm': '/Users/leonliang/.tmp/scan0826/ibm.html',
    'scmp': '/Users/leonliang/.tmp/scan0826/scmp.html',
    'fstb': '/Users/leonliang/.tmp/scan0826/fstb.html',
}

DATE_PAT = re.compile(
    r'(2026[-/年]\s*0?8[-/月]\s*2[0-9]|2[0-9]\s+(?:Aug|August)\s+2026|Aug(?:ust)?\s+2[0-9],?\s+2026|2026[-/]0?8[-/]2[0-9])',
    re.I)

for name, path in FILES.items():
    html = open(path, encoding='utf-8', errors='replace').read()
    print(f'\n########## {name} (size={len(html)}) ##########')
    # find anchors with text
    anchors = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.S)
    seen = set()
    hits = []
    for href, txt in anchors:
        txt = re.sub(r'<[^>]+>', ' ', txt)
        txt = H.unescape(re.sub(r'\s+', ' ', txt)).strip()
        if not txt or href in seen or len(txt) < 18:
            continue
        seen.add(href)
        # context window around this anchor in raw html
        idx = html.find(href)
        ctx = html[max(0, idx - 300): idx + len(href) + 200]
        dates = DATE_PAT.findall(ctx)
        if dates:
            hits.append((dates[0], txt[:85], href[:120]))
    hits.sort(reverse=True)
    for d, t, h in hits[:25]:
        print(f'  {d} | {t} | {h}')
    if not hits:
        print('  (no dated anchors found in window)')
        # fallback: list first 15 anchors
        c = 0
        for href, txt in anchors:
            txt = H.unescape(re.sub(r'<[^>]+>', ' ', txt)).strip()
            if not txt or len(txt) < 18:
                continue
            print('  ? |', txt[:85], '|', href[:110])
            c += 1
            if c >= 15:
                break
