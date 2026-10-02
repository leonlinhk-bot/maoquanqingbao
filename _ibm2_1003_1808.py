import re, html
raw = open('/tmp/ibm.xml', encoding='utf-8', errors='replace').read()
def strip(t): return html.unescape(re.sub(r'<[^>]+>', '', t or '')).strip()
entries = re.findall(r'<entry>(.*?)</entry>', raw, re.S)
print('IBM atom entries:', len(entries))
for e in entries[:30]:
    t = re.search(r'<title[^>]*>(.*?)</title>', e, re.S)
    l = re.search(r'<link[^>]*href="([^"]+)"', e, re.S)
    d = re.search(r'<updated>(.*?)</updated>', e, re.S) or re.search(r'<published>(.*?)</published>', e, re.S)
    s = re.search(r'<summary[^>]*>(.*?)</summary>', e, re.S)
    print('  ', strip(d.group(1)) if d else '?', '|', strip(t.group(1))[:95] if t else '?')
    print('     ', strip(l.group(1)) if l else '?')
    if s: print('      ~', strip(s.group(1))[:180])
