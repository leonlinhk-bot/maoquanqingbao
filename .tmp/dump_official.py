#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump samples of official page raw content for inspection."""
import re, subprocess

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                              capture_output=True, text=True, timeout=t+10).stdout
    except Exception as e:
        return f"ERR {e}"

raw = fetch("https://www.ia.org.hk/en/infocenter/press_releases.html")
print("=== IA PRESS raw head ===")
print(raw[:1500])
print("\n=== IA PRESS all links ===")
for m in re.finditer(r'href="([^"]+)"', raw):
    h = m.group(1)
    if any(k in h.lower() for k in ["press", "2026", "news"]):
        print("  ", h[:130])

raw2 = fetch("https://www.hkma.gov.hk/eng/news-and-media/press-releases/")
print("\n=== HKMA raw head ===")
print(raw2[:800])
print("\n=== HKMA date-ish patterns ===")
for m in re.finditer(r'(20\d\d-\d\d-\d\d)[^<]{0,120}', raw2):
    print("  ", m.group(0)[:160].replace("\n", " "))
