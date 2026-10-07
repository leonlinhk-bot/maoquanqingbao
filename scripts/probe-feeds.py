#!/usr/bin/env python3
"""
六步探测法（robots → sitemap → RSS/Atom → 分页）批量探测器。

用途：① 对库内已有源做「结构化出口普查」（把硬爬改成订阅）
      ② 对候选新源做接入前探测

用法:
  python3 scripts/probe-feeds.py --domains a.com,b.com        # 指定域名
  python3 scripts/probe-feeds.py --from-library 30            # 库内 Top N 域名
  python3 scripts/probe-feeds.py --out report.json
"""
import json, re, sys, time, argparse, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/122.0 Safari/537.36')
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))

FEED_PATHS = ['/feed/', '/rss/', '/feed', '/rss', '/index.xml', '/atom.xml', '/feed.xml', '/rss.xml']
SITEMAP_PATHS = ['/sitemap.xml', '/sitemap_index.xml', '/wp-sitemap.xml']


def get(url, timeout=22):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
    try:
        with OPENER.open(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', 'ignore')
    except urllib.error.HTTPError as e:
        return e.code, ''
    except Exception:
        return -1, ''


def probe(domain):
    out = {'domain': domain, 'robots': None, 'robots_allow_all': None,
           'sitemaps': [], 'feeds': [], 'ok': False}
    base = f"https://{domain}"

    st, body = get(base + '/robots.txt')
    out['robots'] = st
    if st == 200:
        out['sitemaps'] += re.findall(r'(?im)^\s*sitemap:\s*(\S+)', body)
        dis = [x.strip() for x in re.findall(r'(?im)^\s*disallow:\s*(.*)$', body) if x.strip()]
        out['robots_allow_all'] = (len(dis) == 0)

    for p in SITEMAP_PATHS:
        if any(p in s for s in out['sitemaps']):
            continue
        st, body = get(base + p)
        if st == 200 and '<' in body:
            out['sitemaps'].append(base + p)
            break

    for p in FEED_PATHS:
        st, body = get(base + p)
        head = body[:800].lower()
        if st == 200 and ('<rss' in head or '<feed' in head or '<rdf' in head):
            n = len(re.findall(r'<item[\s>]|<entry[\s>]', body))
            dates = re.findall(r'<(?:pubDate|updated|published)>(.*?)</', body)
            out['feeds'].append({'url': base + p, 'items': n, 'size': len(body),
                                 'newest': dates[0][:31] if dates else None})
            if len(out['feeds']) >= 2:
                break

    out['ok'] = bool(out['feeds']) or bool(out['sitemaps'])
    return out


def library_domains(n):
    d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
    cnt = {}
    for i in d['items']:
        m = re.match(r'https?://(?:www\.)?([^/]+)', i.get('originalUrl') or '')
        if m:
            cnt[m.group(1).lower()] = cnt.get(m.group(1).lower(), 0) + 1
    return [k for k, _ in sorted(cnt.items(), key=lambda kv: -kv[1])[:n]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--domains', default='')
    ap.add_argument('--from-library', type=int, default=0)
    ap.add_argument('--out', default='')
    a = ap.parse_args()

    domains = [x.strip() for x in a.domains.split(',') if x.strip()]
    if a.from_library:
        domains += library_domains(a.from_library)
    domains = list(dict.fromkeys(domains))
    print(f"探测 {len(domains)} 个域名...\n")

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=4) as ex:
        results = list(ex.map(probe, domains))
    print(f"耗时 {time.time()-t0:.0f}s\n")

    feeds_ok, sm_ok, none_ok = [], [], []
    for r in results:
        if r['feeds']:
            feeds_ok.append(r)
            f = r['feeds'][0]
            print(f"✔ FEED  {r['domain']:34s} {f['url'][:52]:54s} {f['items']}条 {f['size']//1024}KB")
        elif r['sitemaps']:
            sm_ok.append(r)
            print(f"◐ 仅SITEMAP {r['domain']:30s} {r['sitemaps'][0][:56]}")
        else:
            none_ok.append(r)
            print(f"✘ 无出口  {r['domain']:34s} robots={r['robots']}")

    print(f"\n汇总：FEED {len(feeds_ok)} | 仅sitemap {len(sm_ok)} | 无 {len(none_ok)}")
    if a.out:
        json.dump(results, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print("写入", a.out)


if __name__ == '__main__':
    main()
