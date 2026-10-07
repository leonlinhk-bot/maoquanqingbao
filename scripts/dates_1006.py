import re, html, os
R23='/Users/leonliang/maoquanqingbao/data/_raw_1006_2343'
R18='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
cands = [(R23,'v_ibm_life.html'),(R18,'art_hdi.html'),(R23,'v_hkma_bnm.html'),
         (R18,'ibm_hdi.html'),(R23,'v_mpfa.html')]
for raw,f in cands:
    fp=os.path.join(raw,f)
    if not os.path.exists(fp): print(f'{f} MISSING'); continue
    t=open(fp,encoding='utf-8',errors='ignore').read()
    print(f'\n===== {f}')
    # ISO dates, JSON-LD datePublished, meta published
    for m in re.finditer(r'(datePublished|dateModified|"date"|publishedAt|article:published_time)[^,>]{0,80}', t):
        s=m.group(0)
        if re.search(r'20\d\d-\d\d-\d\d', s): print('   ', s[:120])
    # visible date strings
    txt=p(re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',t))
    for m in re.finditer(r'(?:October|Oct\.?)\s+\d{1,2},?\s+2026|2026-\d\d-\d\d|\d{1,2}\s+October\s+2026', txt):
        print('   vis:', txt[max(0,m.start()-70):m.end()+40][:150])
