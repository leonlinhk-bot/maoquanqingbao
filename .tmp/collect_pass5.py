#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 5: IA via jina proxy, InsuranceAsia feeds, Insurance Business page."""
import re, html, subprocess

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url, ua=None, max_t=40):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", str(max_t), "-A", ua or UA, url],
                              capture_output=True, text=True, timeout=50).stdout
    except Exception as e:
        return f"ERR {e}"

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

# 1. IA circulars via jina reader proxy (no API key needed for r.jina.ai)
raw = fetch("https://r.jina.ai/https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters.html")
print(f"=== IA circulars via jina (len={len(raw)}) ===")
print(strip_tags(raw)[:2500])

# 2. InsuranceAsia RSS alternates
for url in ["https://insuranceasia.com/rss.xml", "https://insuranceasia.com/feed/", "https://insuranceasia.com/insurance/feed/"]:
    raw = fetch(url)
    print(f"\n=== IA RSS {url} (len={len(raw)}) ===")
    print(strip_tags(raw)[:300])

# 3. Insurance Business Asia breaking news
raw = fetch("https://www.insurancebusinessmag.com/asia/news/breaking-news/")
print(f"\n=== InsuranceBusiness breaking (len={len(raw)}) ===")
links = re.findall(r'href="(https://www\.insurancebusinessmag\.com/asia/news/[^"]+)"[^>]*>([^<]{15,120})</a>', raw)
seen = set()
for u, t in links[:15]:
    t = html.unescape(t).strip()
    if t in seen:
        continue
    seen.add(t)
    print(f"- {t[:85]} | {u[:130]}")
