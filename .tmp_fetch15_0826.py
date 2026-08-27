#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, json, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def curl(url, timeout=35):
    return subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                          capture_output=True, text=True).stdout

print('===== EastMoney fast news pages 1-4 (all titles) =====')
seen = set()
for page in range(1, 5):
    try:
        txt = curl(f'https://np-listapi.eastmoney.com/comm/web/getFastNewsList?client=web&biz=web_724&fastColumn=102&sortEnd=&pageSize=80&pageIndex={page}&req_trace=1')
        d = json.loads(txt)
        items = d.get('data', {}).get('fastNewsList', []) or []
        print(f'--- page {page}: {len(items)} items')
        for it in items:
            t = it.get('title', '')
            tm = it.get('showTime', '') or it.get('ctime', '')
            code = it.get('code', '')
            key = (tm, t[:40])
            if key in seen:
                continue
            seen.add(key)
            url = f'https://finance.eastmoney.com/a/{code}.html' if code else ''
            print(f'  {tm} | {t[:80]} | {url}')
    except Exception as e:
        print('ERR page', page, e)

print()
print('===== EastMoney search: 香港保险 / 离岸资产 =====')
for kw in ['香港保险', '离岸资产 监管', '保险 新单 香港']:
    try:
        param = json.dumps({"uid": "", "keyword": kw, "type": ["cmsArticleWebOld"], "client": "web",
                            "clientType": "web", "clientVersion": "curr",
                            "param": {"cmsArticleWebOld": {"searchScope": "default", "sort": "time",
                                      "pageIndex": 1, "pageSize": 8, "preTag": "", "postTag": ""}}},
                           ensure_ascii=False)
        url = 'https://search-api-web.eastmoney.com/search/jsonp?cb=x&param=' + urllib.parse.quote(param)
        txt = curl(url)
        m = re.search(r'^x\((.*)\)$', txt.strip(), re.S)
        d = json.loads(m.group(1)) if m else json.loads(txt)
        arts = d.get('result', {}).get('cmsArticleWebOld', []) or []
        print(f'--- {kw}: {len(arts)} hits')
        for a in arts[:8]:
            t = re.sub(r'<[^>]+>', '', a.get('title', ''))
            u = a.get('url', '')
            dt = a.get('date', '')
            print(f'  {dt} | {t[:70]} | {u[:120]}')
    except Exception as e:
        print('ERR', kw, e)
