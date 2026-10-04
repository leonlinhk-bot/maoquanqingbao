# -*- coding: utf-8 -*-
import json, re, datetime
print('weekday:', datetime.date(2026,10,4).strftime('%A'))

raw = json.load(open('data/_raw_1004_2108.json', encoding='utf-8'))

def scan(key, pat):
    txt = raw.get(key, {}).get('text', '')
    if not txt:
        print(key, 'NO TEXT (', raw.get(key, {}).get('error'), ')')
        return
    print(f'=== {key} ===')
    for m in list(re.finditer(pat, txt))[:12]:
        s = max(0, m.start()-160); e = m.end()+80
        print('  ', re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', txt[s:e])).strip()[:180])

scan('govhk_zh', r'(2026-10-0[34]|0[34]/10/2026|2026年10月0?[34]日)')
for k in ['aia_news', 'prudential_news', 'axa_news', 'sunlife_news']:
    scan(k, r'(Oct(ober)?\s*0?[1-4],?\s*2026|2026-10-0[1-4]|0?[1-4]\.10\.2026|2026年10月0?[1-4]日)')
print()
print('=== raw availability ===')
for k, v in raw.items():
    print(' ', k, 'ERR' if 'error' in v else len(v.get('text','')), v.get('error',''))
