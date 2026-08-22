#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract AXA newsroom items dated 2026-08-21."""
import re, html, sys

fn = sys.argv[1] if len(sys.argv) > 1 else '.tmp/0821d/axa.html'
raw = open(fn, encoding='utf-8', errors='ignore').read()

def strip(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

seen = set()
for m in re.finditer(r'2026-08-2[01]', raw):
    s = max(0, m.start() - 500)
    e = min(len(raw), m.end() + 500)
    chunk = raw[s:e]
    for u, t in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', chunk, re.S):
        t = strip(t)
        if len(t) < 8 or t in seen:
            continue
        seen.add(t)
        print(f"- {t[:110]}")
        print(f"  {u[:170]}")
