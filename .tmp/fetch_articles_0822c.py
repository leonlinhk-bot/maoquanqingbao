#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch article contents for in-window candidates."""
import subprocess, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
OUT = "data/_raw/t0822c"
os.makedirs(OUT, exist_ok=True)

def fetch(name, url, t=45):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                            "-H", "Accept-Language: en,zh-HK;q=0.8,zh;q=0.6", url],
                           capture_output=True, text=True, timeout=60)
        raw = r.stdout
        open(f"{OUT}/{name}", "w").write(raw)
        print(f"{'OK' if len(raw)>3000 else 'SMALL'} {len(raw):8d}  {name}")
    except Exception as e:
        print(f"ERR {e}  {name}")

fetch("hkma-pboC-bills.html", "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260821-3/")
fetch("hkma-scam-banks-0820.html", "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260820-4/")
fetch("ib-aia-broker.html", "https://www.insurancebusinessmag.com/asia/news/life-insurance/aia-narrows-broker-access-as-new-business-grows-21-586775.aspx")
fetch("ib-etf-mainland.html", "https://www.insurancebusinessmag.com/asia/news/life-insurance/mainland-insurers-gain-etf-access-retail-traders-just-lost-587004.aspx")
fetch("scmp-aia-mainland.html", "https://www.scmp.com/business/companies/article/3364620/aia-first-half-profit-11-driven-strong-growth-hong-kong-and-asia-sales")
fetch("scmp-pingan.html", "https://www.scmp.com/business/banking-finance/article/3364710/chinese-insurance-giant-ping-ans-profit-climbs-36-policy-sales-investment-gains")
fetch("ib-pingan.html", "https://www.insurancebusinessmag.com/asia/news/breaking-news/ping-ans-new-business-growth-trails-chinas-insurance-pack-586760.aspx")
print("DONE")
