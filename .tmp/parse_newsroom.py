#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse newsroom HTML files: extract dated news items (date + title + url)."""
import re, html, sys

def strip(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

def parse(fn, max_items=25):
    raw = open(fn, encoding='utf-8', errors='ignore').read()
    print(f"\n===== {fn} ({len(raw)} bytes) =====")
    # Find date-like tokens with nearby links: pattern "DD Mon YYYY" or "YYYY-MM-DD" or "2026/08/21"
    # Strategy: locate all <a href> + capture preceding/following 300 chars for dates
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S)
    seen = set()
    count = 0
    for u, t in links:
        t = strip(t)
        if len(t) < 8 or t in seen:
            continue
        low = (u + ' ' + t).lower()
        if any(k in low for k in ['css', '.js', '.png', '.jpg', '.ico', 'javascript:', 'facebook', 'twitter', 'linkedin', 'youtube', 'instagram']):
            continue
        # only news-like urls (contains year or press/news/release)
        if not re.search(r'(20\d\d|press|news|release|media|announce)', low):
            continue
        seen.add(t)
        count += 1
        print(f"- {t[:100]}")
        print(f"  {u[:160]}")
        if count >= max_items:
            break

if __name__ == "__main__":
    for fn in sys.argv[1:]:
        parse(fn)
