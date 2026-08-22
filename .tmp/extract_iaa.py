#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract IAA article title/date/body + aastocks content."""
import re, html

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

def extract(path, label):
    raw = open(path, encoding="utf-8", errors="replace").read()
    print(f"\n########## {label} ({len(raw)} bytes) ##########")
    t = re.search(r"<title>(.*?)</title>", raw, re.S)
    print("TITLE:", unq(t.group(1))[:160] if t else "")
    og = re.search(r'property="og:title"\s+content="([^"]+)"', raw)
    if og: print("OG:", unq(og.group(1))[:160])
    # date
    for pat in [r'"datePublished"\s*:\s*"([^"]+)"', r'"dateModified"\s*:\s*"([^"]+)"',
                r'(\d{1,2}\s+[A-Z][a-z]{2,8}\s+20\d\d)', r'([A-Z][a-z]{2,8}\s+\d{1,2},?\s+20\d\d)',
                r'(20\d\d[-/]\d{1,2}[-/]\d{1,2})']:
        ms = re.findall(pat, raw)
        if ms:
            print(f"DATES[{pat[:26]}]:", ms[:6])
    # main content
    body = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    body = re.sub(r"<style.*?</style>", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    body = unq(body)
    for kw in ["article", "story"]:
        pass
    # print from first sentence after title area
    print("BODY[0:2200]:", body[:2200])

extract("data/_raw/t0822-iaa-offshore.html", "IAA OFFSHORE REINSURANCE")
extract("data/_raw/t0822-iaa-jplc.html", "IAA JAPANESE LIFE PRIVATE CREDIT")
extract("data/_raw/t0822-pingan-aastocks.html", "AASTOCKS PINGAN")
