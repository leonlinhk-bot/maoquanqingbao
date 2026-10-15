#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, json
D = '/Users/leonliang/maoquanqingbao/data/_1016_0029/'
raw = open(D + 'r2_axa.out', encoding='utf-8', errors='replace').read()
i = raw.find('axa-betterme-weekend')
print(raw[max(0, i - 700):i + 700])
print('======= all article urls with dates =======')
for m in re.finditer(r'"formattedDate":"([^"]+)","url":"([^"]+)"', raw):
    print(m.group(1), '|', m.group(2)[:90])
