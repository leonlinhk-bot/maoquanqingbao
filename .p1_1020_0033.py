import json, re, os, glob
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta

C = '.cache1020_0033'
HK = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 19, 21, 13, tzinfo=HK)

def norm(d):
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(HK)

def rss_items(path, name):
    if not os.path.exists(path): return []
    t = open(path, encoding='utf-8', errors='ignore').read()
    out = []
    for m in re.finditer(r'<item>(.*?)</item>', t, re.S):
        b = m.group(1)
        def g(tag):
            mm = re.search(r'<%s[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</%s>' % (tag, tag), b, re.S)
            return re.sub(r'<[^>]+>', '', mm.group(1)).strip() if mm else ''
        pd = g('pubDate') or g('dc:date')
        dt = None
        if pd:
            try: dt = norm(parsedate_to_datetime(pd))
            except Exception:
                try: dt = norm(datetime.fromisoformat(pd.replace('Z', '+00:00')))
                except Exception: pass
        out.append(dict(src=name, title=g('title'), link=g('link'), date=dt, desc=g('description')[:300]))
    return out

def atom_items(path, name):
    t = open(path, encoding='utf-8', errors='ignore').read()
    out = []
    for m in re.finditer(r'<entry>(.*?)</entry>', t, re.S):
        b = m.group(1)
        title = re.search(r'<title[^>]*>(.*?)</title>', b, re.S)
        link = re.search(r'<link[^>]*href="([^"]+)"', b)
        upd = re.search(r'<(?:updated|published)>(.*?)</', b)
        dt = None
        if upd:
            try: dt = norm(datetime.fromisoformat(upd.group(1).replace('Z', '+00:00')))
            except Exception: pass
        out.append(dict(src=name, title=re.sub(r'<!\[CDATA\[|\]\]>', '', title.group(1)).strip() if title else '',
                        link=link.group(1) if link else '', date=dt, desc=''))
    return out

allitems = []
for p, n in [('insuranceasia.xml','insuranceasia'), ('ibm_rss.xml','ibm'), ('artemis.xml','artemis'), ('rn.xml','rn'), ('govhk.xml','govhk')]:
    allitems += rss_items(os.path.join(C, p), n)

# IAN wordpress json
try:
    j = json.load(open(os.path.join(C, 'ian.json')))
    for post in j:
        dt = None
        try: dt = norm(datetime.fromisoformat(post['date']))
        except Exception: pass
        allitems.append(dict(src='ian', title=re.sub(r'<[^>]+>', '', post['title']['rendered']),
                             link=post['link'], date=dt, desc=re.sub(r'<[^>]+>', '', post.get('excerpt', {}).get('rendered', ''))[:300]))
except Exception as e:
    print('ian err', e)

print('total parsed:', len(allitems))
fresh = [i for i in allitems if i['date'] and i['date'] >= CUT]
fresh.sort(key=lambda x: x['date'], reverse=True)
print('fresh since', CUT.isoformat(), ':', len(fresh))
for i in fresh:
    print(i['date'].strftime('%m-%d %H:%M'), '|', i['src'], '|', i['title'][:110], '|', i['link'][:110])

print('\n== latest 5 per source (for context) ==')
from collections import defaultdict
by = defaultdict(list)
for i in allitems:
    if i['date']: by[i['src']].append(i)
for s, lst in by.items():
    lst.sort(key=lambda x: x['date'], reverse=True)
    print('##', s, lst[0]['date'].strftime('%m-%d %H:%M'))
    for i in lst[:4]:
        print('   ', i['date'].strftime('%m-%d %H:%M'), i['title'][:100])
