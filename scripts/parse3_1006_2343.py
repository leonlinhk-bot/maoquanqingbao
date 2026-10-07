import re, html, os
R23='/Users/leonliang/maoquanqingbao/data/_raw_1006_2343'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()

def grep_near(fp, urlpat, label, width=260, maxn=25):
    t=open(fp,encoding='utf-8',errors='ignore').read()
    print(f'\n##### {label} :: {urlpat}')
    seen=set(); n=0
    for m in re.finditer(urlpat, t):
        s=max(0,m.start()-width); e=min(len(t), m.end()+width)
        chunk=p(t[s:e])
        key=chunk[:70]
        if key in seen: continue
        seen.add(key)
        print('  ', chunk[:170])
        n+=1
        if n>=maxn: break
    print('  ->', n)

grep_near(os.path.join(R23,'hkma_press.html'), r'href="(?:\.\./)*/?eng/news-and-media/press-releases/2026/1[0-9]/[0-9]{8}-[0-9]+/"', 'HKMA list')
grep_near(os.path.join(R23,'artemis.html'), r'href="https://www\.artemis\.bm/news/[a-z0-9\-]{20,}/"', 'Artemis articles')
