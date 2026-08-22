import json, datetime

TZ8 = datetime.timezone(datetime.timedelta(hours=8))
now_iso = datetime.datetime.now(TZ8).strftime("%Y-%m-%dT%H:%M:%S+08:00")

d = json.load(open('data/last-check.json'))
d['lastCheck'] = now_iso
for k, v in d['sources'].items():
    v['last'] = now_iso
json.dump(d, open('data/last-check.json', 'w'), ensure_ascii=False, indent=2)
print("last-check updated:", now_iso)
for k in d['sources']:
    print(" -", k, d['sources'][k]['last'])
