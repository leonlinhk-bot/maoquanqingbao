#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日增量采集 2026-08-27: 插入新条目到 live-items.json 最前, 更新 meta"""
import json, datetime

NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
NOW_STR = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

NEW_ITEMS = [
    {
        "id": "hkma-genai-sandbox-cohort-20260827",
        "clusterCount": 1,
        "score": 90,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "hkma",
        "title": {
            "sc": "金管局联同证监会、保监局及积金局公布「生成式人工智能沙盒++」首批36个用例 [EN原文]",
            "tc": "金管局聯同證監會、保監局及積金局公佈「生成式人工智能沙盒++」首批36個用例 [EN原文]"
        },
        "summary": {
            "sc": "金管局联同证监会、保监局及积金局公布「生成式人工智能沙盒++」首批36个用例：从近100份申请中甄选，涉30家金融机构及27家科技伙伴，聚焦代理式AI应用，评审以创新性、技术复杂度及行业价值为准则。",
            "tc": "金管局聯同證監會、保監局及積金局公佈「生成式人工智能沙盒++」首批36個用例：從近100份申請中甄選，涉30家金融機構及27家科技夥伴，聚焦代理式AI應用，評審以創新性、技術複雜度及行業價值為準則。"
        },
        "why": {
            "sc": "四监管机构联手推动金融业GenAI落地，代理式AI成主旋律；保险机构参与其中，是观察港险AI合规试点与科技生态合作的关键窗口。",
            "tc": "四監管機構聯手推動金融業GenAI落地，代理式AI成主旋律；保險機構參與其中，是觀察港險AI合規試點與科技生態合作的關鍵窗口。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "跟进GenAI监管试点动向", "tc": "跟進GenAI監管試點動向"},
            "lead": {},
            "cross": {"sc": "关注保险机构入选用例与科技伙伴生态", "tc": "關注保險機構入選用例與科技夥伴生態"}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 1},
        "source": {"sc": "香港金融管理局 HKMA", "lang": "en"},
        "boards": ["tech", "reg"],
        "themes": ["ai", "insurtech"],
        "tags": {"sc": ["GenAI", "沙盒", "金管局", "代理式AI"], "tc": ["GenAI", "沙盒", "金管局", "代理式AI"]},
        "contentKind": "press",
        "publishedAt": "2026-08-27",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260827-3/",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "hkma-hkicl-fraud-alert-20260826",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "hkma",
        "title": {
            "sc": "香港银行同业结算公司再揭两假冒网站 仿「买家网上保障」骗FPS用户 [EN原文]",
            "tc": "香港銀行同業結算公司再揭兩假冒網站 仿「買家網上保障」騙FPS用戶 [EN原文]"
        },
        "summary": {
            "sc": "香港银行同业结算公司(HKICL)发现两个假冒网站仿冒「买家网上保障」，以退款、交易报告及支援为饵，诱FPS用户交出身份证件、电话及银行账户资料，并引导联络冒充客服的骗徒。HKICL提醒公众警觉并举报。",
            "tc": "香港銀行同業結算公司(HKICL)發現兩個假冒網站仿冒「買家網上保障」，以退款、交易報告及支援為餌，誘FPS用戶交出身份證件、電話及銀行賬戶資料，並引導聯絡冒充客服的騙徒。HKICL提醒公眾警覺並舉報。"
        },
        "why": {
            "sc": "继8月25日警示后再曝新仿冒网站，FPS钓鱼手法持续升级；转数快及跨境缴费用户风险上升，宜纳入客户防诈提示与渠道风控关注。",
            "tc": "繼8月25日警示後再曝新仿冒網站，FPS釣魚手法持續升級；轉數快及跨境繳費用戶風險上升，宜納入客戶防詐提示與渠道風控關注。"
        },
        "actions": {
            "front": {"sc": "客户防诈提醒素材", "tc": "客戶防詐提醒素材"},
            "midback": {"sc": "缴费环节风控关注", "tc": "繳費環節風控關注"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "香港金融管理局 HKMA", "lang": "en"},
        "boards": ["market"],
        "themes": ["fraud", "cyber"],
        "tags": {"sc": ["HKICL", "FPS", "假冒网站", "防诈"], "tc": ["HKICL", "FPS", "假冒網站", "防詐"]},
        "contentKind": "press",
        "publishedAt": "2026-08-26",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260826-5/",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "hkma-bank-scam-alert-20260826",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "hkma",
        "title": {
            "sc": "金管局汇总四银行诈骗警示：假冒网站及网银登入画面 [EN原文]",
            "tc": "金管局匯總四銀行詐騙警示：假冒網站及網銀登入畫面 [EN原文]"
        },
        "summary": {
            "sc": "金管局提醒公众留意东亚银行、创兴银行、上海商业银行及交通银行(香港)发出的警示，涉及假冒网站及网上银行登入画面。金管局重申银行不会经短信或电邮附连结引导客户交易，亦不会索取敏感资料，遇可疑应即举报。",
            "tc": "金管局提醒公眾留意東亞銀行、創興銀行、上海商業銀行及交通銀行(香港)發出的警示，涉及假冒網站及網上銀行登入畫面。金管局重申銀行不會經短信或電郵附連結引導客戶交易，亦不會索取敏感資料，遇可疑應即舉報。"
        },
        "why": {
            "sc": "银行假冒网站与钓鱼登入画面集中出现，反映针对本港零售银行的网络攻击活跃；保险缴费、转账环节的客户教育可同步引用。",
            "tc": "銀行假冒網站與釣魚登入畫面集中出現，反映針對本港零售銀行的網絡攻擊活躍；保險繳費、轉賬環節的客戶教育可同步引用。"
        },
        "actions": {
            "front": {"sc": "客户防诈提醒素材", "tc": "客戶防詐提醒素材"},
            "midback": {},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "香港金融管理局 HKMA", "lang": "en"},
        "boards": ["market"],
        "themes": ["fraud", "cyber"],
        "tags": {"sc": ["金管局", "假冒网站", "钓鱼", "防诈"], "tc": ["金管局", "假冒網站", "釣魚", "防詐"]},
        "contentKind": "press",
        "publishedAt": "2026-08-26",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260826-4/",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "hkma-north-metro-taskforce-20260826",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "hkma",
        "title": {
            "sc": "北部都会区金融咨询专责小组举行第二次会议 探讨多元融资模式 [EN原文]",
            "tc": "北部都會區金融諮詢專責小組舉行第二次會議 探討多元融資模式 [EN原文]"
        },
        "summary": {
            "sc": "金管局与银行公会合办的北部都会区金融咨询专责小组举行第二次会议，探讨银行业以多元融资模式支持北都项目。财库局在会上介绍政府多元发展模式，包括设立产业园区公司参与开发营运，以及透过公私合营(PPP)引导市场力量加速推进。",
            "tc": "金管局與銀行公會合辦的北部都會區金融諮詢專責小組舉行第二次會議，探討銀行業以多元融資模式支持北都項目。財庫局在會上介紹政府多元發展模式，包括設立產業園區公司參與開發營運，以及透過公私營(PPP)引導市場力量加速推進。"
        },
        "why": {
            "sc": "北都发展牵动跨境金融与保险配套需求（工程险、融资保险、家族办公室布局），银行融资模式动向值得港险跨境团队跟进。",
            "tc": "北都發展牽動跨境金融與保險配套需求（工程險、融資保險、家族辦公室佈局），銀行融資模式動向值得港險跨境團隊跟進。"
        },
        "actions": {
            "front": {},
            "midback": {},
            "lead": {},
            "cross": {"sc": "关注北都基建融资与保险配套机会", "tc": "關注北都基建融資與保險配套機會"}
        },
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 1},
        "source": {"sc": "香港金融管理局 HKMA", "lang": "en"},
        "boards": ["macro", "reg"],
        "themes": ["capital", "cross-border"],
        "tags": {"sc": ["北部都会区", "融资", "金管局", "PPP"], "tc": ["北部都會區", "融資", "金管局", "PPP"]},
        "contentKind": "press",
        "publishedAt": "2026-08-26",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260826-3/",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "iaa-fwd-h1-profit-20260826",
        "clusterCount": 1,
        "score": 75,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "富卫集团上半年净利润增3倍至1.72亿美元创新高 四大分部齐增长 [EN原文]",
            "tc": "富衛集團上半年淨利潤增3倍至1.72億美元創新高 四大分部齊增長 [EN原文]"
        },
        "summary": {
            "sc": "富卫集团公布2026年上半年业绩：净利润1.72亿美元，按年增约3倍创纪录；新业务销售升7%至13.5亿美元，新业务合约服务边际升25%至9.96亿美元。香港澳门、泰国柬埔寨、日本及拓展市场四大分部均正增长，偿付能力比率203%。",
            "tc": "富衛集團公佈2026年上半年業績：淨利潤1.72億美元，按年增約3倍創紀錄；新業務銷售升7%至13.5億美元，新業務合約服務邊際升25%至9.96億美元。香港澳門、泰國柬埔寨、日本及拓展市場四大分部均正增長，償付能力比率203%。"
        },
        "why": {
            "sc": "富卫上市后首个完整半年报，香港澳门分部领跑；新业务CSM与盈利质量同步改善，是观察港险竞争格局与上市险企估值的重要样本。",
            "tc": "富衛上市後首個完整半年報，香港澳門分部領跑；新業務CSM與盈利質量同步改善，是觀察港險競爭格局與上市險企估值的重要樣本。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "同业业绩对标", "tc": "同業業績對標"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "InsuranceAsia", "lang": "en"},
        "boards": ["insurer", "market"],
        "themes": ["results", "market"],
        "tags": {"sc": ["富卫", "FWD", "中期业绩", "净利润"], "tc": ["富衛", "FWD", "中期業績", "淨利潤"]},
        "contentKind": "news",
        "publishedAt": "2026-08-26T05:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/fwd-profit-triples-record-172m-in-h1-2026",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "iaa-manulife-ai-drive-20260826",
        "clusterCount": 1,
        "score": 73,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "宏利亚洲CEO：以AI驱动健康与财富业务 目标2027年AI创造超10亿美元价值 [EN原文]",
            "tc": "宏利亞洲CEO：以AI驅動健康與財富業務 目標2027年AI創造超10億美元價值 [EN原文]"
        },
        "summary": {
            "sc": "宏利亚洲总裁兼CEO Steve Finch称，集团把AI转型列为核心战略，目标2027年亚洲贡献集团核心盈利一半。宏利已在香港推出全天候双语AI客服助理，全球91个生成式AI用例投产、121个开发中，并以AI提升代理生产力与核保处理效率。",
            "tc": "宏利亞洲總裁兼CEO Steve Finch稱，集團把AI轉型列為核心戰略，目標2027年亞洲貢獻集團核心盈利一半。宏利已在香港推出全天候雙語AI客服助理，全球91個生成式AI用例投產、121個開發中，並以AI提升代理生產力與核保處理效率。"
        },
        "why": {
            "sc": "港险头部公司AI落地全景：客户服务、代理生产力、核保三大场景；对同业AI投入与渠道效率对标有直接参考价值。",
            "tc": "港險頭部公司AI落地全景：客戶服務、代理生產力、核保三大場景；對同業AI投入與渠道效率對標有直接參考價值。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "AI投入与渠道效率对标", "tc": "AI投入與渠道效率對標"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "InsuranceAsia", "lang": "en"},
        "boards": ["tech", "insurer"],
        "themes": ["ai", "insurtech"],
        "tags": {"sc": ["宏利", "Manulife", "AI", "代理生产力"], "tc": ["宏利", "Manulife", "AI", "代理生產力"]},
        "contentKind": "news",
        "publishedAt": "2026-08-26T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/exclusive/manulife-asia-pushes-ai-drive-health-wealth-growth",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "iaa-china-nonmotor-moodys-20260827",
        "clusterCount": 1,
        "score": 68,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "穆迪：中国非车险新规见效或慢于车险 产品多元市场复杂拖累 [EN原文]",
            "tc": "穆迪：中國非車險新規見效或慢於車險 產品多元市場複雜拖累 [EN原文]"
        },
        "summary": {
            "sc": "穆迪评级认为，金融监管总局针对非车险市场的新规属信用正面，有望强化产品治理、市场行为及中介监管，并改善非车险承保盈利；但非车险产品跨度大、市场动态更复杂，改善速度或慢于车险板块。",
            "tc": "穆迪評級認為，金融監管總局針對非車險市場的新規屬信用正面，有望強化產品治理、市場行為及中介監管，並改善非車險承保盈利；但非車險產品跨度大、市場動態更複雜，改善速度或慢於車險板塊。"
        },
        "why": {
            "sc": "内地非车险监管趋严，直接影响港险公司内地布局、再保与投资环境；穆迪视角供跨境业务与风控团队参考。",
            "tc": "內地非車險監管趨嚴，直接影響港險公司內地佈局、再保與投資環境；穆迪視角供跨境業務與風控團隊參考。"
        },
        "actions": {
            "front": {},
            "midback": {},
            "lead": {},
            "cross": {"sc": "关注内地非车险监管传导", "tc": "關注內地非車險監管傳導"}
        },
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 1},
        "source": {"sc": "InsuranceAsia", "lang": "en"},
        "boards": ["reg", "market"],
        "themes": ["china", "reg"],
        "tags": {"sc": ["穆迪", "非车险", "金融监管总局", "承保盈利"], "tc": ["穆迪", "非車險", "金融監管總局", "承保盈利"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T05:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/china-non-motor-reforms-face-slower-payoff-moodys",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "iaa-taiwan-spillover-20260826",
        "clusterCount": 1,
        "score": 62,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "台湾外溢效应保单上半年新单保费暴增152% [EN原文]",
            "tc": "台灣外溢效應保單上半年新單保費暴增152% [EN原文]"
        },
        "summary": {
            "sc": "台湾金管会数据显示，2026年上半年外溢效应保单新契约保费收入按年大增152%至15.3亿美元，15家寿险公司共338款产品获核准；新契约件数74.6万件、升29%，实物给付保单件数则跌5%。",
            "tc": "台灣金管會數據顯示，2026年上半年外溢效應保單新契約保費收入按年大增152%至15.3億美元，15家壽險公司共338款產品獲核准；新契約件數74.6萬件、升29%，實物給付保單件數則跌5%。"
        },
        "why": {
            "sc": "外溢保单（健康行为挂钩）在台湾爆发式增长，与港险健康生活类产品同源，可作产品创新与客群运营参考。",
            "tc": "外溢保單（健康行為掛鉤）在台灣爆發式增長，與港險健康生活類產品同源，可作產品創新與客群運營參考。"
        },
        "actions": {
            "front": {},
            "midback": {},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "InsuranceAsia", "lang": "en"},
        "boards": ["product", "market"],
        "themes": ["product", "health"],
        "tags": {"sc": ["外溢保单", "台湾", "健康险", "金管会"], "tc": ["外溢保單", "台灣", "健康險", "金管會"]},
        "contentKind": "news",
        "publishedAt": "2026-08-26T07:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/taiwan-spillover-effect-premiums-surge-152",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-prudential-h1-20260827",
        "clusterCount": 1,
        "score": 72,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "保诚上半年新业务利润增8%至13.8亿美元 银保渠道成增长引擎 [EN原文]",
            "tc": "保誠上半年新業務利潤增8%至13.8億美元 銀保渠道成增長引擎 [EN原文]"
        },
        "summary": {
            "sc": "保诚公布2026年上半年业绩：新业务利润13.8亿美元，按固定汇率计增8%，新业务利润率扩2个百分点至40%，所有主要市场均正增长；东盟新业务利润升13%，银保渠道表现突出，集团正以科技与AI提升代理生产力。",
            "tc": "保誠公佈2026年上半年業績：新業務利潤13.8億美元，按固定匯率計增8%，新業務利潤率擴2個百分點至40%，所有主要市場均正增長；東盟新業務利潤升13%，銀保渠道表現突出，集團正以科技與AI提升代理生產力。"
        },
        "why": {
            "sc": "保诚为港险市场核心玩家，中期业绩含香港市场信号；银保渠道贡献与AI提升代理效率的路径值得对标。",
            "tc": "保誠為港險市場核心玩家，中期業績含香港市場信號；銀保渠道貢獻與AI提升代理效率的路徑值得對標。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "同业业绩对标", "tc": "同業業績對標"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["insurer", "market"],
        "themes": ["results", "channel"],
        "tags": {"sc": ["保诚", "Prudential", "中期业绩", "银保渠道"], "tc": ["保誠", "Prudential", "中期業績", "銀保渠道"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T15:08:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/prudential-posts-8-new-business-profit-growth--the-bancassurance-channel-drove-it-587680.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-guy-carpenter-pacific-ceo-20260827",
        "clusterCount": 1,
        "score": 66,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "Guy Carpenter委任Justin Ward为太平洋区CEO 再保费率市场转趋买方 [EN原文]",
            "tc": "Guy Carpenter委任Justin Ward為太平洋區CEO 再保費率市場轉趨買方 [EN原文]"
        },
        "summary": {
            "sc": "Marsh旗下再保经纪Guy Carpenter宣布委任Justin Ward为太平洋区CEO，即日生效。任命正值市场转趋买方主导：Howden Re数据显示澳新无损再保业务7月续转费率下调10%-15%，全球承保能力充裕、再保商盈利持续。",
            "tc": "Marsh旗下再保經紀Guy Carpenter宣佈委任Justin Ward為太平洋區CEO，即日生效。任命正值市場轉趨買方主導：Howden Re數據顯示澳新無損再保業務7月續轉費率下調10%-15%，全球承保能力充裕、再保商盈利持續。"
        },
        "why": {
            "sc": "再保费率下行信号明确，直接影响港险分保成本与产品定价空间；再保经纪人事变动亦是行业风向标。",
            "tc": "再保費率下行信號明確，直接影響港險分保成本與產品定價空間；再保經紀人事變動亦是行業風向標。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "再保成本与定价关注", "tc": "再保成本與定價關注"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["market", "firm"],
        "themes": ["reinsurance", "pricing"],
        "tags": {"sc": ["Guy Carpenter", "再保", "人事任命", "费率"], "tc": ["Guy Carpenter", "再保", "人事任命", "費率"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T14:00:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/guy-carpenter-appoints-new-pacific-ceo-for-reinsurance-broking-587670.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-prudential-ipamc-sale-20260826",
        "clusterCount": 1,
        "score": 65,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "保诚拟出售ICICI保诚资管最多2%股权 套现约3.11亿至3.27亿美元 [EN原文]",
            "tc": "保誠擬出售ICICI保誠資管最多2%股權 套現約3.11億至3.27億美元 [EN原文]"
        },
        "summary": {
            "sc": "保诚8月26日宣布，子公司PCHL将于8月27日经公开市场出售所持ICICI保诚资产管理最多2%股权，作价较收市价折让2%-7%，预计套现3.11亿至3.27亿美元；完成后保诚仍持32.6%，治理权利不变，市场视为合规节奏而非战略撤退。",
            "tc": "保誠8月26日宣佈，子公司PCHL將於8月27日經公開市場出售所持ICICI保誠資產管理最多2%股權，作價較收市價折讓2%-7%，預計套現3.11億至3.27億美元；完成後保誠仍持32.6%，治理權利不變，市場視為合規節奏而非戰略撤退。"
        },
        "why": {
            "sc": "外资险企减持印度资管股权属合规调整样本；对关注保诚资本动作与亚洲资产布局的读者有跟踪价值。",
            "tc": "外資險企減持印度資管股權屬合規調整樣本；對關注保誠資本動作與亞洲資產佈局的讀者有跟蹤價值。"
        },
        "actions": {
            "front": {},
            "midback": {},
            "lead": {},
            "cross": {"sc": "关注保诚亚洲资本动作", "tc": "關注保誠亞洲資本動作"}
        },
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 1},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["insurer", "cross"],
        "themes": ["firm", "capital"],
        "tags": {"sc": ["保诚", "ICICI", "股权出售", "印度"], "tc": ["保誠", "ICICI", "股權出售", "印度"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T00:59:54+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/prudentials-327-million-ipamc-sale-is-a-compliance-event-not-a-retreat-587610.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]

def main():
    path = 'data/live-items.json'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    items = data['items']
    existing_ids = {it.get('id') for it in items}
    dup = [it['id'] for it in NEW_ITEMS if it['id'] in existing_ids]
    if dup:
        print('SKIP duplicates:', dup)
    fresh = [it for it in NEW_ITEMS if it['id'] not in existing_ids]
    # dedup by (sourceKey, title.sc)
    titles = {(it.get('sourceKey'), it.get('title', {}).get('sc')) for it in items}
    fresh = [it for it in fresh if (it.get('sourceKey'), it.get('title', {}).get('sc')) not in titles]
    items[:0] = fresh
    data['items'] = items
    meta = data['meta']
    meta['itemCount'] = len(items)
    meta['generatedAt'] = NOW_STR
    meta['windowNote'] = {
        "sc": f"本库{len(items)}条。",
        "tc": f"本庫{len(items)}條。"
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'新增 {len(fresh)} 条 -> 总条数 {len(items)}')
    for it in fresh:
        print(' +', it['id'])

if __name__ == '__main__':
    main()
