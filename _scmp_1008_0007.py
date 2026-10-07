import re
D='.tmp/1008_0007'
h=open(f'{D}/scmp_rss.xml',encoding='utf-8',errors='ignore').read()
items=re.findall(r'<item>(.*?)</item>', h, re.S)
print('scmp items', len(items))
for it in items:
    t=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
    p=re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    l=re.search(r'<link>(.*?)</link>', it, re.S)
    print((p.group(1).strip() if p else ''), '|', (t.group(1).strip() if t else '')[:100], '|', (l.group(1).strip() if l else ''))
