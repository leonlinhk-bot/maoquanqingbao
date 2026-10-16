#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re, html, sys
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta

HK = timezone(timedelta(hours=8))
WIN_START = datetime(2026, 10, 16, 18, 8, tzinfo=HK)
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'

def strip(t):
    t = re.sub(r'<[^>]+>', '', t or '')
    return html.unescape(t).strip()

def parse_date(s):
    s = strip(s)
    if not s:
        return None
    for f in ('%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z',
              '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S'):
        try:
            dt = datetime.strptime(s, f)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(HK)
        except Exception:
            pass
    try:
        return parsedate_to_datetime(s).astimezone(HK)
    except Exception:
        return None

def feed(path):
    raw = open(D + path, encoding='utf-8', errors='replace').read()
    out = []
    for e in re.findall(r'<item[\s>].*?</item>', raw, re.S) + re.findall(r'<entry[\s>].*?</entry>', raw, re.S):
        ti = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', e, re.S)
        li = re.search(r'<link[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', e, re.S)
        pu = re.search(r'<(?:pubDate|published|updated|dc:date)[^>]*>(.*?)</', e, re.S)
        de = re.search(r'<description[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>', e, re.S)
        url = strip(li.group(1)) if li else ''
        if not url:
            m = re.search(r'<link[^>]*href="([^"]+)"', e)
            url = m.group(1) if m else ''
        out.append({'t': strip(ti.group(1)) if ti else '', 'u': url,
                    'd': parse_date(pu.group(1)) if pu else None,
                    'desc': strip(de.group(1))[:400] if de else ''})
    return out

FILES = ['iaasia.out', 'ibm.out', 'scmp.out', 'govhk.out', 'artemis.out',
         'reinsnews.out', 'air.out', 'hkma.out']
for f in FILES:
    try:
        ent = feed(f)
    except Exception as ex:
        print('###', f, 'ERR', ex); continue
    new = [x for x in ent if x['d'] and x['d'] >= WIN_START]
    print('### %s  total=%d  in-window=%d' % (f, len(ent), len(new)))
    for x in new:
        print('  ', x['d'].strftime('%m-%d %H:%M'), '|', x['t'][:110])
        print('      ', x['u'][:160])
        if x['desc']:
            print('      >', x['desc'][:220])

try:
    j = json.load(open(D + 'ian.out', encoding='utf-8'))
    print('### ian.out total=%d' % len(j))
    for p in j:
        dt = parse_date((p.get('date_gmt') or '').rstrip('Z') + '+00:00') or parse_date(p.get('date', ''))
        if dt and dt >= WIN_START:
            print('  ', dt.strftime('%m-%d %H:%M'), '|', strip(p.get('title', {}).get('rendered', ''))[:110])
            print('      ', p.get('link'))
            print('      >', strip(p.get('excerpt', {}).get('rendered', ''))[:220])
except Exception as ex:
    print('### ian ERR', ex)
