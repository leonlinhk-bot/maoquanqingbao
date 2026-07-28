#!/usr/bin/env python3
"""Rebuild feed JSON + RSS from live-items.json. Run after each data update."""
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data/live-items.json'
FEED = ROOT / 'feed'; FEED.mkdir(parents=True, exist_ok=True)
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def tx(obj):
    if not obj: return ''
    if isinstance(obj, dict): return obj.get('sc','') or obj.get('tc','') or ''
    return str(obj)
def esc(s): return str(s or '').replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

data = json.loads(LIVE.read_text(encoding='utf-8'))
items = data['items']

def light(it):
    return {'id':it['id'],'title':tx(it.get('title')),'summary':tx(it.get('summary')),
            'why':tx(it.get('why')),'sourceLabel':tx(it.get('source','')),
            'sourceTier':it.get('sourceTier',''),
            'tags':(it.get('tags',{}).get('sc',[]) if isinstance(it.get('tags'),dict) else (it.get('tags') or [])),
            'themes':it.get('themes',[]),'publishedAt':it.get('publishedAt',''),
            'effectiveAt':it.get('effectiveAt',''),'score':it.get('score',0),
            'originalUrl':it.get('originalUrl',''),
            'canonicalUrl':f"https://hkmaoquanqingbao.com/#item={it['id']}",
            'verifyStatus':it.get('verifyStatus','pending'),'rolesImpact':it.get('rolesImpact',{})}

feat = [i for i in items if i.get('featured')][:20]
FEED.joinpath('featured.json').write_text(json.dumps({
    'feed':'featured','title':'猫圈儿港险情报站 · 精选','generatedAt':now,'itemCount':len(feat),'items':[light(i) for i in feat]
},ensure_ascii=False,indent=2),encoding='utf-8')

FEED.joinpath('all.json').write_text(json.dumps({
    'feed':'all','title':'猫圈儿港险情报站 · 全部动态索引','generatedAt':now,'itemCount':len(items),
    'items':[{'id':it['id'],'title':tx(it.get('title',{})),'sourceTier':it.get('sourceTier',''),
             'themes':it.get('themes',[]),'publishedAt':it.get('publishedAt',''),
             'score':it.get('score',0),'canonicalUrl':f"https://hkmaoquanqingbao.com/#item={it['id']}",
             'originalUrl':it.get('originalUrl','')} for it in items]
},ensure_ascii=False,indent=2),encoding='utf-8')

rss_body = [f"""    <item>
      <title>{esc(tx(it.get('title',{})))}</title>
      <link>{esc(it.get('originalUrl','') or f'https://hkmaoquanqingbao.com/#item={it["id"]}')}</link>
      <guid isPermaLink="false">{it['id']}@hkmaoquanqingbao</guid>
      <pubDate>{it.get('publishedAt','')}</pubDate>
      <description><![CDATA[{tx(it.get('summary',''))}<br/><br/><strong>为什么重要：</strong>{tx(it.get('why',''))}]]></description>
    </item>""" for it in feat[:20]]
FEED.joinpath('featured.xml').write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>猫圈儿港险情报站 · 精选 RSS</title>
    <link>https://hkmaoquanqingbao.com</link>
    <description>香港保险监管与行业资讯聚合导读 · 每条可回追原文</description>
    <language>zh-Hant</language>
    <lastBuildDate>{now}</lastBuildDate>
    <atom:link href="https://hkmaoquanqingbao.com/feed/featured.xml" rel="self" type="application/rss+xml"/>
{chr(10).join(rss_body)}
  </channel>
</rss>""",encoding='utf-8')
print(f"OK featured={len(feat)} all={len(items)}")
