#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse WP JSON (InsuranceAsia News) + IEEE/Atom feeds with namespace-agnostic tags."""
import json
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta

HK = timezone(timedelta(hours=8))


def local(tag):
    return tag.split('}')[-1]


def fmt(dt):
    return dt.astimezone(HK).strftime('%Y-%m-%dT%H:%M:%S+08:00')


print('===== InsuranceAsia News WP API (/tmp/ian.json) =====')
data = json.load(open('/tmp/ian.json', encoding='utf-8'))
print('posts:', len(data))
for p in data:
    dg = p.get('date_gmt')
    try:
        dt = datetime.strptime(dg, '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc)
        lbl = fmt(dt)
    except Exception:
        lbl = str(dg)
    print(f"  [{lbl}] {p.get('title', {}).get('rendered', '')}\n      {p.get('link')}")

print()
print('===== IBM Asia Atom feed (namespace-agnostic) =====')
root = ET.parse('/tmp/ibm.xml').getroot()
for e in root.findall('{http://www.w3.org/2005/Atom}entry'):
    d = {}
    for ch in e:
        d[local(ch.tag)] = ch
    title = (d.get('title').text or '').strip() if d.get('title') is not None else ''
    link = ''
    for ch in e:
        if local(ch.tag) == 'link' and ch.get('rel') == 'alternate':
            link = ch.get('href', '')
    upd = (d.get('updated').text or '') if d.get('updated') is not None else ''
    try:
        dt = datetime.strptime(upd, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
        lbl = fmt(dt)
    except Exception:
        lbl = upd
    print(f'  [{lbl}] {title}\n      {link}')
