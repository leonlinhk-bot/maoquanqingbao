#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-11) into live-items.json."""
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
    # 1. InsuranceAsia: China insurance tax follow-up
    item(
        "ia-china-tax-sales-20260811", 68, "verified", "media",
        "insuranceasia:china-tax-sales-20260811",
        "港险征税后续：20%个税令收益差收窄 友邦保诚股价续跌",
        "港險徵稅後續：20%個稅令收益差收窄 友邦保誠股價續跌",
        "内地对境外保单收益征20%个税，令香港与内地储蓄产品收益差收窄，或拖累港险短期销售，友邦保诚股价下挫；Jefferies认为征税落地反带来长期监管确定性，销售重心需转向保障与传承功能。[EN原文]",
        "內地對境外保單收益徵20%個稅，令香港與內地儲蓄產品收益差收窄，或拖累港險短期銷售，友邦保誠股價下挫；Jefferies認為徵稅落地反帶來長期監管確定性，銷售重心需轉向保障與傳承功能。[EN原文]",
        "征税后续最新市场反馈：从「恐慌」转向「产品结构怎么调」，直接决定内地客群销售话术与产品推荐排序，是本月最值得跟踪的主线。",
        "徵稅後續最新市場反饋：從「恐慌」轉向「產品結構怎麼調」，直接決定內地客群銷售話術與產品推薦排序，是本月最值得跟蹤的主線。",
        {"front": {}, "midback": {}, "lead": L("征税落地=话术转向保障与传承", "徵稅落地=話術轉向保障與傳承"), "cross": {}},
        {"front": 2, "midback": 1, "lead": 1, "cross": 1},
        "Insurance Asia", "en", ["reg", "market"], ["taxation", "cross-border", "market"],
        ["港险征税", "收益差", "友邦", "保诚", "MCV"], ["港險徵稅", "收益差", "友邦", "保誠", "MCV"],
        "news", "2026-08-11T05:30:00+08:00",
        "https://insuranceasia.com/insurance/news/china-insurance-tax-threatens-sales-prudential-and-aia-slide",
    ),
    # 2. InsuranceAsia: Asia wealth transfer / Manulife Singapore $384m
    item(
        "ia-asia-wealth-transfer-20260811", 66, "verified", "media",
        "insuranceasia:asia-wealth-transfer-20260811",
        "亚洲财富传承潮：宏利新加坡3.84亿美元巨额寿险保单刷新纪录",
        "亞洲財富傳承潮：宏利新加坡3.84億美元巨額壽險保單刷新紀錄",
        "亚洲超高净值人口2025年增长15.8%、成全球增速最快财富区，预计5.8万亿美元将跨代转移。宏利新加坡年初承保3.84亿美元单一寿险保单创全球纪录（超越汇丰人寿香港两年前的3.2亿美元），巨额保单背后的融资安排与流动性规划需求凸显。[EN原文]",
        "亞洲超高淨值人口2025年增長15.8%、成全球增速最快財富區，預計5.8萬億美元將跨代轉移。宏利新加坡年初承保3.84億美元單一壽險保單創全球紀錄（超越滙豐人壽香港兩年前的3.2億美元），巨額保單背後的融資安排與流動性規劃需求凸顯。[EN原文]",
        "大额保单+保费融资=高净值客户传承刚需的直接证据；对经纪/IFA而言，谈财富传承方案时这是最有说服力的市场背书。",
        "大額保單+保費融資=高淨值客戶傳承剛需的直接證據；對經紀/IFA而言，談財富傳承方案時這是最有說服力的市場背書。",
        {"front": {}, "midback": {}, "lead": L("3.84亿美元保单=传承需求实证", "3.84億美元保單=傳承需求實證"), "cross": {}},
        {"front": 2, "midback": 0, "lead": 1, "cross": 1},
        "Insurance Asia", "en", ["market", "insurer"], ["wealth-transfer", "hnw", "premium-financing"],
        ["财富传承", "巨额保单", "保费融资", "宏利", "高净值"], ["財富傳承", "巨額保單", "保費融資", "宏利", "高淨值"],
        "news", "2026-08-11T09:00:00+08:00",
        "https://insuranceasia.com/commentary/financing-challenge-behind-asias-wealth-transfer",
    ),
    # 3. InsuranceAsia: Sompo Life Re Bermuda platform
    item(
        "ia-sompo-life-re-bermuda-20260810", 64, "verified", "media",
        "insuranceasia:sompo-life-re-bermuda-20260810",
        "损保生命再保推百慕大平台 携手Agam Capital深化资产负债管理",
        "損保生命再保推百慕大平台 攜手Agam Capital深化資產負債管理",
        "Sompo Life Re设立新的百慕大注册寿险再保平台，并与科技型资产负债管理（ALM）专家Agam Capital签署多年期服务协议；Agam在筹建期协助运营建设并取得百慕大牌照。百慕大寿险再保平台持续扩容，与香港高净值万用寿险再保安排形成联动。[EN原文]",
        "Sompo Life Re設立新的百慕大註冊壽險再保平台，並與科技型資產負債管理（ALM）專家Agam Capital簽署多年期服務協議；Agam在籌建期協助營運建設並取得百慕大牌照。百慕大壽險再保平台持續擴容，與香港高淨值萬用壽險再保安排形成聯動。[EN原文]",
        "百慕大平台=香港IUL/高净值保单再保链条的关键一环；平台扩容提示离岸架构与再保服务需求持续上升。",
        "百慕大平台=香港IUL/高淨值保單再保鏈條的關鍵一環；平台擴容提示離岸架構與再保服務需求持續上升。",
        {"front": {}, "midback": {}, "lead": L("百慕大再保扩容=离岸架构信号", "百慕大再保擴容=離岸架構信號"), "cross": {}},
        {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "Insurance Asia", "en", ["insurer", "product"], ["reinsurance", "bermuda", "hnw"],
        ["再保险", "百慕大", "Sompo", "高净值", "资产负债管理"], ["再保險", "百慕大", "Sompo", "高淨值", "資產負債管理"],
        "news", "2026-08-10T06:00:00+08:00",
        "https://insuranceasia.com/insurance/news/sompo-life-re-launches-bermuda-platform",
    ),
    # 4. InsuranceAsia: Aon wars tighten checks
    item(
        "ia-aon-wars-tighten-20260811", 63, "verified", "media",
        "insuranceasia:aon-wars-tighten-20260811",
        "Aon：商险费率续降 战争风险推动海空能源核保趋严",
        "Aon：商險費率續降 戰爭風險推動海空能源核保趨嚴",
        "Aon Q2 2026全球保险市场洞察显示：多数险种容量充裕、费率续降、承保条件改善，但地缘紧张、理赔通胀与更细的风险尽调令局部承压；中东局势相关风险使海事、航空、能源险核保核查显著收紧。[EN原文]",
        "Aon Q2 2026全球保險市場洞察顯示：多數險種容量充裕、費率續降、承保條件改善，但地緣緊張、理賠通脹與更細的風險盡調令局部受壓；中東局勢相關風險使海事、航空、能源險核保核查顯著收緊。[EN原文]",
        "费率下行≠全面宽松：战争相关险种核保趋严，涉中东业务的货运/能源客户续保将更费时费力，排分需预留更长周期。",
        "費率下行≠全面寬鬆：戰爭相關險種核保趨嚴，涉中東業務的貨運/能源客戶續保將更費時費力，排分需預留更長週期。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "Insurance Asia", "en", ["market"], ["pricing", "marine", "geopolitics"],
        ["商险费率", "战争风险", "海事", "能源险", "Aon"], ["商險費率", "戰爭風險", "海事", "能源險", "Aon"],
        "news", "2026-08-11T05:45:00+08:00",
        "https://insuranceasia.com/insurance/news/insurance-prices-fall-wars-push-insurers-tighten-checks-aon",
    ),
    # 5. InsuranceAsia: Japan insurers unwind stakes
    item(
        "ia-japan-unwind-stakes-20260811", 62, "verified", "media",
        "insuranceasia:japan-unwind-stakes-20260811",
        "日本非寿险巨头加速减持战略持股 监管问责驱动资本重置",
        "日本非壽險巨頭加速減持戰略持股 監管問責驅動資本重置",
        "日本主要非寿险公司加快出售企业战略持股：监管将交叉持股与此前不当行为挂钩并责令减持（惠誉指并非偿付能力原因），释放资本投向海外扩张与其他投资，改写日本险企资产负债表格局。[EN原文]",
        "日本主要非壽險公司加快出售企業戰略持股：監管將交叉持股與此前不當行為掛鉤並責令減持（惠譽指並非償付能力原因），釋放資本投向海外擴張與其他投資，改寫日本險企資產負債表格局。[EN原文]",
        "日本险企资本流向变化=亚洲再保与投资市场的容量变量；减持潮释放的资本或进入海外另类资产，值得机构端跟踪。",
        "日本險企資本流向變化=亞洲再保與投資市場的容量變量；減持潮釋放的資本或進入海外另類資產，值得機構端跟蹤。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 0, "midback": 1, "lead": 0, "cross": 1},
        "Insurance Asia", "en", ["market", "insurer"], ["capital", "japan", "shareholding"],
        ["日本", "非寿险", "交叉持股", "资本", "惠誉"], ["日本", "非壽險", "交叉持股", "資本", "惠譽"],
        "news", "2026-08-11T05:00:00+08:00",
        "https://insuranceasia.com/insurance/exclusive/japan-insurers-unwind-corporate-stakes-after-misconduct",
    ),
    # 6. InsuranceAsia: trade disruption demand
    item(
        "ia-trade-disruption-demand-20260811", 61, "verified", "media",
        "insuranceasia:trade-disruption-demand-20260811",
        "GlobalData调查：41%企业预期供应链中断险需求增长最猛",
        "GlobalData調查：41%企業預期供應鏈中斷險需求增長最猛",
        "GlobalData二季度面向Verdict Media用户的调查（107份样本）显示：41.1%受访者预期供应链保险将因地缘风险成为需求增速最快的险种；贸易路线中断与日常运营扰动持续推高投保意愿。[EN原文]",
        "GlobalData第二季面向Verdict Media用戶的調查（107份樣本）顯示：41.1%受訪者預期供應鏈保險將因地緣風險成為需求增速最快的險種；貿易路線中斷與日常營運擾動持續推高投保意願。[EN原文]",
        "供应链中断险=商险下一条增长曲线；面向进出口、制造客户可提前布局需求话术与产品组合。",
        "供應鏈中斷險=商險下一條增長曲線；面向進出口、製造客戶可提前佈局需求話術與產品組合。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 1, "midback": 1, "lead": 0, "cross": 1},
        "Insurance Asia", "en", ["market"], ["supply-chain", "sme", "geopolitics"],
        ["供应链险", "贸易中断", "地缘风险", "商险"], ["供應鏈險", "貿易中斷", "地緣風險", "商險"],
        "news", "2026-08-11T05:15:00+08:00",
        "https://insuranceasia.com/insurance/news/two-in-five-businesses-expect-trade-disruption-cover-lead-demand",
    ),
    # 7. InsuranceAsia: AI datacenter expert opinion
    item(
        "ia-ai-datacenter-risks-20260810", 62, "verified", "media",
        "insuranceasia:ai-datacenter-risks-20260810",
        "专家意见：AI或使全球数据中心用电2030年前近翻三倍 险企须重估敞口",
        "專家意見：AI或使全球數據中心用電2030年前近翻三倍 險企須重估敞口",
        "AI需求或令全球数据中心电力消耗2030年前接近翻三倍，险企须重估电网承压、气候灾害与网络威胁叠加下的设施风险；Aon亚太商险主管指电力可用性与能源韧性已成超大规模数据中心首要承保关切。[EN原文]",
        "AI需求或令全球數據中心電力消耗2030年前接近翻三倍，險企須重估電網受壓、氣候災害與網絡威脅疊加下的設施風險；Aon亞太商險主管指電力可用性與能源韌性已成超大規模數據中心首要承保關切。[EN原文]",
        "数据中心险从「容量故事」进入「电力/能源承保」深水区，与8月8日韩国18.4GW报道互为补充，技术线客户可跟进。",
        "數據中心險從「容量故事」進入「電力/能源承保」深水區，與8月8日韓國18.4GW報道互為補充，技術線客戶可跟進。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "Insurance Asia", "en", ["tech", "market"], ["datacenter", "ai", "energy"],
        ["AI数据中心", "电力", "能源韧性", "承保", "Aon"], ["AI數據中心", "電力", "能源韌性", "承保", "Aon"],
        "news", "2026-08-10T11:00:00+08:00",
        "https://insuranceasia.com/insurance/expert-opinion/how-can-insurers-keep-ai-data-centre-risks",
    ),
    # 8. HKMA: Climate Finance Conference
    item(
        "hkma-dfsa-climate-conf-20260810", 86, "verified", "official",
        "hkma:dfsa-climate-conf-20260810",
        "金管局与迪拜金管局合办第三届气候金融会议 9月10日香港举行",
        "金管局與杜拜金管局合辦第三屆氣候金融會議 9月10日香港舉行",
        "金管局与迪拜金融服务管理局（DFSA）宣布，第三届联合气候金融会议将于9月10日在香港举行，主题「在变化世界中推动转型」，由港交所与纳斯达克迪拜支持；将汇聚企业领袖、投资者与政策制定者，探讨亚洲与中东气候金融合作及创新融资方案。",
        "金管局與杜拜金融服務管理局（DFSA）宣佈，第三屆聯合氣候金融會議將於9月10日在香港舉行，主題「在變化世界中推動轉型」，由港交所與納斯達克杜拜支持；將匯聚企業領袖、投資者與政策制定者，探討亞洲與中東氣候金融合作及創新融資方案。",
        "气候金融=香港国际金融中心新叙事；会议议程可预告监管与产品方向，也是机构客户与家办的话题素材。",
        "氣候金融=香港國際金融中心新敘事；會議議程可預告監管與產品方向，也是機構客戶與家辦的話題素材。",
        {"front": {}, "midback": {}, "lead": L("9月气候金融会议=机构客户话题", "9月氣候金融會議=機構客戶話題"), "cross": {}},
        {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "HKMA", "zh+en", ["reg", "market"], ["climate", "esg", "conference"],
        ["气候金融", "金管局", "DFSA", "转型", "ESG"], ["氣候金融", "金管局", "DFSA", "轉型", "ESG"],
        "press", "2026-08-10T00:00:00+08:00",
        "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260810-3/",
    ),
    # 9. IB: BHSI Macau
    item(
        "ib-bhsi-macau-20260810", 64, "verified", "media",
        "insurancebusinessmag:bhsi-macau-20260810",
        "伯克希尔旗下BHSI进军澳门 再保部门Q2承保改善",
        "伯克希爾旗下BHSI進軍澳門 再保部門Q2承保改善",
        "伯克希尔Q2净利257亿美元（上年同期124亿），主要受127亿美元投资收益推动；再保集团BHRG承保业绩改善（前期准备金有利释放），BHSI扩展澳门市场。正值Aon警示中东风险令海事、航空与贸易险条款收紧，区域承保容量增加。[EN原文]",
        "伯克希爾Q2淨利257億美元（上年同期124億），主要受127億美元投資收益推動；再保集團BHRG承保業績改善（前期準備金有利釋放），BHSI擴展澳門市場。正值Aon警示中東風險令海事、航空與貿易險條款收緊，區域承保容量增加。[EN原文]",
        "伯克希尔再保扩容+澳门落子=区域商险容量与竞争格局变量，对澳门/香港商业险排分与再保安排有参考意义。",
        "伯克希爾再保擴容+澳門落子=區域商險容量與競爭格局變量，對澳門/香港商業險排分與再保安排有參考意義。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "Insurance Business", "en", ["insurer", "market"], ["berkshire", "macau", "reinsurance"],
        ["伯克希尔", "BHSI", "澳门", "再保险", "商险容量"], ["伯克希爾", "BHSI", "澳門", "再保險", "商險容量"],
        "news", "2026-08-10T01:53:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/breaking-news/bhsi-expands-into-macau-as-berkshires-reinsurance-arm-posts-a-stronger-quarter-585472.aspx",
    ),
    # 10. IB: Aon soft market fraying
    item(
        "ib-soft-market-fraying-20260810", 62, "verified", "media",
        "insurancebusinessmag:soft-market-fraying-20260810",
        "Aon全球商险季报：费率续跌 车险/责任险/D&O显软周期裂痕",
        "Aon全球商險季報：費率續跌 車險/責任險/D&O顯軟週期裂痕",
        "Aon Q2 2026全球保险市场概览：容量充裕、竞争激烈，多数客户续保仍享费率优惠；但车险、美国敞口责任险与D&O等板块率先出现软周期松动迹象；Marsh英国商险费率Q2跌8%、财产险跌11%。[EN原文]",
        "Aon Q2 2026全球保險市場概覽：容量充裕、競爭激烈，多數客戶續保仍享費率優惠；但車險、美國敞口責任險與D&O等板塊率先出現軟週期鬆動跡象；Marsh英國商險費率Q2跌8%、財產險跌11%。[EN原文]",
        "软周期「边缘裂痕」=续保议价窗口仍在但收窄，D&O/责任险客户宜趁窗口锁定条件，经纪排分需加速。",
        "軟週期「邊緣裂痕」=續保議價窗口仍在但收窄，D&O/責任險客戶宜趁窗口鎖定條件，經紀排分需加速。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "Insurance Business", "en", ["market"], ["pricing", "soft-market", "dando"],
        ["费率", "软周期", "D&O", "责任险", "车险"], ["費率", "軟週期", "D&O", "責任險", "車險"],
        "news", "2026-08-10T01:24:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/breaking-news/rates-keep-falling-but-car-casualty-and-dando-show-where-the-soft-market-is-fraying-585466.aspx",
    ),
    # 11. IB: OpenAI cyber
    item(
        "ib-openai-cyber-20260810", 63, "verified", "media",
        "insurancebusinessmag:openai-cyber-20260810",
        "OpenAI暂停新模型研发 网络险承保人：AI威胁从预期变成现实",
        "OpenAI暫停新模型研發 網絡險承保人：AI威脅從預期變成現實",
        "8月7日OpenAI以无法排除模型已达「临界」网络安全能力为由，暂停未发布模型Astra的部分研发——AI能力风险首次被贴上具体时间标签；网络险承保人两年来将AI按未来敞口定价，如今须按现实风险重估费率与限额。[EN原文]",
        "8月7日OpenAI以無法排除模型已達「臨界」網絡安全能力為由，暫停未發佈模型Astra的部分研發——AI能力風險首次被貼上具體時間標籤；網絡險承保人兩年來將AI按未來敞口定價，如今須按現實風險重估費率與限額。[EN原文]",
        "AI网络风险「落地」时间点明确化=网络险定价叙事转折，也是企业客户网络险续保谈判的新筹码。",
        "AI網絡風險「落地」時間點明確化=網絡險定價敘事轉折，也是企業客戶網絡險續保談判的新籌碼。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "Insurance Business", "en", ["tech", "market"], ["cyber", "ai", "underwriting"],
        ["OpenAI", "网络险", "AI风险", "承保", "Astra"], ["OpenAI", "網絡險", "AI風險", "承保", "Astra"],
        "news", "2026-08-10T17:40:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/cyber/insurers-thought-the-threat-to-cyber-was-bad-from-ai--now-even-openai-is-scared-585507.aspx",
    ),
    # 12. on.cc: HSBC cuts AIA target price
    item(
        "oncc-hsbc-aia-tp-20260810", 72, "verified", "pro",
        "oncc:hsbc-aia-tp-20260810",
        "滙豐研究削友邦目标价近9%至74元 忧内地访客业务受结构性影响",
        "滙豐研究削友邦目標價近9%至74元 憂內地訪客業務受結構性影響",
        "滙豐研究将友邦目标价下调近9%至74港元，维持「持有」：认为境外保单收益征税或令内地访客（MCV）业务受结构性影响，保险公司或需调整产品结构应对、恐侵蚀新业务价值。为征税风波以来大行首次明确下调友邦目标价。",
        "滙豐研究將友邦目標價下調近9%至74港元，維持「持有」：認為境外保單收益徵稅或令內地訪客（MCV）業務受結構性影響，保險公司或需調整產品結構應對、恐侵蝕新業務價值。為徵稅風波以來大行首次明確下調友邦目標價。",
        "大行首次明确下调=征税影响从「情绪」进入「盈利测算」阶段；对持有友邦或港险板块仓位的客户是重要信号。",
        "大行首次明確下調=徵稅影響從「情緒」進入「盈利測算」階段；對持有友邦或港險板塊倉位的客戶是重要信號。",
        {"front": {}, "midback": {}, "lead": L("大行下调目标价=征税进入盈利测算阶段", "大行下調目標價=徵稅進入盈利測算階段"), "cross": {}},
        {"front": 1, "midback": 1, "lead": 1, "cross": 1},
        "on.cc东网（滙豐研究）", "zh", ["reg", "market"], ["taxation", "aia", "analyst"],
        ["友邦", "目标价", "滙豐研究", "征税", "MCV"], ["友邦", "目標價", "滙豐研究", "徵稅", "MCV"],
        "news", "2026-08-10T20:34:00+08:00",
        "https://hk.on.cc/hk/bkn/cnt/finance/20260810/bkn-20260810203450989-0810_00842_001.html",
    ),
    # 13. STCN: network marketing rules + account crackdown (HK grey chain)
    item(
        "stcn-netmarketing-20260810", 74, "verified", "pro",
        "stcn:netmarketing-20260810",
        "金融产品网络营销新规9月底实施 监管摸排「租号」乱象 港险黑灰产链条被点名",
        "金融產品網絡營銷新規9月底實施 監管摸排「租號」亂象 港險黑灰產鏈條被點名",
        "《金融产品网络营销管理办法》9月30日实施。北京金融监管局要求险企8月底前对抖音、视频号、小红书机构账号全量建档，重点排查「租号」；财险司全面自查严禁借账号推介境外保单，「1200元/年租蓝V账号」「IP漂移港澳宣传港险」等黑灰产链条将被切断。",
        "《金融產品網絡營銷管理辦法》9月30日實施。北京金融監管局要求險企8月底前對抖音、視頻號、小紅書機構賬號全量建檔，重點排查「租號」；財險司全面自查嚴禁借賬號推介境外保單，「1200元/年租藍V賬號」「IP漂移港澳宣傳港險」等黑灰產鏈條將被切斷。",
        "大陆账号端排查直接点名「宣传港险」黑灰产=港险获客渠道合规红线再收紧，对内地展业与引流模式影响直接。",
        "大陸賬號端排查直接點名「宣傳港險」黑灰產=港險獲客渠道合規紅線再收緊，對內地展業與引流模式影響直接。",
        {"front": {}, "midback": {}, "lead": L("账号摸排点名港险引流=合规红线收紧", "賬號摸排點名港險引流=合規紅線收緊"), "cross": {}},
        {"front": 2, "midback": 2, "lead": 1, "cross": 1},
        "证券时报（金融监管动向）", "zh", ["reg", "tech"], ["marketing", "compliance", "cross-border"],
        ["网络营销新规", "租号", "蓝V", "合规", "港险引流"], ["網絡營銷新規", "租號", "藍V", "合規", "港險引流"],
        "news", "2026-08-10T19:37:00+08:00",
        "https://www.stcn.com/article/detail/4068321.html",
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
