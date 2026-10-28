import json, os
for f in ('data/items.json', 'data/core.json'):
    p = os.path.join('/Users/leonliang/maoquanqingbao', f)
    if not os.path.exists(p):
        print(f, 'MISSING'); continue
    d = json.load(open(p))
    print(f, 'items:', len(d['items']), 'itemCount:', d.get('itemCount'), 'gen:', d.get('generatedAt'), 'mtime:', os.path.getmtime(p))
