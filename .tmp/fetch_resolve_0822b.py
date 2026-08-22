#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(name, url, t=50):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                            "-H", "Accept-Language: en,zh-CN;q=0.9", url],
                           capture_output=True, text=True, timeout=65)
        raw = r.stdout
        open(f"data/_raw/t0822b/{name}.html", "w").write(raw)
        print(f"{'OK' if len(raw)>2000 else 'SMALL'} {len(raw):8d}  {name}  {url[:100]}")
        return raw
    except Exception as e:
        print(f"ERR {name} {e}")
        return ""

# wayback raw (id_) for IAA rss and IA press
fetch("wb-id-iaa-rss", "https://web.archive.org/web/2026id_/https://insuranceasia.com/insurance/rss.xml")
fetch("wb-id-ia-press", "https://web.archive.org/web/20260822000000id_/https://www.ia.org.hk/en/infocenter/press_releases.html")

# resolve key gnews links: NFRA evergrande life (點新聞), FSTB ETF connect (香港商报), 招商永隆 (鉅亨網)
fetch("nfra-evergrande-life", "https://www.dotdotnews.com/a/202608/21/AP_66f0a0e5e4b0d0b0a0d0a0d0.html")
fetch("fstb-etf-connect", "https://www.hkcd.com/content/2026-08/21/content_8612345.html")
print("DONE")
