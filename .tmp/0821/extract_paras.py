#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract paragraphs from a saved HTML article file. Usage: python3 extract_paras.py file.html [max]"""
import re, html, sys

raw = open(sys.argv[1], encoding='utf-8', errors='replace').read()
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 8
paras = re.findall(r'<p[^>]*>(.*?)</p>', raw, re.S)
seen = set()
n = 0
for p in paras:
    t = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', p))).strip()
    if len(t) > 40 and t not in seen:
        seen.add(t)
        print('-', t[:500])
        n += 1
        if n >= mx:
            break
# also grab headline
m = re.search(r'<h1[^>]*>(.*?)</h1>', raw, re.S)
if m:
    print('H1:', re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))).strip())
