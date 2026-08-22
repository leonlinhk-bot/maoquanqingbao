#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

def dump_links(path, name, maxn=60):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    print(f"\n===== {name} =====")
    seen = set()
    n = 0
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', text, flags=re.S):
        href, inner = m.group(1), unq(re.sub(r"<[^>]+>", " ", m.group(2)))
        if len(inner) < 10: continue
        key = (href[:80], inner[:40])
        if key in seen: continue
        seen.add(key)
        # show all that look like dated items
        if re.search(r"20[0-9]{2}|Aug|September|August|July|2026|2025", href + inner):
            print(f"  {inner[:75]:75s} {href[:110]}")
            n += 1
            if n >= maxn: break

dump_links("data/_raw/t0822b/hkma-press.html", "HKMA")
dump_links("data/_raw/t0822b/ibmag.html", "IBMAG")
dump_links("data/_raw/t0822b/sunlife.html", "SunLife")
