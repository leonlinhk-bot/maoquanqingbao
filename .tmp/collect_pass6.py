#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 6: InsuranceBusiness details + IA RSS article contents + original URL resolution."""
import re, html, json, subprocess, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                              capture_output=True, text=True, timeout=40).stdout
    except Exception:
        return ""

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

# 1. InsuranceBusiness - find story cards
raw = fetch("https://www.insurancebusinessmag.com/asia/news/breaking-news/")
print(f"=== InsuranceBusiness raw len={len(raw)} ===")
# find all /asia/news/ article urls
arts = re.findall(r'href="(/asia/news/[a-z0-9\-]+/[a-z0-9\-]+)"', raw)
uniq = []
for a in arts:
    if a not in uniq:
        uniq.append(a)
print("story links:", len(uniq))
for a in uniq[:25]:
    print("- https://www.insurancebusinessmag.com" + a)

# 2. IA RSS article contents (the two in-focus + offshore reinsurance + HDI)
print("\n\n=== IA RSS article details ===")
for slug in ["offshore-reinsurance-expands-despite-slower-annuity-growth",
             "japanese-life-insurers-strike-global-deals-private-credit",
             "hdi-global-net-income-rises-7-2496m-in-h1-2026",
             "aia-profit-surges-692-43b-in-h1-2026"]:
    raw = fetch(f"https://insuranceasia.com/insurance/news/{slug}" if "in-focus" not in slug else f"https://insuranceasia.com/insurance/in-focus/{slug}")
    if "in-focus" in slug:
        raw = fetch(f"https://insuranceasia.com/insurance/in-focus/{slug}")
    txt = strip_tags(raw)
    m = re.search(r'(Offshore reinsurance|Japanese life|HDI|AIA).{200,3000}', txt)
    print(f"\n--- {slug} (len={len(raw)}) ---")
    print(txt[:900])
