#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 12: NFRA official announcement search."""
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

# NFRA search API attempt
print("=== NFRA itemList 处罚信息 ===")
raw = fetch("https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=931&itemUrl=ItemListRightList.html&itemName=%E5%A4%84%E7%BD%9A%E4%BF%A1%E6%81%AF&itemsiteId=9152")
print(f"len={len(raw)}")
print(strip_tags(raw)[:400])

# Try NFRA announcement for 恒大人寿 via Bing RSS (worked before for some queries)
print("\n=== Bing RSS hengda ===")
raw = fetch("https://www.bing.com/search?q=" + urllib.parse.quote("site:nfra.gov.cn 恒大人寿 吊销") + "&format=rss&count=15")
print(strip_tags(raw)[:1200])

print("\n=== Bing RSS hengda2 ===")
raw = fetch("https://www.bing.com/search?q=" + urllib.parse.quote("恒大人寿 吊销 业务许可证 8月21日") + "&format=rss&count=15")
print(strip_tags(raw)[:1200])
