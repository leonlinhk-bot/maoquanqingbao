#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
cands = [
    ("ia-press-data", "https://www.ia.org.hk/en/infocenter/press_releases_data.html"),
    ("ia-press-list", "https://www.ia.org.hk/en/infocenter/press_releases_list.html"),
    ("ia-press-json", "https://www.ia.org.hk/en/infocenter/press_releases.json"),
    ("ia-newsroom", "https://www.ia.org.hk/en/infocenter/news.html"),
    ("ia-press-api", "https://www.ia.org.hk/en/infocenter/press_releases_api.html"),
    ("ibmag-rss", "https://www.insurancebusinessmag.com/asia/rss/"),
    ("ibmag-rss2", "https://www.insurancebusinessmag.com/rss/"),
    ("ibmag-rss3", "https://www.insurancebusinessmag.com/asia/news/breaking-news/rss.xml"),
]
os.makedirs("data/_raw/t0822b", exist_ok=True)
for name, url in cands:
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                           capture_output=True, text=True, timeout=35)
        raw = r.stdout
        kind = "RSS" if "<rss" in raw[:300] or "<feed" in raw[:300] else ("HTML" if "<html" in raw[:300].lower() else "RAW")
        print(f"{name:16s} {len(raw):8d} {kind:5s} {url}")
        if len(raw) > 800 and kind == "RSS":
            open(f"data/_raw/t0822b/{name}.xml", "w").write(raw)
        elif len(raw) > 3000 and kind == "HTML":
            open(f"data/_raw/t0822b/{name}.html", "w").write(raw)
    except Exception as e:
        print(f"{name:16s} ERR {e}")
