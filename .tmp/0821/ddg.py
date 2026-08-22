#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DuckDuckGo HTML search. Usage: python3 ddg.py 'query'"""
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
h = fetch(f"https://html.duckduckgo.com/html/?q={quote(q)}")
print(f"--- DDG [{q}] size={len(h)} ---")
if "anomaly" in h.lower() or "captcha" in h.lower():
    print("!! ddg challenge page")
found = 0
for m in re.finditer(r'<a rel="nofollow" class="result__a" href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
    u = html.unescape(m.group(1))
    t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
    print(f"T: {t[:95]}\nU: {u[:170]}")
    found += 1
    if found >= 10:
        break
print("found:", found)
