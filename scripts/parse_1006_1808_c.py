import re, html, json
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
print('===== IBM Asia =====')
t=open(f'{RAW}/ibm_asia.html',encoding='utf-8',errors='ignore').read()
links=re.findall(r'<a[^>]+href="(/asia/news/[^"]+)"[^>]*>(.*?)</a>', t, re.S)
seen=set()
for h,txt in links:
    txt=p(txt)
    if h in seen or len(txt)<15: continue
    seen.add(h)
    print('-', h, '|', txt[:110])
print('\n===== NFRA index =====')
try:
    t2=open(f'{RAW}/nfra_list.html',encoding='utf-8',errors='ignore').read()
    for m in re.finditer(r'href="([^"]+\.html)"[^>]*>(.{5,120}?)</a>', t2, re.S):
        u=p(m.group(1)); txt=p(m.group(2))
        if any(k in txt for k in ['保险','监管','偿付','通']):
            print('-', txt[:100], '=>', u[:90])
except Exception as e:
    print('err',e)
print('\n===== GOVHK titles sample =====')
t3=open(f'{RAW}/govhk_zh.xml',encoding='utf-8',errors='ignore').read()
ents=re.findall(r'<item[\s>].*?</item>', t3, re.S)
print('items', len(ents))
for e in ents[:100]:
    ti=re.search(r'<title>(.*?)</title>', e, re.S)
    d=re.search(r'<pubDate>(.*?)</pubDate>', e, re.S)
    ln=re.search(r'<link>(.*?)</link>', e, re.S)
    raw = ti.group(1) if ti else ''
    print('-', (d.group(1).strip() if d else ''), '|', raw[:90].replace('\n',' '), '|', (ln.group(1).strip() if ln else '')[:70])
