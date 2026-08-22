#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, os

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

for name in ["sl-mpf", "sl-hsu", "sl-free-ride", "sl-135", "sl-pw2", "sl-finlit", "sl-col"]:
    path = f"data/_raw/t0822b/{name}.html"
    raw = open(path, encoding="utf-8", errors="ignore").read()
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    txt = unq(re.sub(r"<[^>]+>", " ", text))
    # title
    tm = re.search(r"<title>(.*?)</title>", raw, flags=re.S)
    title = unq(tm.group(1)) if tm else ""
    # date: look for 2026年X月X日 / 2026-XX-XX / datePublished
    dm = re.search(r"(20\d{2}[年/\-]\d{1,2}[月/\-]\d{1,2}日?)", txt)
    dm2 = re.search(r'"datePublished"\s*:\s*"([^"]+)"', raw)
    dm3 = re.search(r"(?:2026年\d{1,2}月\d{1,2}日)", txt)
    date = (dm3 or dm or dm2)
    print(f"{name}: TITLE={title[:90]}")
    if date:
        print(f"   DATE: {date.group(1) if hasattr(date,'group') else date}")
    # search for date in whole raw with meta
    for pat in [r'"datePublished"\s*:\s*"([^"]+)"', r"property=\"article:published_time\" content=\"([^\"]+)\"", r"datetime=\"([^\"]+)\""]:
        m = re.search(pat, raw)
        if m:
            print(f"   META: {m.group(1)[:40]}")
            break
    # first 300 chars of body
    body_start = txt.find(title[:20]) if title else -1
    print("   BODY:", txt[max(0,body_start):body_start+280].strip()[:280].replace("\n"," "))
    print()
