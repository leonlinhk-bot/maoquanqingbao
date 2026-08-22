#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 11: NFRA official announcement + HKET hengda article details."""
import re, html, subprocess, urllib.parse

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

# NFRA site - search for the announcement. NFRA uses a search endpoint
print("=== NFRA search attempt ===")
raw = fetch("https://www.nfra.gov.cn/cn/search/index.html?keyword=" + urllib.parse.quote("恒大人寿"))
print(f"len={len(raw)}")
print(strip_tags(raw)[:600])

# Try HKET hengda article
print("\n=== HKET hengda via jina ===")
raw = fetch("https://r.jina.ai/https://www.hket.com/article/hengda-life-license", UA)
print(f"len={len(raw)}")

# 文匯報 search
print("\n=== wenweipo search ===")
raw = fetch("https://www.wenweipo.com/search/?q=" + urllib.parse.quote("恒大人寿 吊銷"))
print(f"len={len(raw)}")
print(strip_tags(raw)[:400])

# 21jingji / cls search for hengda
print("\n=== cls.cn search ===")
raw = fetch("https://www.cls.cn/searchPage?keyword=" + urllib.parse.quote("恒大人寿") + "&type=telegram")
print(f"len={len(raw)}")

# 點新聞 article via jina (need proper URL - try site search)
print("\n=== hkcna hengda search via jina ===")
raw = fetch("https://r.jina.ai/https://www.hkcna.hk/search?keyword=" + urllib.parse.quote("恒大人寿"), UA)
print(f"len={len(raw)}")
print(strip_tags(raw)[:800])
