import json, re

d = json.load(open('data/live-items.json'))
items = d['items']
print("--- items with aia/manulife/prudential/axa/sunlife/bowtie/za/fwd in id ---")
for it in items:
    iid = it['id'].lower()
    if any(k in iid for k in ['aia', 'manulife', 'prudential', 'axa', 'sunlife', 'bowtie', 'za-', 'fwd', 'hket', 'insurtech']):
        print(it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:55])
