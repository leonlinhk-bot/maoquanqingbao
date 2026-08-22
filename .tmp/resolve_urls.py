#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resolve original URLs via Google News redirects + Bing HTML search."""
import re, html, json, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                              capture_output=True, text=True, timeout=40).stdout
    except Exception:
        return ""

def resolve_gnews(gn_url):
    raw = fetch(gn_url)
    # Google News redirect page contains <a href="real url"> or window.location
    m = re.search(r'href="(https?://[^"]+)"[^>]*>(?:<[^>]+>)*?(?:Visit|前往|阅读)', raw)
    m2 = re.search(r'<a[^>]+href="(https?://(?!news\.google)[^"]+)"', raw)
    if m:
        return html.unescape(m.group(1))
    if m2:
        return html.unescape(m2.group(1))
    return raw[:200]

def bing_html(q):
    raw = fetch("https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&setlang=zh-hk")
    res = re.findall(r'<h2><a href="([^"]+)"[^>]*>(.*?)</a></h2>', raw, re.S)
    if not res:
        res = re.findall(r'<a[^>]+href="(http[^"]+)"[^>]*><h2>(.*?)</h2></a>', raw, re.S)
    out = []
    for u, t in res[:6]:
        t = html.unescape(re.sub(r'<[^>]+>', '', t)).strip()
        out.append((t, u))
    return out

# 1. Hengda license revocation (點新聞 gnews link)
print("=== 1. HENGDA resolve ===")
u = "https://news.google.com/rss/articles/CBMiekFVX3lxTFB5Yjk0QWNOWktSQ2lyVjl3X1BZWGpDOHA3THMtbDM2Yzc4Vkk4dzFPVzdCdTlMbzAtUVpjNktyTGttOVZ0OVpJb1d5czRTS1BSS"
print("gnews->", resolve_gnews(u)[:300])
print("\nBing HTML:")
for t, u2 in bing_html("恒大人寿 吊销 保险业务许可 金融监管总局"):
    print(f"* {t[:80]} | {u2[:140]}")

# 2. UBS AIA target
print("\n=== 2. UBS AIA ===")
u = "https://news.google.com/rss/articles/CBMicEFBVV95cUxOb2tEWFZ0a1NvVnpzUUh0ZmdDVElOdjJwVkdmWUF1bmZKc1JCMGE5cm1jNm5EaGF1Qlk2a24zTlZ0SlJfZzJyU3RDaU9ESWU3b"
print("gnews->", resolve_gnews(u)[:300])
print("\nBing HTML:")
for t, u2 in bing_html("瑞银 友邦 目标价 102港元 买入"):
    print(f"* {t[:80]} | {u2[:140]}")

# 3. HKEJ AIA tax
print("\n=== 3. HKEJ AIA ===")
u = "https://news.google.com/rss/articles/CBMitwJBVV95cUxPZlJCQ2ZhQ0FBT2xQdnUyNTBYaEJQRW56cGZIMjRCMXJFcTRVenpjNi15bXFnNmItTVlSYzZkeC00MER1dDltNm5ZdVlncVdQc"
print("gnews->", resolve_gnews(u)[:300])

# 4. Manulife AIRSIDE etnet
print("\n=== 4. Manulife AIRSIDE ===")
u = "https://news.google.com/rss/articles/CBMiggRBVV95cUxNWHlpMF9wWDJrTGhraHZWRDJ6ZzR6YUxfSF9GSHBnR1RTRjd6bTVydHRuRGdnM2ZXTHZsN3pzeU9sbGhTTVQ5QjdNM3FZQ05Uc"
print("gnews->", resolve_gnews(u)[:300])

# 5. Silver bond
print("\n=== 5. Silver bond ===")
u = "https://news.google.com/rss/articles/CBMiYkFVX3lxTFBFdC00Rl8xMHc2ZU1fX0FkSXpLdmJKdExRSVZOYTJBVmhsME05RGVHQ1QzRnlkZmhzZ2FoZEx6eWZJVWVtMTlaLWdwazk5aUFsM"
print("gnews->", resolve_gnews(u)[:300])
