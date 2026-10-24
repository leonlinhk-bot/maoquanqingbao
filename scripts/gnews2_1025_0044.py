#!/usr/bin/env python3
import urllib.request, urllib.parse, html, re, email.utils, json
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'

def gnews(q, hl='zh-HK', gl='HK', ceid='HK:zh-Hant'):
    url = ('https://news.google.com/rss/search?q=' + urllib.parse.quote(q) +
           f'&hl={hl}&gl={gl}&ceid={ceid}')
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode('utf-8', 'ignore')

for q in ['保監局', '香港保险 最新']:
    try:
        txt = gnews(q)
        its = re.findall(r'<item>(.*?)</item>', txt, re.S)
        print(f'== {q}: total {len(its)} items')
        for b in its[:6]:
            d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
            t = re.search(r'<title>(.*?)</title>', b, re.S)
            print('   ', (d.group(1) if d else '?')[:31], '|', html.unescape(re.sub(r'<[^>]+>', '', t.group(1)))[:85] if t else '')
    except Exception as e:
        print('FAIL', q, type(e).__name__, str(e)[:80])

# NFRA list API
try:
    api = 'https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectByCondition.json?pageNum=1&pageSize=15&itemId=931'
    req = urllib.request.Request(api, headers={'User-Agent': UA, 'Referer': 'https://www.nfra.gov.cn/'})
    with urllib.request.urlopen(req, timeout=25) as r:
        j = json.loads(r.read().decode('utf-8', 'ignore'))
    rows = j.get('data', {}).get('rows') or j.get('rows') or []
    print('== NFRA rows', len(rows))
    for r in rows[:10]:
        print('   ', r.get('publishDate') or r.get('docPublishDate'), '|', (r.get('docTitle') or r.get('title') or '')[:80])
except Exception as e:
    print('NFRA FAIL', type(e).__name__, str(e)[:120])
