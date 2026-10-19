import json, re, os
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta
C = '.cache1020_0033'
HK = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 19, 21, 13, tzinfo=HK)
out = []
j = json.load(open(os.path.join(C, 'ian.json')))
for post in j:
    dt = datetime.fromisoformat(post['date']).astimezone(HK)
    if dt >= CUT:
        out.append(dict(src='ian', title=re.sub(r'<[^>]+>', '', post['title']['rendered']), link=post['link'],
                        date=dt.isoformat(), excerpt=re.sub(r'<[^>]+>', '', post.get('excerpt', {}).get('rendered', ''))[:400]))
for f, s in [('artemis.xml', 'artemis'), ('rn.xml', 'rn')]:
    t = open(os.path.join(C, f), encoding='utf-8', errors='ignore').read()
    for m in re.finditer(r'<item>(.*?)</item>', t, re.S):
        b = m.group(1)
        def g(tag):
            mm = re.search(r'<%s[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</%s>' % (tag, tag), b, re.S)
            return re.sub(r'<[^>]+>', '', mm.group(1)).strip() if mm else ''
        try:
            dt = parsedate_to_datetime(g('pubDate')).astimezone(HK)
        except Exception:
            continue
        if dt >= CUT:
            out.append(dict(src=s, title=g('title'), link=g('link'), date=dt.isoformat(), excerpt=g('description')[:400]))
json.dump(out, open('.cache1020_0033/fresh.json', 'w'), ensure_ascii=False, indent=1)
for i in out:
    print(i['date'][:16], i['src'], '|', i['title'][:80])
    print('   ', i['link'])
