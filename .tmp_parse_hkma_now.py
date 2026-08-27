#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse HKMA press release list page: links + dates."""
import re

html = open('.tmp/hkma.html', encoding='utf-8', errors='replace').read()
print('HTML size:', len(html))
links = re.findall(r'href="(/eng/news-and-media/press-releases/\d{4}/\d{2}/[^"]+)"', html)
seen = set()
for l in links:
    if l in seen:
        continue
    seen.add(l)
    m = re.search(r'/(\d{8})-\d+/?', l)
    print(l, '|', m.group(1) if m else '?')
print('count:', len(seen))
