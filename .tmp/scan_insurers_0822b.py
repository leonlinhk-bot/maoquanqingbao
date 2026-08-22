#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, os

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

def scan(name, path, pats, maxn=40):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    print(f"\n===== {name} ({len(raw)}B) =====")
    seen = set(); n = 0
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', text, flags=re.S):
        href, inner = m.group(1), unq(re.sub(r"<[^>]+>", " ", m.group(2)))
        if len(inner) < 8: continue
        key = (href[:80], inner[:40])
        if key in seen: continue
        seen.add(key)
        # recent date markers
        if re.search(r"2026[/-]0?8[/-](1[89]|2[0-2])|2026年8月|Aug(?:ust)?\s+(?:1[89]|2[0-2])|(?:1[89]|2[0-2])\s+Aug|2026-08-2", href + " " + inner):
            print(f"  {inner[:70]:70s} {href[:100]}")
            n += 1
            if n >= maxn: break

scan("AIA newsroom", "data/_raw/t0822b/aia.html", [])
scan("Prudential newsroom", "data/_raw/t0822b/prudential.html", [])
scan("AXA newsroom", "data/_raw/t0822b/axa.html", [])
