import re, html, glob, os
from datetime import datetime, timezone, timedelta
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'
HK = timezone(timedelta(hours=8))
for f in sorted(glob.glob(CACHE + 'gn_*.xml')):
    name = os.path.basename(f)
    data = open(f, encoding='utf-8', errors='replace').read()
    blocks = re.findall(r'<item>(.*?)</item>', data, re.S)
    good = 0
    samples = []
    for b in blocks:
        d = re.findall(r'<pubDate>(.*?)</pubDate>', b, re.S)
        if not d:
            continue
        ds = d[0].strip()
        try:
            dt = datetime.strptime(ds, '%a, %d %b %Y %H:%M:%S %z').astimezone(HK)
            good += 1
            if len(samples) < 3:
                samples.append(dt.strftime('%m-%d %H:%M'))
        except Exception as e:
            if len(samples) < 3:
                samples.append('ERR:' + ds[:40])
    print(f'{name:24} blocks={len(blocks):3} dated={good:3} samples={samples}')
