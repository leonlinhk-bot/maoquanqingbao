#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse GNews RSS files: title, pubDate, source, link; filter since cutoff."""
import glob, re, html as H
from datetime import datetime, timezone, timedelta
import xml.etree.ElementTree as ET

TZ = timezone(timedelta(hours=8))
CUTOFF = datetime(2026, 8, 25, 18, 18, 5, tzinfo=TZ)  # last check
NOW = datetime(2026, 8, 26, 16, 40, 0, tzinfo=TZ)

def parse_dt(s):
    s = s.strip()
    for fmt in ('%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S GMT', '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%SZ'):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None

for f in sorted(glob.glob('/Users/leonliang/.tmp/scan0826/g_*.xml')):
    try:
        tree = ET.parse(f)
    except Exception as e:
        print(f, 'PARSE ERR', e)
        continue
    items = tree.findall('.//item')
    print(f'\n===== {f} ({len(items)} items) =====')
    for it in items:
        title = H.unescape((it.findtext('title') or '').strip())
        pub = it.findtext('pubDate') or ''
        src = it.findtext('source') or ''
        link = it.findtext('link') or ''
        dt = parse_dt(pub)
        if dt is None:
            print('NO-DATE |', title[:90], '|', link[:100])
            continue
        dt_hk = dt.astimezone(TZ)
        mark = '<<<' if dt_hk >= CUTOFF else ''
        if dt_hk >= CUTOFF:
            print(f'{dt_hk.strftime("%m-%d %H:%M")} | {src[:22]:22s} | {title[:80]} | {link[:90]} {mark}')
