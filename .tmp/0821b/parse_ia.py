#!/usr/bin/env python3
import re, html, glob, os

for f in sorted(glob.glob('.tmp/0821b/ia_*.html')):
    print('====', f, os.path.getsize(f))
    txt = open(f, encoding='utf-8', errors='ignore').read()
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{4,200})</a>', txt)
    for h, t in links[:40]:
        print(' -', html.unescape(t).strip()[:90], '||', h[:120])
    if not links:
        print('NO LINKS; head:', txt[:500].replace('\n',' '))
