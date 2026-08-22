#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract press-release-ish titles from AIA AEM JSON + check Prudential/SunLife raw for article cards."""
import re, html, json

def scan(fname, name):
    raw = open(fname, encoding="utf-8", errors="ignore").read()
    print(f"== {name}: {len(raw)}b")
    # AEM JSON: find "title" fields with URLs
    titles = re.findall(r'"dc:title":"([^"]{10,120})"', raw)
    seen = []
    for t in titles:
        t2 = html.unescape(t)
        if t2 not in seen:
            seen.append(t2)
    print(f"   dc:title count unique: {len(seen)}")
    for t in seen[:30]:
        print("   T:", t[:110])
    # links with 2026 in URL
    urls = re.findall(r'"xdm:linkURL":"([^"]*2026[^"]*)"', raw)
    print("   links w/ 2026:", len(urls))
    for u in urls[:15]:
        print("   U:", u[:130])

scan(".tmp/aia-press.html", "aia")
print()
scan(".tmp/prudential-press.html", "prudential")
print()
scan(".tmp/sunlife-press.html", "sunlife")
