#!/usr/bin/env python3
"""Verify data/items.json + live site carry the new items."""
import json, urllib.request

base = '/Users/leonliang/maoquanqingbao/'
wanted = ['ian-moodys-apac-repricing-20261027',
          'ian-blackrock-captives-third-party-capital-20261027',
          'ian-php2shell-cyber-ai-visibility-20261027']

loc = json.load(open(base + 'data/items.json'))
loc_ids = {i['id'] for i in loc['items']}
print("local items.json:", len(loc['items']), "| itemCount:", loc.get('itemCount'))
for w in wanted:
    print("  local:", w, w in loc_ids)

UA = {"User-Agent": "Mozilla/5.0"}
for u in ["https://hkmaoquanqingbao.com/data/items.json",
          "https://hkmaoquanqingbao.com/data/core.json"]:
    try:
        raw = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40).read()
        d = json.loads(raw)
        if 'items' in d and u.endswith('items.json'):
            ids = {i['id'] for i in d['items']}
            print(f"online {u}: items={len(d['items'])} new_present={[w in ids for w in wanted]}")
        else:
            print(f"online {u}: totalItems={d.get('stats',{}).get('intelligence',{}).get('totalItems')}")
    except Exception as e:
        print("online ERR", u, type(e).__name__, e)
