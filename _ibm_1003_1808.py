import re, html
raw=open('/tmp/ibm.xml',encoding='utf-8',errors='replace').read()
def strip(t): return html.unescape(re.sub(r'<[^>]+>','',t or '')).strip()
items=re.findall(r'<item>(.*?)</item>',raw,re.S)
print('IBM items:',len(items))
for it in items[:22]:
    t=re.search(r'<title[^>]*>(.*?)</title>',it,re.S); l=re.search(r'<link[^>]*>(.*?)</link>',it,re.S)
    d=re.search(r'<pubDate>(.*?)</pubDate>',it,re.S)
    print('  ',strip(d.group(1)) if d else '?','|',strip(t.group(1))[:95] if t else '?')
    print('     ',strip(l.group(1)) if l else '?')
