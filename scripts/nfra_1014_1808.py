#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 14, 2, 11, tzinfo=HKT)
d = json.load(open('data/_1014/nfra_dynamics.raw', encoding='utf-8'))
for r in d['data']['rows']:
    dt = datetime.strptime(r['publishDate'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=HKT)
    flag = 'NEW ' if dt > CUT else '    '
    print(f"{flag}{r['publishDate']} | {r['docTitle'].replace(chr(10),' ')} | https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId={r['docId']}&itemId=915")
