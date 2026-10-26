import re, json

raw = open('.cache1025_2108/hkma.raw', encoding='utf-8', errors='replace').read()
txt = re.sub(r'<[^>]+>', '\n', raw)
lines = [l.strip() for l in txt.split('\n') if l.strip()]
# find lines with 2026 dates
hits = []
for i, l in enumerate(lines):
    if re.search(r'\b(2026|25 Oct|24 Oct|23 Oct)\b', l):
        ctx = ' '.join(lines[max(0, i-2):i+3])
        hits.append(ctx[:300])
print('--- HKMA date-ish lines (first 25) ---')
for h in hits[:25]:
    print('*', h)

print('\n--- HKMA lines containing insurance keywords ---')
kw = ['nsur', 'annuit', 'MPF', 'retirement', 'policy', 'scheme']
for i, l in enumerate(lines):
    if any(k in l for k in kw) and len(l) > 25:
        print(l[:200])
