#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch article bodies for 4 candidates."""
import subprocess, re, html, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, out, t=35):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                            "-H", "Accept-Language: en,zh-CN;q=0.9",
                            "-H", "Referer: https://www.google.com/", url],
                           capture_output=True, text=True, timeout=50)
        raw = r.stdout
        open(out, "w").write(raw)
        print(f"OK  {len(raw):8d}  {url}")
        return raw
    except Exception as e:
        print(f"ERR {e}  {url}")
        return ""

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

# 1. IBMAG AIA broker (variants)
fetch("https://www.insurancebusinessmag.com/asia/news/life-insurance/aia-narrows-broker-access-as-new-business-grows-21-586/", "data/_raw/t0822-ib-aia-broker2.html")
fetch("https://www.insurancebusinessmag.com/asia/news/breaking-news/aia-narrows-broker-access-as-new-business-grows-21-586/", "data/_raw/t0822-ib-aia-broker3.html")

# 2. IAA offshore reinsurance
fetch("https://insuranceasia.com/insurance/news/offshore-reinsurance-expands-despite-slower-annuity-growth", "data/_raw/t0822-iaa-offshore.html")

# 3. IAA japanese life private credit
fetch("https://insuranceasia.com/insurance/in-focus/japanese-life-insurers-strike-global-deals-private-credit", "data/_raw/t0822-iaa-jplc.html")

# 4. Ping An: HKEX announcement search via GN redirect resolution -> try aastocks page
fetch("https://www.aastocks.com/tc/stocks/analysis/stock-aafn/2318/now/2318/1/all/1", "data/_raw/t0822-pingan-aastocks.html")
