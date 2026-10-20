import re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
rss = open(os.path.join(BASE, 'ibm_rss.xml'), encoding='utf-8', errors='ignore').read()
print('ITEMS:')
for m in re.finditer(r'<item[ >].*?</item>', rss, re.S):
    b = m.group(0)
    ti = re.search(r'<title[^>]*>(.*?)</title>', b, re.S)
    li = re.search(r'<link[^>]*>(.*?)</link>', b, re.S)
    pd = re.search(r'<pubDate[^>]*>(.*?)</pubDate>', b, re.S)
    print((pd.group(1)[:25] if pd else '??'), '|', html.unescape(re.sub(r'<[^>]+>', '', ti.group(1)))[:95] if ti else '')
    print('   ', li.group(1).strip()[:110] if li else '')
