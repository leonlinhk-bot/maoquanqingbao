#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-14 18:08 run) into live-items.json + update last-check.json."""
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
    # 1. IA CEO Clement Cheung reappointment (official gov.hk press release, verified)
    item(
        "govhk-ia-ceo-reappointment-20260814", 86, "verified", "official",
        "govhk",
        "香港政府再度委任张云正为保监局行政总监 任期延至2029年8月",
        "香港政府再度委任張雲正為保監局行政總監 任期延至2029年8月",
        "政府8月14日宣布，行政长官根据《保险业条例》批准再度委任张云正为保监局行政总监，任期三年（2026年8月15日至2029年8月14日）。张氏2018年首度出任，任内推进风险为本资本制度及检讨、强化保险相连证券市场、提升专属自保业务竞争力。财库局局长许正宇表示，相信他会继续加强审慎监管、保障保单持有人利益。",
        "政府8月14日宣佈，行政長官根據《保險業條例》批准再度委任張雲正為保監局行政總監，任期三年（2026年8月15日至2029年8月14日）。張氏2018年首度出任，任內推進風險為本資本制度及檢討、強化保險相連證券市場、提升專屬自保業務競爭力。財庫局局長許正宇表示，相信他會繼續加強審慎監管、保障保單持有人利益。",
        "IA行政总监人事确定，标志监管政策方向延续，亦为观察香港风险为本资本检讨、ILS及自保市场后续动作提供锚点，属监管层一手信号。",
        "IA行政總監人事確定，標誌監管政策方向延續，亦為觀察香港風險為本資本檢討、ILS及自保市場後續動作提供錨點，屬監管層一手信號。",
        {"front": {}, "midback": L("监管层人事稳定=政策延续信号", "監管層人事穩定=政策延續信號"), "lead": {}, "cross": L("国际风险管理中心定位再确认", "國際風險管理中心定位再確認")},
        {"front": 0, "midback": 2, "lead": 2, "cross": 2},
        "香港政府新闻公报（info.gov.hk）", "zh",
        ["reg"], ["reg", "career"],
        ["保监局", "张云正", "行政总监", "委任", "风险为本资本"], ["保監局", "張雲正", "行政總監", "委任", "風險為本資本"],
        "press", "2026-08-14T16:00:00+08:00",
        "https://www.info.gov.hk/gia/general/202608/14/P2026081400295.htm",
    ),
    # 2. AM Best: global reinsurers beat cost of capital 3rd straight year
    item(
        "insuranceasia-ambest-reinsurers-capital-20260814", 74, "verified", "pro",
        "insuranceasia",
        "AM Best：全球再保险业连续第三年跑赢资本成本 2025年中位股本回报16.3%",
        "AM Best：全球再保險業連續第三年跑贏資本成本 2025年中位股本回報16.3%",
        "AM Best报告显示，2025年全球再保险公司中位股本回报率达16.3%，连续第三年高于资本成本，主因再定价及组合去风险带动承保表现。但行业加权平均资本成本由2024年7.67%升至8.23%，2026年首季再升至8.63%；市场转软加快，分析师指更严条款与更高起赔点仍支撑业绩。[EN原文]",
        "AM Best報告顯示，2025年全球再保險公司中位股本回報率達16.3%，連續第三年高於資本成本，主因再定價及組合去風險帶動承保表現。但行業加權平均資本成本由2024年7.67%升至8.23%，2026年首季再升至8.63%；市場轉軟加快，分析師指更嚴條款與更高起賠點仍支撐業績。[EN原文]",
        "再保险行业回报与资本成本走势直接牵动香港市场分出价格与承保能力，是观察再保定价周期拐点的量化参考。",
        "再保險行業回報與資本成本走勢直接牽動香港市場分出價格與承保能力，是觀察再保定價週期拐點的量化參考。",
        {"front": {}, "midback": L("再保成本线=分出定价参考", "再保成本線=分出定價參考"), "lead": {}, "cross": L("资本充足=巨灾承保能力信号", "資本充足=巨災承保能力信號")},
        {"front": 0, "midback": 2, "lead": 1, "cross": 2},
        "Insurance Asia（转引AM Best报告）", "en",
        ["market"], ["reinsurance", "capital", "results"],
        ["AM Best", "再保险", "股本回报", "资本成本", "市场转软"], ["AM Best", "再保險", "股本回報", "資本成本", "市場轉軟"],
        "news", "2026-08-14T05:30:00+08:00",
        "https://insuranceasia.com/insurance/news/global-reinsurers-beat-capital-costs-third-straight-year",
    ),
    # 3. R&W / W&I deal insurance demand rises
    item(
        "insuranceasia-deal-insurance-rw-20260814", 71, "verified", "pro",
        "insuranceasia",
        "并购保障需求升温：58%受访者预期2026年陈述与保证保险使用增加",
        "併購保障需求升溫：58%受訪者預期2026年陳述與保證保險使用增加",
        "诺顿罗氏富布莱特与Mergermarket联合调查显示，58%受访者预期2026年并购交易的陈述与保证保险（R&W/W&I）使用量将上升，其中32%预计显著增加；52%预期全球并购活动增长，AI相关标的成最大吸引力（78%提及）。私募信贷料继续成为并购融资关键来源，估值差距仍是撮合交易首要障碍。[EN原文]",
        "諾頓羅氏富萊特與Mergermarket聯合調查顯示，58%受訪者預期2026年併購交易的陳述與保證保險（R&W/W&I）使用量將上升，其中32%預計顯著增加；52%預期全球併購活動增長，AI相關標的成最大吸引力（78%提及）。私募信貸料繼續成為併購融資關鍵來源，估值差距仍是撮合交易首要障礙。[EN原文]",
        "R&W保险需求被视为并购活跃度的领先指标，其增长趋势反映企业并购风险对冲意识提升，与专业责任险市场走向相关。",
        "R&W保險需求被視為併購活躍度的領先指標，其增長趨勢反映企業併購風險對沖意識提升，與專業責任險市場走向相關。",
        {"front": {}, "midback": {}, "lead": {}, "cross": L("R&W保险=并购交易风险抓手", "R&W保險=併購交易風險抓手")},
        {"front": 1, "midback": 1, "lead": 1, "cross": 2},
        "Insurance Asia（转引诺顿罗氏/Mergermarket调查）", "en",
        ["market"], ["market", "product"],
        ["陈述与保证保险", "R&W", "并购", "Mergermarket", "私募信贷"], ["陳述與保證保險", "R&W", "併購", "Mergermarket", "私募信貸"],
        "news", "2026-08-14T05:15:00+08:00",
        "https://insuranceasia.com/insurance/news/deal-insurance-demand-rises-buyers-guard-against-ma-risk",
    ),
    # 4. Philippine cat pool first major test
    item(
        "insuranceasia-philippine-cat-pool-20260814", 66, "verified", "media",
        "insuranceasia",
        "双灾考验菲律宾巨灾保险池：PCIF首次实战 51家非寿险仅10家入池",
        "雙災考驗菲律賓巨災保險池：PCIF首次實戰 51家非壽險僅10家入池",
        "6月棉兰老岛7.8级地震成为菲律宾巨灾保险机制（PCIF）首个重大实战考验。PCIF于2025年7月成立、聚合地震风险，惟51家非寿险公司中仅10家加入，报案有限未真正检验其承灾能力。瑞士再保险估算新兴亚洲巨灾韧性仅5%，菲律宾保险渗透率仅2%居东盟末位，巨灾保障缺口凸显。[EN原文]",
        "6月棉蘭老島7.8級地震成為菲律賓巨災保險機制（PCIF）首個重大實戰考驗。PCIF於2025年7月成立、聚合地震風險，惟51家非壽險公司中僅10家加入，報案有限未真正檢驗其承災能力。瑞士再保險估算新興亞洲巨災韌性僅5%，菲律賓保險滲透率僅2%居東盟末位，巨災保障缺口凸顯。[EN原文]",
        "亚洲新兴市场巨灾保障缺口与再保需求直接相关，PCIF运作情况是观察区域巨灾风险转移与再保分出结构的样本。",
        "亞洲新興市場巨災保障缺口與再保需求直接相關，PCIF運作情況是觀察區域巨災風險轉移與再保分出結構的樣本。",
        {"front": {}, "midback": {}, "lead": {}, "cross": L("亚洲巨灾韧性=再保需求线索", "亞洲巨災韌性=再保需求線索")},
        {"front": 0, "midback": 1, "lead": 1, "cross": 2},
        "Insurance Asia", "en",
        ["market"], ["reinsurance", "catastrophe"],
        ["菲律宾", "巨灾保险池", "PCIF", "地震", "保障缺口"], ["菲律賓", "巨災保險池", "PCIF", "地震", "保障缺口"],
        "news", "2026-08-14T05:00:00+08:00",
        "https://insuranceasia.com/insurance/exclusive/twin-disasters-expose-philippine-insurance-gap",
    ),
    # 5. QBE H1 FY26 results
    item(
        "insurancebusiness-qbe-h1-20260814", 72, "verified", "pro",
        "insurancebusiness",
        "QBE中期调整后净利润10.3亿美元 股本回报17.7%超中期目标",
        "QBE中期調整後淨利潤10.3億美元 股本回報17.7%超中期目標",
        "QBE公布2026年中期业绩：调整后净利润10.33亿美元（上年同期9.97亿），股本回报17.7%高于15%+中期目标。平均续保费率升幅降至0.3%（上年2.1%），物业及部分Lloyd's业务转软；公司于百慕大推出新主险承保能力，并以AI辅助算法核保缩短复杂专业风险报价周期，国际业务（含亚洲）综合成本率改善。[EN原文]",
        "QBE公佈2026年中期業績：調整後淨利潤10.33億美元（上年同期9.97億），股本回報17.7%高於15%+中期目標。平均續保費率升幅降至0.3%（上年2.1%），物業及部分Lloyd's業務轉軟；公司於百慕大推出新主險承保能力，並以AI輔助算法核保縮短複雜專業風險報價週期，國際業務（含亞洲）綜合成本率改善。[EN原文]",
        "全球性综合险企中期业绩与定价走势为香港一般保险市场提供参照，AI核保提速及百慕大主险布局亦具行业信号意义。",
        "全球性綜合險企中期業績與定價走勢為香港一般保險市場提供參照，AI核保提速及百慕大主險佈局亦具行業信號意義。",
        {"front": {}, "midback": L("ROE 17.7%=国际同业标杆", "ROE 17.7%=國際同業標桿"), "lead": {}, "cross": L("百慕大主险能力=国际布局信号", "百慕大主險能力=國際佈局信號")},
        {"front": 0, "midback": 2, "lead": 1, "cross": 2},
        "Insurance Business", "en",
        ["insurer"], ["results", "capital", "market"],
        ["QBE", "中期业绩", "股本回报", "AI核保", "百慕大"], ["QBE", "中期業績", "股本回報", "AI核保", "百慕大"],
        "news", "2026-08-14T07:53:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/breaking-news/qbe-reports-1-03-billion-adjusted-profit-as-roe-hits-17-7-586101.aspx",
    ),
    # 6. Howden adds Sonija Cheng to HK financial lines team
    item(
        "insuranceasianews-howden-financial-lines-20260814", 62, "pending", "media",
        "insuranceasianews",
        "Howden委任Sonija Cheng为香港金融险团队总监 此前任职Willis逾七年",
        "Howden委任Sonija Cheng為香港金融險團隊總監 此前任職Willis逾七年",
        "经纪商Howden宣布委任Sonija Cheng加入其香港金融险（Financial Lines）团队出任总监。据Howden香港金融险团队负责人Franky Mok于LinkedIn公布，Cheng此前在Willis任职逾七年。Howden近期持续扩充亚洲金融险及专业责任险人才储备，反映该细分业务竞争加剧。[EN原文]",
        "經紀商Howden宣佈委任Sonija Cheng加入其香港金融險（Financial Lines）團隊出任總監。據Howden香港金融險團隊負責人Franky Mok於LinkedIn公佈，Cheng此前在Willis任職逾七年。Howden近期持續擴充亞洲金融險及專業責任險人才儲備，反映該細分業務競爭加劇。[EN原文]",
        "头部经纪商香港金融险团队人事动向是观察专业责任险、D&O等细分市场竞争格局的微观信号。",
        "頭部經紀商香港金融險團隊人事動向是觀察專業責任險、D&O等細分市場競爭格局的微觀信號。",
        {"front": {}, "midback": L("金融险人才流动=团队扩张信号", "金融險人才流動=團隊擴張信號"), "lead": {}, "cross": {}},
        {"front": 0, "midback": 2, "lead": 1, "cross": 1},
        "InsuranceAsia News", "en",
        ["market"], ["career", "market"],
        ["Howden", "金融险", "委任", "经纪商", "人才流动"], ["Howden", "金融險", "委任", "經紀商", "人才流動"],
        "news", "2026-08-14T16:42:00+08:00",
        "https://insuranceasianews.com/howden-adds-sonija-cheng-to-hong-kong-financial-lines-team/",
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

    # update last-check.json: all source timestamps -> now
    lc = json.loads(LASTCHECK.read_text(encoding='utf-8'))
    lc['lastCheck'] = INGESTED
    for k in lc['sources']:
        lc['sources'][k]['last'] = INGESTED
    LASTCHECK.write_text(json.dumps(lc, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"INSERTED {len(added)} items; total now {len(items)}")
    for it in added:
        print(' +', it['id'], '|', it['sourceTier'], it['score'], '|', it['publishedAt'])


if __name__ == '__main__':
    main()
