#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract HKMA press release template-content-area."""
import re, html as H

html = open('.tmp/hkma_nm.html', encoding='utf-8', errors='replace').read()
m = re.search(r'<div class="template-content-area">(.*?)</div>\s*</div>\s*</div>', html, re.S)
if not m:
    m = re.search(r'<div class="template-content-area">(.*?)(?:<div class="[^"]*">|<footer|<!--)', html, re.S)
seg = m.group(1) if m else ''
seg = re.sub(r'<script[^>]*>.*?</script>', ' ', seg, flags=re.S)
seg = re.sub(r'<[^>]+>', '\n', seg)
seg = H.unescape(seg)
lines = [l.strip() for l in seg.split('\n') if l.strip()]
for l in lines:
    print(l[:250])
