#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse batch-2 raws: AIR rss, IAN feed, HKMA speeches/insight; flag in-window items."""
import os, re, json, html
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
import xml.etree.ElementTree as ET

HKT = timezone(timedelta(hours=8))
DIR = '/Users/leonliang/maoquanqingbao/data/_1015'
CUT = datetime(2026, 10, 14, 21, 38, tzinfo=HKT)
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
urls = {(it.get('originalUrl') or '').rstrip('/') for it in d['items']}


def strip_html(s):
    s = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', '', s or '')
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def to_hkt(s):
    if not s:
        return None
    try:
        dt = parsedate_to_datetime(s)
    except Exception:
        try:
            dt = datetime.fromisoformat(s.replace('Z', '+00:00'))
        except Exception:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(HKT)


def feed(path, label):
    print(f'\n##### {label} #####')
    p = os.path.join(DIR, path)
    if not os.path.exists(p):
        print('  MISSING'); return
    raw = open(p, encoding='utf-8').read()
    for mk in ('<?xml', '<rss', '<feed'):
        i = raw.find(mk)
        if i >= 0:
            raw = raw[i:]; break
    try:
        root = ET.fromstring(raw)
    except Exception as e:
        print('  XML ERR', e); return
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    nodes = root.findall('.//item') or root.findall('.//atom:entry', ns)
    rows = []
    for n in nodes:
        def t(tag):
            el = n.find(tag) if not tag.startswith('atom:') else n.find(tag, ns)
            return el.text.strip() if (el is not None and el.text) else ''
        link = t('link')
        if not link:
            el = n.find('atom:link', ns)
            link = el.get('href') if el is not None else ''
        dt = to_hkt(t('pubDate') or t('atom:updated') or t('updated') or t('published'))
        rows.append((dt, strip_html(t('title')), link, strip_html(t('description'))[:200]))
    rows.sort(key=lambda r: (r[0] is None, r[0] or datetime.min.replace(tzinfo=HKT)), reverse=True)
    print(f'  entries {len(rows)}')
    for dt, title, link, desc in rows[:14]:
        tag = ''
        if dt and dt > CUT:
            tag = '  <<IN-WINDOW'
        elif link.rstrip('/') not in urls:
            tag = '  (not-in-db)'
        print(f'  [{dt.isoformat() if dt else "?"}] {title[:90]}{tag}')
        print(f'      {link[:130]}')
        if desc:
            print(f'      {desc[:150]}')


feed('air_rss.raw', 'Asia Insurance Review RSS')
feed('ian_feed.raw', 'InsuranceAsia News feed')

print('\n##### HKMA speeches (dates) #####')
raw = open(os.path.join(DIR, 'hkma_speeches.raw'), encoding='utf-8').read()
txt = strip_html(raw)
print(txt[:1200])
print('\n##### HKMA insight (dates) #####')
raw = open(os.path.join(DIR, 'hkma_insight.raw'), encoding='utf-8').read()
print(strip_html(raw)[:1200])
