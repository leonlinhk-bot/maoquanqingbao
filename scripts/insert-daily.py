#!/usr/bin/env python3
"""Insert daily collected items into live-items.json"""
import json, sys
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime(2026, 7, 30, 18, 0, 0, tzinfo=HKT)

new_items = [
    {
        "id": "hkma-fed-response-jul30",
        "clusterCount": 1, "score": 88, "verifyStatus": "verified",
        "sourceTier": "official", "sourceKey": "hkma:fed-response-20260730",
        "title": {"sc": "HKMA回应美联储利率决议：维持联系汇率稳定", "tc": "HKMA回應美聯儲利率決議：維持聯繫匯率穩定"},
        "summary": {"sc": "2026年7月30日，香港金管局就美联储利率决策作出回应，重申香港联系汇率制度稳健运行，银行体系流动性充裕。金管局表示将继续密切监察市场变化，确保货币市场有序运作。[EN原文]", "tc": "金管局就聯儲局利率決策作回應，重申聯繫匯率制度穩健，銀行體系流動性充裕。"},
        "why": {"sc": "美联储利率路径直接影响港元利率与保险产品定价", "tc": "美聯儲利率直接影響港元利率與保險定價"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "HKMA", "tc": "HKMA", "lang": "en"},
        "boards": ["reg"], "themes": ["market", "monetary"],
        "tags": {"sc": ["HKMA", "美联储", "利率", "联系汇率"], "tc": ["HKMA", "美聯儲", "利率", "聯繫匯率"]},
        "contentKind": "press", "publishedAt": "2026-07-30T14:30:00+08:00",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260730-4/"
    },
    {
        "id": "mof-rmb-bonds-cmu-jul30",
        "clusterCount": 1, "score": 86, "verifyStatus": "verified",
        "sourceTier": "official", "sourceKey": "hkma:mof-rmb-bonds-20260730",
        "title": {"sc": "财政部在CMU发行人民币国债 巩固香港离岸人民币枢纽", "tc": "財政部在CMU發行人民幣國債 鞏固香港離岸人民幣樞紐"},
        "summary": {"sc": "2026年7月30日，中国财政部通过香港金管局债务工具中央结算系统（CMU）发行人民币国债，进一步巩固香港作为离岸人民币业务枢纽地位。此举有助于丰富香港人民币产品生态，为保险业提供更多优质人民币资产配置选择。[EN原文]", "tc": "財政部經CMU發行人民幣國債，鞏固香港離岸人民幣樞紐，豐富人民幣資產配置。"},
        "why": {"sc": "人民币国债扩容=香港保险业人民币资产配置选项增加", "tc": "人民幣國債擴容=保險業人民幣資產選項增加"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "HKMA", "tc": "HKMA", "lang": "zh+en"},
        "boards": ["market"], "themes": ["bond", "rmb"],
        "tags": {"sc": ["HKMA", "人民币国债", "CMU", "离岸人民币"], "tc": ["HKMA", "人民幣國債", "CMU", "離岸人民幣"]},
        "contentKind": "press", "publishedAt": "2026-07-30T15:00:00+08:00",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260730-3/"
    },
    {
        "id": "hkma-cmu-network-jul29",
        "clusterCount": 1, "score": 85, "verifyStatus": "verified",
        "sourceTier": "official", "sourceKey": "hkma:cmu-network-20260729",
        "title": {"sc": "HKMA欢迎CMU扩展国际网络及服务范围", "tc": "HKMA歡迎CMU擴展國際網絡及服務範圍"},
        "summary": {"sc": "2026年7月29日，香港金管局欢迎债务工具中央结算系统（CMU）扩展国际网络与服务，新增与多个国际中央证券存管机构的连接。此举将提升香港债券市场基础设施的国际化水平，便利跨境债券投资与结算。[EN原文]", "tc": "CMU擴展國際網絡，新增多個ICSD連接，提升香港債券基建國際化水平。"},
        "why": {"sc": "CMU国际化=保险公司跨境债券投资更便利", "tc": "CMU國際化=保險公司跨境債券投資更便利"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "HKMA", "tc": "HKMA", "lang": "en"},
        "boards": ["market"], "themes": ["infrastructure", "bond"],
        "tags": {"sc": ["HKMA", "CMU", "债券市场", "金融基建"], "tc": ["HKMA", "CMU", "債券市場", "金融基建"]},
        "contentKind": "press", "publishedAt": "2026-07-29T16:00:00+08:00",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260729-3/"
    },
    {
        "id": "hkma-quantum-whitepaper-jul27",
        "clusterCount": 1, "score": 85, "verifyStatus": "verified",
        "sourceTier": "official", "sourceKey": "hkma:quantum-whitepaper-20260727",
        "title": {"sc": "HKMA发布量子准备白皮书及指数 推动银行业量子时代转型", "tc": "HKMA發布量子準備白皮書及指數 推動銀行業量子時代轉型"},
        "summary": {"sc": "2026年7月27日，香港金管局发布量子准备白皮书及配套指数，支持银行业为量子计算时代做好准备。白皮书涵盖加密算法迁移、量子风险管理框架等核心议题，保险业可参照其方法论评估自身量子风险敞口。[EN原文]", "tc": "金管局發布量子準備白皮書，涵蓋加密遷移與量子風險管理，保險業可參考評估。"},
        "why": {"sc": "量子计算威胁现有加密体系=保险业数据安全需前瞻布局", "tc": "量子計算威脅加密體系=保險業數據安全需前瞻佈局"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "HKMA", "tc": "HKMA", "lang": "en"},
        "boards": ["tech"], "themes": ["quantum", "cyber"],
        "tags": {"sc": ["HKMA", "量子计算", "白皮书", "网络安全"], "tc": ["HKMA", "量子計算", "白皮書", "網絡安全"]},
        "contentKind": "press", "publishedAt": "2026-07-27T16:30:00+08:00",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260727-3/"
    },
    {
        "id": "hk-premiums-q1-2026-jul25",
        "clusterCount": 1, "score": 82, "verifyStatus": "verified",
        "sourceTier": "pro", "sourceKey": "insurancebusiness:hk-q1-20260725",
        "title": {"sc": "香港保险Q1总保费2916亿港元同比增32.3% 分红业务领涨", "tc": "香港保險Q1總保費2916億港元同比增32.3% 分紅業務領漲"},
        "summary": {"sc": "Insurance Business 2026年7月25日报道：保监局公布2026年Q1临时统计，总保费2916亿港元同比增32.3%。非相连个人业务贡献1353亿（+50.2%），其中分红业务达1257亿（+53.7%）。但内地访客数据连续第五季暂停披露，跨境数据缺口扩大。[EN原文]", "tc": "Q1總保費$2916億同比+32.3%，分紅業務$1257億+53.7%；內地訪客數據連續五季未披露。"},
        "why": {"sc": "Q1数据=全年市场趋势风向标，分红业务增速惊人", "tc": "Q1數據=全年趨勢風向標，分紅業務增速驚人"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "tc": "Insurance Business", "lang": "en"},
        "boards": ["market"], "themes": ["statistics", "growth"],
        "tags": {"sc": ["Q1", "保费", "分红", "统计数据", "内地访客"], "tc": ["Q1", "保費", "分紅", "統計數據", "內地訪客"]},
        "contentKind": "news", "publishedAt": "2026-07-25T14:00:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/hong-kong-insurance-market-extends-growth-run-as-data-gap-widens-583673.aspx"
    },
    {
        "id": "ia-sales-rules-tightening-jul15",
        "clusterCount": 1, "score": 87, "verifyStatus": "pending",
        "sourceTier": "pro", "sourceKey": "insuranceasia:ia-sales-rules-20260715",
        "title": {"sc": "保监局收紧销售规则 高管直接对全流程合规负责", "tc": "保監局收緊銷售規則 高管直接對全流程合規負責"},
        "summary": {"sc": "Insurance Asia报道：香港保监局推出一系列监管更新及执法措施，收紧保险销售行为。7月起实施跨行业背景查核安排覆盖逾11万名中介人；高管对销售全流程合规承担直接责任。此前6月已限制两家经纪公司牌照续期，因其未能有效管理转介业务。[EN原文]", "tc": "保監局收緊銷售規則，跨行業背景查核覆蓋11萬中介人，高管直接對銷售合規負責。"},
        "why": {"sc": "监管从紧+跨行业背景查核=合规成本上升，中介洗牌加速", "tc": "監管從緊+跨行業查核=合規成本上升，中介洗牌加速"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 3, "lead": 2, "cross": 0},
        "source": {"sc": "Insurance Asia", "tc": "Insurance Asia", "lang": "en"},
        "boards": ["reg"], "themes": ["compliance", "intermediary"],
        "tags": {"sc": ["IA", "销售规则", "合规", "背景查核", "中介人"], "tc": ["IA", "銷售規則", "合規", "背景查核", "中介人"]},
        "contentKind": "news", "publishedAt": "2026-07-15T12:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-ia-tightens-sales-rules-misconduct-scrutiny-grows"
    },
    {
        "id": "aia-q1-market-leader-jul24",
        "clusterCount": 1, "score": 80, "verifyStatus": "pending",
        "sourceTier": "insurer", "sourceKey": "aia:q1-leader-20260724",
        "title": {"sc": "友邦香港2026年Q1勇夺7个市场第一 继续领跑", "tc": "友邦香港2026年Q1勇奪7個市場第一 繼續領跑"},
        "summary": {"sc": "2026年7月24日友邦香港公布，根据保监局Q1临时统计数字，公司在有效业务、新造保单等维度勇夺最多市场第一，持续稳居香港保险市场之冠。CEO Alger Fung表示这反映客户信任而非仅是排名。[EN原文]", "tc": "友邦香港Q1奪7個市場第一，CEO馮偉昌表示反映客戶信任。"},
        "why": {"sc": "AIA连续领跑=市场份额格局验证，竞争优势持续", "tc": "AIA連續領跑=市場份額格局驗證"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "AIA HK", "tc": "AIA HK", "lang": "zh"},
        "boards": ["insurer"], "themes": ["market-leader", "quarterly"],
        "tags": {"sc": ["AIA", "友邦", "市场第一", "Q1"], "tc": ["AIA", "友邦", "市場第一", "Q1"]},
        "contentKind": "press", "publishedAt": "2026-07-24T10:00:00+08:00",
        "originalUrl": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2026/aia-press-release-20260724"
    },
    {
        "id": "axa-menopause-survey-jul23",
        "clusterCount": 1, "score": 75, "verifyStatus": "pending",
        "sourceTier": "insurer", "sourceKey": "axa:menopause-survey-20260723",
        "title": {"sc": "AXA安盛调查：香港在职女性更年期认知严重不足", "tc": "AXA安盛調查：香港在職女性更年期認知嚴重不足"},
        "summary": {"sc": "2026年7月23日AXA安盛发布调查，揭示香港在职女性对更年期健康认知普遍不足，多数受访者缺乏相关知识且不知如何获取专业协助。AXA倡导企业加强女性健康保障，呼应其医疗及危疾产品线的市场定位。"},
        "why": {"sc": "女性健康保障缺口=保险公司产品创新与市场教育机会", "tc": "女性健康保障缺口=產品創新與市場教育機會"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "AXA 安盛", "tc": "AXA 安盛", "lang": "zh"},
        "boards": ["insurer"], "themes": ["health", "women"],
        "tags": {"sc": ["AXA", "安盛", "更年期", "女性健康", "调查"], "tc": ["AXA", "安盛", "更年期", "女性健康", "調查"]},
        "contentKind": "press", "publishedAt": "2026-07-23T11:00:00+08:00",
        "originalUrl": "https://www.axa.com.hk/zh/news-room/2026"
    },
    {
        "id": "sunlife-ride-to-shine-jul22",
        "clusterCount": 1, "score": 73, "verifyStatus": "pending",
        "sourceTier": "insurer", "sourceKey": "sunlife:ride-to-shine-20260722",
        "title": {"sc": "Sun Life永明启动「善德永明耀香港」智能单车创举", "tc": "Sun Life永明啟動「善德永明耀香港」智能單車創舉"},
        "summary": {"sc": "2026年7月22日，Sun Life永明与香港善德基金会合作启动Ride-To-Shine Hong Kong智能单车动力创举。活动以全民参与为理念，结合运动科技与社区公益，展现永明在港品牌深耕及ESG承诺。"},
        "why": {"sc": "保司ESG+社区参与=品牌差异化与客户忠诚度建设", "tc": "保司ESG+社區參與=品牌差異化與客戶忠誠度"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "Sun Life 永明", "tc": "Sun Life 永明", "lang": "zh"},
        "boards": ["insurer"], "themes": ["esg", "community"],
        "tags": {"sc": ["Sun Life", "永明", "ESG", "社区公益"], "tc": ["Sun Life", "永明", "ESG", "社區公益"]},
        "contentKind": "press", "publishedAt": "2026-07-22T14:00:00+08:00",
        "originalUrl": "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/ride-to-shine-hong-kong/"
    },
    {
        "id": "allianz-hsbc-singapore-jul24",
        "clusterCount": 1, "score": 82, "verifyStatus": "verified",
        "sourceTier": "media", "sourceKey": "reuters:allianz-hsbc-20260724",
        "title": {"sc": "安联21亿美元收购汇丰新加坡寿险 亚洲版图再扩张", "tc": "安聯21億美元收購滙豐新加坡壽險 亞洲版圖再擴張"},
        "summary": {"sc": "2026年7月24日Reuters报道：汇丰同意以27亿新加坡元（约21亿美元）将新加坡人寿及健康保险业务售予安联。汇丰将继续聚焦亚洲财富管理及批发银行业务，安联则进一步巩固亚太保险版图。交易含15年独家银保合作。[EN原文]", "tc": "滙豐$21億售新加坡壽險予安聯，含15年獨家銀保合作。"},
        "why": {"sc": "安联-汇丰交易=亚洲保险市场并购活跃信号，银保渠道价值凸显", "tc": "安聯-滙豐交易=亞洲保險併購活躍，銀保渠道價值凸顯"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 2, "cross": 0},
        "source": {"sc": "Reuters", "tc": "Reuters", "lang": "en"},
        "boards": ["market"], "themes": ["ma", "bancassurance"],
        "tags": {"sc": ["安联", "汇丰", "收购", "新加坡", "银保"], "tc": ["安聯", "滙豐", "收購", "新加坡", "銀保"]},
        "contentKind": "news", "publishedAt": "2026-07-24T08:00:00+08:00",
        "originalUrl": "https://www.reuters.com/world/asia-pacific/hsbc-sells-singapore-insurance-business-germanys-allianz-209-billion-deal-2026-07-23/"
    },
    {
        "id": "ia-ai-cohort-new-insurers-jul",
        "clusterCount": 1, "score": 80, "verifyStatus": "pending",
        "sourceTier": "pro", "sourceKey": "insurancebusiness:ia-ai-cohort-202607",
        "title": {"sc": "保监局AI Cohort新增三家保险公司 中银人寿、国寿海外等加入", "tc": "保監局AI Cohort新增三家保險公司 中銀人壽、國壽海外等加入"},
        "summary": {"sc": "Insurance Business报道：香港保监局AI Cohort Programme迎来第三批成员，新增中银集团人寿、中国人寿（海外）及另一家保险公司。该计划旨在推动保险业人工智能应用，此前已在Cyberport举办AI Cohort Symposium 2026。[EN原文]", "tc": "保監局AI Cohort新增中銀人壽、國壽海外等三家，推動保險AI應用。"},
        "why": {"sc": "AI监管沙盒扩容=保险科技合规创新加速", "tc": "AI監管沙盒擴容=保險科技合規創新加速"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "tc": "Insurance Business", "lang": "en"},
        "boards": ["tech"], "themes": ["ai", "insurtech"],
        "tags": {"sc": ["IA", "AI Cohort", "中银人寿", "国寿海外", "InsurTech"], "tc": ["IA", "AI Cohort", "中銀人壽", "國壽海外", "InsurTech"]},
        "contentKind": "news", "publishedAt": "2026-07-28T10:00:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/insurance-authority-adds-three-insurers-to-ai-cohort-programme-579133.aspx"
    },
    {
        "id": "nfra-shanghai-reins-center-jul07",
        "clusterCount": 1, "score": 84, "verifyStatus": "verified",
        "sourceTier": "official", "sourceKey": "nfra:shanghai-reins-20260707",
        "title": {"sc": "金融监管总局发布加快上海国际再保险中心建设措施", "tc": "金融監管總局發布加快上海國際再保險中心建設措施"},
        "summary": {"sc": "2026年7月7日，国家金融监督管理总局联合上海市政府印发《加快上海国际再保险中心建设的若干措施》，提出包括税收优惠、跨境再保险便利化、机构集聚等一揽子政策。此举将深化上海与香港再保险市场的竞合关系，影响亚洲再保险版图。"},
        "why": {"sc": "上海再保中心=香港再保险竞争优势与分流效应需关注", "tc": "上海再保中心=香港再保險競爭需關注"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 2, "cross": 1},
        "source": {"sc": "NFRA", "tc": "國家金融監管總局", "lang": "zh"},
        "boards": ["reg"], "themes": ["reinsurance", "greater-bay"],
        "tags": {"sc": ["NFRA", "上海", "再保险", "政策"], "tc": ["NFRA", "上海", "再保險", "政策"]},
        "contentKind": "circular", "publishedAt": "2026-07-07T09:00:00+08:00",
        "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1263701&itemId=928"
    },
    {
        "id": "nfra-cybersecurity-rules-jul",
        "clusterCount": 1, "score": 83, "verifyStatus": "pending",
        "sourceTier": "official", "sourceKey": "nfra:cyber-rules-202607",
        "title": {"sc": "金融监管总局就银行业保险业网络安全管理办法征求意见", "tc": "金融監管總局就銀行業保險業網絡安全管理辦法徵求意見"},
        "summary": {"sc": "国家金融监督管理总局近日就《银行业保险业网络安全管理办法（征求意见稿）》公开征求意见，涵盖网络安全管理体系、数据安全、应急响应等要求。该办法将统一银行保险业网络安全监管标准，对保险公司IT治理提出更高合规要求。"},
        "why": {"sc": "网络安全管理升级=保险公司IT合规投入将增加", "tc": "網絡安全管理升級=保險公司IT合規投入增加"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 0},
        "source": {"sc": "NFRA", "tc": "國家金融監管總局", "lang": "zh"},
        "boards": ["reg"], "themes": ["cyber", "compliance"],
        "tags": {"sc": ["NFRA", "网络安全", "管理办法", "征求意见"], "tc": ["NFRA", "網絡安全", "管理辦法", "徵求意見"]},
        "contentKind": "circular", "publishedAt": "2026-07-25T09:00:00+08:00",
        "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1264203&itemId=915"
    },
    {
        "id": "prudential-health-summit-2026",
        "clusterCount": 1, "score": 76, "verifyStatus": "pending",
        "sourceTier": "insurer", "sourceKey": "prudential:health-summit-2026",
        "title": {"sc": "保诚保险举办2026健康论坛 聚焦优化患者医疗体验", "tc": "保誠保險舉辦2026健康論壇 聚焦優化患者醫療體驗"},
        "summary": {"sc": "保诚保险于2026年举办健康论坛「优化患者医疗体验」，汇聚医疗界资深领袖与健康合作伙伴，探讨如何深化合作，为患者提供更清晰的指引及全面支持。此前保诚已扩展癌症直付服务至指定肿瘤中心，持续强化健康保障生态。"},
        "why": {"sc": "保司健康生态布局=从理赔者向健康管理伙伴转型", "tc": "保司健康生態佈局=從理賠者轉向健康管理夥伴"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "Prudential 保诚", "tc": "Prudential 保誠", "lang": "zh"},
        "boards": ["insurer"], "themes": ["health", "ecosystem"],
        "tags": {"sc": ["保诚", "健康论坛", "患者体验", "健康管理"], "tc": ["保誠", "健康論壇", "患者體驗", "健康管理"]},
        "contentKind": "press", "publishedAt": "2026-07-24T10:00:00+08:00",
        "originalUrl": "https://www.prudential.com.hk/tc/about-us/newsroom/prudential-health-summit-improving-care-for-every-patient/"
    },
    {
        "id": "manulife-asian-care-survey-2026",
        "clusterCount": 1, "score": 75, "verifyStatus": "pending",
        "sourceTier": "insurer", "sourceKey": "manulife:asia-care-2026",
        "title": {"sc": "宏利2026亚洲关怀调查：84%港人重视晚年独立自主", "tc": "宏利2026亞洲關懷調查：84%港人重視晚年獨立自主"},
        "summary": {"sc": "宏利2026年亚洲关怀调查显示，84%香港受访者将独立自主（不依赖他人的能力）视为重要人生目标。调查结果反映港人对退休规划、长期护理保障的需求持续升温，为保险公司年金及长期护理产品开发提供市场洞察。"},
        "why": {"sc": "老龄化+独立自主诉求=年金/长期护理产品需求确定性", "tc": "老齡化+獨立自主=年金/長期護理產品需求確定"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "Manulife 宏利", "tc": "Manulife 宏利", "lang": "zh"},
        "boards": ["market"], "themes": ["retirement", "consumer"],
        "tags": {"sc": ["宏利", "亚洲关怀调查", "退休规划", "独立自主"], "tc": ["宏利", "亞洲關懷調查", "退休規劃", "獨立自主"]},
        "contentKind": "news", "publishedAt": "2026-07-26T10:00:00+08:00",
        "originalUrl": "https://www.manulife.com.hk/en/individual/promotions/asia-care-survey-2026.html"
    }
]

