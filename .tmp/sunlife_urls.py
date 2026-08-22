#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract exact SunLife release URLs + look for dates near them; check WB IA press data URL."""
import re, html, subprocess

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

raw = open("data/_raw/t0822-sunlife.html", encoding="utf-8", errors="replace").read()
print("=== SunLife full release URLs + context dates ===")
seen = set()
for m in re.finditer(r'<a[^>]+href="(/zh-hant/about-us/newsroom/news-releases/2026/[^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    href, txt = m.group(1), unq(m.group(2))
    if href in seen or len(txt) < 10:
        continue
    seen.add(href)
    s = max(0, m.start()-600)
    ctx = raw[s:m.start()]
    dm = re.findall(r"(20\d\d[-/.]\d{1,2}[-/.]\d{1,2}|[A-Z][a-z]{2}\s+\d{1,2},?\s+20\d\d|\d{1,2}\s+[A-Z][a-z]{2}\s+20\d\d)", ctx)
    print("-", dm[:3], "|", href, "|", txt[:70])

print("\n=== WB IA press: look for data/api URLs ===")
raw = open("data/_raw/t0822-wb-ia-press.html", encoding="utf-8", errors="replace").read()
for m in re.findall(r'(?:src|href|data-url|action)="([^"]+)"', raw):
    if any(k in m for k in ["api", "json", "ajax", "press", "list", "feed", "rss"]):
        print("  ", m[:160])
for m in re.findall(r"[\w./-]*press[\w./-]*\.(?:json|xml|js|php)[^\"']*", raw):
    print("  PAT:", m[:160])
