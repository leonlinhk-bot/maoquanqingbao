#!/usr/bin/env python3
import re, html, json, sys

def extract_hkma(path):
    h = open(path, encoding='utf-8', errors='ignore').read()
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{5,160})</a>', h)
    seen = set()
    out = []
    for href, txt in links:
        txt = html.unescape(txt).strip()
        if 'press-releases' in href and ('2026' in txt or '2026' in href):
            key = (href, txt)
            if key not in seen:
                seen.add(key)
                out.append({'href': href, 'txt': txt})
    return out

if __name__ == '__main__':
    out = extract_hkma('.tmp/0821b/hkma.html')
    print('TOTAL:', len(out))
    for o in out[:40]:
        print(o['txt'][:90], '||', o['href'][:120])
