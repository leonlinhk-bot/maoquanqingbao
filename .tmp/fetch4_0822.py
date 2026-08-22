#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wayback fetches: IA press, IA circulars, IBMAG aia article + SunLife release pages."""
import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, out, t=45):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                           capture_output=True, text=True, timeout=60)
        raw = r.stdout
        open(out, "w").write(raw)
        print(f"OK  {len(raw):8d}  {url}")
        return raw
    except Exception as e:
        print(f"ERR {e}  {url}")
        return ""

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

# 1. Wayback: IA press releases (nearest snapshot)
fetch("https://web.archive.org/web/20260822000000/https://www.ia.org.hk/en/infocenter/press_releases.html", "data/_raw/t0822-wb-ia-press.html", 60)

# 2. Wayback: IA circulars reg matters
fetch("https://web.archive.org/web/20260822000000/https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters.html", "data/_raw/t0822-wb-ia-circ.html", 60)

# 3. Wayback: IBMAG aia broker article
fetch("https://web.archive.org/web/2026/https://www.insurancebusinessmag.com/asia/news/life-insurance/aia-narrows-broker-access-as-new-business-grows-21-586", "data/_raw/t0822-wb-ib-aia.html", 60)

# 4. SunLife releases
fetch("https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-launches-private-wealth-i", "data/_raw/t0822-sl-pw.html")
fetch("https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-mpf-nearly-20-of-mpf-memb", "data/_raw/t0822-sl-mpf.html")
