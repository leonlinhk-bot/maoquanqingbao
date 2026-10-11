import re, json, html
D='.tmp/1012_0022'
def strip(s):
    return html.unescape(re.sub('<[^>]+>','',s)).strip()

# artemis rss
t=open(f'{D}/artemis_rss.xml',encoding='utf-8',errors='ignore').read()
items=re.findall(r'<item>(.*?)</item>', t, re.S)
print('### artemis RSS', len(items))
for it in items[:14]:
    ti=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
    pd=re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    ln=re.search(r'<link>(.*?)</link>', it, re.S)
    print(' ', pd.group(1) if pd else '', '|', strip(ti.group(1))[:85] if ti else '', '|', (ln.group(1) if ln else '')[:95])

# scmp rss
t=open(f'{D}/scmp_rss.xml',encoding='utf-8',errors='ignore').read()
items=re.findall(r'<item>(.*?)</item>', t, re.S)
print('### scmp RSS', len(items))
for it in items[:16]:
    ti=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
    pd=re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    ln=re.search(r'<link>(.*?)</link>', it, re.S)
    print(' ', pd.group(1) if pd else '', '|', strip(ti.group(1))[:85] if ti else '', '|', (ln.group(1) if ln else '')[:95])

# nfra
print('### nfra list head')
print(open(f'{D}/nfra_list.json',encoding='utf-8',errors='ignore').read()[:1500])
