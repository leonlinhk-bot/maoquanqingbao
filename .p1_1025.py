import json, os, sys, re
base = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044/'

def show(name, n=40):
    p = base + name
    if not os.path.exists(p):
        print(f'!! missing {name}'); return
    print('='*20, name, os.path.getsize(p))
    txt = open(p, encoding='utf-8', errors='replace').read()
    try:
        d = json.loads(txt)
        print(json.dumps(d, ensure_ascii=False, indent=1)[:3500])
    except Exception:
        print(txt[:2500])

for f in ['feeds_recent2.json', 'gnews_recent.json', 'ia_sitemap.xml', 'ia_jina.txt']:
    show(f)
