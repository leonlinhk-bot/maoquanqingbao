#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-11 18:08 run) into live-items.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data/live-items.json'
INGESTED = "2026-08-11T18:08:00+08:00"

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
    # 1. Insurance Business / Swiss Re Institute: H1 2026 nat cat losses
    item(
        "ib-swissre-natcat-h1-2026", 72, "verified", "pro",
        "insurancebusinessmag:swissre-natcat-h1-2026",
        "瑞士再保险研究院：H1全球巨灾保险损失420亿美元 六年低位难掩风险上行",
        "瑞士再保險研究院：H1全球巨災保險損失420億美元 六年低位難掩風險上行",
        "瑞士再保险研究院数据显示，2026上半年全球巨灾保险损失约420亿美元，较十年均值低16%；但山火损失正以每年8-11%的速度累积，飓风季尚未到来。报告警告业界勿将上半年低损失读数直接套入续保定价，风险轨迹仍在上升。[EN原文]",
        "瑞士再保險研究院數據顯示，2026上半年全球巨災保險損失約420億美元，較十年均值低16%；但山火損失正以每年8-11%的速度累積，颶風季尚未到來。報告警告業界勿將上半年低損失讀數直接套入續保定價，風險軌跡仍在上升。[EN原文]",
        "巨灾损失低位≠费率宽松：山火累积增速与飓风季临近是财险/再保续保定价的关键变量，机构客户与再保排分需预留上行空间。",
        "巨災損失低位≠費率寬鬆：山火累積增速與颶風季臨近是財險/再保定價的關鍵變量，機構客戶與再保排分需預留上行空間。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "Insurance Business（瑞士再保险研究院）", "en",
        ["market", "insurer"], ["natcat", "reinsurance", "pricing"],
        ["瑞士再保险", "巨灾损失", "山火", "飓风", "再保定价"], ["瑞士再保險", "巨災損失", "山火", "颶風", "再保定價"],
        "news", "2026-08-11T17:13:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/catastrophe/sixyearlow-catastrophe-losses-arent-the-reassurance-they-look-like-585669.aspx",
    ),
    # 2. Insurance Business: Typhoon Dolphin accumulation across China & Philippines
    item(
        "ib-typhoon-dolphin-20260811", 64, "verified", "media",
        "insurancebusinessmag:dolphin-accumulation-20260811",
        "台风「白海豚」登陆浙江玉环 中国菲律宾多险种同时触发赔付累积",
        "颱風「白海豚」登陸浙江玉環 中國菲律賓多險種同時觸發賠付累積",
        "台风白海豚周日傍晚登陆浙江玉环，同时触发中国与菲律宾两地财产、船舶船体、货运、建工一切险、业务中断及航空险的赔付累积；分析指该区域属此类风暴结构性保障不足最严重的市场之一，区域保单常将各险种与地域割裂看待。[EN原文]",
        "颱風白海豚週日傍晚登陸浙江玉環，同時觸發中國與菲律賓兩地財產、船舶船體、貨運、建工一切險、業務中斷及航空險的賠付累積；分析指該區域屬此類風暴結構性保障不足最嚴重的市場之一，區域保單常將各險種與地域割裂看待。[EN原文]",
        "单一台风触发跨市场多险种累积=巨灾建模与区域累积风险的现实案例，涉中国/菲律宾敞口的货运、工程险客户需重估累积限额。",
        "單一颱風觸發跨市場多險種累積=巨災建模與區域累積風險的現實案例，涉中國/菲律賓敞口的貨運、工程險客戶需重估累積限額。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 1, "midback": 2, "lead": 0, "cross": 1},
        "Insurance Business", "en",
        ["market"], ["natcat", "marine", "china"],
        ["台风白海豚", "浙江", "巨灾", "货运险", "建工险"], ["颱風白海豚", "浙江", "巨災", "貨運險", "建工險"],
        "news", "2026-08-11T08:22:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/catastrophe/dolphin-is-not-one-loss--it-is-an-accumulation-problem-across-two-markets-585556.aspx",
    ),
    # 3. 观点网: HK considers extending carried interest tax reform to prop trading firms
    item(
        "hk-tax-prop-trading-20260811", 64, "verified", "media",
        "guandian:hk-tax-prop-trading-20260811",
        "港据报拟将自营交易公司纳入税务改革 附带权益优惠或扩围 财库局称不限特定管理者",
        "港據報擬將自營交易公司納入稅務改革 附帶權益優惠或擴圍 財庫局稱不限特定管理者",
        "外媒指香港拟将自营交易公司纳入税务改革：立法会审议中的附带权益优惠税制条例草案，拟将低税率扩至对冲基金、私募、风投、私人信贷及家办等更广泛投资利润；财经事务及库务局回应称优惠不限于特定类型管理者，被视为与新加坡争夺顶尖金融人才。",
        "外媒指香港擬將自營交易公司納入稅務改革：立法會審議中的附帶權益優惠稅制條例草案，擬將低稅率擴至對沖基金、私募、風投、私人信貸及家辦等更廣泛投資利潤；財經事務及庫務局回應稱優惠不限於特定類型管理者，被視為與新加坡爭奪頂尖金融人才。",
        "附带权益税制扩围=香港基金/家办生态的直接利好信号，涉家族办公室架构与跨境税务规划客户可跟进条例草案审议进程。",
        "附帶權益稅制擴圍=香港基金/家辦生態的直接利好信號，涉家族辦公室架構與跨境稅務規劃客戶可跟進條例草案審議進程。",
        {"front": {}, "midback": {}, "lead": L("附带权益扩围=家办/基金税务利好", "附帶權益擴圍=家辦/基金稅務利好"), "cross": {}},
        {"front": 1, "midback": 1, "lead": 1, "cross": 2},
        "观点网（今日头条·金融界）", "zh",
        ["market", "family"], ["taxation", "family-office", "fund"],
        ["附带权益", "税务改革", "家族办公室", "基金", "财库局"], ["附帶權益", "稅務改革", "家族辦公室", "基金", "財庫局"],
        "news", "2026-08-11T14:58:00+08:00",
        "http://m.toutiao.com/group/7672664766363517466/",
    ),
    # 4. 观澜财研: CRS 2.0 timeline explainer on HK insurance tax
    item(
        "toutiao-crs-tax-timeline-20260811", 62, "verified", "media",
        "toutiao:crs-tax-timeline-20260811",
        "港险征税拆解：CRS 2.0今年生效2027年首次信息交换 合规评估窗口期明确",
        "港險徵稅拆解：CRS 2.0今年生效2027年首次信息交換 合規評估窗口期明確",
        "自媒体拆解港险征税：财新曝北京杭州征税个案、港股保险板块应声暴跌、税务总局表态「非新政策」，法理争议未决、统一细则未出。关键节点：CRS 2.0已于2026年1月1日生效、2027年首次信息交换，香港自动交换资料条例修订草案已交立法会首读，2027年前为合规评估窗口期。",
        "自媒體拆解港險徵稅：財新曝北京杭州徵稅個案、港股保險板塊應聲暴跌、稅務總局表態「非新政策」，法理爭議未決、統一細則未出。關鍵節點：CRS 2.0已於2026年1月1日生效、2027年首次信息交換，香港自動交換資料條例修訂草案已交立法會首讀，2027年前為合規評估窗口期。",
        "CRS 2.0时间表=征税从「个案」走向「系统化」的确定性路径，对持单客户与跨境架构是必须提前沟通的合规节点。",
        "CRS 2.0時間表=徵稅從「個案」走向「系統化」的確定性路徑，對持單客戶與跨境架構是必須提前溝通的合規節點。",
        {"front": {}, "midback": L("CRS2.0时间表=客户合规沟通话术", "CRS2.0時間表=客戶合規溝通話術"), "lead": {}, "cross": {}},
        {"front": 2, "midback": 2, "lead": 1, "cross": 2},
        "观澜财研（今日头条）", "zh",
        ["reg", "market"], ["taxation", "cross-border", "compliance"],
        ["港险征税", "CRS 2.0", "信息交换", "合规", "自动交换资料"], ["港險徵稅", "CRS 2.0", "信息交換", "合規", "自動交換資料"],
        "news", "2026-08-11T13:54:45+08:00",
        "http://m.toutiao.com/group/7672648195784180287/",
    ),
    # 5. InsuranceAsia: SafetyCulture rebrands to Mitti Insurance, US expansion
    item(
        "ia-mitti-rebrand-20260811", 61, "verified", "media",
        "insuranceasia:mitti-rebrand-20260811",
        "澳洲保险科技独角兽SafetyCulture更名Mitti 携AI风控进军美国市场",
        "澳洲保險科技獨角獸SafetyCulture更名Mitti 攜AI風控進軍美國市場",
        "澳洲保险科技独角兽SafetyCulture（估值13亿美元）更名Mitti并进军美国：保险业务今年已承保保费7000万美元、目标占集团业务至少30%，新增商责与财产险（ISR）产品；已获美国51州牌照、首批聚焦中西部10州，未来将自行承保部分风险，并以AI视觉识别做风险预防。[EN原文]",
        "澳洲保險科技獨角獸SafetyCulture（估值13億美元）更名Mitti並進軍美國：保險業務今年已承保保費7000萬美元、目標佔集團業務至少30%，新增商責與財產險（ISR）產品；已獲美國51州牌照、首批聚焦中西部10州，未來將自行承保部分風險，並以AI視覺識別做風險預防。[EN原文]",
        "数据+AI定价保险的商业模式样本：从安全工具到承保商的路径，对观察保险科技与嵌入式保险趋势有参考价值。",
        "數據+AI定價保險的商業模式樣本：從安全工具到承保商的路徑，對觀察保險科技與嵌入式保險趨勢有參考價值。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 1, "midback": 1, "lead": 0, "cross": 0},
        "Insurance Asia", "en",
        ["tech"], ["insurtech", "ai", "us-expansion"],
        ["保险科技", "Mitti", "SafetyCulture", "AI风控", "美国市场"], ["保險科技", "Mitti", "SafetyCulture", "AI風控", "美國市場"],
        "news", "2026-08-11T12:38:00+08:00",
        "https://insuranceasia.com/insurance/news/australias-safetyculture-rebrands-mitti-insurance-and-eyes-us-expansion",
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
data['meta']['itemCount'] = len(data['items'])
LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print(f"Inserted {len(added)} items. Total: {len(data['items'])}")
