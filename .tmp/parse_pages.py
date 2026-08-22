#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse fetched insurer/newsroom HTML files for recent items."""
import re, html, sys, glob, os

def strip(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

def show(fn, limit=30):
    raw = open(fn, encoding='utf-8', errors='ignore').read()
    print(f"\n===== {fn} ({len(raw)} bytes) =====")
    # generic: links with nearby text, try date patterns first
    dates = re.findall(r'(20\d\d)[-/年.](\d{1,2})[-/月.](\d{1,2})', raw)
    if dates:
        print("sample dates:", dates[:10])
    # common newsroom patterns: <a href="...">Title</a> with date in li/span
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{10,150})</a>', raw)
    seen = set()
    for u, t in links:
        t = strip(t)
        if len(t) < 10 or t in seen:
            continue
        seen.add(t)
        low = (u + t).lower()
        if any(k in low for k in ['2026', 'aug', 'august', '21', '20']) and not any(k in low for k in ['css', 'js', '.png', '.jpg', '.ico', 'javascript']):
            print(f"- {t[:90]} | {u[:130]}")
            if len(seen) > limit:
                break

for fn in sys.argv[1:]:
    show(fn)
