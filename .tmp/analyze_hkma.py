import re

raw = open('.tmp/hkma.html', encoding='utf-8', errors='replace').read()
print('len:', len(raw))
dates = re.findall(r'20(?:25|26)-\d{2}-\d{2}', raw)
print('date strings sample:', dates[:15])
links = re.findall(r'href="([^"]*press[^"]*)"', raw)
print('press links sample:', links[:12])

# Find the block around a recent date
for m in re.finditer(r'20(?:25|26)-\d{2}-\d{2}', raw):
    i = m.start()
    snippet = raw[max(0, i-200):i+200].replace('\n', ' ')
    print('---')
    print(snippet[:420])
    if dates.index(m.group(0)) > 3:
        break
