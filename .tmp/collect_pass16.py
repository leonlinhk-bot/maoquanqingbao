#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 16: find article URLs from outlet channel pages."""
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

# 點新聞 兩岸 channel
print("=== hkcna 兩岸 channel ===")
raw = fetch("https://www.hkcna.hk/channel/docList.jsp?channelId=4010&pageNo=1")
print(f"len={len(raw)}")
print(strip_tags(raw)[:300])

# 文匯報 finance channel
print("\n=== wenweipo finance ===")
raw = fetch("https://www.wenweipo.com/news/channel/finance/")
print(f"len={len(raw)}")
links = re.findall(r'href="(https?://www\.wenweipo\.com/[^"]+)"[^>]*>([^<]{10,100})</a>', raw)
for u, t in links[:15]:
    t = html.unescape(t).strip()
    print(f"- {t[:70]} | {u[:120]}")

# Try hkcna specific URL pattern for the hengda story
print("\n=== hkcna hengda guess ===")
raw = fetch("https://www.hkcna.hk/docDetail.jsp?id=100600001")
print(f"len={len(raw)}")

# 21jingji
print("\n=== 21jingji ===")
raw = fetch("https://www.21jingji.com/search?keyword=" + urllib.parse.quote("恒大人寿"))
print(f"len={len(raw)}")
print(strip_tags(raw)[:400])
