#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse fetched feeds (rss/xml/json) and list entries newer than a cutoff."""
import json, re, sys, xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta

HK = timezone(timedelta(hours=8))


def fmt(dt):
    return dt.astimezone(HK).strftime('%Y-%m-%dT%H:%M:%S+08:00')


def parse_rss(path, label, limit=40):
    print(f'===== {label} ({path}) =====')
    try:
        tree = ET.parse(path)
    except Exception as e:
        print('  parse error', e)
        return
    root = tree.getroot()
    items = root.findall('.//item')
    if not items:
        items = root.findall('.//{http://www.w3.org/2005/Atom}entry')
    print('  entries:', len(items))
    rows = []
    for it in items[:limit]:
        title = (it.findtext('title') or '').strip()
        link = (it.findtext('link') or '').strip()
        if not link:
            l = it.find('link')
            if l is not None:
                link = l.get('href', '')
        pub = (it.findtext('pubDate') or it.findtext('published')
               or it.findtext('updated') or it.findtext('{http://purl.org/dc/elements/1.1/}date') or '')
        try:
            dt = parsedate_to_datetime(pub)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            pubb = fmt(dt)
        except Exception:
            pubb = pub
        rows.append((pubb, title, link))
    for pubb, title, link in rows:
        print(f'  [{pubb}] {title}\n      {link}')


def parse_wp(path, label, limit=40):
    print(f'===== {label} ({path}) =====')
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print('  parse error', e)
        return
    print('  posts:', len(data))
    for p in data[:limit]:
        print(f"  [{p.get('date_gmt')}Z] {p.get('title', {}).get('rendered', '')}\n      {p.get('link')}")


if __name__ == '__main__':
    parse_rss('/tmp/iaa.xml', 'InsuranceAsia RSS')
    parse_rss('/tmp/ibm.xml', 'InsuranceBusiness Asia RSS')
    parse_rss('/tmp/art.xml', 'Artemis RSS')
    parse_wp('/tmp/ian.json', 'InsuranceAsia News WP API')
