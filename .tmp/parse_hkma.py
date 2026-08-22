#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse HKMA press releases page for recent entries."""
import re, html, datetime

raw = open('.tmp/hkma.html', encoding='utf-8', errors='replace').read()
print("len:", len(raw))

# HKMA press release items usually in <a class="news ..."> or list items
# Try generic link+date patterns
items = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{10,120})</a>', raw)
seen = set()
for u, t in items:
    t = html.unescape(t).strip()
    if not t or t in seen:
        continue
    seen.add(t)
    if any(k in u.lower() for k in ['press', 'news', 'speech']):
        print(f"- {t[:90]} | {u[:120]}")
