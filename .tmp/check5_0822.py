#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()
for tag, path in [("WB-IA-PRESS", "data/_raw/t0822-wb-ia-press.html"),
                  ("WB-IA-CIRC", "data/_raw/t0822-wb-ia-circ.html"),
                  ("WB-IBMAG", "data/_raw/t0822-wb-ib-aia.html")]:
    raw = open(path, encoding="utf-8", errors="replace").read()
    print(f"\n===== {tag} ({len(raw)}) =====")
    body = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    print(unq(body)[:700])
print("\n===== SUNLIFE PW page: title/date/json =====")
raw = open("data/_raw/t0822-sl-pw.html", encoding="utf-8", errors="replace").read()
for pat in [r"<title>(.*?)</title>", r"2026[-/年]\d{1,2}[-/月]\d{1,2}", r'"datePublished"[^,]{0,60}', r'"publishDate"[^,]{0,60}', r'"(?:title|headline)"\s*:\s*"([^"]{10,150})"']:
    ms = re.findall(pat, raw, re.S)
    print(f"--- {pat[:40]}: {len(ms)}")
    for m in ms[:6]:
        print("   ", unq(m if isinstance(m, str) else m)[:140])
