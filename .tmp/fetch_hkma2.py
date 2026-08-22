#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract main article text from HKMA press release pages."""
import re, html, subprocess

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True, timeout=40).stdout

def article_text(raw):
    # HKMA puts article in div with class containing "article" or main content
    m = re.search(r'<div[^>]*class="[^"]*(?:article|content-main|press-release|news-detail)[^"]*"[^>]*>(.*?)</div>\s*</div>', raw, re.S)
    if not m:
        # fallback: find between <h1 and footer
        m = re.search(r'(<h1.*?</h1>.*?)(?:<footer|<!--|Related)', raw, re.S)
    seg = m.group(1) if m else raw
    seg = re.sub(r'<script.*?</script>', ' ', seg, flags=re.S)
    seg = re.sub(r'<style.*?</style>', ' ', seg, flags=re.S)
    seg = re.sub(r'<[^>]+>', ' ', seg)
    seg = html.unescape(seg)
    seg = re.sub(r'\s+', ' ', seg).strip()
    return seg

for slug, label in [("20260820-4", "HKMA scam alert banks"),
                    ("20260821-3", "HKMA PBOC RMB bills"),
                    ("20260821-4", "HKMA Exchange Fund Notes Tender")]:
    raw = fetch(f"https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/{slug}/")
    txt = article_text(raw)
    print(f"\n=== {label} ===")
    print(txt[:1500])
