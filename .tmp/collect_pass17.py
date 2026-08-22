#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 17: direct URL patterns for hkej/etnet/silverbond/ubs stories."""
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

# etnet news listing
print("=== etnet finance news ===")
raw = fetch("https://www.etnet.com.hk/www/tc/news/allnews.php")
print(f"len={len(raw)}")
links = re.findall(r'href="([^"]*(?:news|article)[^"]*)"[^>]*>([^<]{10,110})</a>', raw)
for u, t in links[:20]:
    t = html.unescape(t).strip()
    print(f"- {t[:75]} | {u[:110]}")

# hkej today listing
print("\n=== hkej finance ===")
raw = fetch("https://www.hkej.com/landing/finance")
print(f"len={len(raw)}")
links = re.findall(r'href="(/landing/article[^"]*)"[^>]*>([^<]{10,110})</a>', raw)
for u, t in links[:20]:
    t = html.unescape(t).strip()
    print(f"- {t[:75]} | https://www.hkej.com{u[:110]}")

# Now news
print("\n=== now news finance ===")
raw = fetch("https://news.now.com/home/finance")
print(f"len={len(raw)}")
links = re.findall(r'href="(https://news\.now\.com/home/finance/player\?newsId=[^"]+)"[^>]*>([^<]{10,110})</a>', raw)
for u, t in links[:10]:
    t = html.unescape(t).strip()
    print(f"- {t[:75]} | {u[:110]}")
