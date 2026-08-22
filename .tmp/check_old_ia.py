#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()
for tag, path in [("IA-RSS-OLD", ".tmp/ia-rss.xml"), ("IA-PRESS-OLD", ".tmp/ia-press.html")]:
    try:
        raw = open(path, encoding="utf-8", errors="replace").read()
    except Exception as e:
        print(tag, "ERR", e)
        continue
    print(f"\n===== {tag} ({len(raw)} bytes) =====")
    print(raw[:400])
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    if items:
        print("RSS items:", len(items))
        for it in items[:6]:
            t = re.search(r"<title[^>]*>(.*?)</title>", it, re.S)
            l = re.search(r"<link>(.*?)</link>", it, re.S)
            d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
            print(" -", unq(d.group(1))[:30] if d else "", "|", unq(t.group(1))[:80] if t else "", "|", (l.group(1)[:80] if l else ""))
    body = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    b = unq(body)
    idx = b.find("Press")
    print("BODY:", b[:500])
