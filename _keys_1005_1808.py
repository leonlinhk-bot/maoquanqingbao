import json, re, html
d = json.load(open('data/live-items.json'))
items = d['items']
KEYS = ('ia', 'ia_circular', 'hkma', 'aia', 'manulife', 'prudential', 'prudential-hk', 'axa', 'axa-hk', 'sunlife', 'fstb', 'family_office', 'insurtech', 'scmp', 'nfra')
print('=== existing ids by key (last 6 each) ===')
for k in KEYS:
    sel = [i for i in items if i.get('sourceKey') == k][:6]
    if sel:
        print('--', k, len([i for i in items if i.get('sourceKey') == k]))
        for i in sel:
            print('   ', i.get('publishedAt'), '|', i.get('id'))

print()
print('=== all ids containing 20261005 / 20261004 ===')
for i in items:
    if '20261005' in (i.get('id') or '') or '20261004' in (i.get('id') or ''):
        print('  ', i.get('publishedAt'), '|', i.get('sourceKey'), '|', i.get('id'))
