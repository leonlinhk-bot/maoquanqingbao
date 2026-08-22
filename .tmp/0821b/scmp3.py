#!/usr/bin/env python3
import re, html

raw = open('.tmp/0821/scmp.html', encoding='utf-8', errors='ignore').read()
targets = ['Ping An', 'Mainland Chinese investors', 'Beijing urges', 'tax shift', 'regional clientele',
           'reappoint', 'HSBC reshuffles', 'Don\'t panic', 'slid following', 'wealth to next generation',
           'affluent buyers', 'Shenzhen aircraft', 'weather Beijing']
seen = set()
for m in re.finditer(r'<a[^>]+href="(https://www\.scmp\.com/[^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    href = m.group(1)
    txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
    txt = re.sub(r'\s+', ' ', txt)
    if len(txt) < 25:
        continue
    for t in targets:
        if t.lower() in txt.lower():
            key = (txt[:60], href[:90])
            if key in seen:
                continue
            seen.add(key)
            ctx = raw[max(0, m.start()-1000):m.start()]
            dm = re.findall(r'(\d{4}-\d{1,2}-\d{1,2})', ctx)
            dm2 = re.findall(r'([A-Z][a-z]{2,8} \d{1,2}, 20\d{2})', ctx)
            d = dm[-1] if dm else (dm2[-1] if dm2 else '')
            print(f'[{d}] {txt[:95]}')
            print(f'    {href}')
            break
