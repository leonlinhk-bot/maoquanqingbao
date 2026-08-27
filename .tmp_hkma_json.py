#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract embedded JSON content from HKMA article page."""
import re, json

html = open('.tmp/hkma_nm.html', encoding='utf-8', errors='replace').read()

# find all occurrences of Northern Metropolis with context of 800 chars
for m in re.finditer(r'Northern Metropolis', html):
    s = max(0, m.start() - 200)
    ctx = html[s:m.start() + 700]
    ctx = re.sub(r'\s+', ' ', ctx)
    print('---')
    print(ctx[:900])
    if m.start() > 30000:
        break
