import re
x=open('.tmp/1008_0007/fstb.xml',encoding='utf-8',errors='ignore').read()
items=re.findall(r'<item>(.*?)</item>', x, re.S)
kw=['保險','保監','積金','強積金','退休','理財','金融','財經','基金','年金','儲蓄','稅']
print('govhk items', len(items))
cnt=0
for it in items:
    t=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
    p=re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    l=re.search(r'<link>(.*?)</link>', it, re.S)
    title=t.group(1).strip() if t else ''
    if any(k in title for k in kw):
        cnt+=1
        print((p.group(1).strip() if p else ''), '|', title[:95], '|', (l.group(1).strip() if l else ''))
print('matched', cnt)
