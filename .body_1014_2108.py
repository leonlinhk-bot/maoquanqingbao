#!/usr/bin/env python3
import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1014_2108'


def paras(path, needle=None):
    raw = open(path, encoding='utf-8', errors='replace').read()
    out = []
    for m in re.finditer(r'(?is)<p[^>]*>(.*?)</p>', raw):
        t = html.unescape(re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', m.group(1)))).strip()
        if len(t) > 45:
            out.append(t)
    return out


for f in ['iaasia_tataaia', 'iaasia_sunlife_ph', 'art_karenclark']:
    ps = paras(f'{D}/{f}.html')
    print(f'\n===== {f} ({len(ps)} paras) =====')
    for p in ps[:6]:
        print(' *', p[:420])
