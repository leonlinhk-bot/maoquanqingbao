#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
OUT = "data/_raw/t0822c"

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

fetch("ib-aia-broker.html", "https://www.insurancebusinessmag.com/asia/news/life-insurance/aia-narrows-broker-access-as-new-business-grows-21-586906.aspx")
fetch("ib-etf-mainland.html", "https://www.insurancebusinessmag.com/asia/news/life-insurance/mainland-insurers-gain-etf-access-retail-traders-just-lost-587035.aspx")
fetch("ib-pingan.html", "https://www.insurancebusinessmag.com/asia/news/breaking-news/ping-ans-new-business-growth-trails-chinas-insurance-pack-586912.aspx")
print("DONE")
