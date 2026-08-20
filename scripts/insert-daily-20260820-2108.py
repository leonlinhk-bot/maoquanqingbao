#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-20 evening run) into live-items.json + update last-check.json.

Window: after lastCheck 2026-08-20T03:54:46+08:00 (early run) -> now (~21:08).
web_extract/web_search (Firecrawl) unconfigured this run -> doubao_search fallback per skill.
Items (all cross-checked, verified against 2+ sources):
  1. IA circular on premium-financing insurance (issue date 20 Aug 2026; PF = ~36% of new business
     premiums in H1 2026 vs 21% LY; joint IA-HKMA thematic inspection started) [official, verified]
  2. AIA 2026 interim results (announced 20 Aug 09:00 HKT; VONB US$3,212m +10% CER; HK VONB US$1,168m
     +10% with NBM 72.0%; interim DPS 53.90 HK cents +10%) [insurer, verified]
  3. AIA results market reaction: Bloomberg/The Edge (CFO: MCV demand strong; tax rules unchanged),
     Citi largely-in-line/Buy, Goldman slightly below est. [media, pending]
  4. HKMA press release 20 Aug: fake "digital HKD" document scam alert [official, verified]
Skipped as out-of-window/dup: Manulife Q2 (5 Aug), Prudential Taikoo HQ (19 Aug, in library),
险资ETF互联互通 (18 Aug, in library), 偿付能力5家不达标 (in library), 富卫入股隽天 (19 Aug, in library),
Deloitte家办调查 (Feb, in library).
"""
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
    # 1. IA premium-financing circular (official, verified)
    item(
        "ia-premium-financing-circular-20260820", 90, "verified", "official",
        "ia_circular",
        "保监局发通函：保费融资上半年占新造业务保费约36% 要求险企检讨产品与风控",
        "保監局發通函：保費融資上半年佔新造業務保費約36% 要求險企檢討產品與風控",
        "保监局8月20日发保费融资通函：上半年保费融资占新造业务保费约36%（去年同期21%），部分险企新单主要依赖该业务；要求检讨产品设计、定价、销售及风控，并联合金管局启动新一轮主题查察；检视发现个别销售材料暗示10%保费可达9倍杠杆等不当宣传。",
        "保監局8月20日發保費融資通函：上半年保費融資佔新造業務保費約36%（去年同期21%），部分險企新單主要依賴該業務；要求檢討產品設計、定價、銷售及風控，並聯合金管局啟動新一輪主題查察；檢視發現個別銷售材料暗示10%保費可達9倍槓桿等不當宣傳。",
        "保费融资占新单比例半年间由21%飙至36%，监管通函+主题查察双管齐下，直接划定杠杆营销红线；做高净值储蓄险与大额保单的渠道须重审融资方案合规话术，是本周最重要的监管信号。",
        "保費融資佔新單比例半年間由21%飆至36%，監管通函+主題查察雙管齊下，直接劃定槓桿營銷紅線；做高淨值儲蓄險與大額保單的渠道須重審融資方案合規話術，是本週最重要的監管信號。",
        {"front": {}, "midback": {}, "lead": L("保费融资合规话术自查", "保費融資合規話術自查"),
         "cross": L("保费融资监管动态跟踪", "保費融資監管動態跟蹤")},
        {"front": 0, "midback": 0, "lead": 2, "cross": 1},
        "香港保监局通函（经金管局BRDR发布）", "zh+en",
        ["reg"], ["premium-financing", "compliance"],
        ["保费融资", "通函", "保监局", "主题查察", "杠杆风险"], ["保費融資", "通函", "保監局", "主題查察", "槓桿風險"],
        "circular", "2026-08-20",
        "https://brdr.hkma.gov.hk/eng/doc-ldg/current/20260818-1-EN",
    ),
    # 2. AIA 2026 interim results (insurer, verified)
    item(
        "aia-h1-2026-results-20260820", 88, "verified", "insurer",
        "aia",
        "友邦中期业绩：新业务价值32.12亿美元增10% 香港利润率升至72% 中期息增10%",
        "友邦中期業績：新業務價值32.12億美元增10% 香港利潤率升至72% 中期息增10%",
        "友邦8月20日公布2026年中期业绩：新业务价值32.12亿美元（+10%，撇除泰国+14%）；香港VONB 11.68亿美元（+10%）、新业务价值利润率由65.8%升至72.0%；内地VONB 9.37亿美元（+20%）；税后营运溢利41.63亿美元、每股+13%，中期股息每股53.90港仙（+10%），料超额完成2023-26年每股OPAT增长目标。",
        "友邦8月20日公佈2026年中期業績：新業務價值32.12億美元（+10%，撇除泰國+14%）；香港VONB 11.68億美元（+10%）、新業務價值利潤率由65.8%升至72.0%；內地VONB 9.37億美元（+20%）；稅後營運溢利41.63億美元、每股+13%，中期股息每股53.90港仙（+10%），料超額完成2023-26年每股OPAT增長目標。",
        "港险龙头中报落地：香港继续为最大新业务市场且利润率显著走高，内地访客与本地客约各占一半、需求保持旺盛；业绩数据与管理层对内地征税的回应，是渠道校准全年谈单叙事的第一手基准。",
        "港險龍頭中報落地：香港繼續為最大新業務市場且利潤率顯著走高，內地訪客與本地客約各佔一半、需求保持旺盛；業績數據與管理層對內地徵稅的回應，是渠道校準全年談單敘事的第一手基準。",
        {"front": {}, "midback": {}, "lead": L("友邦中报要点与渠道话术", "友邦中報要點與渠道話術"),
         "cross": L("港险中报季同业对照", "港險中報季同業對照")},
        {"front": 0, "midback": 0, "lead": 2, "cross": 1},
        "友邦保险（HKEX业绩公告）", "zh+en",
        ["insurer"], ["results", "market"],
        ["友邦保险", "中期业绩", "新业务价值", "香港市场", "内地访客"], ["友邦保險", "中期業績", "新業務價值", "香港市場", "內地訪客"],
        "press", "2026-08-20T09:00:00+08:00",
        "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0820/2026082000001.pdf",
    ),
    # 3. AIA results market reaction (media, pending)
    item(
        "aia-h1-results-market-reaction-20260820", 65, "pending", "media",
        "theedge",
        "彭博/花旗点评友邦中报：内地访客需求旺盛 股价跌约1.8% 花旗维持买入 [EN原文]",
        "彭博/花旗點評友邦中報：內地訪客需求旺盛 股價跌約1.8% 花旗維持買入 [EN原文]",
        "彭博引述友邦CFO指内地访客需求依然旺盛，内地税法并无改变、客户来港投保并非主要为税务原因；业绩后花旗指中报大致符合预期、维持买入，高盛指略低于预期主因二季度香港贡献偏软；友邦当日股价收跌约1.8%，VONB 32.1亿美元略低于彭博汇总的32.6亿美元预期中值。[EN原文]",
        "彭博引述友邦CFO指內地訪客需求依然旺盛，內地稅法並無改變、客戶來港投保並非主要為稅務原因；業績後花旗指中報大致符合預期、維持買入，高盛指略低於預期主因二季度香港貢獻偏軟；友邦當日股價收跌約1.8%，VONB 32.1億美元略低於彭博匯總的32.6億美元預期中值。[EN原文]",
        "市场如何解读港险龙头中报、征税传闻下内地访客需求成焦点——股价与大行评级的即时反应，是判断渠道端谈单信心的温度计。",
        "市場如何解讀港險龍頭中報、徵稅傳聞下內地訪客需求成焦點——股價與大行評級的即時反應，是判斷渠道端談單信心的溫度計。",
        {"front": {}, "midback": {}, "lead": L("中报后市场口径跟进", "中報後市場口徑跟進"),
         "cross": L("内地征税影响跟踪", "內地徵稅影響跟蹤")},
        {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "The Edge Singapore（引述彭博）", "en",
        ["market"], ["results", "market"],
        ["友邦保险", "中报点评", "内地访客", "花旗", "高盛"], ["友邦保險", "中報點評", "內地訪客", "花旗", "高盛"],
        "news", "2026-08-20T13:05:00+08:00",
        "https://www.theedgesingapore.com/news/insurance/aia-posts-growth-new-business-value-hong-kong-china",
    ),
    # 4. HKMA fake-document scam alert (official, verified)
    item(
        "hkma-fake-doc-scam-alert-20260820", 85, "verified", "official",
        "hkma_press",
        "金管局提醒：提防伪冒金管局文件 假借「数码港元」诱骗投资",
        "金管局提醒：提防偽冒金管局文件 假借「數碼港元」誘騙投資",
        "金管局8月20日发新闻稿：有骗徒假借「数码港元」名义冒认金管局发出「外汇基金票竞标」文件，声称透过虚假应用程式参与竞标可获「数码港元」收益并提现；金管局澄清文件与投资全属伪造、已报警，并重申数码港元先导计划及沙盒参与机构不会以相关计划名义向公众集资或提供投资产品。",
        "金管局8月20日發新聞稿：有騙徒假借「數碼港元」名義冒認金管局發出「外匯基金票競標」文件，聲稱透過虛假應用程式參與競標可獲「數碼港元」收益並提現；金管局澄清文件與投資全屬偽造、已報警，並重申數碼港元先導計劃及沙盒參與機構不會以相關計劃名義向公眾集資或提供投資產品。",
        "高净值客户是骗徒重点目标，「数码港元」题材新骗局提醒渠道在客户教育中同步传递官方防骗口径；金管局官方澄清可作一线谈单时的可信背书。",
        "高淨值客戶是騙徒重點目標，「數碼港元」題材新騙局提醒渠道在客戶教育中同步傳遞官方防騙口徑；金管局官方澄清可作一線談單時的可信背書。",
        {"front": {}, "midback": {}, "lead": L("客户防骗提示素材", "客戶防騙提示素材"),
         "cross": L("数码港元进展跟踪", "數碼港元進展跟蹤")},
        {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "香港金管局新闻稿", "zh",
        ["reg"], ["compliance", "market"],
        ["金管局", "防骗", "数码港元", "外汇基金票", "诈骗警示"], ["金管局", "防騙", "數碼港元", "外匯基金票", "詐騙警示"],
        "press", "2026-08-20",
        "https://www.hkma.gov.hk/gb_chi/news-and-media/press-releases/2026/08/20260820-3/",
    ),
]


def main():
    data = json.loads(LIVE.read_text(encoding='utf-8'))
    items = data['items']

    existing_ids = {i['id'] for i in items}
    existing_urls = {i.get('originalUrl', '') for i in items}
    added = []
    for it in new_items:
        if it['id'] in existing_ids or it['originalUrl'] in existing_urls:
            print(f"SKIP duplicate: {it['id']}")
            continue
        added.append(it)

    if not added:
        print("Nothing to add.")
        return

    items[0:0] = added
    data['items'] = items
    data['meta']['itemCount'] = len(items)
    data['meta']['generatedAt'] = INGESTED
    data['meta']['windowNote'] = {
        "sc": f"本库{len(items)}条。",
        "tc": f"本庫{len(items)}條。"
    }
    LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f"ADDED {len(added)} items -> live-items.json (total {len(items)})")
    for it in added:
        print(f"  + {it['id']} | {it['title']['sc']}")

    # update last-check.json
    lc = json.loads(LASTCHECK.read_text(encoding='utf-8'))
    lc['lastCheck'] = INGESTED
    for k in lc.get('sources', {}):
        lc['sources'][k]['last'] = INGESTED
    LASTCHECK.write_text(json.dumps(lc, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"last-check.json updated: lastCheck={INGESTED}")


if __name__ == '__main__':
    main()
