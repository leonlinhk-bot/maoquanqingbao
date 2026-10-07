import re, html, os
R='/Users/leonliang/maoquanqingbao/data/_raw_1006_2343'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
for f in ['v_mpfa.html','v_govhk_free.html','v_hkma_bnm.html','v_ibm_life.html','v_fo_singtao.html']:
    t=open(os.path.join(R,f),encoding='utf-8',errors='ignore').read()
    ti=re.search(r'<title[^>]*>(.*?)</title>', t, re.S)
    print(f'\n===== {f} :: {p(ti.group(1))[:110] if ti else "(no title)"}')
    # find date-ish and first meaningful body text
    body=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',t)
    txt=p(body)
    print('   ', txt[:400])
