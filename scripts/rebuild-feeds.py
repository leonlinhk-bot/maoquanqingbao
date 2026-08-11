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

# --- Auto-sync: update meta.windowNote + app.js embedded DATA ---
n = len(items)
data['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
data['meta']['itemCount'] = n
# Auto-refresh stats.intelligence from real data (keep other stats blocks untouched)
try:
    inte = data.setdefault('stats', {}).setdefault('intelligence', {})
    from collections import Counter as _C
    tiers = _C(i.get('sourceTier', '?') for i in items)
    tier_labels = {'official': '监管一手', 'insurer': '保司公告', 'media': '媒体报道',
                   'pro': '专业解读', 'research': '机构研究'}
    inte['totalItems'] = n
    inte['subtitle'] = {'sc': f'自动从 {n} 条资讯聚合 · sourceKey 标准化完成',
                        'tc': f'自動從 {n} 條資訊聚合 · sourceKey 標準化完成'}
    inte['sourceTiers'] = [{'tier': t, 'count': tiers.get(t, 0), 'label': tier_labels.get(t, t)}
                           for t in ('official', 'insurer', 'media', 'pro', 'research') if tiers.get(t)]
    themes = _C()
    for i in items:
        for t in (i.get('themes') or []):
            themes[t] += 1
    theme_labels = {'market': '市场', 'reg': '监管', 'compliance': '合规', 'firm': '保司',
                    'offshore': '跨境', 'macro': '宏观', 'product': '产品', 'channel': '渠道',
                    'tech': '科技', 'family-office': '家办', 'par': '分红', 'uw': '核保理赔',
                    'career': '职业', 'identity-planning': '身份规划', 'global-allocation': '全球配置'}
    inte['topThemes'] = [{'theme': t, 'count': c, 'label': theme_labels.get(t, t)}
                         for t, c in themes.most_common(10)]
    dates = sorted(i.get('publishedAt', '') for i in items if i.get('publishedAt'))
    if dates:
        inte['dateRange'] = {'sc': f"{dates[0][:10]} ~ {dates[-1][:10]}",
                             'tc': f"{dates[0][:10]} ~ {dates[-1][:10]}"}
except Exception as e:
    print(f'[warn] intelligence auto-refresh failed: {e}')
LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

app_path = ROOT / 'app.js'
app = app_path.read_text(encoding='utf-8')
start = app.find('window.HKII_DATA = ')
if start >= 0:
    obj_start = start + len('window.HKII_DATA = ')
    while app[obj_start] in ' \n\r\t': obj_start += 1
    depth = 0; in_str = False; esc2 = False; quote = ''
    j = obj_start
    while j < len(app):
        ch = app[j]
        if in_str:
            if esc2: esc2 = False
            elif ch == '\\': esc2 = True
            elif ch == quote: in_str = False
            j += 1; continue
        if ch in '"\'':
            in_str = True; quote = ch; j += 1; continue
        if ch == '{': depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0: j += 1; break
        j += 1
    end_j = j
    while end_j < len(app) and app[end_j] in '; \n\r\t': end_j += 1
    new_block = 'window.HKII_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
    app = app[:start] + new_block + app[end_j:]
    app_path.write_text(app, encoding='utf-8')

print(f"OK featured={len(feat)} all={n} windowNote=synced app.js=rebuilt")
# --- Closure check ---
checks = []
try:
    import json
    # 1. live-items.json
    live = json.loads(LIVE.read_text(encoding='utf-8'))
    live_n = len(live.get('items',[]))
    checks.append(f"live-items: {live_n}")
    # 2. feed/all.json
    allf = json.loads(FEED.joinpath('all.json').read_text(encoding='utf-8'))
    checks.append(f"feed/all: {allf.get('itemCount','?')}")
    # 3. feed/featured.json
    featf = json.loads(FEED.joinpath('featured.json').read_text(encoding='utf-8'))
    checks.append(f"feed/featured: {featf.get('itemCount','?')}") 
    # 4. app.js embedded DATA (brace-match extract)
    app_data = (ROOT/"app.js").read_text(encoding='utf-8')
    dstart = app_data.find('window.HKII_DATA = ')
    if dstart >= 0:
        dop = dstart + len('window.HKII_DATA = ')
        while app_data[dop] in ' \n\r\t': dop += 1
        ddepth = 0; din = False; desc = False; dq = ''
        dj = dop
        while dj < len(app_data):
            dc = app_data[dj]
            if din:
                if desc: desc = False
                elif dc == '\\': desc = True
                elif dc == dq: din = False
                dj += 1; continue
            if dc in '"\'':
                din = True; dq = dc; dj += 1; continue
            if dc == '{': ddepth += 1
            elif dc == '}':
                ddepth -= 1
                if ddepth == 0: dj += 1; break
            dj += 1
        if ddepth == 0 and dj > dop:
            try:
                embedded = json.loads(app_data[dop:dj])
                checks.append(f"app.js DATA: {len(embedded.get('items',[]))}")
            except: checks.append("app.js DATA: parse error")
    # 5. digests
    dig = live.get('digests',{})
    for p in ['daily','weekly','monthly','yearly']:
        checks.append(f"digests-{p}: {len(dig.get(p,[]))}")
    # 6. windowNote
    wn = live.get('meta',{}).get('windowNote',{})
    checks.append(f"windowNote: {wn.get('sc','?')}")
    # 7. agent.html (check if item count is embedded)
    agent_path = ROOT / 'agent.html'
    if agent_path.exists():
        agent_content = agent_path.read_text(encoding='utf-8')
        checks.append("agent.html: exists")
    # 8. sync stats.json from live-items stats
    stats_path = ROOT / 'data' / 'stats.json'
    if stats_path.exists():
        import json as _j2
        st = _j2.loads(stats_path.read_text(encoding='utf-8'))
        si = live.get('stats', {}).get('intelligence', {})
        st['intelligence'] = si
        stats_path.write_text(_j2.dumps(st, ensure_ascii=False, indent=2), encoding='utf-8')
        checks.append("stats.json: synced")
    print("  closure: " + " | ".join(checks))
except Exception as e:
    print(f"  closure check failed: {e}")
