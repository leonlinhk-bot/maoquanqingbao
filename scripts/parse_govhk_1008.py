#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse govhk general_zh RSS for items published on 2026-10-08."""
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from datetime import timezone, timedelta

HK = timezone(timedelta(hours=8))
root = ET.parse('/tmp/govhk.xml').getroot()
n = 0
for it in root.findall('.//item'):
    title = (it.findtext('title') or '').strip()
    link = (it.findtext('link') or '').strip()
    pub = (it.findtext('pubDate') or '').strip()
    try:
        dt = parsedate_to_datetime(pub)
        lbl = dt.astimezone(HK).strftime('%Y-%m-%dT%H:%M:%S+08:00')
    except Exception:
        lbl = pub
    if lbl >= '2026-10-08T00:00':
        n += 1
        print(f'  [{lbl}] {title}\n      {link}')
print('total items in feed:', len(root.findall(".//item")), '| matched 2026-10-08:', n)
