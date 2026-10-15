#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, os, glob
D = '/Users/leonliang/maoquanqingbao/data/_1016_0029/'

def clean(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

pat = re.compile(r'(1[5-6]\s*(?:Oct|October|Oct\.)\s*2026|2026[-/年]\s*1?0[-/月]\s*1[56]日?)', re.I)
for f in sorted(glob.glob(D + 'r2_*.out')):
    if os.path.getsize(f) < 5000:
        print('== %-22s (%d bytes, skip)' % (os.path.basename(f), os.path.getsize(f)))
        continue
    raw = open(f, encoding='utf-8', errors='replace').read()
    hits = []
    for m in pat.finditer(raw):
        seg = clean(raw[max(0, m.start() - 260):m.end() + 260])
        if seg and seg not in hits:
            hits.append(seg)
    print('== %-22s hits=%d' % (os.path.basename(f), len(hits)))
    for h in hits[:6]:
        print('    *', h[:230])
