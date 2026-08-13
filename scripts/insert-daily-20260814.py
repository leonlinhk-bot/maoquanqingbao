#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-14 catch-up run) into live-items.json + update last-check.json."""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data/live-items.json'
LASTCHECK = ROOT / 'data/last-check.json'
HKT = timezone(timedelta(hours=8))
INGESTED = datetime.now(HKT).isoformat(timespec='seconds')


def item(id_, score, verify, tier, key, title_sc, title_tc, sum_sc, sum_tc,
         why_sc, why_tc, actions, roles, src_sc, lang, boards, themes,
         tags_sc, tags_tc, kind, published, url):
    return {
        "id": id_, "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": key,
        "title": {"sc": title_sc, "tc": title_tc},
        "summary": {"sc": sum_sc, "tc": sum_tc},
        "why": {"sc": why_sc, "tc": why_tc},
        "actions": actions, "rolesImpact": roles,
        "source": {"sc": src_sc, "lang": lang},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags_sc, "tc": tags_tc},
        "contentKind": kind, "publishedAt": published, "originalUrl": url,
        "ingestedAt": INGESTED,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False, "evergreen": False,
    }


def L(sc, tc):
    return {"sc": sc, "tc": tc}


new_items = [
    # 1. XChange TEC x First Cycle (HK AI insurtech) — Aug 13 21:54 in-window
    item(
        "xchange-first-cycle-loi-20260813", 70, "verified", "pro",
        "xchange:first-cycle-loi-20260813",
        "XChange TEC拟收购香港AI公司First Cycle 打造智能体AI保险生态平台",
        "XChange TEC擬收購香港AI公司First Cycle 打造智能體AI保險生態平台",
        "美股上市保险中介及科技平台XChange TEC（纳斯达克：XHG）宣布与香港AI公司First Cycle签署非约束性收购意向书。First Cycle专注智能体AI（agentic AI）技术，可自动完成投保资料收集、核保决策支持与理赔实时路由，缩短理赔周期并降低理赔费用。XChange服务中国内地及香港市场，拟借并购向「AI驱动的保险生态系统平台」转型，加速亚太布局。[EN原文]",
        "美股上市保險中介及科技平台XChange TEC（納斯達克：XHG）宣佈與香港AI公司First Cycle簽署非約束性收購意向書。First Cycle專注智能體AI（agentic AI）技術，可自動完成投保資料收集、核保決策支援與理賠實時路由，縮短理賠週期並降低理賠費用。XChange服務中國內地及香港市場，擬借併購向「AI驅動的保險生態系統平台」轉型，加速亞太佈局。",
        "首家以智能体AI切入香港保险承保理赔流程的并购案，为观察「AI+保险」落地与内地平台出海提供线索，亦折射港险科技生态对外资的吸引力。",
        "首家以智能體AI切入香港保險承保理賠流程的併購案，為觀察「AI+保險」落地與內地平台出海提供線索，亦折射港險科技生態對外資的吸引力。",
        {"front": {}, "midback": L("智能体AI理赔=运营效率参照", "智能體AI理賠=營運效率參照"), "lead": {}, "cross": L("香港保险科技生态=出海桥头堡", "香港保險科技生態=出海橋頭堡")},
        {"front": 1, "midback": 2, "lead": 1, "cross": 2},
        "PRNewswire（AI-Watch转引）", "en",
        ["tech"], ["insurtech", "ai"],
        ["XChange TEC", "First Cycle", "智能体AI", "保险科技", "并购"], ["XChange TEC", "First Cycle", "智能體AI", "保險科技", "併購"],
        "news", "2026-08-13T21:54:00+08:00",
        "https://ai-watch.jp/english/57468/",
    ),
    # 2. S&P: tax may affect HK bank/insurer sales (Aug 13 14:06, missed by last run)
    item(
        "aastocks-sp-tax-sales-20260813", 70, "verified", "pro",
        "aastocks:sp-tax-sales-20260813",
        "标普：内地征税或拖慢港银港险面向内地客户销售 寿险两年仍可增长8%-10%",
        "標普：內地徵稅或拖慢港銀港險面向內地客戶銷售 壽險兩年仍可增長8%-10%",
        "标普全球表示，内地对居民境外保单收益征税或影响香港银行及保险业面向内地客户的销售，消费者投保前会更审慎评估税务影响。但标普预计银行可借财富管理平台多元化与产品组合调整消化手续费收入的短期下滑，寿险商在底层需求具韧性的情况下，未来两年仍可维持8%-10%增长。[EN原文]",
        "標普全球表示，內地對居民境外保單收益徵稅或影響香港銀行及保險業面向內地客戶的銷售，消費者投保前會更審慎評估稅務影響。但標普預計銀行可借財富管理平台多元化與產品組合調整消化手續費收入的短期下滑，壽險商在底層需求具韌性的情況下，未來兩年仍可維持8%-10%增長。",
        "评级机构对征税影响的最新机构视角：短期销售承压但增长预期不变，为评估港险需求韧性与板块估值提供参照。",
        "評級機構對徵稅影響的最新機構視角：短期銷售受壓但增長預期不變，為評估港險需求韌性與板塊估值提供參照。",
        {"front": L("征税影响分层=客户预期管理", "徵稅影響分層=客戶預期管理"), "midback": {}, "lead": L("8-10%增长预期=行业信心锚", "8-10%增長預期=行業信心錨"), "cross": {}},
        {"front": 2, "midback": 1, "lead": 2, "cross": 1},
        "AASTOCKS（标普观点）", "en",
        ["market"], ["taxation", "firm"],
        ["港险征税", "标普", "寿险增长", "银行保险", "内地客户"], ["港險徵稅", "標普", "壽險增長", "銀行保險", "內地客戶"],
        "news", "2026-08-13T14:06:00+08:00",
        "http://freequote.aastocks.com/en/stocks/news/aafn-con/NOW.1538066/latest-news/AAFN",
    ),
    # 3. 险资举牌 trend (Aug 13 17:24, missed by last run)
    item(
        "ce-inscap-stakes-20260813", 64, "verified", "media",
        "ce:inscap-stakes-trend-20260813",
        "险资举牌画风突变：年内仅6次 转向硬科技IPO战略配售与同业互持",
        "險資舉牌畫風突變：年內僅6次 轉向硬科技IPO戰略配售與同業互持",
        "中国保险行业协会数据显示，2026年以来平安人寿、太保寿险、富德产险仅举牌上市公司6次，去年同期逾20次。配置逻辑转向：一是经战略配售、私募股权投资参与宇树科技、长鑫科技等硬科技企业IPO；二是同业增持升温，平安人寿年内三度举牌中国人寿H股、持股升至15%。分析指险资正从「二级市场扫货」转向「一级半+同业互持」的哑铃型配置。",
        "中國保險行業協會數據顯示，2026年以來平安人壽、太保壽險、富德產險僅舉牌上市公司6次，去年同期逾20次。配置邏輯轉向：一是經戰略配售、私募股權投資參與宇樹科技、長鑫科技等硬科技企業IPO；二是同業增持升溫，平安人壽年內三度舉牌中國人壽H股、持股升至15%。分析指險資正從「二級市場掃貨」轉向「一級半+同業互持」的啞鈴型配置。",
        "险资举牌骤减与打法转变，影响内地保险板块资金面与友邦、保诚等港险同业估值叙事，是观察低利率下险资配置的风向标。",
        "險資舉牌驟減與打法轉變，影響內地保險板塊資金面與友邦、保誠等港險同業估值敘事，是觀察低利率下險資配置的風向標。",
        {"front": {}, "midback": {}, "lead": L("险资配置转向=板块资金面提示", "險資配置轉向=板塊資金面提示"), "cross": {}},
        {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "中国经济网（中国银行保险报）", "zh",
        ["market"], ["china", "firm"],
        ["险资举牌", "平安人寿", "中国人寿H股", "硬科技", "同业互持"], ["險資舉牌", "平安人壽", "中國人壽H股", "硬科技", "同業互持"],
        "news", "2026-08-13T17:24:00+08:00",
        "http://finance.ce.cn/insurance1/scrollnews/202608/t20260813_3146705.shtml",
    ),
    # 4. Bamboo Works: tax crackdown erodes edge for HK insurers (Aug 13)
    item(
        "bambooworks-tax-edge-20260813", 62, "pending", "media",
        "bambooworks:tax-edge-20260813",
        "Bamboo Works：内地客2024年贡献港险新单628亿港元 征税常态化才是真正考验",
        "Bamboo Works：內地客2024年貢獻港險新單628億港元 徵稅常態化才是真正考驗",
        "英文财经媒体Bamboo Works分析：内地访客2024年为香港贡献新单保费628亿港元、占新单约29%，2025年香港长期业务新单保费飙增50.6%至3309亿港元。若境外保单征税在内地常态化执行，主打高回报的分红储蓄产品将承压；但多币种、全球配置与财富传承功能仍支撑跨境需求，关键考验是税后回报相对内地产品的优势能否维持。[EN原文]",
        "英文財經媒體Bamboo Works分析：內地訪客2024年為香港貢獻新單保費628億港元、佔新單約29%，2025年香港長期業務新單保費飆增50.6%至3309億港元。若境外保單徵稅在內地常態化執行，主打高回報的分紅儲蓄產品將受壓；但多幣種、全球配置與財富傳承功能仍支撐跨境需求，關鍵考驗是稅後回報相對內地產品的優勢能否維持。",
        "以最新保费数据量化内地访客业务占比，把征税冲击置于「税后回报差」框架下分析，是客户沟通与产品比较的实用参照。",
        "以最新保費數據量化內地訪客業務佔比，把徵稅衝擊置於「稅後回報差」框架下分析，是客戶溝通與產品比較的實用參照。",
        {"front": L("税后回报差=产品沟通框架", "稅後回報差=產品溝通框架"), "midback": {}, "lead": {}, "cross": L("跨境需求韧性=长期配置逻辑", "跨境需求韌性=長期配置邏輯")},
        {"front": 2, "midback": 1, "lead": 1, "cross": 2},
        "Bamboo Works", "en",
        ["market"], ["taxation", "cross-border"],
        ["港险征税", "内地访客", "新单保费", "分红储蓄", "跨境需求"], ["港險徵稅", "內地訪客", "新單保費", "分紅儲蓄", "跨境需求"],
        "news", "2026-08-13T00:00:00+08:00",
        "https://thebambooworks.com/tax-crackdown-erodes-edge-for-hong-kong-insurers/",
    ),
]

# ---- insert into live-items.json ----
data = json.loads(LIVE.read_text(encoding='utf-8'))
existing_keys = {it.get('sourceKey') for it in data['items']}
added = []
for it in new_items:
    if it['sourceKey'] in existing_keys:
        print(f"SKIP duplicate: {it['sourceKey']}")
        continue
    added.append(it)
    existing_keys.add(it['sourceKey'])

data['items'] = added + data['items']
data['meta']['generatedAt'] = INGESTED
data['meta']['itemCount'] = len(data['items'])
data['meta']['windowNote'] = {
    "sc": f"本庫{len(data['items'])}條。",
    "tc": f"本庫{len(data['items'])}條。"
}
LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print(f"Inserted {len(added)} items. Total: {len(data['items'])}")

# ---- update last-check.json (checkpoint mechanism) ----
now = datetime.now(HKT).isoformat(timespec='seconds')
lc = json.loads(LASTCHECK.read_text(encoding='utf-8'))
lc['lastCheck'] = now
for key, src in lc['sources'].items():
    src['last'] = now
LASTCHECK.write_text(json.dumps(lc, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print("last-check.json updated ->", now)
