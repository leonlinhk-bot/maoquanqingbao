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
# Future-date guard: 手动入库可能误把文章内部引用的日期当作发布时间
from datetime import datetime as _dt, timezone as _tz
_now = _dt.now(_tz.utc)
_future_ids = []
for _i in items:
    _s = (_i.get('publishedAt') or '').replace('Z', '+00:00')
    if not _s:
        continue
    try:
        _d = _dt.fromisoformat(_s)
        if _d.tzinfo is None:
            _d = _d.replace(tzinfo=_tz.utc)
        if _d > _now:
            _future_ids.append(_i['id'])
    except Exception:
        pass
if _future_ids:
    print(f'[guard] future-dated items: {_future_ids}')
# Auto-refresh stats.intelligence from real data (keep other stats blocks untouched)
try:
    inte = data.setdefault('stats', {}).setdefault('intelligence', {})
    from collections import Counter as _C
    tiers = _C(i.get('sourceTier', '?') for i in items)
    tier_labels = {'official': '监管一手', 'insurer': '保司公告', 'broker': '经纪行',
                   'media': '媒体报道', 'pro': '专业解读', 'research': '机构研究'}
    inte['totalItems'] = n
    inte['subtitle'] = {'sc': f'自动从 {n} 条资讯聚合 · sourceKey 标准化完成',
                        'tc': f'自動從 {n} 條資訊聚合 · sourceKey 標準化完成'}
    inte['sourceTiers'] = [{'tier': t, 'count': tiers.get(t, 0), 'label': tier_labels.get(t, t)}
                           for t in ('official', 'insurer', 'broker', 'media', 'pro', 'research') if tiers.get(t)]
    themes = _C()
    for i in items:
        for t in (i.get('themes') or []):
            themes[t] += 1
    theme_labels = {'market': '市场', 'reg': '监管', 'compliance': '合规', 'firm': '保司',
                    'offshore': '跨境', 'macro': '宏观', 'product': '产品', 'channel': '渠道',
                    'tech': '科技', 'family-office': '家办', 'par': '分红', 'uw': '核保理赔',
                    'career': '职业', 'identity-planning': '身份规划', 'global-allocation': '全球配置',
                    'reinsurance': '再保险', 'cross-border': '跨境', 'health': '健康医疗',
                    'insurtech': '保险科技', 'taxation': '税务', 'results': '业绩',
                    'retirement': '退休养老', 'benchmark': '对标', 'esg': 'ESG',
                    'captive': '专属自保', 'ai': '人工智能', 'cyber': '网络风险',
                    'annuity': '年金', 'global-wealth': '全球财富', 'ils': '保险相连证券'}
    inte['topThemes'] = [{'theme': t, 'count': c, 'label': theme_labels.get(t, t)}
                         for t, c in themes.most_common(10)]
    dates = sorted(i.get('publishedAt', '') for i in items if i.get('publishedAt'))
    if dates:
        inte['dateRange'] = {'sc': f"{dates[0][:10]} ~ {dates[-1][:10]}",
                             'tc': f"{dates[0][:10]} ~ {dates[-1][:10]}"}
except Exception as e:
    print(f'[warn] intelligence auto-refresh failed: {e}')

# --- Auto-sync: digests 自动补桶（daily/weekly/monthly/yearly 跟随时段最新日期） ---
# 历史 digests 是手动构建的静态数据（曾停在 2026-07-30 不随每日更新）。
# 规则：按 publishedAt 归入对应日/周/月/年桶；已有桶的 key 不重建（保留 itemIds 语义），只补缺的桶。
try:
    from datetime import datetime as _dts, timedelta as _td
    _dig = data.setdefault('digests', {})
    _have_d = set(x.get('key') for x in _dig.get('daily', []))
    _have_w = set(x.get('key') for x in _dig.get('weekly', []))
    _have_m = set(x.get('key') for x in _dig.get('monthly', []))
    _have_y = set(x.get('key') for x in _dig.get('yearly', []))
    # 只对「当日之前」的条目建桶，防止未来日期污染
    _today = _dt.now(_tz.utc).strftime('%Y-%m-%d')
    _bk_d, _bk_w, _bk_m, _bk_y = {}, {}, {}, {}
    for _i in items:
        _s = (_i.get('publishedAt') or '')[:10]
        if not _s or _s > _today:
            continue
        try:
            _dd = _dt.strptime(_s, '%Y-%m-%d')
        except Exception:
            continue
        # ISO 周号（与历史 2026-W31 格式一致）
        _iso = _dd.isocalendar()
        _wk = f"{_iso[0]}-W{_iso[1]:02d}"
        _bk_d.setdefault(_s, []).append(_i['id'])
        _bk_w.setdefault(_wk, []).append(_i['id'])
        _bk_m.setdefault(_s[:7], []).append(_i['id'])
        _bk_y.setdefault(_s[:4], []).append(_i['id'])
    def _mk(key, ids, suffix=''):
        return {'key': key, 'label': {'sc': key + suffix, 'tc': key + suffix},
                'itemCount': len(ids), 'itemIds': ids}
    # 各粒度：新桶 + 已有桶合并，按 key 倒序统一排序（无条件执行，幂等修正历史乱序）
    def _merged(existing, newmap, newkeys, suffix=''):
        out = [_mk(k, newmap[k], suffix) for k in newkeys]
        return sorted(out + (existing or []), key=lambda x: x.get('key',''), reverse=True)
    _new_d = sorted((k for k in _bk_d if k not in _have_d), reverse=True)
    _dig['daily'] = _merged(_dig.get('daily', []), _bk_d, _new_d)
    _new_w = sorted((k for k in _bk_w if k not in _have_w), reverse=True)
    _dig['weekly'] = _merged(_dig.get('weekly', []), _bk_w, _new_w)
    _new_m = sorted((k for k in _bk_m if k not in _have_m), reverse=True)
    _dig['monthly'] = _merged(_dig.get('monthly', []), _bk_m, _new_m)
    _new_y = sorted((k for k in _bk_y if k not in _have_y), reverse=True)
    _dig['yearly'] = _merged(_dig.get('yearly', []), _bk_y, _new_y, suffix=' 年')
    if _new_d or _new_w or _new_m or _new_y:
        print(f"[digests] 补桶 daily+{len(_new_d)} weekly+{len(_new_w)} monthly+{len(_new_m)} yearly+{len(_new_y)}")
except Exception as e:
    print(f'[warn] digests auto-fill failed: {e}')

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

# 更新 index.html 的 app.js 版本号（cache-busting，避免浏览器缓存旧版）
import re as _re
_idx_path = ROOT / 'index.html'
if _idx_path.exists():
    _idx = _idx_path.read_text(encoding='utf-8')
    _idx_new = _re.sub(r'app\.js(\?v=[^"]*)?', f'app.js?v={n}', _idx)
    if _idx_new != _idx:
        _idx_path.write_text(_idx_new, encoding='utf-8')

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
