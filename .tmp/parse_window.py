import re, html, os, json, datetime

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')
CUTOFF = datetime.datetime(2026, 8, 19, 13, 17, 0, tzinfo=datetime.timezone.utc)  # 21:17+08:00

def parse_ts(s):
    s = s.strip()
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%S%z", "%d %b %Y"):
        try:
            dt = datetime.datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=datetime.timezone.utc)
            return dt.astimezone(datetime.timezone.utc)
        except ValueError:
            continue
    return None

def parse_gn(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    out = []
    for it in re.findall(r'<item>(.*?)</item>', raw, re.S):
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        s = re.search(r'<source[^>]*url="([^"]+)"[^>]*>(.*?)</source>', it, re.S)
        if not (t and d and l):
            continue
        title = html.unescape(re.sub(r'<[^>]+>', '', t.group(1))).strip()
        ts = parse_ts(d.group(1))
        out.append({
            'title': title, 'pubDate': ts.isoformat() if ts else d.group(1),
            'ts': ts, 'link': html.unescape(l.group(1)).strip(),
            'source': html.unescape(s.group(2)).strip() if s else '',
            'sourceUrl': s.group(1) if s else '',
        })
    return out

def parse_scmp(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    out = []
    for it in re.findall(r'<item>(.*?)</item>', raw, re.S):
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        if not (t and d and l):
            continue
        title = html.unescape(re.sub(r'<[^>]+>', '', t.group(1))).strip()
        ts = parse_ts(d.group(1))
        out.append({'title': title, 'pubDate': ts.isoformat() if ts else d.group(1),
                    'ts': ts, 'link': html.unescape(l.group(1)).strip(), 'source': 'SCMP', 'sourceUrl': ''})
    return out

allres = {}
for f in sorted(os.listdir(FDIR)):
    if f.endswith('.xml') and f.startswith('g_'):
        key = f.replace('.xml', '')
        items = parse_gn(os.path.join(FDIR, f))
        fresh = [i for i in items if i['ts'] and i['ts'] >= CUTOFF]
        allres[key] = fresh
        print(f"== {key}: {len(items)} items, {len(fresh)} in window")
        for i in fresh:
            print(f"   {i['pubDate'][:16]} | {i['source']} | {i['title'][:75]}")
    elif f == 'scmp-rss.xml':
        items = parse_scmp(os.path.join(FDIR, f))
        fresh = [i for i in items if i['ts'] and i['ts'] >= CUTOFF]
        allres['scmp'] = fresh
        print(f"== scmp: {len(items)} items, {len(fresh)} in window")
        for i in fresh:
            print(f"   {i['pubDate'][:16]} | {i['title'][:75]}")

json.dump({k: [{kk: (vv.isoformat() if isinstance(vv, datetime.datetime) else vv) for kk, vv in i.items() if kk != 'ts'} for i in v] for k, v in allres.items()},
          open(os.path.join(FDIR, 'window.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("saved window.json")
