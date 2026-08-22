#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Probe InsuranceAsia + IBmag pages."""
import re, subprocess, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                              capture_output=True, text=True, timeout=t+10).stdout
    except Exception as e:
        return f"ERR {e}"

for name, url in [
    ("iaasia_home", "https://insuranceasia.com/"),
    ("iaasia_insurance", "https://insuranceasia.com/insurance"),
    ("iaasia_sitemap", "https://insuranceasia.com/sitemap.xml"),
    ("ibmag", "https://www.insurancebusinessmag.com/asia/news/breaking-news/"),
]:
    raw = fetch(url)
    print(f"== {name}: {len(raw)} bytes")
    if raw.startswith("ERR"):
        print("   ", raw[:100])
        continue
    if name == "iaasia_sitemap":
        urls = re.findall(r"<loc>([^<]+)</loc>", raw)
        print("   sitemap urls:", len(urls))
        for u in urls[:12]:
            print("   ", u[:120])
    elif name == "iaasia_home" or name == "iaasia_insurance":
        # look for article links with dates
        arts = re.findall(r'href="(/insurance/[^"]+|/[^"]*article[^"]*)"[^>]*>(.*?)</a>', raw, re.S)[:15]
        for href, txt in arts:
            t = re.sub(r"<[^>]+>", "", txt).strip()
            if t:
                print("   ", html.unescape(t)[:90], "->", href[:100])
    else:
        arts = re.findall(r'href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S)
        n = 0
        for href, txt in arts:
            t = re.sub(r"<[^>]+>", "", txt).strip()
            if t and ("article" in href or "news" in href):
                print("   ", html.unescape(t)[:85], "->", href[:100])
                n += 1
                if n > 12:
                    break
