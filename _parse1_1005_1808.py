import json, re, sys, html
from datetime import datetime, timedelta, timezone
HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 5, 2, 39, tzinfo=HKT)
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def cliptxt(s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

print('=== InsuranceAsia RSS ===')
try:
    x = open(CACHE+'insuranceasia.xml', encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'<item>(.*?)</item>', x, re.S):
        b = m.group(1)
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        l = re.search(r'<link>(.*?)</link>', b, re.S)
        print('  ', (d.group(1) if d else '?').strip(), '|', (t.group(1) if t else '?').strip()[:110])
        print('      ', (l.group(1) if l else '').strip())
except Exception as e:
    print('ERR', e)

print()
print('=== InsuranceAsiaNews WP API ===')
try:
    d = json.load(open(CACHE+'ian.json'))
    for p in d:
        print('  ', p.get('date'), '|', cliptxt(p.get('title',{}).get('rendered',''))[:110])
        print('      ', p.get('link'))
except Exception as e:
    print('ERR', e)
