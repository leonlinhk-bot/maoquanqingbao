#!/usr/bin/env python3
import re, html

raw = open('.tmp/0821/scmp.html', encoding='utf-8', errors='ignore').read()
# find all scmp links with heading context
pat = re.compile(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', re.S)
matches = list(pat.finditer(raw))
print('total links:', len(matches))
cnt = 0
for m in matches:
    href = m.group(1)
    inner = m.group(2)
    txt = html.unescape(re.sub(r'<[^>]+>', '', inner)).strip()
    txt = re.sub(r'\s+', ' ', txt)
    # only links whose inner text contains heading tags or long text
    if '<h' in inner and len(txt) > 20 and ('insurance' in txt.lower() or 'insurer' in txt.lower() or 'Ping An' in txt or '保' in txt):
        print(f'- {txt[:100]}')
        print(f'  {href[:150]}')
        cnt += 1
        if cnt >= 25:
            break
