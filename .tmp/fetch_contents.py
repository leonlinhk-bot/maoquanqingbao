#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 4: fetch content of key stories to build summaries + find originals."""
import re, html, json, subprocess, urllib.parse

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

def show(url, label, maxlen=1200):
    raw = fetch(url)
    txt = strip_tags(raw)
    print(f"\n=== {label}: {url} (len={len(raw)}) ===")
    print(txt[:maxlen])

# HKMA scam alert content
show("https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260820-4/", "HKMA scam alert banks")
# PBOC RMB bills
show("https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260821-3/", "HKMA PBOC RMB bills")
