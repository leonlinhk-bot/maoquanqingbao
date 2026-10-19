import re
t = open('.cache1020_0033/hkma.html', encoding='utf-8', errors='ignore').read()
txt = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
txt = re.sub(r'<[^>]+>', '\n', txt)
txt = re.sub(r'&nbsp;', ' ', txt)
lines = [l.strip() for l in txt.split('\n') if l.strip()]
for i, l in enumerate(lines):
    if re.search(r'October 2026', l):
        print('>>>', i, '|', ' || '.join(lines[max(0,i-3):i+3])[:400])
print('---- first 60 lines ----')
print('\n'.join(lines[:60]))
