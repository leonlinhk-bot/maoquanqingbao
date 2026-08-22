#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
d = json.load(open('data/live-items.json'))
items = d['items']
print("total:", len(items))
kws = ['narrows-broker', 'broker access', 'ping an', 'pingan', 'etf access', 'el nino', 'allianz trade',
       'indonesia holding', 'GIC Re', 'oona', 'fake-doc', 'scam alert', 'sun life', '永明', 'sunlife',
       'axa', 'prudential', '保诚', 'manulife', '宏利', 'aia', '友邦', 'hkma', '金管局', 'fstb', '家办',
       'family office', 'nfra', '金融监管', 'insurtech', '保监局', 'ia_press', 'ia-press']
for kw in kws:
    hits = [it for it in items if kw.lower() in (it['id'] + ' ' + it['title']['sc'] + ' ' + str(it.get('sourceKey',''))).lower()]
    if hits:
        print(f"--- '{kw}': {len(hits)}")
        for it in hits[:5]:
            print("   ", it['id'], '|', it.get('sourceKey'), '|', it['publishedAt'], '|', it['title']['sc'][:60])
