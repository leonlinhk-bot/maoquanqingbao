#!/usr/bin/env python3
# 猫圈儿使用度周报生成器
# 拉取 Worker 聚合的微观行为数据（7/14/30 天），生成 markdown 周报
# 用法：python3 scripts/usage-weekly-report.py [days=7] [--out FILE]
import json, sys, urllib.request, datetime, os
from pathlib import Path

EP = "https://stats.hkmaoquanqingbao.com"
def get(path):
    # 绕过系统代理（本机代理会拦 stats 域名的 urllib 请求；curl --noproxy 正常）
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    req = urllib.request.Request(EP + path, headers={
        "Accept":"application/json",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    })
    # 重试 5 次（KV 最终一致，读取可能滞后 ~60s）
    import time
    for attempt in range(5):
        try:
            with opener.open(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code not in (500, 502, 503):
                raise
            time.sleep(20)  # KV 同步窗口
    raise RuntimeError("Worker 连续重试失败")

def bar(n, maxn, width=14):
    if maxn <= 0: return ""
    w = int(round(n/maxn*width))
    return "█"*w + "░"*(width-w)

def main():
    days = int(sys.argv[1]) if len(sys.argv)>1 and sys.argv[1].isdigit() else 7
    out = None
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out")+1]
    try:
        stats = get(f"/stats?days={days}")
        hot = get(f"/hot?n=15&days={days}")
    except Exception as e:
        print(f"ERROR: Worker 拉取失败: {e}")
        sys.exit(1)

    now = datetime.datetime.now()
    d0 = (now - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    d1 = now.strftime("%Y-%m-%d")
    L = []
    L.append(f"# 猫圈儿使用度周报（{d0} ~ {d1}）")
    L.append(f"> 数据源：使用度 Worker（微观行为）· 生成 {now.strftime('%Y-%m-%d %H:%M')}")
    L.append("")

    # 1. 总览
    daily = sorted(stats.get("daily") or [], key=lambda x: x["date"])
    tot_ev = sum(d.get("events",0) for d in daily)
    tot_fav = stats.get("favs",0); tot_exp = stats.get("exports",0)
    L.append("## 一、本周总览")
    L.append(f"- 行为事件总数：**{tot_ev}**（近 {days} 天）")
    L.append(f"- 收藏 **{tot_fav}** 次 · 导出 MD **{tot_exp}** 次")
    L.append("")
    L.append("| 日期 | 事件数 |")
    L.append("|------|-------|")
    for d in daily:
        L.append(f"| {d['date']} | {d['events']} |")
    L.append("")

    # 2. 大家都在搜（真实热搜）
    L.append("## 二、大家都在搜（全站热搜 TOP 15）")
    items = hot.get("items") or []
    if items:
        maxc = max(x.get("count",1) for x in items)
        L.append("| # | 搜索词 | 次数 | 热度 |")
        L.append("|---|--------|------|------|")
        for i,x in enumerate(items,1):
            L.append(f"| {i} | {x.get('term','')} | {x.get('count',0)} | {bar(x.get('count',0),maxc)} |")
    else:
        L.append("（暂无搜索数据——搜索词满 2 字才记录，拼音中间态已过滤）")
    L.append("")

    # 3. 角色分布
    roles = stats.get("roles") or {}
    role_names = {"front":"前线 IFA","midback":"中后台合规","lead":"团队管理","cross":"跨境架构"}
    L.append("## 三、角色使用分布")
    if roles:
        L.append("| 角色 | 行为数 | 占比 |")
        L.append("|------|-------|------|")
        tot = sum(roles.values())
        for k in ["front","midback","lead","cross"]:
            v = roles.get(k,0)
            if v:
                pct = v/tot*100
                L.append(f"| {role_names.get(k,k)} | {v} | {pct:.0f}% |")
    else:
        L.append("（暂无角色数据——用户切换角色时记录）")
    L.append("")

    # 4. 视图偏好
    views = stats.get("views") or {}
    view_names = {"pulse":"今日脉搏","all":"全部动态","themes":"主题雷达","board":"情报看板","archive":"档案","fav":"我的收藏","download":"数据下载","agent":"Agent接入","deep":"监管深度"}
    L.append("## 四、页面/视图偏好")
    if views:
        L.append("| 视图 | 次数 | 热度 |")
        L.append("|------|------|------|")
        vsorted = sorted(views.items(), key=lambda x:-x[1])[:8]
        maxv = max(v for _,v in vsorted) if vsorted else 1
        for k,v in vsorted:
            L.append(f"| {view_names.get(k,k)} | {v} | {bar(v,maxv)} |")
    else:
        L.append("（暂无视图数据）")
    L.append("")

    # 5. 海报
    posters = stats.get("posters") or {}
    L.append("## 五、海报下载")
    if posters:
        L.append(f"- 深色版式 {posters.get('dark',0)} 次 · 浅色版式 {posters.get('light',0)} 次")
    else:
        L.append("（暂无海报下载）")
    L.append("")

    # 6. 最热条目
    L.append("## 六、最受关注条目（打开次数 TOP）")
    L.append("（需要单条打开明细，可在 Worker /stats 扩展；当前已按主题聚合）")
    L.append("")
    L.append("---")
    L.append("*宏观流量（PV/UV/来源/设备）见 Cloudflare 面板：dash.cloudflare.com → Analytics → Web Analytics*")

    report = "\n".join(L)
    if out:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(report, encoding="utf-8")
        print(f"已写入: {out}")
    print(report)

if __name__ == "__main__":
    main()
