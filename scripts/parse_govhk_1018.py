#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET, re, html, os
C = '/Users/leonliang/maoquanqingbao/.cache1018_0012'
raw = open(os.path.join(C,'govhk.xml'),'rb').read()
root = ET.fromstring(raw)
items = root.findall('.//item')
print('items', len(items))
for it in items[:45]:
    t = (it.findtext('title') or '').strip()
    l = (it.findtext('link') or '').strip()
    d = (it.findtext('pubDate') or '').strip()
    desc = re.sub(r'<[^>]+>',' ',(it.findtext('description') or ''))
    desc = html.unescape(re.sub(r'\s+',' ',desc)).strip()
    print('%s | %s\n   %s\n   %s' % (d, t, l, desc[:200]))
