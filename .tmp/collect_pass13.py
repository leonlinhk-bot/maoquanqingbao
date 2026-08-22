#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 13: direct article fetches for Hengda story."""
import re, html, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url, ua=None):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", ua or UA, url],
                              capture_output=True, text=True, timeout=40).stdout
    except Exception:
        return ""

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

# 文匯報 search page (they have /search or use site search)
print("=== wenweipo search ===")
raw = fetch("https://www.wenweipo.com/s/action/search?q=" + urllib.parse.quote("恒大人寿"))
print(f"len={len(raw)}")
print(strip_tags(raw)[:500])

# Try wenweipo search via jina
print("\n=== wenweipo via jina ===")
raw = fetch("https://r.jina.ai/https://www.wenweipo.com/s/action/search?q=" + urllib.parse.quote("恒大人寿"), UA)
print(f"len={len(raw)}")
print(strip_tags(raw)[:900])

# HKET search
print("\n=== HKET search via jina ===")
raw = fetch("https://r.jina.ai/https://www.hket.com/search?q=" + urllib.parse.quote("恒大人寿 吊銷"), UA)
print(f"len={len(raw)}")
print(strip_tags(raw)[:900])

# Try NFRA direct announcement URL patterns - 2026 penalties
print("\n=== NFRA site map check ===")
raw = fetch("https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=930")
print(f"len={len(raw)}")
