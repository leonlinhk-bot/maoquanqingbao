import json, re, os, html
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
import glob

RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
HK = timezone(timedelta(hours=8))
def rd(n):
    p = os.path.join(RAW, n)
    try:
        return open(p, encoding='utf-8', errors='ignore').read()
    except Exception as e:
        return ''

def norm(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def show(name, rows, n=25):
    print(f'===== {name} ({len(rows)}) =====')
    for r in rows[:n]:
        print(' -', r)

# --- RSS generic ---
def parse_rss(txt):
    out = []
    for m in re.finditer(r'<item>(.*?)</item>', txt, re.S):
        blk = m.group(1)
        def g(tag):
            mm = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', blk, re.S)
            return norm(mm.group(1)) if mm else ''
        out.append({'title': g('title'), 'link': g('link'), 'date': g('pubDate') or g('dc:date'), 'desc': g('description')[:200]})
    return out

for f in ['insuranceasia.rss', 'scmp_ins.rss']:
    rows = parse_rss(rd(f))
    print(f'===== {f} ({len(rows)}) =====')
    for r in rows[:18]:
        print(' -', r['date'], '|', r['title'][:110], '|', r['link'][:110])

# --- google news ---
for f in ['gnews_ia.xml','gnews_ins.xml','gnews_fo.xml','gnews_insurer.xml','gnews_cn.xml']:
    txt = rd(f)
    rows = parse_rss(txt)
    print(f'===== {f} ({len(rows)}) =====')
    for r in rows[:20]:
        d = r['date']
        try:
            d = parsedate_to_datetime(r['date']).astimezone(HK).strftime('%m-%d %H:%M')
        except Exception:
            pass
        print(' -', d, '|', r['title'][:110])

# --- govhk rss ---
txt = rd('govhk_zh.xml')
rows = parse_rss(txt)
print(f'===== govhk_zh.xml ({len(rows)}) =====')
for r in rows[:25]:
    d = r['date']
    try:
        d = parsedate_to_datetime(r['date']).astimezone(HK).strftime('%m-%d %H:%M')
    except Exception:
        pass
    print(' -', d, '|', r['title'][:110], '|', r['link'][:90])

# --- insuranceasia news (WP json) ---
try:
    j = json.loads(rd('ian.json'))
    print(f'===== ian.json ({len(j)}) =====')
    for it in j[:15]:
        print(' -', it.get('date'), '|', norm(it.get('title',{}).get('rendered',''))[:110], '|', it.get('link'))
except Exception as e:
    print('ian.json err', e)
