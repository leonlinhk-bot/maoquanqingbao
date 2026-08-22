#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse fetched pages: extract dated entries (2026-08-20 21:00+)."""
import re, html, json, glob, os

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

def list_dir(path):
    return sorted(os.listdir(path)) if os.path.isdir(path) else []

def show(name, path, pats, maxn=25):
    try:
        raw = open(path, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        print(f"{name}: READ ERR {e}")
        return
    print(f"\n===== {name} ({len(raw)} bytes) =====")
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    # find date-ish tokens near links
    seen = set()
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', text, flags=re.S):
        href, inner = m.group(1), unq(re.sub(r"<[^>]+>", " ", m.group(2)))
        if len(inner) < 8 or not href.startswith("http"):
            continue
        if any(p in href + " " + inner for p in pats):
            # date check: 2026-08-2x or 21 Aug / 22 Aug
            has_date = bool(re.search(r"2026-08-2[012]|2026-08-2[12]|21 Aug|22 Aug|20 Aug", href + " " + inner))
            key = (href[:80], inner[:40])
            if key in seen: continue
            seen.add(key)
            mark = " <== DATE" if has_date else ""
            print(f"  {inner[:70]:70s} {href[:90]}{mark}")

# IA press (small, check structure first)
show("ia-press", "data/_raw/t0822b/ia-press.html", ["press", "Press", "新闻", "20", "21", "22"])
show("ia-circ2026", "data/_raw/t0822b/ia-circ2026.html", ["circular", "通函", "2026"])
show("ia-insurtech", "data/_raw/t0822b/ia-insurtech.html", ["insurtech", "Insurtech", "task", "Task"])
show("fstb", "data/_raw/t0822b/fstb.html", ["press", "Press", "news", "News", "20", "21", "22"])
