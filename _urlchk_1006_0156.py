import re, os
C = 'data/_cache1006_0156'
s = open(os.path.join(C, 'scmp_ins.xml'), encoding='utf-8', errors='ignore').read()
print('=== SCMP target links ===')
for m in re.finditer(r'<link>([^<]*3369(?:7|8)\d\d[^<]*)</link>', s):
    print(m.group(1))
print('=== SCMP all links (first 12) ===')
for m in list(re.finditer(r'<link>([^<]+)</link>', s))[:12]:
    print(m.group(1)[:120])
r = open(os.path.join(C, 'reinasia.html'), encoding='utf-8', errors='ignore').read()
print('=== REINASIA target slugs ===')
for pat in ['cigna-hk', 'cigna-healthcare', 'cpic-hk', 'prediction-markets', 'motor-insurance-fraud', 'trade-credit']:
    for m in set(re.findall(r'href="(https://reinasia\.com/[^"]*' + pat + r'[^"]*)"', r)):
        print(' ', m)
