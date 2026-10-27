#!/usr/bin/env python3
"""SCMP RSS: items dated 27 Oct 2026, flag insurance/finance relevance."""
import re, urllib.request, html

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0"}
req = urllib.request.Request("https://www.scmp.com/rss/92/feed", headers=UA)
x = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')

items = re.findall(r'<item>(.*?)</item>', x, re.S)
print("items:", len(items))
KW = ['insur', 'annuit', 'pension', 'MPF', 'wealth', 'family office', 'reinsur', 'underwrit', 'actuar', 'health']
for it in items:
    t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
    d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    l = re.search(r'<link>(.*?)</link>', it, re.S)
    ti = html.unescape(t.group(1)).strip() if t else ''
    dd = d.group(1).strip() if d else ''
    ll = l.group(1).strip() if l else ''
    if '27 Oct 2026' in dd or '26 Oct 2026' in dd:
        flag = '<<' if any(k.lower() in ti.lower() for k in KW) else '  '
        print(f"{flag} {dd[:22]} | {ti[:95]} | {ll[:95]}")
