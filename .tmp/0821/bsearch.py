#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bing search helper. Usage: python3 bsearch.py 'query'"""
import subprocess, re, html, sys
from urllib.parse import quote

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def fetch(url):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                           capture_output=True, text=True, timeout=35)
        return r.stdout
    except Exception:
        return ""

q = sys.argv[1]
h = fetch(f"https://www.bing.com/search?q={quote(q)}&count=12")
print(f"--- Bing [{q}] size={len(h)} ---")
found = 0
for m in re.finditer(r'<h2><a href="([^"]+)"[^>]*>(.*?)</a></h2>', h, re.S):
    u = html.unescape(m.group(1))
    t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
    print(f"T: {t[:95]}\nU: {u[:170]}")
    found += 1
if found == 0:
    for m in re.finditer(r'<li class="b_algo".*?<a href="(https?://[^"]+)"[^>]*>(.*?)</a>', h, re.S):
        u = html.unescape(m.group(1))
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        print(f"T: {t[:95]}\nU: {u[:170]}")
        found += 1
print("found:", found)
