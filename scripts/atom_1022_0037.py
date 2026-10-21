import xml.etree.ElementTree as ET, datetime, re, email.utils, json
D = '/Users/leonliang/maoquanqingbao/data/_1022_0037'
HKT = datetime.timezone(datetime.timedelta(hours=8))
NS = {'a': 'http://www.w3.org/2005/Atom'}
tree = ET.parse(D + '/ibm_rss.xml')
root = tree.getroot()
print('feed updated:', root.findtext('a:updated', namespaces=NS))
for e in root.findall('a:entry', NS):
    t = e.findtext('a:title', namespaces=NS)
    upd = e.findtext('a:updated', namespaces=NS) or e.findtext('a:published', namespaces=NS)
    link = ''
    for l in e.findall('a:link', NS):
        if l.get('rel') == 'alternate':
            link = l.get('href')
    summ = re.sub(r'<[^>]+>', '', e.findtext('a:summary', namespaces=NS) or '')[:160]
    dt = None
    if upd:
        try:
            dt = datetime.datetime.fromisoformat(upd.replace('Z', '+00:00')).astimezone(HKT)
        except Exception:
            pass
    print(f"{dt.strftime('%m-%d %H:%M') if dt else '?'} | {t}")
    print(f"   {link}")
    print(f"   {summ.strip()}")
