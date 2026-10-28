#!/usr/bin/env python3
import os, re, html
D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030/arts')


def txt(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


for name in ('a1', 'a2'):
    raw = open(f'{D}/{name}.html', encoding='utf-8', errors='replace').read()
    body = txt(raw)
    i = body.find('RenRe') if name == 'a1' else body.find('Aon')
    print('=' * 60, name)
    print(body[1200:4200])
