#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
from email.utils import parsedate_to_datetime
from datetime import timezone, timedelta
HK = timezone(timedelta(hours=8))
D = '/Users/leonliang/maoquanqingbao/data/_1016_0029/'
WANT = ['stand-hires-former-nephila', 'marsh-ceo-flags-client-interest', 'artex-capital-solutions',
        'james-winn-appointed', 'marsh-leans-into-ai-growth', 'aces-specialty-insurance-company-gets-approval',
        'antares-global-names', 'marsh-revenue-rises-8']
for f in ['artemis.out', 'reinsnews.out', 'ibm.out']:
    raw = open(D + f, encoding='utf-8', errors='replace').read()
    for e in re.findall(r'<item[\s>].*?</item>', raw, re.S):
        li = re.search(r'<link[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', e, re.S)
        url = html.unescape(li.group(1)).strip() if li else ''
        if any(w in url for w in WANT):
            pu = re.search(r'<pubDate[^>]*>(.*?)</', e, re.S)
            raw_d = re.sub(r'<[^>]+>', '', pu.group(1)).strip() if pu else ''
            try:
                dt = parsedate_to_datetime(raw_d).astimezone(HK)
                dt = dt.strftime('%Y-%m-%dT%H:%M:%S+08:00')
            except Exception:
                dt = raw_d
            print(f, '|', dt, '|', url)
