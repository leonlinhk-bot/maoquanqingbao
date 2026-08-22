#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scan AIA/Prudential press pages: links w/ 2026-08 dates."""
import re, subprocess, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                          capture_output=True, text=True, timeout=t+10).stdout

for name, url in [
    ("aia", "https://www.aia.com.hk/en/about-aia/about-us/media-centre/press-releases.html"),
    ("prudential", "https://www.prudential.com.hk/en/about-us/newsroom/"),
    ("sunlife", "https://www.sunlife.com.hk/en/about-us/newsroom/news-releases/"),
]:
    raw = fetch(url)
    fname = f".tmp/{name}-press.html"
    open(fname, "w").write(raw)
    print(f"== {name}: {len(raw)}b saved")
    # find text blocks containing 2026-08-2x or Aug 2026
    for m in re.finditer(r'([^<>{}]{0,60}(?:2026-08-2\d|Aug(?:ust)? 2\d,? 2026)[^<>{}]{0,80})', raw):
        txt = html.unescape(m.group(1)).strip()
        if txt:
            print("   ", txt[:140].replace("\n", " "))
