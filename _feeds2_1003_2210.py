import subprocess, re, html, xml.etree.ElementTree as ET
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'
feeds = {
 'artemis': 'https://www.artemis.bm/feed/',
 'asr': 'https://www.asiainsurancereview.com/RSS/News',
 'ibm_asia_rss': 'https://www.insurancebusinessmag.com/asia/rss/',
 'ian_rss': 'https://insuranceasianews.com/feed/',
}
for k, u in feeds.items():
    r = subprocess.run(['curl', '-sSL', '-m', '30', '-A', UA, u], capture_output=True, text=True)
    t = r.stdout or ''
    print('===', k, u, 'len', len(t))
    if '<' not in t[:200]:
        print('   non-xml:', t[:200]); continue
    try:
        root = ET.fromstring(t)
        n = 0
        for it in root.iter('item'):
            ti = (it.findtext('title') or '').strip()
            pd = (it.findtext('pubDate') or '').strip()
            lk = (it.findtext('link') or '').strip()
            print(f'   {pd} | {ti[:100]}')
            print(f'        {lk}')
            n += 1
            if n > 14: break
        if n == 0: print('   no items')
    except Exception as e:
        print('   parse err', e, t[:200])
