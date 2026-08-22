#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
live = json.load(open('data/live-items.json'))
items = live['items']
kw = ['恒大', 'hengda', '银债', '銀債', 'silver', 'julius', 'AIRSIDE', 'airside', 'ubs', '瑞銀', '央行票据', '央行票據', 'manulife', '宏利', 'prudential', '保誠']
for it in items:
    blob = json.dumps(it, ensure_ascii=False)
    for k in kw:
        if k.lower() in blob.lower():
            print(f"[{k}] {it.get('id')} | {it.get('publishedAt')} | {it.get('sourceKey')} | {(it.get('title') or {}).get('sc','')[:70]}")
            break
