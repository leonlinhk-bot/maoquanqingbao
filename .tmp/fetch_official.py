#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch official pages: IA press, IA circulars, HKMA press, InsuranceAsia RSS."""
import re, html, subprocess, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                              capture_output=True, text=True, timeout=t+10).stdout
    except Exception as e:
        return f"ERR {e}"

pages = {
    "ia_press": "https://www.ia.org.hk/en/infocenter/press_releases.html",
    "ia_circular": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters.html",
    "hkma_press": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/",
    "ia_rss": "https://www.ia.org.hk/en/infocenter/press_releases.xml",
    "iaasia_rss": "https://insuranceasia.com/insurance/rss.xml",
}

for name, url in pages.items():
    raw = fetch(url)
    if raw.startswith("ERR") or len(raw) < 200:
        print(f"== {name}: FETCH FAIL ({raw[:80]})")
        continue
    print(f"== {name}: {len(raw)} bytes")
    # look for date patterns near links
    if name == "hkma_press":
        for m in re.finditer(r'href="(/eng/news-and-media/press-releases/(\d{4}-\d{2}-\d{2})\.html)"[^>]*>([^<]+)</a>', raw):
            print("   ", m.group(2), "|", html.unescape(m.group(3)).strip()[:90], "|", "https://www.hkma.gov.hk"+m.group(1))
    elif name == "ia_circular":
        for m in re.finditer(r'href="([^"]*circulars[^"]*)"[^>]*>([^<]+)</a>', raw):
            txt = html.unescape(m.group(2)).strip()
            if len(txt) > 5:
                print("   ", txt[:100], "|", m.group(1)[:120])
    elif name == "ia_rss":
        for it in re.findall(r"<item>(.*?)</item>", raw, re.S)[:10]:
            t = re.search(r"<title>(.*?)</title>", it, re.S)
            d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
            print("   ", (d.group(1) if d else "?"), "|", html.unescape(t.group(1))[:90] if t else "")
    elif name == "iaasia_rss":
        for it in re.findall(r"<item>(.*?)</item>", raw, re.S)[:15]:
            t = re.search(r"<title>(.*?)</title>", it, re.S)
            d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
            l = re.search(r"<link>(.*?)</link>", it, re.S)
            print("   ", (d.group(1) if d else "?"), "|", html.unescape(t.group(1))[:90] if t else "", "|", (l.group(1)[:100] if l else ""))
    else:  # ia_press
        # press release rows usually have date + title
        for m in re.finditer(r'href="([^"]*press_releases[^"]*)"[^>]*>([^<]+)</a>', raw):
            txt = html.unescape(m.group(2)).strip()
            if len(txt) > 8 and "press_release" not in txt.lower():
                print("   ", txt[:100], "|", m.group(1)[:120])
    print()
