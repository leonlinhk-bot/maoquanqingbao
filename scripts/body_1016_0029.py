#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, os, glob
D = '/Users/leonliang/maoquanqingbao/data/_1016_0029/'

def totext(raw):
    raw = re.sub(r'(?is)<(script|style|nav|header|footer|svg|noscript)[^>]*>.*?</\1>', ' ', raw)
    raw = re.sub(r'(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>', '\n', raw)
    t = re.sub(r'(?s)<[^>]+>', ' ', raw)
    t = html.unescape(t)
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return t.strip()

for f in sorted(glob.glob(D + 'a_*.html')):
    if os.path.getsize(f) < 3000:
        print('====', os.path.basename(f), 'too small'); continue
    t = totext(open(f, encoding='utf-8', errors='replace').read())
    # find main body: heuristics — print chunk around first long paragraph
    lines = [l.strip() for l in t.split('\n') if len(l.strip()) > 60]
    print('====', os.path.basename(f))
    for l in lines[:16]:
        print('   ', l[:300])
    print()
