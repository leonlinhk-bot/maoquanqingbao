import re, html, json
from datetime import datetime, timezone, timedelta
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

p = '/Users/leonliang/maoquanqingbao/.cache1023_0023/govhk.xml'
raw = re.sub(rb'^\s*<\?xml[^>]*\?>', b'', open(p, 'rb').read())
root = ET.fromstring(raw)
HKT = timezone(timedelta(hours=8))
kws = ['保險', '保監', '強積金', '年金', '財富', '退休', '金融', '跨境', '資產管理', '風險']
for it in root.iter('item'):
    t = (it.findtext('title') or '').strip()
    d = it.findtext('pubDate') or ''
    try:
        dt = parsedate_to_datetime(d).astimezone(HKT)
    except Exception:
        continue
    if dt < datetime(2026, 10, 22, 18, 0, tzinfo=HKT):
        continue
    if any(k in t for k in kws):
        print(dt.strftime('%m-%d %H:%M'), '|', t[:90])
        print('   ', it.findtext('link'))
