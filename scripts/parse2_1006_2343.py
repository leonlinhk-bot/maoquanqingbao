import re, html, os, json
from datetime import datetime, timezone, timedelta
R23='/Users/leonliang/maoquanqingbao/data/_raw_1006_2343'
R18='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()

def show(path, raw, label, pats, maxn=26):
    fp=os.path.join(raw,path)
    if not os.path.exists(fp): print(f'\n##### {label} MISSING'); return
    t=open(fp,encoding='utf-8',errors='ignore').read()
    print(f'\n##### {label} ({path}, {len(t)}b)')
    seen=set()
    n=0
    for m in re.finditer(pats, t, re.S):
        if m.lastindex and m.lastindex>=2:
            url, txt = m.group(1), p(m.group(2))
        else:
            url, txt = m.group(1), ''
        if len(txt) < 12: continue
        key=txt[:60]
        if key in seen: continue
        seen.add(key)
        print('  ', txt[:92], '=>', url[:95])
        n+=1
        if n>=maxn: break
    print(f'  -> {n} rows')

A = r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>'
show('hkma_press.html',R23,'HKMA press',A,20)
show('artemis.html',R23,'Artemis',A,20)
show('hkfi.html',R23,'HKFI',A,14)
show('mpfa.html',R23,'MPFA',A,14)
show('axa.html',R23,'AXA-HK',A,14)
show('aia.html',R18,'AIA-HK(18:08)',A,14)
show('manulife.html',R18,'Manulife-HK(18:08)',A,10)
show('prudential.html',R18,'Prudential-HK(18:08)',A,14)
show('sunlife.html',R18,'SunLife-HK(18:08)',A,14)
show('ibm_asia.html',R18,'IBM Asia(18:08)',A,26)
show('nfra_list.html',R18,'NFRA list(18:08)',A,16)
