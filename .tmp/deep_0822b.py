#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(name, url, t=35):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                            "-H", "Accept-Language: en,zh-CN;q=0.9", url],
                           capture_output=True, text=True, timeout=50)
        raw = r.stdout
        open(f"data/_raw/t0822b/{name}.html", "w").write(raw)
        print(f"{'OK' if len(raw)>2000 else 'SMALL'} {len(raw):8d}  {name}")
        return raw
    except Exception as e:
        print(f"ERR {name} {e}")
        return ""

# HKMA scam alert 20260820-4 + PBoC RMB bills 20260821-3 + EF notes tender 20260821-4
fetch("hkma-20260820-4", "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260820-4/")
fetch("hkma-20260821-3", "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260821-3/")

# Full HKMA list page already have; grep all 2026/08 entries + 2026/07 late entries
raw = open("data/_raw/t0822b/hkma-press.html", encoding="utf-8", errors="ignore").read()
text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
seen = set()
print("\n--- HKMA list: all /2026/08/ and /2026/07/ links ---")
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', text, flags=re.S):
    href, inner = m.group(1), html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
    mm = re.search(r"/2026/(0[78])/([0-9]+)", href)
    if mm and (href, inner) not in seen:
        seen.add((href, inner))
        print(f"  {mm.group(1)}/{mm.group(2)}  {inner[:80]:80s} {href[:70]}")

# SunLife list: get full text with dates
raw = open("data/_raw/t0822b/sunlife.html", encoding="utf-8", errors="ignore").read()
text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
text = re.sub(r"<[^>]+>", " ", text)
text = html.unescape(re.sub(r"\s+", " ", text))
# find date tokens near release titles
print("\n--- SunLife page: date-ish tokens ---")
for m in re.finditer(r"(2026[年/-][0-9]{1,2}[月/-][0-9]{1,2}日?|Aug(?:ust)?\s+[0-9]{1,2},?\s+2026|[0-9]{1,2}\s+Aug(?:ust)?\s+2026)", text):
    s = max(0, m.start()-60)
    print("  ...", text[s:m.end()+40].strip()[:130])
