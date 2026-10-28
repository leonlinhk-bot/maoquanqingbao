#!/usr/bin/env python3
import re, os
D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030/arts')
for name in ('c1', 'c5', 'c6'):
    raw = open(f'{D}/{name}.html', encoding='utf-8', errors='replace').read()
    print('=' * 40, name)
    for m in re.finditer(r'(\d+ (?:minutes?|hours?|days?) ago)', raw):
        s = max(0, m.start() - 220)
        print('  CTX:', re.sub(r'<[^>]+>', ' ', raw[s:m.end() + 60]).replace('\n', ' ')[-260:])
        print('  ---')
    for m in re.finditer(r'2026-10-28T06:00:00\+0800|20\d\d-\d\d-\d\dT\d\d:\d\d:\d\d\+\d\d:?\d\d', raw):
        s = max(0, m.start() - 160)
        print('  TS:', re.sub(r'<[^>]+>', ' ', raw[s:m.end() + 80]).replace('\n', ' ')[-230:])
        print('  ...')
        break
