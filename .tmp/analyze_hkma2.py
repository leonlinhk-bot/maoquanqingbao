import re

raw = open('.tmp/hkma.html', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'href="(/eng/news-and-media/press-releases/2026/08/2026082\d-\d+/)"', raw):
    i = m.start()
    snippet = raw[max(0, i-350):i+100].replace('\n', ' ')
    print('===')
    print(snippet[-420:])
    print()
