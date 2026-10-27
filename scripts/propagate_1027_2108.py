#!/usr/bin/env python3
"""Check deploy propagation: origin (github.io) vs CDN, with cache buster."""
import json, time, urllib.request, datetime

UA = {"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"}

def probe(url, label):
    u = url + ("&" if "?" in url else "?") + "cb=" + str(int(time.time()))
    try:
        req = urllib.request.Request(u, headers=UA)
        d = json.loads(urllib.request.urlopen(req, timeout=40).read())
        if 'items' in d:
            ids = {i['id'] for i in d['items']}
            print(f"{label}: items={len(d['items'])} moodys={'ian-moodys-apac-repricing-20261027' in ids}")
        else:
            print(f"{label}: totalItems={d.get('stats',{}).get('intelligence',{}).get('totalItems')}")
    except Exception as e:
        print(label, "ERR", type(e).__name__, e)

print(datetime.datetime.now().isoformat())
probe("https://leonlinhk-bot.github.io/maoquanqingbao/data/items.json", "ghpages items")
probe("https://hkmaoquanqingbao.com/data/items.json", "cdn items")
