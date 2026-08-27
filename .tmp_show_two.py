#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

d = json.load(open('data/live-items.json'))
for it in d['items']:
    if it['id'] in ('hkma-bank-scam-alert-20260826', 'ibm-prudential-h1-20260827'):
        print(json.dumps(it, ensure_ascii=False, indent=1))
        print('---')
