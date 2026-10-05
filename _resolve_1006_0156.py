import re, html, os, json, subprocess
C = 'data/_cache1006_0156'
def clean(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()

def items(f):
    p = os.path.join(C, f)
    h = open(p, encoding='utf-8', errors='ignore').read()
    out = []
    for m in re.finditer(r'<item>(.*?)</item>', h, re.S):
        b = m.group(1)
        t = clean(re.search(r'<title>(.*?)</title>', b, re.S).group(1))
        l = clean(re.search(r'<link>(.*?)</link>', b, re.S).group(1))
        d = clean(re.search(r'<pubDate>(.*?)</pubDate>', b, re.S).group(1)) if '<pubDate>' in b else ''
        s = clean(re.search(r'<source[^>]*>(.*?)</source>', b, re.S).group(1)) if '<source' in b else ''
        out.append({'title': t, 'link': l, 'date': d, 'source': s})
    return out

want = []
for f in ['gn_fam.xml', 'gn_insurtech.xml', 'gn_ia.xml']:
    for it in items(f):
        if re.search(r'\b(0?5|0?6)\s+Oct\s+2026', it['date']):
            want.append(it)

print('candidates:', len(want))
res = []
for it in want:
    u = it['link']
    try:
        r = subprocess.run(['curl', '-sIL', '-m', '20', '-o', '/dev/null',
                            '-w', '%{url_effective}', u], capture_output=True, text=True)
        final = r.stdout.strip()
    except Exception as e:
        final = 'ERR ' + str(e)
    item = dict(it, finalUrl=final)
    res.append(item)
    print('---')
    print('T:', it['title'][:95])
    print('S:', it['source'], '|', it['date'])
    print('F:', final[:150])
json.dump(res, open('.tmp/gnresolved_1006.json', 'w'), ensure_ascii=False, indent=1)
print('saved', len(res))
