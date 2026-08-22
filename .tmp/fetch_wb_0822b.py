#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wayback fetches for blocked/JS pages."""
import subprocess, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
OUT = "data/_raw/t0822b"
os.makedirs(OUT, exist_ok=True)

def fetch(name, url, t=60):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                           capture_output=True, text=True, timeout=80)
        raw = r.stdout
        open(f"{OUT}/{name}.html", "w").write(raw)
        print(f"{'OK' if len(raw)>2000 else 'SMALL'} {len(raw):8d}  {name}  {url}")
    except Exception as e:
        print(f"ERR {e}  {name}")

fetch("wb-ia-press", "https://web.archive.org/web/20260822000000*/ia.org.hk/en/infocenter/press_releases.html")
fetch("wb-ia-press2", "https://web.archive.org/web/20260822000000/https://www.ia.org.hk/en/infocenter/press_releases.html")
fetch("wb-ia-circ", "https://web.archive.org/web/20260822000000/https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html")
fetch("wb-iaa-rss", "https://web.archive.org/web/2026/https://insuranceasia.com/insurance/rss.xml")
fetch("wb-nfra", "https://web.archive.org/web/2026/https://www.nfra.gov.cn/")
fetch("wb-manulife", "https://web.archive.org/web/20260822000000/https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html")
fetch("wb-fstb-press", "https://web.archive.org/web/20260822000000/https://www.fstb.gov.hk/en/news/press/index.php")
print("DONE")
