import re, html
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
t=open(f'{RAW}/probe_f114bec3dd5bded575317a40b5c1a033.html',encoding='utf-8',errors='ignore').read()
m=re.search(r'<title[^>]*>(.*?)</title>', t, re.S); print('TITLE:', p(m.group(1)) if m else '?')
# find main content
body=re.sub(r'<script.*?</script>','',t,flags=re.S)
txt=p(body)
i=txt.find('Press')
print(txt[:200])
print('...')
for kw in ['10.3','DIS','7.1','9.5','September 2026','2026']:
    j=txt.find(kw)
    if j>0:
        print(f'[{kw}]', txt[max(0,j-150):j+250])
        break
# dump last portion which usually has content
print('\n--- tail 2500 ---')
print(txt[-2500:])
