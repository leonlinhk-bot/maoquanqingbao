import re, html, os, json
RAW18='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
RAW23='/Users/leonliang/maoquanqingbao/data/_raw_1006_2343'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()

for raw,label in [(RAW18,'18:08'),(RAW23,'23:43')]:
    for f in ['ia_press.html','ia_circ.html','ia_stats.html']:
        path=os.path.join(raw,f)
        if not os.path.exists(path): continue
        t=open(path,encoding='utf-8',errors='ignore').read()
        print(f"\n########## {label} {f} len={len(t)}")
        # find all date-like tokens and nearby anchors
        for m in re.finditer(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
            txt=p(m.group(2))
            if len(txt)<8: continue
            print('  A|', txt[:90], '=>', m.group(1)[:80])
