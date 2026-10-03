import json, re, html
raw = json.load(open('data/_raw_1003_2210.json'))
txt = raw['hkma_press']['text']
found = re.findall(r'href="(/eng/news-and-media/press-releases/2026/10/[^"]+)"', txt)
print('hkma oct links:', sorted(set(found)))
idx = txt.find('press-releases/2026/09/20260930-9')
print(txt[max(0,idx-3000):idx+500].replace('\n',' ')[-2000:])
