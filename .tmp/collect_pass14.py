#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 14: Google News article redirect + alternate engines."""
import re, html, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url, ua=None):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", ua or UA, url, "-I"],
                              capture_output=True, text=True, timeout=40).stdout
    except Exception:
        return ""

def fetch_body(url, ua=None):
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

# Google News article redirect with proper params
print("=== gnews redirect HEAD ===")
u = "https://news.google.com/articles/CBMid0FVX3lxTE1yV014cDJiUndJLUhTSnJOMTJ6Tnh1Z3VyOTdLVU1ZRlQ2emRWZEFZT2xhbzUxcFdrcHo?hl=zh-HK&gl=HK&ceid=HK:zh-HK"
print(fetch(u)[:800])

# Try moz search
print("\n=== mojeek ===")
raw = fetch_body("https://www.mojeek.com/search?q=" + urllib.parse.quote("恒大人寿 吊销 保险 业务许可证"))
print(f"len={len(raw)}")
links = re.findall(r'<a[^>]+class="ob"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S)
for l, t in links[:10]:
    print(f"* {html.unescape(re.sub(r'<[^>]+>','',t)).strip()[:80]} | {l[:120]}")

# Try startpage
print("\n=== startpage ===")
raw = fetch_body("https://www.startpage.com/sp/search?query=" + urllib.parse.quote("恒大人寿 吊销 保险许可证"))
print(f"len={len(raw)}")
links = re.findall(r'<a[^>]+href="(https?://[^"]+)"[^>]*class="w-gl__result-url"[^>]*>(.*?)</a>', raw, re.S)
for l, t in links[:10]:
    print(f"* {html.unescape(re.sub(r'<[^>]+>','',t)).strip()[:80]} | {l[:120]}")
