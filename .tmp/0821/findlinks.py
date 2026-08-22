#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grep saved HTML for article links; fetch pages."""
import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def fetch(url):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                           capture_output=True, text=True, timeout=35)
        return r.stdout
    except Exception:
        return ""

# 1. AIR article links for Changsheng / healthcare plan
raw = open('.tmp/0821/air-news.html', encoding='utf-8', errors='replace').read()
for pat in ['Changsheng', 'healthcare insurance plan', 'healthcare']:
    for m in re.finditer(r'href="(/News/View-NewsLetter-Article/[^"]*)"[^>]*>([^<]{10,110})', raw):
        href, txt = m.group(1), m.group(2).strip()
        if pat.lower() in txt.lower():
            print(f"AIR: {txt} -> https://www.asiainsurancereview.com{href}")

# 2. Asia Insurance Post: fetch news list, grep Fitch
h = fetch("https://www.asiainsurancepost.com/news")
print(f"\nAIPost size={len(h)}")
for m in re.finditer(r'href="(https://www\.asiainsurancepost\.com/[^"]+)"[^>]*>(.*?)</a>', h, re.S):
    t = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
    if len(t) > 20 and ('Fitch' in t or 'China' in t or 'insurance' in t.lower()):
        print(f"AIP: {t[:90]} -> {m.group(1)[:150]}")
