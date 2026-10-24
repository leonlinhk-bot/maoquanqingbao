#!/usr/bin/env python3
import os, re, urllib.request, urllib.parse, html, json, email.utils
from datetime import datetime, timezone, timedelta

OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044'
HKT = timezone(timedelta(hours=8))
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
CUT = datetime(2026, 10, 24, 0, 0, tzinfo=HKT)

QUERIES = [
    ('zh', '香港 保險 監管'),
    ('zh', '香港保險 保監局'),
    ('zh', '香港 保險 新產品 推出'),
    ('zh', '香港 家族辦公室'),
    ('zh', '保险 监管 总局 保险业'),
    ('en', 'Hong Kong insurance'),
    ('en', 'Hong Kong Insurance Authority'),
    ('en', 'insurance Asia captive'),
]

def gnews(q, lang):
    if lang == 'zh':
        url = ('https://news.google.com/rss/search?q=' + urllib.parse.quote(q) +
               '&hl=zh-HK&gl=HK&ceid=HK:zh-Hant')
    else:
        url = ('https://news.google.com/rss/search?q=' + urllib.parse.quote(q) +
               '&hl=en-US&gl=US&ceid=US:en')
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read()

def pd(s):
    try:
        d = email.utils.parsedate_to_datetime(s)
        if d.tzinfo is None: d = d.replace(tzinfo=timezone.utc)
        return d.astimezone(HKT)
    except Exception:
        return None

rows = []
for lang, q in QUERIES:
    try:
        raw = gnews(q, lang)
    except Exception as e:
        print(f'FAIL {q} {type(e).__name__}: {str(e)[:70]}'); continue
    txt = raw.decode('utf-8', 'ignore')
    n_new = 0
    for m in re.finditer(r'<item>(.*?)</item>', txt, re.S):
        b = m.group(1)
        def g(tag):
            mm = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', b, re.S)
            if not mm: return ''
            v = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', mm.group(1), flags=re.S)
            return html.unescape(v).strip()
        d = pd(g('pubDate'))
        if not d or d < CUT:
            continue
        title = re.sub(r'<[^>]+>', '', g('title'))
        rows.append({'q': q, 'date': d.strftime('%Y-%m-%dT%H:%M:%S%z'), 'title': title,
                     'link': g('link'), 'src': re.sub(r'<[^>]+>', '', g('source'))})
        n_new += 1
        print(f"  {d.strftime('%m-%d %H:%M')} [{re.sub(r'<[^>]+>','',g('source'))[:18]}] {title[:95]}")
    print(f'== {q} -> {n_new} since 10-24')

json.dump(rows, open(os.path.join(OUT, 'gnews_recent.json'), 'w'), ensure_ascii=False, indent=1)
print('total', len(rows))
