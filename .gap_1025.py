import json
from datetime import datetime

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
known_ids = {i['id'] for i in d['items']}
known_urls = {(i.get('originalUrl') or '').split('?')[0] for i in d['items']}

def check(path, label):
    items = json.load(open(path))
    print(f'===== {label}')
    for i in items:
        dt = (i.get('dt') or '')[:10]
        if dt < '2026-10-23':
            continue
        u = (i.get('link') or '').split('?')[0]
        dup = 'DUP' if u in known_urls else '   '
        print(f"{i.get('dt','')[:16]} {dup} | {i.get('title','')[:88]}")

check('/Users/leonliang/maoquanqingbao/data/_raw_1025_0052/all.json', 'round1')
check('/Users/leonliang/maoquanqingbao/data/_raw_1025_0052/all2.json', 'round2')
