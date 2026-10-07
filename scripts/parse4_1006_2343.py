import re, html, os, json
from datetime import datetime, timezone, timedelta
R23='/Users/leonliang/maoquanqingbao/data/_raw_1006_2343'
R18='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
HKT=timezone(timedelta(hours=8))
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()

# ---- 1. insuranceasianews wp-json
print('##### IAN wp-json (fresh)')
j=json.load(open(f'{R23}/ian.json',encoding='utf-8'))
for it in j[:16]:
    print('  ', it.get('date'), '|', p(it['title']['rendered'])[:78], '|', it.get('link'))

# ---- 2. IBM Asia cache (18:08) article cards
print('\n##### IBM Asia cards (18:08 cache)')
t=open(f'{R18}/ibm_asia.html',encoding='utf-8',errors='ignore').read()
seen=set()
for m in re.finditer(r'href="(/asia/news/[^"]+\.aspx)"[^>]*>\s*([^<]{15,140})</', t):
    url, ti = m.group(1), p(m.group(2))
    if ti in seen: continue
    seen.add(ti); print('  ', ti[:88], '=>', url[:80])
print('  total', len(seen))

# ---- 3. GovHK RSS titles
print('\n##### GovHK RSS titles (fresh)')
g=open(f'{R23}/govhk_zh.xml',encoding='utf-8',errors='ignore').read()
ents=re.findall(r'<item[\s>].*?</item>', g, re.S)
print('  items:', len(ents))
for e in ents[:14]:
    ti=re.search(r'<title>\s*(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?\s*</title>', e, re.S)
    d=re.search(r'<pubDate>(.*?)</pubDate>', e, re.S)
    ln=re.search(r'<link>(.*?)</link>', e, re.S)
    print('  ', p(d.group(1)) if d else '', '|', p(ti.group(1))[:88] if ti else '(no title)', '|', p(ln.group(1))[:70] if ln else '')

# ---- 4. IA circular list (18:08 cache) - newest
print('\n##### IA circular (18:08 cache) newest')
c=open(f'{R18}/ia_circ.html',encoding='utf-8',errors='ignore').read()
for m in re.finditer(r'<a\s[^>]*href="(files/[^"]+)"[^>]*>(.*?)</a>', c, re.S):
    txt=p(m.group(2))
    if len(txt)<15: continue
    print('  ', txt[:88], '=>', m.group(1)[:80])
