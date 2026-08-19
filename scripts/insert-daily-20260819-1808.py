#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-19 18:08 run) into live-items.json + update last-check.json.

Items collected after lastCheck 2026-08-19T00:55:16+08:00:
  1. IBMag: Gallagher Re creates digital risk unit as AI reshapes accumulation (2026-08-19 17:11+08)
  2. AASTOCKS: UBS initiates coverage on FWD (01828.HK) Neutral TP HKD32 (2026-08-19 13:02+08)
  3. 观点地产网: 保诚扩充太古坊香港总部办公空间至约8.3万方呎 (2026-08-19 12:03+08)
  4. InsuranceAsia: How cyber insurance gaps can leave factory damage uncovered (2026-08-19 05:00+08)
  5. Insurtech Insights: Bowtie launches StillCover supplementary medical plan (2026-08-18 18:08+08, 上轮遗漏补采)
  6. Manulife: The New Fluidity research - HK affluent rethink retirement (2026-08-18, 上轮遗漏补采)
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
    # 1. Gallagher Re digital risk unit (pro, EN)
    item(
        "ibmag-gallagherre-digital-risk-20260819", 70, "verified", "pro",
        "insurancebusinessmag",
        "Gallagher Re成立数字风险部门：AI重塑风险累积 将AI责任险、数据中心与网络险纳入统一框架",
        "Gallagher Re成立數字風險部門：AI重塑風險累積 將AI責任險、數據中心與網絡險納入統一框架",
        "再保险经纪Gallagher Re新设数字风险部门，将AI责任、数据中心与网络风险纳入同一承保与顾问框架，应对跨险类技术风险累积。公司称随着AI采用加速，传统风险累积模型被打破，需以跨学科团队整合承保、风险工程与数据能力，为不断增长的数字化暴露提供再保容量。[EN原文]",
        "再保險經紀Gallagher Re新設數字風險部門，將AI責任、數據中心與網絡風險納入同一承保與顧問框架，應對跨險類技術風險累積。公司稱隨著AI採用加速，傳統風險累積模型被打破，需以跨學科團隊整合承保、風險工程與數據能力，為不斷增長的數字化暴露提供再保容量。[EN原文]",
        "AI、数据中心与网络风险正从分散险类走向聚合管理，再保端以专门部门承接跨险类技术风险，预示新兴风险承保能力与条款创新方向，对港险再保与科技险布局有前瞻参照。",
        "AI、數據中心與網絡風險正從分散險類走向聚合管理，再保端以專門部門承接跨險類技術風險，預示新興風險承保能力與條款創新方向，對港險再保與科技險佈局有前瞻參照。",
        {"front": {}, "midback": L("新兴风险再保容量与条款调研", "新興風險再保容量與條款調研"), "lead": {}, "cross": L("AI/数据中心险全球格局跟踪", "AI/數據中心險全球格局跟蹤")},
        {"front": 0, "midback": 2, "lead": 1, "cross": 1},
        "Insurance Business Asia", "en",
        ["tech"], ["ai", "cyber"],
        ["Gallagher Re", "数字风险", "AI责任险", "数据中心", "网络风险"], ["Gallagher Re", "數字風險", "AI責任險", "數據中心", "網絡風險"],
        "news", "2026-08-19T17:11:11+08:00",
        "https://www.insurancebusinessmag.com/asia/news/breaking-news/gallagher-re-creates-digital-risk-unit-as-ai-reshapes-accumulation-586647.aspx",
    ),
    # 2. UBS initiates coverage on FWD (pro, EN原文/中文导读)
    item(
        "aastocks-ubs-fwd-coverage-20260819", 72, "verified", "pro",
        "aastocks",
        "瑞银首次覆盖富卫集团：给予「中性」评级 目标价32港元",
        "瑞銀首次覆蓋富衛集團：給予「中性」評級 目標價32港元",
        "瑞银发表研报首次覆盖富卫集团（01828.HK），给予「中性」评级，目标价32港元。报告指亚洲保险市场受保障缺口扩大、财富创造及政策支持推动具结构性吸引力；预测富卫2025-2030年新业务价值及税后营运利润年均复合增长12%及16%，但公司高度依赖第三方渠道（2025年占新业务价值78%），面临监管风险与佣金竞争，2025年内含价值仅相当于友邦的8.9%。[EN原文]",
        "瑞銀發表研報首次覆蓋富衛集團（01828.HK），給予「中性」評級，目標價32港元。報告指亞洲保險市場受保障缺口擴大、財富創造及政策支持推動具結構性吸引力；預測富衛2025-2030年新業務價值及稅後營運利潤年均複合增長12%及16%，但公司高度依賴第三方渠道（2025年佔新業務價值78%），面臨監管風險與佣金競爭，2025年內含價值僅相當於友邦的8.9%。[EN原文]",
        "上市刚满一年的富卫迎来首家覆盖研报，大行对其经纪渠道依赖与监管风险的定性，是评估港险新势力估值与渠道格局的重要坐标，对中介与同业竞争判断有直接参考价值。",
        "上市剛滿一年的富衛迎來首家覆蓋研報，大行對其經紀渠道依賴與監管風險的定性，是評估港險新勢力估值與渠道格局的重要座標，對中介與同業競爭判斷有直接參考價值。",
        {"front": L("富卫渠道与产品定位话术", "富衛渠道與產品定位話術"), "midback": {}, "lead": L("港险新势力估值对照", "港險新勢力估值對照"), "cross": L("大行港险覆盖跟踪", "大行港險覆蓋跟蹤")},
        {"front": 2, "midback": 0, "lead": 1, "cross": 1},
        "阿思达克财经网（AASTOCKS，瑞银研报）", "zh+en",
        ["market"], ["channel", "results"],
        ["瑞银", "富卫集团", "首次覆盖", "中性评级", "目标价32港元"], ["瑞銀", "富衛集團", "首次覆蓋", "中性評級", "目標價32港元"],
        "news", "2026-08-19T13:02:00+08:00",
        "https://wdatacn.aastocks.com/en/mobile/news.aspx?newsid=NOW.1539244&newssource=AAFN",
    ),
    # 3. Prudential Taikoo Place HQ expansion (insurer announcement, zh)
    item(
        "prudential-taikoo-hq-20260819", 75, "pending", "insurer",
        "prudential",
        "保诚与太古地产签署租赁协议 扩充太古坊香港总部至约8.3万方呎",
        "保誠與太古地產簽署租賃協議 擴充太古坊香港總部至約8.3萬方呎",
        "保诚保险与太古地产签署租赁协议，扩充及提升其于太古坊的办公空间，总部楼面面积将增至约8.3万平方呎，并整合营运至太古坊一座及港岛东中心。保诚自2011年进驻太古坊，行政总裁林智刚表示，扩充体现保诚对香港长远发展前景的信心，持续投入人才发展与业务能力建设，应对长期健康保障、财富管理及退休规划需求的增长。",
        "保誠保險與太古地產簽署租賃協議，擴充及提升其於太古坊的辦公空間，總部樓面面積將增至約8.3萬平方呎，並整合營運至太古坊一座及港島東中心。保誠自2011年進駐太古坊，行政總裁林智剛表示，擴充體現保誠對香港長遠發展前景的信心，持續投入人才發展與業務能力建設，應對長期健康保障、財富管理及退休規劃需求的增長。",
        "保诚以扩容总部巩固香港根基，是2026年港险竞争白热化下保司加码本地布局的微观信号；太古坊办公生态扩容亦与中环-东区保险业聚集带变化相关，值得渠道与同业观察。",
        "保誠以擴容總部鞏固香港根基，是2026年港險競爭白熱化下保司加碼本地佈局的微觀信號；太古坊辦公生態擴容亦與中環-東區保險業聚集帶變化相關，值得渠道與同業觀察。",
        {"front": {}, "midback": {}, "lead": L("保诚香港布局动态跟踪", "保誠香港佈局動態跟蹤"), "cross": L("保司写字楼与人才投入信号", "保司寫字樓與人才投入信號")},
        {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "观点地产网（保诚公告）", "zh",
        ["insurer"], ["firm", "career"],
        ["保诚", "太古坊", "太古地产", "总部扩容", "香港"], ["保誠", "太古坊", "太古地產", "總部擴容", "香港"],
        "news", "2026-08-19T12:03:10+08:00",
        "http://m.toutiao.com/group/7675588382818386478/",
    ),
    # 4. InsuranceAsia cyber insurance factory gaps (media, EN)
    item(
        "ia-cyber-factory-gaps-20260819", 66, "verified", "media",
        "insuranceasia",
        "InsuranceAsia：亚太互联工厂网络风险上升 网络险与财产险承保缺口暴露",
        "InsuranceAsia：亞太互聯工廠網絡風險上升 網絡險與財產險承保缺口暴露",
        "InsuranceAsia独家报道指，亚太互联工厂正面临日益增长的网络风险，攻击已延伸至运营技术系统，暴露出网络保险与财产保险之间的承保缺口。工厂物理损坏若源于网络事件，可能因保单措辞差异而得不到赔偿；报告呼吁企业与经纪重新审视风险累积、条款衔接及网络-财产险整合方案。[EN原文]",
        "InsuranceAsia獨家報道指，亞太互聯工廠正面臨日益增長的網絡風險，攻擊已延伸至運營技術系統，暴露出網絡保險與財產保險之間的承保缺口。工廠物理損壞若源於網絡事件，可能因保單措辭差異而得不到賠償；報告呼籲企業與經紀重新審視風險累積、條款銜接及網絡-財產險整合方案。[EN原文]",
        "网络事件引发物理损失的「网络-财产险断层」是2026年新兴风险焦点，直接影响工商业客户的保障设计与经纪方案，对港险一般保险与科技险产品开发有直接参照价值。",
        "網絡事件引發物理損失的「網絡-財產險斷層」是2026年新興風險焦點，直接影響工商業客戶的保障設計與經紀方案，對港險一般保險與科技險產品開發有直接參照價值。",
        {"front": L("工商业客户网络-财产险方案话术", "工商業客戶網絡-財產險方案話術"), "midback": L("网络/财产险条款衔接调研", "網絡/財產險條款銜接調研"), "lead": {}, "cross": L("新兴风险承保缺口跟踪", "新興風險承保缺口跟蹤")},
        {"front": 2, "midback": 2, "lead": 0, "cross": 1},
        "Insurance Asia", "en",
        ["tech"], ["cyber", "uw"],
        ["网络保险", "财产险", "互联工厂", "承保缺口", "运营技术"], ["網絡保險", "財產險", "互聯工廠", "承保缺口", "運營技術"],
        "news", "2026-08-19T05:00:00+08:00",
        "https://insuranceasia.com/insurance/exclusive/how-cyber-insurance-gaps-can-leave-factory-damage-uncovered",
    ),
    # 5. Bowtie StillCover (insurtech/media, EN)
    item(
        "bowtie-stillcover-20260818", 64, "pending", "media",
        "insurtechinsights",
        "Bowtie推出StillCover补充医疗险：面向慢性病患者及公院使用者",
        "Bowtie推出StillCover補充醫療險：面向慢性病患者及公院使用者",
        "香港虚拟保险公司Bowtie推出补充医疗险计划Bowtie StillCover，为依赖公营医院服务或患有慢性疾病、较难投保传统私家医疗保障的香港居民提供额外保障。产品针对公立医疗轮候与保障缺口设计，是本地虚拟险企向细分人群延展产品的又一尝试。[EN原文]",
        "香港虛擬保險公司Bowtie推出補充醫療險計劃Bowtie StillCover，為依賴公營醫院服務或患有慢性疾病、較難投保傳統私家醫療保障的香港居民提供額外保障。產品針對公立醫療輪候與保障缺口設計，是本地虛擬險企向細分人群延展產品的又一嘗試。[EN原文]",
        "虚拟险企以细分人群切入补充医疗市场，反映港险健康险竞争从标准体向次标准体与公院使用者延展，是产品创新与渠道数字化的观察样本。",
        "虛擬險企以細分人群切入補充醫療市場，反映港險健康險競爭從標準體向次標準體與公院使用者延展，是產品創新與渠道數字化的觀察樣本。",
        {"front": L("健康险细分人群产品对比", "健康險細分人群產品對比"), "midback": {}, "lead": {}, "cross": L("虚拟险企产品线跟踪", "虛擬險企產品線跟蹤")},
        {"front": 2, "midback": 0, "lead": 0, "cross": 1},
        "Insurtech Insights（Bowtie发布）", "en",
        ["product"], ["health", "insurtech"],
        ["Bowtie", "StillCover", "补充医疗险", "慢性病", "虚拟保险"], ["Bowtie", "StillCover", "補充醫療險", "慢性病", "虛擬保險"],
        "news", "2026-08-18T18:08:00+08:00",
        "https://www.insurtechinsights.com/knowledge-bank/",
    ),
    # 6. Manulife The New Fluidity research (insurer, zh+en)
    item(
        "manulife-new-fluidity-20260818", 78, "verified", "insurer",
        "manulife",
        "宏利×FT Longitude研究：长寿趋势重塑港人财富规划 仅18%富裕人士拥有整合财富计划",
        "宏利×FT Longitude研究：長壽趨勢重塑港人財富規劃 僅18%富裕人士擁有整合財富計劃",
        "宏利香港与FT Longitude联合发布《The New Fluidity》研究，访问亚太及中东11地共1000名高净值及大众富裕人士。结果显示香港富裕人士正按更长、更多元的人生阶段重构工作、投资与财富管理策略，但仅18%已制定整合投资、税务、传承、法律架构与家族治理的全面财富计划；32%计划较传统退休年龄多工作5至10年，「退而不休」成新常态。",
        "宏利香港與FT Longitude聯合發佈《The New Fluidity》研究，訪問亞太及中東11地共1000名高淨值及大眾富裕人士。結果顯示香港富裕人士正按更長、更多元的人生階段重構工作、投資與財富管理策略，但僅18%已制定整合投資、稅務、傳承、法律架構與家族治理的全面財富計劃；32%計劃較傳統退休年齡多工作5至10年，「退而不休」成新常態。",
        "头部保司联合国际研究机构揭示港人财富规划从「单一退休」转向「多阶段人生」，财富整合规划缺口即业务机会所在，对高净值客群经营、家办与传承服务有直接指引意义。",
        "頭部保司聯合國際研究機構揭示港人財富規劃從「單一退休」轉向「多階段人生」，財富整合規劃缺口即業務機會所在，對高淨值客群經營、家辦與傳承服務有直接指引意義。",
        {"front": L("高净值多阶段人生规划话术", "高淨值多階段人生規劃話術"), "midback": {}, "lead": L("财富整合规划缺口商机", "財富整合規劃缺口商機"), "cross": L("家办/传承服务趋势跟踪", "家辦/傳承服務趨勢跟蹤")},
        {"front": 2, "midback": 0, "lead": 2, "cross": 1},
        "宏利香港新闻稿（FT Longitude研究）", "zh+en",
        ["family"], ["family-office", "retirement"],
        ["宏利", "The New Fluidity", "FT Longitude", "财富规划", "长寿趋势"], ["宏利", "The New Fluidity", "FT Longitude", "財富規劃", "長壽趨勢"],
        "news", "2026-08-18T10:00:00+08:00",
        "https://www.manulife.com.hk/en/individual/about/newsroom/hong-kongs-affluent-rethink-retirement-and-wealth-strategies.html",
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
