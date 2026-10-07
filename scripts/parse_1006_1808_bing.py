import re, html
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
for f in ['bing_bochk.html','bing_mpfa.html','bing_aia.html','bing_hsbc.html','bing_fo.html','bing_nfra.html']:
    print('\n=====', f)
    t=open(f'{RAW}/{f}',encoding='utf-8',errors='ignore').read()
    blocks=re.findall(r'<li class="b_algo".*?</li>', t, re.S)
    print('results:', len(blocks))
    for b in blocks[:6]:
        m=re.search(r'<h2[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if not m: continue
        url=html.unescape(m.group(1)); title=p(m.group(2))
        sn=re.search(r'<p[^>]*>(.*?)</p>', b, re.S)
        print('-', title[:95])
        print('   ', url[:150])
        if sn: print('   ', p(sn.group(1))[:170])
