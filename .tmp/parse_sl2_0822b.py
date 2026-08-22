#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

# 1. get full sunlife release URLs from list page
raw = open("data/_raw/t0822b/sunlife.html", encoding="utf-8", errors="ignore").read()
text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
links = {}
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', text, flags=re.S):
    href, inner = m.group(1), unq(re.sub(r"<[^>]+>", " ", m.group(2)))
    if "news-releases/2026" in href and len(inner) > 12:
        links[inner[:30]] = href
print("SUNLIFE release URLs:")
for k, v in links.items():
    print("  ", k, "->", v)

# 2. parse fetched article pages for dates
def parse_article(name):
    try:
        raw = open(f"data/_raw/t0822b/{name}.html", encoding="utf-8", errors="ignore").read()
    except Exception:
        return
    tm = re.search(r"<title>(.*?)</title>", raw, flags=re.S)
    title = unq(tm.group(1)) if tm else "?"
    dates = set()
    for pat in [r"(\d{4}年\d{1,2}月\d{1,2}日)", r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})', r'"(datePublished|publishedAt)"\s*:\s*"([^"]+)"']:
        for m in re.finditer(pat, raw):
            dates.add(m.group(1) if m.lastindex == 1 else m.group(2))
    txt = unq(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", " ", raw, flags=re.S)))
    print(f"\n{name}: {title[:80]}")
    print("   dates:", sorted(dates)[:6])
    i = txt.find("2026年")
    if i > 0:
        print("   ctx:", txt[max(0,i-80):i+40].strip()[:160])

for n in ["sl-mpf", "sl-hsu", "sl-free-ride", "sl-135", "sl-pw2", "sl-finlit", "sl-col"]:
    parse_article(n)
