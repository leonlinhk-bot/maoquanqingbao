#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re, os, html
from datetime import datetime, timezone, timedelta
import xml.etree.ElementTree as ET

C = '/Users/leonliang/maoquanqingbao/.cache1018_0012'
HKT = timezone(timedelta(hours=8))

def show_rss(fn, label, limit=25):
    print('='*20, label, fn)
    p = os.path.join(C, fn)
    raw = open(p, 'rb').read()
    try:
        root = ET.fromstring(raw)
    except Exception as e:
        print('parse fail', e); return
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    items = root.findall('.//item') or root.findall('.//atom:entry', ns)
    for it in items[:limit]:
        def g(tag):
            el = it.find(tag)
            if el is None:
                el = it.find('atom:'+tag, ns)
            return (el.text or '').strip() if el is not None and el.text else ''
        title = g('title')
        link = g('link')
        if not link:
            le = it.find('atom:link', ns)
            if le is not None:
                link = le.get('href','')
        date = g('pubDate') or g('published') or g('updated') or g('dc:date')
        print(' %s | %s | %s' % (date[:31], title[:110], link[:150]))

def show_wp(fn, label, limit=20):
    print('='*20, label, fn)
    d = json.load(open(os.path.join(C, fn), encoding='utf-8'))
    for p in d[:limit]:
        print(' %s | %s | %s | %s' % (p.get('date'), p.get('modified'), html.unescape(p['title']['rendered'])[:100], p.get('link')))

show_rss('rn.xml', 'REINSURANCE NEWS')
show_rss('artemis.xml', 'ARTEMIS')
show_rss('insuranceasia.xml', 'INSURANCE ASIA')
show_rss('ibm_rss.xml', 'INSURANCE BUSINESS')
show_wp('ian.json', 'INSURANCEASIA NEWS')
