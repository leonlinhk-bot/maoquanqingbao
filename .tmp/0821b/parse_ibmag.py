#!/usr/bin/env python3
import re, html

def links(path, label, domain_filter=None, min_len=20):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    print(f'===== {label} ({len(raw)} bytes) =====')
    if 'Just a moment' in raw[:600]:
        print('  [Cloudflare]')
        return
    seen = set()
    n = 0
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        href = m.group(1)
        txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        txt = re.sub(r'\s+', ' ', txt)
        if len(txt) < min_len:
            continue
        if domain_filter and domain_filter not in href:
            continue
        key = (txt[:60], href[:100])
        if key in seen:
            continue
        seen.add(key)
        ctx = raw[max(0, m.start()-900):m.start()]
        dm = re.findall(r'(20\d{2}[-/.]\d{1,2}[-/.]\d{1,2})', ctx)
        dm2 = re.findall(r'(Aug|Sep|Oct)\s+\d{1,2},\s+20\d{2}', ctx)
        d = dm[-1] if dm else (dm2[-1] if dm2 else '')
        print(f'  [{d}] {txt[:95]}')
        print(f'      {href[:140]}')
        n += 1
        if n >= 45:
            break

links('.tmp/0821/ibmag.html', 'IB-MAG breaking news')
print()
links('.tmp/0821/iaasia_home.html', 'IAASIA home', min_len=25)
