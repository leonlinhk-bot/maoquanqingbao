import json
d=json.load(open('.tmp/1008_0007/live_items.json'))
print('LIVE items.json itemCount:', d.get('itemCount'), 'len:', len(d.get('items',[])))
ids={it['id'] for it in d['items']}
for k in ['ian-awbury-syndicate-japan-20261007','ibm-south-korea-nhis-fraud-window-20261007','artemis-picc-great-wall-re-catbond-3-12m-20261007','iaasia-allianz-ceo-reshuffle-kunzmann-20261006']:
    print(' ', k, 'in live:', k in ids)
