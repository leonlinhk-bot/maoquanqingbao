#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Final probe: insurer newsrooms for anything fresh (last 24h markers)."""
import re, subprocess, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                          capture_output=True, text=True, timeout=t+10).stdout

targets = {
    "aia": "https://www.aia.com.hk/en/about-aia/about-us/media-centre/press-releases.html",
    "manulife": "https://www.manulife.com.hk/en/individual/about/newsroom.html",
    "prudential": "https://www.prudential.com.hk/en/about-us/newsroom/",
    "axa": "https://www.axa.com.hk/en/news-room",
    "sunlife": "https://www.sunlife.com.hk/en/about-us/newsroom/news-releases/",
}
for name, url in targets.items():
    raw = fetch(url)
    if raw.startswith("ERR") or len(raw) < 300:
        print(f"== {name}: FAIL ({len(raw)}b)")
        continue
    # find Aug 2026 dates in text near titles
    hits = re.findall(r"([A-Z][A-Za-z ,]{0,80}2026[^<]{0,40})", raw)
    aug = [h.strip() for h in hits if "Aug" in h or "2026-08" in h]
    print(f"== {name}: {len(raw)}b, Aug-2026 mentions: {len(aug)}")
    for h in aug[:5]:
        print("   ", h[:110].replace("\n", " "))
