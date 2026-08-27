#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, json, html as htmllib, subprocess, urllib.parse, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def curl(url, timeout=35):
    return subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                          capture_output=True, text=True).stdout

print('===== 1. HKEX retry (lang=E, searchType=0, wider) =====')
for params in [
    'lang=E&category=0&market=SEHK&searchType=0&documentType=-1&fromDate=20260820&toDate=20260826&title=&stockId=966',
    'lang=CH&category=0&market=SEHK&searchType=0&documentType=-1&fromDate=20260820&toDate=20260826&title=太平&stockId=',
]:
    u = 'https://www1.hkexnews.hk/search/titleSearchServlet.do?' + params
    txt = curl(u)
    print('---', params[:60], '->', txt[:800])

print()
print('===== 2. EastMoney fast news =====')
try:
    txt = curl('https://np-listapi.eastmoney.com/comm/web/getFastNewsList?client=web&biz=web_724&fastColumn=102&sortEnd=&pageSize=80&req_trace=1')
    d = json.loads(txt)
    items = d.get('data', {}).get('fastNewsList', []) or d.get('data', {}).get('list', [])
    print('items:', len(items))
    for it in items[:60]:
        t = it.get('title', '')
        code = it.get('code', '')
        tm = it.get('showTime', '') or it.get('ctime', '')
        url = ''
        if code:
            url = f'https://finance.eastmoney.com/a/{code}.html'
        if any(k in t for k in ['保险', '太平', '巴克', '离岸', '家办', '家族办公', '香港', '资管', '财富']):
            print('  ', tm, '|', t[:70], '|', url)
except Exception as e:
    print('ERR', e)

print()
print('===== 3. Sina 7x24 =====')
try:
    txt = curl('https://zhibo.sina.com.cn/api/zhibo/feed?callback=x&page=1&page_size=100&zhibo_id=152')
    m = re.search(r'^x\((.*)\)$', txt.strip(), re.S)
    d = json.loads(m.group(1)) if m else json.loads(txt)
    feed = d['result']['data']['feed']['list']
    print('items:', len(feed))
    for it in feed[:60]:
        t = it.get('rich_text', '') or it.get('text', '')
        tm = it.get('create_time', '')
        u = it.get('url', '') or ''
        if any(k in t for k in ['保险', '太平', '巴克', '离岸', '家办', '家族办公', '香港', '资管']):
            print('  ', tm, '|', re.sub(r'<[^>]+>', '', t)[:75], '|', u[:110])
except Exception as e:
    print('ERR', e)
