import re, html
def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s); s = html.unescape(s); return re.sub(r'\s+', ' ', s).strip()
t = open('/tmp/scmp92.xml', encoding='utf-8', errors='ignore').read()
print('channel:', clean(re.search(r'<title>(.*?)</title>', t, re.S).group(1))[:120] if re.search(r'<title>', t) else '')
for it in re.findall(r'<item>(.*?)</item>', t, re.S)[:20]:
    ti = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
    da = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    lk = re.search(r'<link>(.*?)</link>', it, re.S)
    de = re.search(r'<description>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>', it, re.S)
    print('*', clean(da.group(1)) if da else '?', '|', clean(ti.group(1)) if ti else '?')
    print('   ', (lk.group(1).strip() if lk else '')[:110])
    if de:
        print('    desc:', clean(de.group(1))[:150])
