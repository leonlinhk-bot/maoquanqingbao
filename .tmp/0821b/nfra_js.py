#!/usr/bin/env python3
import re, html

raw = open('.tmp/0821/nfra_itemlist.js', encoding='utf-8', errors='ignore').read()
print('len:', len(raw))
print(raw[:3000])
