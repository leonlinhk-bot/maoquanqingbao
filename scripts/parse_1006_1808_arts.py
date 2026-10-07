import re, html
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
def og(t, prop):
    m=re.search(r'<meta[^>]+(?:property|name)="%s"[^>]+content="([^"]*)"'%prop, t, re.I)
    if not m:
        m=re.search(r'<meta[^>]+content="([^"]*)"[^>]+(?:property|name)="%s"'%prop, t, re.I)
    return p(m.group(1)) if m else ''
for f in ['art_fo.html','art_msig.html','art_aon.html','art_india.html','art_meritz.html','art_pruism.html','art_hdi.html']:
    t=open(f'{RAW}/{f}',encoding='utf-8',errors='ignore').read()
    m=re.search(r'<title[^>]*>(.*?)</title>', t, re.S)
    print('=====', f)
    print(' TITLE:', p(m.group(1))[:160] if m else '?')
    print(' OG-DESC:', og(t,'og:description')[:300])
    print(' OG-TITLE:', og(t,'og:title')[:160])
    # first paragraphs
    paras=[p(x) for x in re.findall(r'<p[^>]*>(.*?)</p>', t, re.S)]
    paras=[x for x in paras if len(x)>60]
    for x in paras[:3]:
        print('  P:', x[:320])
print('\n===== hkb sitemap =====')
print(open(f'{RAW}/hkb_sitemap.xml',encoding='utf-8',errors='ignore').read()[:1200])
print('\n===== nfra items =====')
print(p(open(f'{RAW}/nfra_items.html',encoding='utf-8',errors='ignore').read())[:1200])
