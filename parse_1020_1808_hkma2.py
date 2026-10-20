import json, re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
p = os.path.join(BASE, 'hkma_api.json')
d = json.load(open(p, encoding='utf-8'))
print('keys', list(d.keys())[:10])
res = d.get('result', {})
print('result keys', list(res.keys())[:10] if isinstance(res, dict) else type(res))
recs = res.get('records') if isinstance(res, dict) else None
print('n recs', len(recs) if recs else 0)
for r in (recs or [])[:25]:
    print(r.get('date'), '|', r.get('title_en', r.get('title', ''))[:110])
    print('   ', r.get('link', r.get('url', '')))
