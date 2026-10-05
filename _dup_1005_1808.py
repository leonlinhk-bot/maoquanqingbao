import json, re
d = json.load(open('data/live-items.json'))
items = d['items']
KW = ['cheung', 'reappoint', 'ba-kai', 'bakai', 'cargo', 'data centre', 'data center', 'drought', 'aerospace', 'cyber',
      'korean re', 'di pasquale', 'bajaj', 'parametric', 'ucits', 'eaton vance', 'life science', 'unimed',
      ' disciplinary panel', 'panel pool', 'expert advisor', 'z世代', 'mpf 投資組合', 'gen z']
for i in items:
    blob = json.dumps(i, ensure_ascii=False).lower()
    hit = [k for k in KW if k.lower() in blob]
    if hit:
        print('  ', i.get('publishedAt'), '|', i.get('sourceKey'), '|', i.get('id'), '| HIT:', hit)
