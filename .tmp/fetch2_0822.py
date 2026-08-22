#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch article pages + NFRA + SCMP parse + PRU release URL scan."""
import subprocess, re, html, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, out):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "35", "-A", UA, url],
                           capture_output=True, text=True, timeout=45)
        raw = r.stdout
        open(out, "w").write(raw)
        print(f"OK  {len(raw):8d}  {url}")
        return raw
    except Exception as e:
        print(f"ERR {e}  {url}")
        return ""

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

# 1. IBMAG AIA broker access article
fetch("https://www.insurancebusinessmag.com/asia/news/life-insurance/aia-narrows-broker-access-as-new-business-grows-21-586", "data/_raw/t0822-ib-aia-broker.html")

# 2. SunLife 2026 news releases index (with dates)
fetch("https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/", "data/_raw/t0822-sunlife-2026.html")

# 3. NFRA real index
fetch("https://www.nfra.gov.cn/cn/view/pages/index/index.html", "data/_raw/t0822-nfra2.html")

# 4. SCMP insurance topics (parse inline)
raw = open("data/_raw/t0822-scmp.html", encoding="utf-8", errors="replace").read()
print("\n=== SCMP article candidates ===")
for m in re.finditer(r'href="(/news/[^"]*(?:insur|policy|premium|life)[^"]*)"[^>]*>(.*?)</a>', raw, re.S):
    href, txt = m.group(1), unq(m.group(2))
    if len(txt) > 14 and "scmp" not in txt.lower():
        print("-", href[:100], "|", txt[:90])
print("SCMP date pats:", len(re.findall(r"20\d\d[-/.]0[78][-/.]\d{1,2}", raw)))

# 5. PRU release URLs with year
raw = open("data/_raw/t0822-prudential.html", encoding="utf-8", errors="replace").read()
print("\n=== PRU newsroom links ===")
seen = set()
for m in re.finditer(r'href="([^"]*(?:newsroom|news)[^"]*)"', raw):
    u = m.group(1)
    if u not in seen and ("tc/about-us/newsroom" in u or "en/about-us/newsroom" in u) and len(u) > 40:
        seen.add(u)
        print("-", u[:150])
