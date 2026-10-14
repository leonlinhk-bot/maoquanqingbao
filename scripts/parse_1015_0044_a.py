#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse fetched raws: list entries with HKT timestamps > 2026-10-14T13:38Z window."""
import os, re, json, html
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
import xml.etree.ElementTree as ET

HKT = timezone(timedelta(hours=8))
DIR = '/Users/leonliang/maoquanqingbao/data/_1015'
CUT = datetime(2026, 10, 14, 21, 38, tzinfo=HKT)   # last check
look = datetime(2026, 10, 13, 0, 0, tzinfo=HKT)    # show a bit wider


def strip_html(s):
    s = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', '', s or '')
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def to_hkt(dt_str):
    if not dt_str:
        return None
    try:
        dt = parsedate_to_datetime(dt_str)
    except Exception:
        try:
            dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
        except Exception:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(HKT)


def parse_feed(path, label):
    print(f'\n########## {label} ##########')
    try:
        raw = open(path, encoding='utf-8').read()
    except Exception as e:
        print('  ERR', e)
        return
    for marker in ('<?xml', '<rss', '<feed', '<rdf'):
        i = raw.find(marker)
        if i >= 0:
            raw = raw[i:]
            break
    try:
        root = ET.fromstring(raw)
    except Exception as e:
        print('  XML ERR', e)
        return
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    nodes = root.findall('.//item') or root.findall('.//atom:entry', ns)
    print(f'  entries: {len(nodes)}')
    rows = []
    for n in nodes:
        def t(tag):
            el = n.find(tag) if not tag.startswith('atom:') else n.find(tag, ns)
            return el.text.strip() if (el is not None and el.text) else ''
        link = t('link')
        if not link:
            el = n.find('atom:link', ns)
            link = el.get('href') if el is not None else ''
        dt = to_hkt(t('pubDate') or t('atom:updated') or t('updated') or t('atom:published') or t('published'))
        rows.append((dt, strip_html(t('title')), link))
    rows.sort(key=lambda r: (r[0] is None, r[0] or datetime.min.replace(tzinfo=HKT)), reverse=True)
    for dt, title, link in rows[:20]:
        flag = '  <<<< NEW' if (dt and dt > CUT) else ''
        print(f"  [{dt.isoformat() if dt else '?'}] {title[:95]}{flag}")
        print(f"        {link[:140]}")


def parse_html_dates(path, label, urlpat):
    print(f'\n########## {label} ##########')
    try:
        raw = open(path, encoding='utf-8').read()
    except Exception as e:
        print('  ERR', e)
        return
    # find hrefs with nearby date texts
    hits = []
    for m in re.finditer(r'href="([^"]+)"', raw):
        u = m.group(1)
        if not re.search(urlpat, u):
            continue
        ctx = strip_html(raw[max(0, m.start() - 500): m.start() + 900])
        hits.append((u, ctx[:300]))
    seen = set()
    for u, ctx in hits:
        if u in seen:
            continue
        seen.add(u)
        print(f'  {u[:130]}')
        print(f'     ctx: {ctx[:220]}')
    print(f'  total hrefs: {len(seen)}')


for f, lab in [('insuranceasia_rss.raw', 'InsuranceAsia RSS'),
               ('ibm_rss.raw', 'InsuranceBusiness RSS'),
               ('scmp_rss.raw', 'SCMP RSS'),
               ('govhk_rss.raw', 'GOVHK RSS zh'),
               ('govhk_rss_en.raw', 'GOVHK RSS en'),
               ('artemis_rss.raw', 'Artemis RSS'),
               ('hkma_press.raw', 'HKMA press (html-as-feed attempt)')]:
    parse_feed(os.path.join(DIR, f), lab)

# InsuranceAsia News WP JSON
print('\n########## InsuranceAsia News WP API ##########')
try:
    posts = json.load(open(os.path.join(DIR, 'ian_api.raw'), encoding='utf-8'))
    print(f'  posts: {len(posts)}')
    for p in posts:
        dt = p.get('date_gmt') or p.get('date')
        try:
            d = datetime.fromisoformat(dt.replace('Z', '+00:00')).astimezone(HKT)
        except Exception:
            d = None
        flag = '  <<<< NEW' if (d and d > CUT) else ''
        print(f"  [{d.isoformat() if d else '?'}]{flag} {strip_html(p.get('title', {}).get('rendered', ''))[:95]}")
        print(f"        {p.get('link', '')[:140]}")
except Exception as e:
    print('  ERR', e)
