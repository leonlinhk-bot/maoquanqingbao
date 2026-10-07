import re, os, html, json, sys
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
HK = timezone(timedelta(hours=8))
def rd(n):
    return open(os.path.join(RAW, n), encoding='utf-8', errors='ignore').read()
def clean(s):
    s = re.sub(r'<!--.*?-->', ' ', s or '', flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

CUT = datetime(2026, 10, 6, 16, 0, tzinfo=timezone.utc)  # = 2026-10-07 00:00 HKT

def add(out, t, url, src):
    out.append({'title': t, 'url': url, 'src': src})

out = []
# --- RSS feeds ---
def rss_items(txt):
    res = []
    for m in re.finditer(r'<item>(.*?)</item>', txt, re.S):
        b = m.group(1)
        def g(tag):
            mm = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', b, re.S)
            if not mm: return ''
            v = mm.group(1)
            v = re.sub(r'^<!\[CDATA\[|\]\]>$', '', v.strip())
            return clean(v)
        res.append({'title': g('title'), 'link': g('link'), 'date': g('pubDate'), 'desc': g('description')})
    return res

for f, src in [('insuranceasia.rss','insuranceasia'), ('scmp_ins.rss','scmp'), ('govhk_zh.xml','govhk')]:
    for it in rss_items(rd(f)):
        d = None
        try: d = parsedate_to_datetime(it['date'])
        except Exception: pass
        if d and d >= CUT:
            out.append({'src': src, 'when': d.astimezone(HK).strftime('%m-%d %H:%M'), 'title': it['title'], 'url': it['link'], 'desc': it['desc'][:180]})

for f in ['gnews_ia.xml','gnews_ins.xml','gnews_fo.xml','gnews_insurer.xml','gnews_cn.xml']:
    for it in rss_items(rd(f)):
        d = None
        try: d = parsedate_to_datetime(it['date'])
        except Exception: pass
        if d and d >= CUT:
            out.append({'src': f.replace('gnews_','gnews:').replace('.xml',''), 'when': d.astimezone(HK).strftime('%m-%d %H:%M'), 'title': it['title'], 'url': it['link'], 'desc': it['desc'][:150]})

# --- insuranceasia news wp json ---
try:
    for it in json.loads(rd('ian.json')):
        d = datetime.fromisoformat(it['date']).replace(tzinfo=timezone.utc)
        if d >= CUT:
            out.append({'src':'ian','when':d.astimezone(HK).strftime('%m-%d %H:%M'),'title':clean(it['title']['rendered']),'url':it['link'],'desc':clean(it.get('excerpt',{}).get('rendered',''))[:180]})
except Exception as e:
    print('ian err', e)

# --- HKMA ---
t = rd('hkma_press.html')
for m in re.finditer(r'<a href="(/eng/news-and-media/press-releases/2026/10/[^"]+)"[^>]*>(.*?)</a>', t, re.S):
    title = clean(m.group(2))
    if title.startswith('x '): # attr leak
        title = clean(re.sub(r'^[^"]*">', '', m.group(2)))
    out.append({'src':'hkma','when':m.group(1).split('/')[-2],'title':title[:160],'url':'https://www.hkma.gov.hk'+m.group(1)})

# --- IBM Asia ---
t = rd('ibm_asia.html')
for m in re.finditer(r'<a class="content-list__item__title[^"]*"\s+href="([^"]+)"[^>]*title="([^"]*)"', t):
    out.append({'src':'ibm','when':'10-07','title':html.unescape(m.group(2)),'url':'https://www.insurancebusinessmag.com'+m.group(1)})
if not any(o['src']=='ibm' for o in out):
    for m in re.finditer(r'href="(/asia/news/[^"]+\.aspx)"[^>]*>([^<]{20,160})</a>', t):
        out.append({'src':'ibm','when':'?','title':clean(m.group(2)),'url':'https://www.insurancebusinessmag.com'+m.group(1)})

# --- IA circulars ---
t = rd('ia_circ.html')
for m in re.finditer(r'(\d{1,2} \w+ 2026)\s*</td>\s*<td[^>]*>(.*?)</td>', t, re.S):
    out.append({'src':'ia_circ','when':m.group(1),'title':clean(m.group(2))[:150],'url':'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html'})

# --- NFRA ---
t = rd('nfra_list.html')
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{8,120})</a>', t):
    txt = clean(m.group(2))
    if re.search(r'保险|监管|金融|通知|公告', txt):
        out.append({'src':'nfra','when':'?','title':txt,'url':m.group(1)[:130]})

for o in out:
    print(f"[{o['src']}] {o.get('when')} | {o['title'][:120]} | {o['url'][:120]}")
print('TOTAL', len(out))
