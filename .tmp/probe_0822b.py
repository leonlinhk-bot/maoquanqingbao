#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

for name, path in [("IAA-rss", "data/_raw/t0822b/wb-iaa-rss.html"),
                   ("HKMA", "data/_raw/t0822b/hkma-press.html"),
                   ("WB-IA-press2", "data/_raw/t0822b/wb-ia-press2.html"),
                   ("WB-IA-press-big", "data/_raw/t0822b/wb-ia-press.html"),
                   ("WB-IA-circ", "data/_raw/t0822b/wb-ia-circ.html"),
                   ("FSTB", "data/_raw/t0822b/wb-fstb-press.html")]:
    raw = open(path, encoding="utf-8", errors="ignore").read()
    print(f"\n===== {name} ({len(raw)}B) =====")
    # first: is it an RSS feed?
    if "<rss" in raw[:500] or "<feed" in raw[:500]:
        print("RSS detected. items:", raw.count("<item>"))
        for m in list(re.finditer(r"<item>(.*?)</item>", raw, flags=re.S))[:6]:
            b = m.group(1)
            t = re.search(r"<title>(.*?)</title>", b, flags=re.S)
            d = re.search(r"<pubDate>(.*?)</pubDate>", b, flags=re.S)
            l = re.search(r"<link>(.*?)</link>", b, flags=re.S)
            print("  -", unq(re.sub(r"<[^>]+>", "", t.group(1) if t else ""))[:70],
                  "|", unq(d.group(1) if d else ""),
                  "|", unq(l.group(1) if l else "")[:90])
        continue
    # count <a> links
    links = re.findall(r'<a[^>]+href="([^"]+)"', raw)
    print("links:", len(links))
    # show first 500 chars of body text
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = unq(text)
    print("BODY:", text[:400])
