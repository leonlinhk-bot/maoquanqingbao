import json

d = json.load(open('data/live-items.json'))
items = d['items']
print('== hkma items ==')
for it in items:
    if it.get('sourceKey') == 'hkma' or 'hkma' in it['id']:
        print(it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:60])
print()
print('== insurancebusinessmag items 8/18-8/21 ==')
for it in items:
    if it.get('sourceKey') == 'insurancebusinessmag':
        print(it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:60])
print()
print('== insuranceasia items 8/19-8/21 ==')
for it in items:
    if it.get('sourceKey') == 'insuranceasia':
        print(it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:60])
