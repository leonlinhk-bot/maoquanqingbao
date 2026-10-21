import json, re, glob, os, datetime, email.utils, xml.etree.ElementTree as ET

D = '/Users/leonliang/maoquanqingbao/data/_1022_0037'
START = datetime.datetime(2026, 10, 21, 1, 6, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
END   = datetime.datetime(2026, 10, 22, 0, 40, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
HKT = datetime.timezone(datetime.timedelta(hours=8))

def norm(dt):
    if dt.tzinfo is None:
        return dt.replace(tzinfo=HKT)
    return dt.astimezone(HKT)

def inwin(dt):
    d = norm(dt)
    return START <= d <= END

def parse_rss(path, label):
    out = []
    try:
        tree = ET.parse(path)
    except Exception as e:
        print(f'!! {label} parse error: {e}')
        return out
    root = tree.getroot()
    for it in root.iter('item'):
        t = (it.findtext('title') or '').strip()
        link = (it.findtext('link') or '').strip()
        pd = it.findtext('pubDate') or it.findtext('{http://purl.org/dc/elements/1.1/}date') or ''
        dt = None
        if pd:
            try:
                dt = norm(email.utils.parsedate_to_datetime(pd))
            except Exception:
                try:
                    dt = norm(datetime.datetime.fromisoformat(pd.replace('Z', '+00:00')))
                except Exception:
                    pass
        desc = re.sub(r'<[^>]+>', '', (it.findtext('description') or ''))[:200].strip()
        out.append({'src': label, 'title': t, 'link': link, 'dt': dt, 'desc': desc})
    return out

all_items = []
for path, label in [('artemis.xml', 'artemis'), ('reins.xml', 'reinsurancenews'),
                    ('ibm_rss.xml', 'insurancebusinessmag'), ('iaasia.xml', 'insuranceasia'),
                    ('scmp.xml', 'scmp'), ('govhk.xml', 'govhk')]:
    p = os.path.join(D, path)
    if os.path.exists(p):
        all_items += parse_rss(p, label)

# InsuranceAsia News WP JSON
p = os.path.join(D, 'ian.json')
if os.path.exists(p):
    try:
        data = json.load(open(p))
        for it in data:
            dt = norm(datetime.datetime.fromisoformat(it['date']))
            title = re.sub(r'<[^>]+>', '', it.get('title', {}).get('rendered', '')).strip()
            desc = re.sub(r'<[^>]+>', '', it.get('excerpt', {}).get('rendered', '')).strip()[:200]
            all_items.append({'src': 'insuranceasianews', 'title': title,
                              'link': it.get('link', ''), 'dt': dt, 'desc': desc})
    except Exception as e:
        print('!! ian.json error', e)

print('=== IN WINDOW (Oct21 01:06 -> Oct22 00:40) ===')
win = [x for x in all_items if x['dt'] and inwin(x['dt'])]
win.sort(key=lambda x: x['dt'], reverse=True)
for x in win:
    print(f"{x['dt'].strftime('%m-%d %H:%M')} | {x['src']:22s} | {x['title'][:70]}")
    print(f"    {x['link']}")

print(f"\n=== TOTALS: fetched={len(all_items)} in-window={len(win)} ===")
print('\n=== per-source newest 3 (regardless of window, for sanity) ===')
by = {}
for x in all_items:
    by.setdefault(x['src'], []).append(x)
for s, lst in by.items():
    lst2 = [y for y in lst if y['dt']]
    lst2.sort(key=lambda y: y['dt'], reverse=True)
    print(f'-- {s} ({len(lst)}):')
    for y in lst2[:3]:
        print('   ', y['dt'].strftime('%Y-%m-%d %H:%M'), y['title'][:60])
json.dump([{k: (v.isoformat() if isinstance(v, datetime.datetime) else v) for k, v in x.items()} for x in win],
          open('/Users/leonliang/maoquanqingbao/data/_1022_0037/window.json', 'w'), ensure_ascii=False, indent=1)
