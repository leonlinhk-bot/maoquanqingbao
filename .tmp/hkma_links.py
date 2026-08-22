#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inspect HKMA page links structure."""
import re, subprocess, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                          capture_output=True, text=True, timeout=t+10).stdout

raw = fetch("https://www.hkma.gov.hk/eng/news-and-media/press-releases/")
# all <a href> with text
links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S)
print("total links:", len(links))
count = 0
for href, txt in links:
    t = re.sub(r"<[^>]+>", "", txt).strip()
    t = html.unescape(t)
    if ("press" in href.lower() or "2026" in href) and t:
        print(f"  {t[:80]}  ->  {href[:110]}")
        count += 1
        if count > 40:
            break
