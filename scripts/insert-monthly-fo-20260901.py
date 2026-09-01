#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每月家办与跨境政策扫描 2026-09-01：插入 3 条新条目 + 回写 last-check / collect-progress。"""
import json, datetime

TZ = datetime.timezone(datetime.timedelta(hours=8))
now_iso = datetime.datetime.now(TZ).strftime("%Y-%m-%dT%H:%M:%S+08:00")

NEW_ITEMS = [
    {
        "id": "hk-sg-fo-competition-20260826",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "verified",
        "sourceTier": "pro",
        "sourceKey": "wallstreetclub",
        "title": {
            "sc": "新港家办竞争2026：香港扩免税抢人才 vs 新加坡收紧13O/13U审查",
            "tc": "新港家辦競爭2026：香港擴免稅搶人才 vs 新加坡收緊13O/13U審查"
        },
        "summary": {
            "sc": "香港《2026年税务（修订）条例草案》放宽基金及附带权益优惠，叠加活跃IPO与雄厚资金池，巩固全球最大跨境财富中心地位；新加坡则推业绩回报免税、升级精英签证并收紧家办实质运营审查。分析指亚太财富管理趋向「双中心」分工：香港锚定大中华资本与交易执行，新加坡侧重量化与算力研发。",
            "tc": "香港《2026年稅務（修訂）條例草案》放寬基金及附帶權益優惠，疊加活躍IPO與雄厚資金池，鞏固全球最大跨境財富中心地位；新加坡則推業績回報免稅、升級精英簽證並收緊家辦實質運營審查。分析指亞太財富管理趨向「雙中心」分工：香港錨定大中華資本與交易執行，新加坡側重量化與算力研發。"
        },
        "why": {
            "sc": "港险高净值客群的家办架构选址直接受两地政策差异驱动；香港「宽进」与新加坡「严管」的分化，为跨境财富架构与身份规划提供清晰对标坐标。",
            "tc": "港險高淨值客群的家辦架構選址直接受兩地政策差異驅動；香港「寬進」與新加坡「嚴管」的分化，為跨境財富架構與身份規劃提供清晰對標坐標。"
        },
        "actions": {
            "front": {"sc": "两地政策对比可作高净值客户话术素材", "tc": "兩地政策對比可作高淨值客戶話術素材"},
            "midback": {},
            "lead": {"sc": "家办架构选址的长期判断依据", "tc": "家辦架構選址的長期判斷依據"},
            "cross": {"sc": "跨境财富/身份规划客户重点跟进", "tc": "跨境財富/身份規劃客戶重點跟進"}
        },
        "rolesImpact": {"front": 1, "midback": 0, "lead": 2, "cross": 2},
        "source": {"sc": "华尔街俱乐部（新浪财经）", "lang": "zh"},
        "boards": ["family", "market"],
        "themes": ["family-office", "benchmark", "offshore"],
        "tags": {
            "sc": ["新加坡", "家办竞争", "13O/13U", "跨境财富"],
            "tc": ["新加坡", "家辦競爭", "13O/13U", "跨境財富"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-26T23:46:00+08:00",
        "originalUrl": "https://www.sina.cn/news/detail/5336311277817093.html"
    },
    {
        "id": "fstb-carried-interest-clarify-20260812",
        "clusterCount": 1,
        "score": 86,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "fstb",
        "title": {
            "sc": "财库局澄清：自营交易业务酬金不符附带权益免税资格 基金/家控工具税改边界厘清",
            "tc": "財庫局澄清：自營交易業務酬金不符附帶權益免稅資格 基金/家控工具稅改邊界釐清"
        },
        "summary": {
            "sc": "财库局8月12日就《2026年税务（修订）（基金、家控工具及附带权益优惠税制）条例草案》澄清：自营交易业务不符「基金」定义（参与者须对管理无日常控制），其分发酬金不符免税资格；基金经理雇员报酬是否属具资格附带权益须视实质是否属投资管理服务。草案扩大附带权益适用范围至私募股权以外。",
            "tc": "財庫局8月12日就《2026年稅務（修訂）（基金、家控工具及附帶權益優惠稅制）條例草案》澄清：自營交易業務不符「基金」定義（參與者須對管理無日常控制），其分發酬金不符免稅資格；基金經理僱員報酬是否屬具資格附帶權益須視實質是否屬投資管理服務。草案擴大附帶權益適用範圍至私募股權以外。"
        },
        "why": {
            "sc": "界定附带权益优惠税制边界，直接影响基金与家办高管的绩效报酬税务规划；区分「基金投资管理」与「自营交易」，是跨境家办与对冲基金架构落地前的关键合规红线。",
            "tc": "界定附帶權益優惠稅制邊界，直接影響基金與家辦高管的績效報酬稅務規劃；區分「基金投資管理」與「自營交易」，是跨境家辦與對沖基金架構落地前的關鍵合規紅線。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "税务合规红线自查", "tc": "稅務合規紅線自查"},
            "lead": {"sc": "基金/家办绩效报酬税务规划", "tc": "基金/家辦績效報酬稅務規劃"},
            "cross": {"sc": "跨境家办架构落地前合规确认", "tc": "跨境家辦架構落地前合規確認"}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 2, "cross": 2},
        "source": {"sc": "财经事务及库务局（政府新闻网）", "lang": "zh"},
        "boards": ["reg", "family"],
        "themes": ["taxation", "family-office", "fund"],
        "tags": {
            "sc": ["附带权益", "税务优惠", "家控工具"],
            "tc": ["附帶權益", "稅務優惠", "家控工具"]
        },
        "contentKind": "press",
        "publishedAt": "2026-08-12T19:58:00+08:00",
        "originalUrl": "https://www.news.gov.hk/chi/2026/08/20260812/20260812_171802_940.html"
    },
    {
        "id": "fstb-malaysia-fo-roadshow-20260722",
        "clusterCount": 1,
        "score": 68,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "zhitong",
        "title": {
            "sc": "许正宇出访马来西亚招揽家办：会见双威/成功集团 出席香港信托协会跨境论坛",
            "tc": "許正宇出訪馬來西亞招攬家辦：會見雙威/成功集團 出席香港信託協會跨境論壇"
        },
        "summary": {
            "sc": "财库局局长许正宇7月出访马来西亚，会晤双威集团、成功集团、皇家雪兰莪、RHL Ventures等家办与投资机构，介绍香港家办生态（单一家办两年增逾25%）；并出席香港信托协会吉隆坡「环球家族办公室新时代」论坛。许正宇指香港已提交立法建议，将优惠税制扩至私募债权及贵金属。",
            "tc": "財庫局局長許正宇7月出訪馬來西亞，會晤雙威集團、成功集團、皇家雪蘭莪、RHL Ventures等家辦與投資機構，介紹香港家辦生態（單一家辦兩年增逾25%）；並出席香港信託協會吉隆坡「環球家族辦公室新時代」論壇。許正宇指香港已提交立法建議，將優惠稅制擴至私募債權及貴金屬。"
        },
        "why": {
            "sc": "港府主动南下东盟揽才，印证香港与新加坡对区域家族资本的竞争白热化；「优惠税制扩至私募债权/贵金属」为家办资产配置与跨境信托结构提供新空间。",
            "tc": "港府主動南下東盟攬才，印證香港與新加坡對區域家族資本的競爭白熱化；「優惠稅制擴至私募債權/貴金屬」為家辦資產配置與跨境信託結構提供新空間。"
        },
        "actions": {
            "front": {"sc": "东盟高净值客源线索", "tc": "東盟高淨值客源線索"},
            "midback": {},
            "lead": {"sc": "香港家办区域拓展动向", "tc": "香港家辦區域拓展動向"},
            "cross": {"sc": "跨境信托架构客户可关注优惠税制扩围", "tc": "跨境信託架構客戶可關注優惠稅制擴圍"}
        },
        "rolesImpact": {"front": 1, "midback": 0, "lead": 1, "cross": 1},
        "source": {"sc": "智通财经（财库局局长出访）", "lang": "zh"},
        "boards": ["family"],
        "themes": ["family-office", "offshore", "fo-ecosystem"],
        "tags": {
            "sc": ["许正宇", "马来西亚", "家办", "跨境信托"],
            "tc": ["許正宇", "馬來西亞", "家辦", "跨境信託"]
        },
        "contentKind": "news",
        "publishedAt": "2026-07-22T21:19:00+08:00",
        "originalUrl": "http://m.toutiao.com/group/7665341175590699530/?upstream_biz=VolcEngine"
    }
]

# --- 1. live-items.json ---
path = "data/live-items.json"
data = json.load(open(path, encoding="utf-8"))
existing_ids = {it["id"] for it in data["items"]}
added = []
for it in NEW_ITEMS:
    if it["id"] in existing_ids:
        print("SKIP (dup id):", it["id"])
        continue
    data["items"].insert(0, it)
    added.append(it["id"])

data["meta"]["itemCount"] = len(data["items"])
data["meta"]["generatedAt"] = now_iso
data["meta"]["windowNote"] = {
    "sc": f"本库{len(data['items'])}条。",
    "tc": f"本庫{len(data['items'])}條。"
}
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"INSERTED {len(added)} items; total now {len(data['items'])}")
for a in added:
    print(" +", a)

# --- 2. last-check.json (仅更新 family_office 信源检查时间) ---
lc_path = "data/last-check.json"
lc = json.load(open(lc_path, encoding="utf-8"))
lc["sources"]["family_office"]["last"] = now_iso
json.dump(lc, open(lc_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"last-check.json family_office.last -> {now_iso}")

# --- 3. collect-progress.json (月度扫描进度) ---
cp_path = "data/collect-progress.json"
try:
    cp = json.load(open(cp_path, encoding="utf-8"))
except Exception:
    cp = {}
cp["lastMonth"] = "2026-08"
cp["done"] = cp.get("done", []) + added
json.dump(cp, open(cp_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"collect-progress.json lastMonth -> {cp['lastMonth']}, done={len(cp['done'])}")
