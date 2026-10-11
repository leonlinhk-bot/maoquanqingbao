import re, json, os, html
from datetime import datetime, timezone, timedelta

D='.tmp/1012_0022'
HKT=timezone(timedelta(hours=8))
now=datetime.now(HKT)
cut=now - timedelta(hours=30)

def show(title, lines):
    print('='*20, title, '='*20)
    for l in lines:
        print(l)

# --- govhk RSS ---
try:
    t=open(f'{D}/govhk.xml',encoding='utf-8').read()
    items=re.findall(r'<item>(.*?)</item>', t, re.S)
    out=[]
    for it in items:
        ti=re.search(r'<title>(.*?)</title>', it, re.S)
        ln=re.search(r'<link>(.*?)</link>', it, re.S)
        pd=re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        if not pd: continue
        out.append((pd.group(1), (ti.group(1) if ti else '')[:90], (ln.group(1) if ln else '')[:110]))
    show('govhk RSS count=%d'%len(out), ['%s | %s | %s'%o for o in out[:30]])
except Exception as e:
    print('govhk err', e)

# --- insuranceasia RSS ---
try:
    t=open(f'{D}/iaasia2.xml',encoding='utf-8').read()
    items=re.findall(r'<item>(.*?)</item>', t, re.S)
    out=[]
    for it in items:
        ti=re.search(r'<title>(.*?)</title>', it, re.S)
        ln=re.search(r'<link>(.*?)</link>', it, re.S)
        pd=re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        out.append(((pd.group(1) if pd else ''), (ti.group(1) if ti else '')[:100], (ln.group(1) if ln else '')[:120]))
    show('insuranceasia RSS count=%d'%len(out), ['%s | %s | %s'%o for o in out[:25]])
except Exception as e:
    print('iaasia err', e)

# --- insuranceasianews wp json ---
try:
    j=json.load(open(f'{D}/ianews.json',encoding='utf-8'))
    show('ianews.json count=%d'%len(j), ['%s | %s | %s'%(p.get('date',''), html.unescape(re.sub('<[^>]+>','',p['title']['rendered']))[:95], p.get('link','')[:110]) for p in j[:20]])
except Exception as e:
    print('ianews err', e)
