import re, html, json
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
def title(path):
    t=open(f'{RAW}/{path}',encoding='utf-8',errors='ignore').read()
    m=re.search(r'<title[^>]*>(.*?)</title>', t, re.S)
    d=re.search(r'(?:Date|date|Published|publish)[^<]{0,40}?(\d{1,2}\s+\w+\s+20\d\d|\d{4}-\d\d-\d\d)', t)
    print('==',path,'|',p(m.group(1))[:130] if m else 'NO TITLE', '| datehint:', d.group(1) if d else '-')
    body=re.sub(r'<script.*?</script>','',t,flags=re.S)
    txt=p(body)
    print('   first:', txt[:400])
for f in ['hkma1006_4.html','hkma1006_3.html','ibm_hdi.html']:
    title(f)
print('\n===== insurer newsrooms =====')
import os
for f in ['aia.html','prudential.html','axa.html','sunlife.html']:
    t=open(f'{RAW}/{f}',encoding='utf-8',errors='ignore').read()
    print('---', f, len(t))
    # find date-like + nearby link text
    cands=[]
    for m in re.finditer(r'(20\d\d[-/年]\s?\d{1,2}[-/月]\s?\d{1,2})[^<]{0,200}', t):
        seg=p(m.group(0))
        cands.append((m.group(1), seg[:110]))
    for c in cands[:14]:
        print('  ', c[0], '|', c[1])
print('\n===== SCMP insurance topic =====')
t=open(f'{RAW}/scmp_insurance.html',encoding='utf-8',errors='ignore').read()
for m in re.finditer(r'href="(/[^"]*article/\d+[^"]*)"[^>]*>(.{5,150}?)</a>', t, re.S):
    s=p(m.group(2))
    if len(s)>20 and 'utm' not in m.group(1)[:20]:
        print('-', s[:100], '=>', m.group(1)[:80])
print('\n===== FSTB =====')
print(p(open(f'{RAW}/fstb.html',encoding='utf-8',errors='ignore').read())[:700])
print('\n===== IA stats =====')
print(p(open(f'{RAW}/ia_stats.html',encoding='utf-8',errors='ignore').read())[:500])
