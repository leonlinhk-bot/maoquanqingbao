import re, html, os
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
HKT=timezone(timedelta(hours=8))
NOW=datetime.now(HKT)
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
for f in ['gn_hk_ia.xml','gn_hk_ins.xml','gn_hk_fo.xml','gn_hk_mpf.xml','gn_en_hkins.xml','gn_cn_ins.xml']:
    print('\n===== ', f)
    t=open(f'{RAW}/{f}',encoding='utf-8',errors='ignore').read()
    ents=re.findall(r'<item[\s>].*?</item>', t, re.S)
    rows=[]
    for e in ents:
        ti=re.search(r'<title>(.*?)</title>', e, re.S); d=re.search(r'<pubDate>(.*?)</pubDate>', e, re.S); ln=re.search(r'<link>(.*?)</link>', e, re.S); src=re.search(r'<source[^>]*>(.*?)</source>', e, re.S)
        try: dt=parsedate_to_datetime(d.group(1).strip()).astimezone(HKT)
        except Exception: dt=None
        rows.append((dt, p(ti.group(1)) if ti else '', p(src.group(1)) if src else '', (ln.group(1).strip() if ln else '')))
    rows=[r for r in rows if r[0]]
    rows.sort(key=lambda x: x[0], reverse=True)
    new=[r for r in rows if r[0] >= NOW-timedelta(hours=30)]
    print('total', len(rows), 'within30h', len(new))
    for dt,txt,s,u in new[:18]:
        print('-', dt.strftime('%m-%d %H:%M'), '|', s[:22], '|', txt[:95], '|', u[:75])
    if not new:
        for dt,txt,s,u in rows[:6]:
            print('  (older)', dt.strftime('%m-%d %H:%M'), '|', s[:20], '|', txt[:80])
