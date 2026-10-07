import re, html, os, json
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
R23='/Users/leonliang/maoquanqingbao/data/_raw_1006_2343'
R18='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
HKT=timezone(timedelta(hours=8))
NOW=datetime(2026,10,6,23,50,tzinfo=HKT)
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()

def rss(path, raw, label, hours=40, limit=30):
    fp=os.path.join(raw,path)
    if not os.path.exists(fp): print(f'\n##### {label} MISSING'); return
    t=open(fp,encoding='utf-8',errors='ignore').read()
    ents=re.findall(r'<item[\s>].*?</item>', t, re.S) or re.findall(r'<entry[\s>].*?</entry>', t, re.S)
    print(f'\n##### {label} ({len(ents)} items, showing <= {hours}h)')
    n=0
    for e in ents[:limit]:
        ti=re.search(r'<title[^>]*>(.*?)</title>', e, re.S)
        ln=re.search(r'<link[^>]*>(.*?)</link>', e, re.S)
        d=re.search(r'<(pubDate|updated|published|dc:date)[^>]*>(.*?)</\1>', e, re.S)
        url=p(ln.group(1)) if ln else ''
        if not url:
            m=re.search(r'<link[^>]*href="([^"]+)"', e); url=m.group(1) if m else ''
        src=re.search(r'<source[^>]*>(.*?)</source>', e, re.S)
        dt=None
        if d:
            rawd=p(d.group(2))
            try: dt=parsedate_to_datetime(rawd).astimezone(HKT)
            except Exception:
                try: dt=datetime.fromisoformat(rawd.replace('Z','+00:00')).astimezone(HKT)
                except Exception: pass
        if dt is None or dt >= NOW - timedelta(hours=hours):
            n+=1
            tag = dt.strftime('%m-%d %H:%M') if dt else '??'
            print(f'  [{tag}] {p(ti.group(1))[:78] if ti else ""} | {p(src.group(1))[:22] if src else ""} | {url[:100]}')
    print(f'  -> {n} within {hours}h')

rss('gn_hk_ia.xml',R23,'GN 保监局')
rss('gn_hk_ins.xml',R23,'GN 香港保险')
rss('gn_hk_fo.xml',R23,'GN 家族办公室')
rss('gn_hk_mpf.xml',R23,'GN 强积金')
rss('gn_en_hkins.xml',R23,'GN HK insurance EN')
rss('gn_cn_ins.xml',R23,'GN 金融监管总局')
rss('insuranceasia.rss',R23,'InsuranceAsia RSS')
rss('scmp_ins.rss',R23,'SCMP RSS', hours=40)
rss('govhk_zh.xml',R23,'GovHK RSS', hours=40)
