import re, json, html, os, sys
from datetime import datetime, timezone, timedelta
try:
    from email.utils import parsedate_to_datetime
except Exception:
    parsedate_to_datetime=None
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
HKT=timezone(timedelta(hours=8))
NOW=datetime.now(HKT)
CUT=NOW-timedelta(hours=30)
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
def rss(path, label, limit=25):
    print('\n===== RSS', label, path)
    if not os.path.exists(f'{RAW}/{path}'):
        print('missing'); return
    t=open(f'{RAW}/{path}',encoding='utf-8',errors='ignore').read()
    ents=re.findall(r'<item[\s>].*?</item>', t, re.S) or re.findall(r'<entry[\s>].*?</entry>', t, re.S)
    print('items:',len(ents))
    for e in ents[:limit]:
        ti=re.search(r'<title[^>]*>(.*?)</title>', e, re.S)
        ln=re.search(r'<link[^>]*>(.*?)</link>', e, re.S)
        d=re.search(r'<(pubDate|updated|published|dc:date)[^>]*>(.*?)</\1>', e, re.S)
        url = p(ln.group(1)) if ln else ''
        if '<link href' in e and not url:
            m=re.search(r'<link[^>]*href="([^"]+)"', e); url=m.group(1) if m else ''
        dt=''
        if d:
            raw=p(d.group(2))
            try:
                dt=parsedate_to_datetime(raw).astimezone(HKT).strftime('%Y-%m-%dT%H:%M')
            except Exception:
                dt=raw
        print('-',dt,'|',p(ti.group(1))[:80] if ti else '','|',url[:110])
rss('insuranceasia.rss','insuranceasia')
rss('scmp_ins.rss','scmp')
rss('govhk_zh.xml','govhk')
# insuranceasianews json
print('\n===== ian.json')
j=json.load(open(f'{RAW}/ian.json',encoding='utf-8'))
print('count',len(j))
for it in j[:15]:
    print('-',it.get('date'),it.get('modified'),'|',p(it['title']['rendered'])[:80],'|',it.get('link'))
