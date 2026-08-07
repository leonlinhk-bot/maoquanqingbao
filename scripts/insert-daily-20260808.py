#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-08) into live-items.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data/live-items.json'
INGESTED = "2026-08-08T18:08:00+08:00"

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

new_items = [
    item(
        "scmp-beijing-tax-not-new-aug07", 75, "pending", "media",
        "scmp:beijing-tax-not-new-20260807",
        "SCMP：北京称境外保单20%征税并非新政策 且不针对香港",
        "SCMP：北京稱境外保單20%徵稅並非新政策 且不針對香港",
        "SCMP引述北京方面表态：对境外保险收益按20%征税并非新政策，且不针对香港，呼吁市场勿过度反应。此前路透报道北京及杭州已开始对港险收益（含分红派息及预付保费利息）适用20%个人所得税率，保监局回应称申报义务一直存在。京方口径与此呼应，为恐慌情绪降温。[EN原文]",
        "SCMP引述北京方面表態：對境外保險收益按20%徵稅並非新政策，且不針對香港，呼籲市場勿過度反應。此前路透報道北京及杭州已開始對港險收益（含分紅派息及預付保費利息）適用20%個人所得稅率，保監局回應稱申報義務一直存在。京方口徑與此呼應，為恐慌情緒降溫。[EN原文]",
        "征税传闻的第二只靴子落地——北京官方口径「非新政策、不针对香港」，与保监局此前回应形成双重定调；恐慌叙事可告一段落，向客户解释税务合规问题有了更完整的官方依据链。",
        "徵稅傳聞的第二隻靴子落地——北京官方口徑「非新政策、不針對香港」，與保監局此前回應形成雙重定調；恐慌敘事可告一段落，向客戶解釋稅務合規問題有了更完整的官方依據鏈。",
        {"front": {"sc": "恐慌降温=客户沟通转向常态合规", "tc": "恐慌降溫=客戶溝通轉向常態合規"},
         "midback": {}, "lead": {"sc": "税务口径明确=跨境架构按既定规则走", "tc": "稅務口徑明確=跨境架構按既定規則走"},
         "cross": {}},
        {"front": 2, "midback": 0, "lead": 1, "cross": 1},
        "SCMP", "en", ["reg", "market"], ["tax", "offshore"],
        ["境外保单征税", "北京表态", "SCMP", "市场情绪"],
        ["境外保單徵稅", "北京表態", "SCMP", "市場情緒"],
        "news", "2026-08-07T12:23:00+08:00",
        "https://www.scmp.com/business/banking-finance/article/3363348/beijing-says-20-offshore-insurance-tax-not-new-and-does-not-target-hong-kong",
    ),
    item(
        "hkma-hkmca-boclife-annuity", 85, "verified", "official",
        "hkma:hkmca-boclife-annuity-20260807",
        "香港年金公司与中银人寿达成策略合作 指定中介可转介「香港年金计划」",
        "香港年金公司與中銀人壽達成策略合作 指定中介可轉介「香港年金計劃」",
        "香港按揭证券全资子公司香港年金公司8月7日宣布，与中银集团人寿建立策略合作，授权中银人寿指定持牌保险中介向客户介绍「香港年金计划」并转介合资格客户；行政总裁梁国权表示将持续发展本地年金市场，让更多中介协助公众认识年金在退休规划中的关键作用。[EN原文]",
        "香港按揭證券全資子公司香港年金公司8月7日宣佈，與中銀集團人壽建立策略合作，授權中銀人壽指定持牌保險中介向客戶介紹「香港年金計劃」並轉介合資格客戶；行政總裁梁國權表示將持續發展本地年金市場，讓更多中介協助公眾認識年金在退休規劃中的關鍵作用。[EN原文]",
        "公营年金借银行系中介扩渠，退休年金市场供给端再添渠道变量——银保渠道销售公营年金的模式或成新常态，值得关注其对私营养老金产品竞争格局的影响。",
        "公營年金借銀行系中介擴渠，退休年金市場供給端再添渠道變量——銀保渠道銷售公營年金的模式或成新常態，值得關注其對私營養老金產品競爭格局的影響。",
        {"front": {}, "midback": {"sc": "银保渠道卖公营年金=渠道格局新动向", "tc": "銀保渠道賣公營年金=渠道格局新動向"},
         "lead": {}, "cross": {}},
        {"front": 0, "midback": 1, "lead": 0, "cross": 1},
        "HKMA", "en", ["product", "market"], ["annuity", "distribution"],
        ["香港年金", "中银人寿", "银保渠道", "退休规划"],
        ["香港年金", "中銀人壽", "銀保渠道", "退休規劃"],
        "press", "2026-08-07T16:00:00+08:00",
        "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260807-3/",
    ),
    item(
        "sunlife-asia-q2-2026", 70, "verified", "pro",
        "insuranceasia:sunlife-asia-q2-20260807",
        "永明亚洲Q2净利润+153%至1.44亿美元 香港销售动能与在岸业务成主引擎",
        "永明亞洲Q2淨利潤+153%至1.44億美元 香港銷售動能與在岸業務成主引擎",
        "InsuranceAsia报道，永明亚洲Q2净利润1.44亿美元按年+153%，受股票市场利好及市场相关影响改善推动；基础净利润+18%至1.58亿美元，得益于香港销售动能与在岸业务增长、费用下降及信贷经验改善，部分被eMPF平台迁移令管理费用收入下降所抵销。[EN原文]",
        "InsuranceAsia報道，永明亞洲Q2淨利潤1.44億美元按年+153%，受股票市場利好及市場相關影響改善推動；基礎淨利潤+18%至1.58億美元，得益於香港銷售動能與在岸業務增長、費用下降及信貸經驗改善，部分被eMPF平台遷移令管理費用收入下降所抵銷。[EN原文]",
        "香港被点名撑起亚洲业绩——各渠道销售全面增长+在岸业务走强；同时新业务合约服务边际（CSM）下滑反映香港竞争加剧，对渠道而言是「市场在扩张、利润率承压」的又一注脚。",
        "香港被點名撐起亞洲業績——各渠道銷售全面增長+在岸業務走強；同時新業務合約服務邊際（CSM）下滑反映香港競爭加劇，對渠道而言是「市場在擴張、利潤率受壓」的又一注腳。",
        {"front": {}, "midback": {}, "lead": {"sc": "香港销售动能=在岸业务走强的证据链", "tc": "香港銷售動能=在岸業務走強的證據鏈"},
         "cross": {"sc": "eMPF迁移=费用结构新变量", "tc": "eMPF遷移=費用結構新變量"}},
        {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "InsuranceAsia", "en", ["insurer", "market"], ["results", "hongkong"],
        ["永明", "Q2业绩", "香港", "亚洲"],
        ["永明", "Q2業績", "香港", "亞洲"],
        "news", "2026-08-07T12:18:00+08:00",
        "https://insuranceasia.com/insurance/news/sun-lifes-asia-segment-net-income-surges-153-144m-in-q2",
    ),
    item(
        "prudential-plan-rename-aug24", 75, "verified", "insurer",
        "prudential:plan-name-update-20260824",
        "保诚香港8月24日起更新部分计划名称 储蓄型产品名加入「保險」字样",
        "保誠香港8月24日起更新部分計劃名稱 儲蓄型產品名加入「保險」字樣",
        "配合保监局与金管局最新命名要求，保诚香港将于8月24日起为逾20个储蓄、人寿及危疾计划更名，英文名加入「Insurance」、中文名加入「保險」，适用于现有保单及8月24日或之后的新单；保障、条款与保费不变，客户无需任何操作，通知信9月初起寄出。[EN原文+官方通知]",
        "配合保監局與金管局最新命名要求，保誠香港將於8月24日起為逾20個儲蓄、人壽及危疾計劃更名，英文名加入「Insurance」、中文名加入「保險」，適用於現有保單及8月24日或之後的新單；保障、條款與保費不變，客戶無需任何操作，通知信9月初起寄出。[EN原文+官方通知]",
        "监管推动「储蓄型产品名称须明示保险属性」已落地到头部保司——更名涉及在售主力储蓄/寿险计划，销售话术、材料与保单单据名称需同步更新，亦是全行业命名规范收紧的先行信号。",
        "監管推動「儲蓄型產品名稱須明示保險屬性」已落地到頭部保司——更名涉及在售主力儲蓄/壽險計劃，銷售話術、材料與保單單據名稱需同步更新，亦是全行業命名規範收緊的先行信號。",
        {"front": {"sc": "在售计划更名=话术与材料同步更新", "tc": "在售計劃更名=話術與材料同步更新"},
         "midback": {"sc": "系统保单名称切换=运营准备", "tc": "系統保單名稱切換=營運準備"},
         "lead": {}, "cross": {}},
        {"front": 2, "midback": 1, "lead": 0, "cross": 0},
        "保诚香港", "zh+en", ["product", "reg"], ["product", "compliance"],
        ["保诚", "计划更名", "监管要求", "储蓄险"],
        ["保誠", "計劃更名", "監管要求", "儲蓄險"],
        "news", "2026-07-01T00:00:00+08:00",
        "https://www.prudential.com.hk/en/claims-and-services/tools/customer-notices/customer-notice-products-name-change/",
    ),
    item(
        "axa-xl-srm-cyber-aug07", 60, "pending", "media",
        "insurancebusinessmag:axa-xl-srm-20260807",
        "AXA XL收购网络安全咨询公司S-RM剩余股份 整合网络险供应商面板",
        "AXA XL收購網絡安全諮詢公司S-RM剩餘股份 整合網絡險供應商面板",
        "AXA XL宣布收购已持股约49%的企业情报与网络安全咨询公司S-RM的剩余股份，交易预计监管批准后于9月底完成；S-RM此前亦服务AXA XL的竞争对手，经纪人在运行多保司网络险项目时需尽快确认其供应商安排是否延续。网络险理赔响应供应链正被险企纵向整合。[EN原文]",
        "AXA XL宣佈收購已持股約49%的企業情報與網絡安全諮詢公司S-RM的剩餘股份，交易預計監管批准後於9月底完成；S-RM此前亦服務AXA XL的競爭對手，經紀人在運行多保司網絡險項目時需盡快確認其供應商安排是否延續。網絡險理賠響應供應鏈正被險企縱向整合。[EN原文]",
        "再保险/网络险巨头纵向整合理赔响应服务商，预示网络险服务供应链集中化趋势，对香港经纪及网络险客户的供应商选择具有参考意义。",
        "再保險/網絡險巨頭縱向整合理賠響應服務商，預示網絡險服務供應鏈集中化趨勢，對香港經紀及網絡險客戶的供應商選擇具有參考意義。",
        {"front": {}, "midback": {}, "lead": {"sc": "网络险供应链整合=服务商格局将变", "tc": "網絡險供應鏈整合=服務商格局將變"}, "cross": {}},
        {"front": 0, "midback": 0, "lead": 1, "cross": 0},
        "Insurance Business", "en", ["tech"], ["cyber", "reinsurance"],
        ["AXA XL", "网络险", "并购", "网络安全"],
        ["AXA XL", "網絡險", "併購", "網絡安全"],
        "news", "2026-08-07T00:00:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/cyber/axa-xl-just-bought-the-vendor-half-of-every-cyber-panel-it-sat-on-585344.aspx",
    ),
]

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
LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print(f"Inserted {len(added)} items. Total: {len(data['items'])}")
