#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch key sources via curl for the 2026-08-22 18:08 run window (after 2026-08-20T21:14+08)."""
import subprocess, os, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
OUT = "data/_raw/t0822c"
os.makedirs(OUT, exist_ok=True)

def fetch(name, url, t=45):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                            "-H", "Accept-Language: en,zh-HK;q=0.8", url],
                           capture_output=True, text=True, timeout=60)
        raw = r.stdout
        open(f"{OUT}/{name}", "w").write(raw)
        print(f"{'OK' if len(raw)>3000 else 'SMALL'} {len(raw):8d}  {name}  {url}")
    except Exception as e:
        print(f"ERR {e}  {name}")

# HKMA press releases
fetch("hkma-press.html", "https://www.hkma.gov.hk/eng/news-and-media/press-releases/")
# IA press releases + circulars (likely Cloudflare-blocked, keep for record)
fetch("ia-press.html", "https://www.ia.org.hk/en/infocenter/press_releases.html")
fetch("ia-circ.html", "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html")
# InsuranceAsia RSS
fetch("iaa-rss.xml", "https://insuranceasia.com/insurance/rss.xml")
# IBMag RSS (atom)
fetch("ibmag.xml", "https://www.insurancebusinessmag.com/asia/rss/")
# Manulife HK newsroom
fetch("manulife-news.html", "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html")
# FSTB press
fetch("fstb-press.html", "https://www.fstb.gov.hk/en/news/press/index.php")
# NFRA (mainland regulator) - news list page
fetch("nfra.html", "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=916&itemId=916")
print("DONE")
