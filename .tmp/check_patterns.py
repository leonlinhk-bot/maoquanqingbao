#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check existing HKMA/AIA items + try IA RSS endpoints."""
import json, re, html, subprocess

live = json.load(open('data/live-items.json'))
items = live['items']
print("=== Recent hkma_press items ===")
for it in items[:60]:
    if it.get('sourceKey') == 'hkma_press':
        print(f"- {it['id']} | {it.get('publishedAt')} | {(it.get('title') or {}).get('sc','')[:80]}")
print("\n=== Recent aia items ===")
for it in items[:60]:
    if it.get('sourceKey') == 'aia':
        print(f"- {it['id']} | {it.get('publishedAt')} | {(it.get('title') or {}).get('sc','')[:80]}")
print("\n=== Recent insuranceasia items ===")
for it in items[:60]:
    if it.get('sourceKey') == 'insuranceasia':
        print(f"- {it['id']} | {it.get('publishedAt')} | {(it.get('title') or {}).get('sc','')[:80]}")

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                              capture_output=True, text=True, timeout=35).stdout
    except Exception:
        return ""
print("\n=== IA RSS endpoint attempts ===")
for url in ["https://www.ia.org.hk/en/infocenter/press_releases.rss",
            "https://www.ia.org.hk/en/infocenter/press_releases.xml",
            "https://www.ia.org.hk/rss/press_releases.xml",
            "https://www.ia.org.hk/en/infocenter/press_releases_rss.xml"]:
    raw = fetch(url)
    print(f"{url}: len={len(raw)} head={raw[:120].strip()[:100]}")
