#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 8: direct site fetches for originals."""
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

# Check what DDG returned
raw = fetch("https://html.duckduckgo.com/html/?q=" + urllib.parse.quote("恒大人寿 保险 业务许可证 吊销"))
print("=== DDG raw head ===")
print(strip_tags(raw)[:600])

# NFRA site search (their search page)
print("\n=== NFRA direct ===")
raw = fetch("https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=930&itemUrl=ItemListRightList.html&itemName=%E5%87%86%E5%85%A5%E7%AE%A1%E7%90%86&itemsiteId=9152")
print(f"len={len(raw)}")
print(strip_tags(raw)[:800])

# 點新聞 hkcna search
print("\n=== hkcna search ===")
raw = fetch("https://www.hkcna.hk/docDetail.jsp?id=" )
print(f"len={len(raw)}")

# etnet Manulife AIRSIDE - try site search
print("\n=== etnet search ===")
raw = fetch("https://www.etnet.com.hk/www/eng/news/search.php?q=" + urllib.parse.quote("宏利 AIRSIDE 樂活節奏健康節"))
print(f"len={len(raw)}")

# HKEJ search
print("\n=== hkej search ===")
raw = fetch("https://www.hkej.com/landing/articleSearch?q=" + urllib.parse.quote("友邦 稅策"))
print(f"len={len(raw)}")
print(strip_tags(raw)[:500])
