#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse AIA HK press releases page: extract titles, links, dates."""
import re, json

html = open('/tmp/nr.html', encoding='utf-8', errors='replace').read()
print('AIA HTML size:', len(html))

# AIA press release links usually like /en/about-aia/about-us/media-centre/press-releases/2026/press-...
links = re.findall(r'href="([^"]*press[^"]*)"[^>]*>(.*?)</a>', html, re.S)
seen = set()
count = 0
for href, txt in links:
    txt = re.sub(r'<[^>]+>', '', txt).strip()
    if not txt or href in seen:
        continue
    seen.add(href)
    if len(txt) < 20:
        continue
    print('|', href[:110], '|', txt[:90])
    count += 1
    if count > 25:
        break
print('shown:', count)
