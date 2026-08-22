#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

# 1. parse IBMAG rss
raw = open("data/_raw/t0822b/ibmag-rss.xml", encoding="utf-8", errors="ignore").read()
print(f"IBMAG RSS items: {raw.count('<item>')}")
for m in list(re.finditer(r"<item>(.*?)</item>", raw, flags=re.S))[:25]:
    b = m.group(1)
    t = re.search(r"<title>(.*?)</title>", b, flags=re.S)
    d = re.search(r"<pubDate>(.*?)</pubDate>", b, flags=re.S)
    l = re.search(r"<link>(.*?)</link>", b, flags=re.S)
    title = unq(re.sub(r"<[^>]+>", "", t.group(1) if t else ""))
    date = unq(d.group(1) if d else "")
    print(f"  [{date}] {title[:80]} -> {unq(l.group(1) if l else '')[:110]}")

# 2. IA rss candidates
UA2 = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
cands = [
    ("ia-rss", "https://www.ia.org.hk/en/infocenter/press_releases_rss.xml"),
    ("ia-rss2", "https://www.ia.org.hk/en/rss/press_releases.xml"),
    ("ia-rss3", "https://www.ia.org.hk/en/infocenter/press_releases/rss.xml"),
    ("iaa-rss-direct", "https://insuranceasia.com/insurance/rss.xml"),
]
print("\n--- IA/IAA rss probes ---")
for name, url in cands:
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA2,
                            "-H", "Accept: application/rss+xml,application/xml;q=0.9,*/*;q=0.8", url],
                           capture_output=True, text=True, timeout=35)
        raw2 = r.stdout
        print(f"{name:16s} {len(raw2):8d}  rss={('<rss' in raw2[:300] or '<feed' in raw2[:300])}  {url}")
        if "<rss" in raw2[:300] or "<feed" in raw2[:300]:
            open(f"data/_raw/t0822b/{name}.xml", "w").write(raw2)
    except Exception as e:
        print(f"{name:16s} ERR {e}")
