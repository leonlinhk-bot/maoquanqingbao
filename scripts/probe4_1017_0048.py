#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'
def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

for f, pat in [('prudential.out', r'href="(/tc/about-us/newsroom/[^"]+)"'),
               ('axa.out', r'href="([^"]*news[^"]*)"'),
               ('sunlife.out', r'href="([^"]*news[^"]*)"'),
               ('manulife.out', r'href="([^"]*news[^"]*)"'),
               ('nfra.out', r'href="([^"]+)"')]:
    print('=====', f)
    try:
        r = open(D + f, encoding='utf-8', errors='replace').read()
    except Exception as e:
        print(' ERR', e); continue
    seen = []
    for m in re.findall(pat, r):
        if m not in seen:
            seen.append(m)
    for u in seen[:20]:
        print('  ', u[:150])
