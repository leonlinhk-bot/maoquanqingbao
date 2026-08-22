#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, datetime

cands = json.load(open('.tmp/cands.json'))
tz8 = datetime.timezone(datetime.timedelta(hours=8))

print("=== ALL FRESH CANDIDATES ===")
for tag, lst in cands.items():
    if not lst:
        continue
    print(f"\n--- {tag} ---")
    for r in lst:
        dt = r.get('dt', '')
        if dt and not isinstance(dt, str):
            dt = dt.astimezone(tz8).strftime('%m-%d %H:%M')
        print(f"* [{dt}] src={r.get('source','')[:25]} | {r.get('title','')[:100]}")
        print(f"  {r.get('link','')[:150]}")

# existing sourceKeys
live = json.load(open('data/live-items.json'))
keys = set()
for it in live['items']:
    keys.add(it.get('sourceKey',''))
    keys.add(it.get('id',''))
print("\n=== existing keys sample (last 30) ===")
print(sorted(keys)[-30:])
