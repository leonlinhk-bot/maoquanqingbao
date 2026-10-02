import json
d = json.load(open('data/live-items.json'))
items = d['items']
for k in ['ai-trust', 'ai trust', '客戶數據', '客户数据', 'customer-specific', 'GenA.I. 沙盒', '沙盒++', 'Insurers told']:
    hits = [it['id'] for it in items if k.lower() in json.dumps(it, ensure_ascii=False).lower()]
    print(f'{k}: {len(hits)} -> {hits[:8]}')
