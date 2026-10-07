import re, json, html, os
from datetime import datetime, timezone, timedelta
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
HKT=timezone(timedelta(hours=8))
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()

print('===== IA press releases page ====')
t=open(f'{RAW}/ia_press.html',encoding='utf-8',errors='ignore').read()
for m in re.finditer(r'(20\d\d[-/]\d\d[-/]\d\d)\s*</?\w*>?\s*([^<]{10,120})', t):
    print('-', m.group(1), p(m.group(2))[:100])
print('--- raw links ---')
for m in re.finditer(r'href="([^"]+)"[^>]*>([^<]{10,140})<', t):
    print('*', m.group(1)[:90], '|', p(m.group(2))[:90])

print('\n===== IA circulars 2026 ====')
t=open(f'{RAW}/ia_circ.html',encoding='utf-8',errors='ignore').read()
rows=re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.S)
print('rows',len(rows))
for r in rows[:20]:
    cells=[p(c) for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)]
    link=re.search(r'href="([^"]+)"', r)
    print('|', ' ;; '.join(cells)[:170], '=>', (link.group(1) if link else '')[:80])

print('\n===== HKMA press releases ====')
t=open(f'{RAW}/hkma_press.html',encoding='utf-8',errors='ignore').read()
# HKMA page has items with dates like 06 Oct 2026
for m in re.finditer(r'(\d{2}\s+\w{3}\s+20\d\d)(.{0,400}?)href="([^"]+)"', t, re.S):
    txt=p(m.group(2))
    print('-', m.group(1), '|', txt[:120], '=>', m.group(3)[:80])