# Load existing JSON
with open("data/live-items.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Check for duplicates
existing_ids = {item["id"] for item in data["items"]}
existing_source_keys = {item.get("sourceKey", "") for item in data["items"]}

filtered = []
for item in new_items:
    if item["id"] in existing_ids:
        print(f"SKIP (dup id): {item['id']}")
        continue
    if item.get("sourceKey", "") in existing_source_keys:
        print(f"SKIP (dup sourceKey): {item['sourceKey']}")
        continue
    item["ingestedAt"] = NOW.isoformat()
    item["contentRole"] = {"sc": "本站导读", "tc": "本站導讀"}
    item["featured"] = False
    item["evergreen"] = False
    filtered.append(item)

# Prepend to items
data["items"] = filtered + data["items"]

# Update meta
data["meta"]["generatedAt"] = NOW.isoformat()
data["meta"]["itemCount"] = len(data["items"])
data["meta"]["windowNote"] = {
    "sc": f"本库{len(data['items'])}条。今日新增{len(filtered)}条。",
    "tc": f"本庫{len(data['items'])}條。今日新增{len(filtered)}條。"
}
data["meta"]["asOf"] = "2026-07-30"

# Write back
with open("data/live-items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Inserted {len(filtered)} new items. Total: {len(data['items'])}")
for item in filtered:
    print(f"  + {item['id']} [{item['sourceTier']}] {item['title']['sc'][:50]}")
