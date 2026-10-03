import subprocess, json, re, html as H
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'

urls = [
 'https://www.insurancebusinessmag.com/asia/news/life-insurance/regulators-close-in-on-hanwha-lifes-acuon-deal-as-capital-questions-stack-up-592146.aspx',
 'https://www.insurancebusinessmag.com/asia/news/breaking-news/allianz-names-new-ceos-at-allianz-partners-and-allianz-direct-592079.aspx',
]
for u in urls:
    r = subprocess.run(['curl', '-sSL', '-m', '30', '-A', UA, u], capture_output=True, text=True)
    t = r.stdout or ''
    print('===', u.split('/')[-1], 'len', len(t))
    for pat in [r'"datePublished"\s*:\s*"([^"]+)"', r'"dateModified"\s*:\s*"([^"]+)"', r'<time[^>]*>([^<]+)</time>', r'property="article:published_time"\s+content="([^"]+)"']:
        m = re.findall(pat, t)
        if m:
            print('   ', pat, '=>', m[:3])

print('\n##### NFRA APIs #####')
cands = [
 'https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=914&itemId=915',
 'https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=920&itemId=923',
 'https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=921&itemId=924',
 'https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=922&itemId=925',
 'https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=937&itemId=938',
]
for u in cands:
    r = subprocess.run(['curl', '-sSL', '-m', '25', '-A', UA, u], capture_output=True, text=True)
    out = r.stdout or ''
    print('===', u, 'len', len(out))
    try:
        j = json.loads(out)
        data = j.get('data') or {}
        rows = data.get('rows') or data.get('list') or []
        print('   rptCode', j.get('rptCode'), 'rows', len(rows))
        for x in (rows or [])[:8]:
            print('    ', x.get('publishDate', ''), '|', H.unescape(x.get('docTitle') or x.get('title') or '')[:100])
    except Exception as e:
        print('   not json:', out[:160])
