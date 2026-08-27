#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract HKMA press release body from hkma_nm.html"""
import re, html as H

html = open('.tmp/hkma_nm.html', encoding='utf-8', errors='replace').read()
# find the main release section: starts after "Press release" heading
idx = html.find('Northern Metropolis Financial Advisory Taskforce holds its second meeting')
print('headline idx:', idx)
# print a window around it
seg = html[idx:idx+12000]
# strip tags
seg = re.sub(r'<script[^>]*>.*?</script>', ' ', seg, flags=re.S)
seg = re.sub(r'<style[^>]*>.*?</style>', ' ', seg, flags=re.S)
seg = re.sub(r'<[^>]+>', '\n', seg)
seg = H.unescape(seg)
lines = [l.strip() for l in seg.split('\n') if l.strip()]
for l in lines[:60]:
    print(l[:220])
