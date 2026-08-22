#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

for name, path in [("AXA", "data/_raw/t0822b/axa.html"), ("AIA", "data/_raw/t0822b/aia.html"), ("Prudential", "data/_raw/t0822b/prudential.html")]:
    raw = open(path, encoding="utf-8", errors="ignore").read()
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    txt = unq(re.sub(r"<[^>]+>", " ", text))
    print(f"\n===== {name} ({len(raw)}B) =====")
    print("TEXT:", txt[:600])
    # look for date patterns anywhere
    dates = set(re.findall(r"(?:20\d{2}[年/\-]\d{1,2}[月/\-]\d{1,2}日?|Aug(?:ust)?\s+\d{1,2},?\s+2026|\d{1,2}\s+Aug(?:ust)?\s+2026)", txt))
    print("DATES found:", sorted(dates)[:20])
