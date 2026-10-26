import json, re
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher

HKT = timezone(timedelta(hours=8))
d = json.load(open('data/live-items.json'))
items = d['items']

urls = set()
titles = []
for it in items:
    u = (it.get('originalUrl') or '').strip().rstrip('/')
    if u:
        urls.add(u.lower())
    for k in ('sc', 'tc'):
        t = it.get('title', {}).get(k, '')
        if t:
            titles.append(t.lower())

rows = json.load(open('.cache1025_2108/rows.json'))
CUT = datetime(2026, 10, 24, 0, 0, tzinfo=HKT)

def norm(s):
    s = re.sub(r'&#\d+;|&\w+;', ' ', s or '')
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', s.lower())

new = []
for r in rows:
    if not r.get('date'):
        continue
    dt = datetime.fromisoformat(r['date'])
    if dt < CUT:
        continue
    u = (r.get('link') or '').strip().rstrip('/').lower()
    if u and u in urls:
        continue
    nt = norm(r.get('title', ''))
    dup = False
    for t in titles:
        if nt and (nt in norm(t) or norm(t) in nt):
            dup = True
            break
        if nt and SequenceMatcher(None, nt, norm(t)).ratio() > 0.82:
            dup = True
            break
    if not dup:
        new.append(r)

print(f'feed rows since 10-24: {sum(1 for r in rows if r.get("date") and datetime.fromisoformat(r["date"]) >= CUT)}')
print(f'NOT in live-items: {len(new)}\n')
for r in sorted(new, key=lambda x: x['date'], reverse=True):
    print(datetime.fromisoformat(r['date']).strftime('%m-%d %H:%M'), '|', r['src'], '|', r['title'][:110])
    print('    ', r['link'][:130])
