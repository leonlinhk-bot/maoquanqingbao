import re, html, os
R23='/Users/leonliang/maoquanqingbao/data/_raw_1006_2343'
R18='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
t=open(f'{R23}/artemis.html',encoding='utf-8',errors='ignore').read()
print('##### Artemis article links')
seen=set()
for m in re.finditer(r'<a href="(https://www\.artemis\.bm/news/[a-z0-9\-]{15,}/)"[^>]*>(.*?)</a>', t, re.S):
    ti=p(m.group(2))
    if len(ti)<20: continue
    if m.group(1) in seen: continue
    seen.add(m.group(1))
    print('  ', ti[:95])
    print('     ', m.group(1))
print('\n##### IBM Asia article links (18:08)')
b=open(f'{R18}/ibm_asia.html',encoding='utf-8',errors='ignore').read()
s2=set()
for m in re.finditer(r'href="(/asia/news/[^"]+\.aspx)"', b):
    if m.group(1) in s2: continue
    s2.add(m.group(1)); print('  ', m.group(1)[:110])
