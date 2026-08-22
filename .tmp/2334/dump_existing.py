import json

d = json.load(open('data/live-items.json'))
items = d['items']
# dump all items from key sources with id/sourceKey/publishedAt/title
want = ['insuranceasia', 'insurancebusinessmag', 'aia', 'manulife', 'prudential', 'axa', 'sunlife',
        'hkma_press', 'ia_circular', 'ia_press', 'scmp', 'nfra', 'fstb', 'insurtech', 'ia', 'theedge', 'aastocks']
for it in items:
    sk = it.get('sourceKey', '')
    if any(w in sk for w in want):
        print(it['id'], '|', sk, '|', it.get('publishedAt'), '|', it.get('title', {}).get('sc', '')[:60])
