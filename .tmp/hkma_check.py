#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch HKMA 20260820-4 press release page for its publish time."""
import re, subprocess

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                          capture_output=True, text=True, timeout=t+10).stdout

for n in ["20260820-4", "20260820-3"]:
    raw = fetch(f"https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/{n}/")
    print(f"== {n}: {len(raw)}b")
    # title
    m = re.search(r"<title>(.*?)</title>", raw, re.S)
    print("   title:", m.group(1).strip()[:100] if m else "?")
    # look for date published / time
    for pat in [r'(?:datePublished|published_date|datePosted|content)="?([^"]{8,40})"?', r'(20\d\d)\.(\d\d)\.(\d\d)[^<]{0,30}']:
        hits = re.findall(pat, raw)
        if hits:
            print("   date hits:", hits[:6])
            break
    # meta og:title / og:url
    og = re.findall(r'property="og:title" content="([^"]+)"', raw)
    if og:
        print("   og:title:", og[0][:100])
