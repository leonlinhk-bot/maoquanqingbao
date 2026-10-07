#!/usr/bin/env python3
"""
按字段规范采集 RSS/Atom 源 → 标准 JSON（对接站点前端渲染）。

落实的字段规范（源自第三方《信息源情报手册》中被采纳的部分）：
  1. published_hkt  —— pubDate 原文多为 UTC，必须显式转 +08:00
  2. summary        —— 去 HTML 标签，并去掉 WordPress 尾巴
                       （"The post … appeared first on …"）
  3. fingerprint     —— 对「条目集合」做哈希（不是整条 feed！否则 lastBuildDate
                       每次变化都会报假变更 → 天天误报）
  4. 只报新增       —— feed 是滑动窗口，条目退出窗口是正常行为，不算「下架」
  5. paywalled      —— 检测 MemberPress 等付费墙标记，显式标注（避免用户
                       以为内容残缺是 bug）
  6. 轮询守卫       —— 间隔 × 日均产出 ≤ 窗口条数的 1/3，否则告警（防静默漏报）

用法:
  python3 scripts/feed-fetch.py --feed https://x.com/feed/ --key example [--apply]
输出:
  data/_feed-state/<key>.json   状态（已见 id、指纹、上次时间）
  data/_feed-out/<key>.json     标准结构（新增条目 + 口径说明）
"""
import os, re, sys, json, hashlib, argparse, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
import xml.etree.ElementTree as ET

ROOT = '/Users/leonliang/maoquanqingbao'
STATE_DIR = os.path.join(ROOT, 'data', '_feed-state')
OUT_DIR = os.path.join(ROOT, 'data', '_feed-out')
HKT = timezone(timedelta(hours=8))
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/122.0 Safari/537.36')
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))

WP_TAIL = re.compile(r'\s*The post\s+.*?\s+appeared first on\s+.*?\.?\s*$', re.I | re.S)
PAYWALL_MARKERS = ('mepr-unauthorized', 'mp_wrapper', 'MemberPress', 'subscribe to read',
                   'subscription', 'paywall')


def strip_html(s):
    s = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', '', s or '')
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = (s.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<')
          .replace('&gt;', '>').replace('&#8217;', '’').replace('&#8216;', '‘')
          .replace('&#8220;', '“').replace('&#8221;', '”').replace('&#8211;', '–'))
    return re.sub(r'\s+', ' ', s).strip()


def to_hkt(dt_str):
    """RFC822 / ISO → +08:00 ISO 字符串"""
    if not dt_str:
        return None
    try:
        dt = parsedate_to_datetime(dt_str)
    except Exception:
        try:
            dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
        except Exception:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(HKT).isoformat()


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
    with OPENER.open(req, timeout=25) as r:
        return r.read()


def parse_feed(raw):
    # 有些站的 feed 前面带 HTML 注释/空白（例：Drupal 的 THEME DEBUG 输出），
    # 会让 XML 解析器报「declaration not at start of entity」→ 先截到真正的 XML 起点。
    # 教训：解析失败 ≠ 没有内容，先修工具再下结论。
    if isinstance(raw, (bytes, bytearray)):
        for marker in (b'<?xml', b'<rss', b'<feed', b'<rdf'):
            i = raw.find(marker)
            if i >= 0:
                if i > 0:
                    raw = raw[i:]
                break
    root = ET.fromstring(raw)
    items = []
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    nodes = root.findall('.//item') or root.findall('.//atom:entry', ns)
    for n in nodes:
        def t(tag):
            el = n.find(tag) if not tag.startswith('atom:') else n.find(tag, ns)
            return el.text.strip() if (el is not None and el.text) else ''
        link = t('link')
        if not link:
            el = n.find('atom:link', ns)
            link = el.get('href') if el is not None else ''
        desc = ''
        for tag in ('description', 'atom:summary', 'content'):
            desc = t(tag)
            if desc:
                break
        # 付费墙检测：content:encoded 带命名空间，必须按 qname 取
        el = n.find('{http://purl.org/rss/1.0/modules/content/}encoded')
        enc = (el.text or '') if el is not None else (t('atom:content') or '')
        paywalled = any(m.lower() in (enc or '').lower() for m in PAYWALL_MARKERS)
        m = re.search(r'[?&]p=(\d+)', t('guid') or link or '')
        items.append({
            'id': m.group(1) if m else hashlib.sha1(((t('title') or '') + (link or '')).encode()).hexdigest()[:12],
            'title': strip_html(t('title')),
            'url': link,
            'published': t('pubDate') or t('atom:updated') or t('updated'),
            'published_hkt': to_hkt(t('pubDate') or t('atom:updated') or t('updated')),
            'summary': WP_TAIL.sub('', strip_html(desc)),
            'author': t('creator') or t('atom:author') or None,
            'paywalled': paywalled,
        })
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--feed', required=True)
    ap.add_argument('--key', required=True)
    ap.add_argument('--label', default='')
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()

    os.makedirs(STATE_DIR, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)

    raw = fetch(a.feed)
    items = parse_feed(raw)
    if not items:
        print("✘ 解析到 0 条——先怀疑工具，不要下「没有内容」的结论")
        sys.exit(2)

    ids = sorted(i['id'] for i in items)
    # 关键：指纹按「条目集合」，不是整条 feed（lastBuildDate 变化会造成假变更）
    fp = 'sha256:' + hashlib.sha256('|'.join(ids).encode()).hexdigest()[:32]

    sp = os.path.join(STATE_DIR, f"{a.key}.json")
    prev = json.load(open(sp, encoding='utf-8')) if os.path.exists(sp) else {}
    seen = set(prev.get('seen_ids', []))
    new_items = [i for i in items if i['id'] not in seen]

    # 轮询守卫：间隔 × 日均产出 ≤ 窗口 1/3
    window = len(items)
    if prev.get('last_checked'):
        hours = (datetime.now(HKT) - datetime.fromisoformat(prev['last_checked'])).total_seconds() / 3600
        per_day = len(new_items) / max(hours / 24, 0.02)
        guard = 'OK' if per_day * (hours / 24) <= window / 3 else '⚠ 轮询过疏，可能漏报'
    else:
        hours, per_day, guard = 0, 0, '首跑（无基线）'

    out = {
        'source': a.key,
        'source_label': a.label or a.key,
        'fetched_at': datetime.now(HKT).isoformat(),
        'feed_url': a.feed,
        'feed_window': window,
        'entries_fingerprint': fp,
        'changed': len(new_items) > 0,
        'new_count': len(new_items),
        'poll_guard': guard,
        'items': new_items,          # 只报新增，退出窗口的正常条目不报
    }
    print(f"feed={a.feed}")
    print(f"  窗口 {window} 条 | 指纹 {fp[:24]}… | 新增 {len(new_items)} | {guard}")
    for i in new_items[:5]:
        print(f"   + [{i['published_hkt'] or '?'}] {i['title'][:62]}"
              f"{'  [付费墙]' if i['paywalled'] else ''}")
    if a.apply:
        json.dump(out, open(os.path.join(OUT_DIR, f"{a.key}.json"), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        allseen = sorted(seen | set(ids))
        json.dump({'seen_ids': allseen[-500:], 'last_checked': datetime.now(HKT).isoformat(),
                   'fingerprint': fp, 'feed_url': a.feed},
                  open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f"  ✔ 已写 {OUT_DIR}/{a.key}.json")


if __name__ == '__main__':
    main()
