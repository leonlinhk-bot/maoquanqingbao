#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 18:08 增量：插入 9 条（10-27 00:31 之后新发）"""
import json
import datetime

NOW = datetime.datetime.now().astimezone()
INGEST = NOW.isoformat(timespec='seconds')
PATH = 'data/live-items.json'

new_items = [
    {
        "id": "ibm-hk-broker-wealth-gap-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/hong-kong-broker-channel-dominates-as-wealth-planning-gaps-grow-594958.aspx",
        "sourceKey": "insurancebusinessmag",
        "sourceTier": "media",
        "score": 74,
        "boards": ["market", "family"],
        "themes": ["经纪渠道", "财富传承", "新造保费"],
        "title": {
            "sc": "香港中介渠道主导新造　85%想传承仅10%有书面计划",
            "tc": "香港中介渠道主導新造　85%想傳承僅10%有書面計劃"
        },
        "summary": {
            "sc": "永明香港上半年新造 APE 73 亿港元、同比升 44%，其中经纪渠道 50.31 亿升 34% 居市场首位，代理 14.45 亿升 48%、银保 5.93 亿升 65%。集团亚洲调查指香港 85% 受访者想传承财富，仅 10% 已写书面计划并告知继承人。[EN原文]",
            "tc": "永明香港上半年新造 APE 73 億港元、同比升 44%，其中經紀渠道 50.31 億升 34% 居市場首位，代理 14.45 億升 48%、銀保 5.93 億升 65%。集團亞洲調查指香港 85% 受訪者想傳承財富，僅 10% 已寫書面計劃並告知繼承人。[EN原文]"
        },
        "why": {
            "sc": "经纪渠道既是最大增量，也是最容易被「去中介」叙事动摇的一环——这条用同一组 IA 临时统计说明经纪仍占主导。客户「有意图、无计划」正是顾问可切入的位置，谈传承别停在产品收益，落到书面计划与继承人沟通。",
            "tc": "經紀渠道既是最大增量，也是最容易被「去中介」敘事動搖的一環——這條用同一組 IA 臨時統計說明經紀仍佔主導。客戶「有意圖、無計劃」正是顧問可切入的位置，談傳承別停在產品收益，落到書面計劃與繼承人溝通。"
        },
        "tags": {
            "sc": ["经纪渠道", "财富传承", "新造保费", "永明"],
            "tc": ["經紀渠道", "財富傳承", "新造保費", "永明"]
        },
        "actions": {
            "front": {"sc": "客户沟通：传承计划缺口", "tc": "客戶溝通：傳承計劃缺口"},
            "midback": {"sc": "研究：渠道结构变化", "tc": "研究：渠道結構變化"},
            "lead": {"sc": "团队简报：经纪价值证据", "tc": "團隊簡報：經紀價值證據"},
            "cross": {"sc": "跨境高客传承", "tc": "跨境高客傳承"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 3, "cross": 2},
        "source": {"sc": "Insurance Business Asia 2026-10-27", "tc": "Insurance Business Asia 2026-10-27",
                   "name": "insurancebusinessmag", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "iasia-hkmc-mortgage-insurance-155b-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "stats",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27T12:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/news/hkmc-mortgage-insurance-loans-decline-155b-in-h1",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 70,
        "boards": ["market", "product"],
        "themes": ["按揭保险", "楼市", "按证局"],
        "title": {
            "sc": "按保上半年新取用贷款 155 亿　跌约 11%、七成三涉二手楼",
            "tc": "按保上半年新取用貸款 155 億　跌約 11%、七成三涉二手樓"
        },
        "summary": {
            "sc": "香港按证保险中期业绩：上半年按保新取用贷款 155 亿港元，较去年同期 175 亿跌约 11%；其中约 73% 为二手市场物业。期内购入贷款资产 29 亿（去年同期 27 亿），「百分百担保」类计划贷款升至 1.15 亿，6 月底贷款组合余额 741 亿。[EN原文]",
            "tc": "香港按證保險中期業績：上半年按保新取用貸款 155 億港元，較去年同期 175 億跌約 11%；其中約 73% 為二手市場物業。期內購入貸款資產 29 億（去年同期 27 億），「百分百擔保」類計劃貸款升至 1.15 億，6 月底貸款組合餘額 741 億。[EN原文]"
        },
        "why": {
            "sc": "按保是楼市成交量与首次置业杠杆的同步指标：新取用贷款跌 11%，说明交投仍在低位、靠二手支撑。跟客户谈按揭与保障配置顺序时，这组数是现成的市场背景，不必凭感觉描述楼市。",
            "tc": "按保是樓市成交量與首次置業槓桿的同步指標：新取用貸款跌 11%，說明交投仍在低位、靠二手支撐。跟客戶談按揭與保障配置順序時，這組數是現成的市場背景，不必憑感覺描述樓市。"
        },
        "tags": {
            "sc": ["按揭保险", "楼市", "按证局", "首次置业"],
            "tc": ["按揭保險", "樓市", "按證局", "首次置業"]
        },
        "actions": {
            "front": {"sc": "客户沟通：按揭与保障顺序", "tc": "客戶溝通：按揭與保障順序"},
            "midback": {"sc": "研究：楼市杠杆水平", "tc": "研究：樓市槓桿水平"},
            "lead": {"sc": "团队简报：市场背景数据", "tc": "團隊簡報：市場背景數據"},
            "cross": {"sc": "跨境置业融资", "tc": "跨境置業融資"}
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia 2026-10-27", "tc": "Insurance Asia 2026-10-27",
                   "name": "insuranceasia", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "iasia-liberty-hk-ceo-sze-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27T05:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/exclusive/executive-hot-seat-cynthia-sze-ceo-liberty-hong-kong",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 66,
        "boards": ["insurer"],
        "themes": ["高管观点", "业务整合", "AI应用"],
        "title": {
            "sc": "Liberty 香港 CEO：个人险与特殊险已并成一家　AI 不替代人的判断",
            "tc": "Liberty 香港 CEO：個人險與特殊險已併成一家　AI 不替代人的判斷"
        },
        "summary": {
            "sc": "Liberty International Insurance 香港 CEO 施（Cynthia Sze）5 月上任后受访，指市场仍以为个人与中小企险、特殊险是两盘生意各自为政，实际已整合为单一持牌实体。她谈跨境融合带来的新风险、AI 在核保与理赔流程的角色，以及减少纸本流程的进度。[EN原文]",
            "tc": "Liberty International Insurance 香港 CEO 施（Cynthia Sze）5 月上任後受訪，指市場仍以為個人與中小企險、特殊險是兩盤生意各自為政，實際已整合為單一持牌實體。她談跨境融合帶來的新風險、AI 在核保與理賠流程的角色，以及減少紙本流程的進度。[EN原文]"
        },
        "why": {
            "sc": "保司整合持牌实体，直接影响经纪的对接方式：同一集团内原本要分两条线报的案子，现在走一个入口。值得记下来，报价与转介路径可能要重问一次，别沿用旧的组织图。",
            "tc": "保司整合持牌實體，直接影響經紀的對接方式：同一集團內原本要分兩條線報的案子，現在走一個入口。值得記下來，報價與轉介路徑可能要重問一次，別沿用舊的組織圖。"
        },
        "tags": {
            "sc": ["高管观点", "业务整合", "AI应用", "Liberty"],
            "tc": ["高管觀點", "業務整合", "AI應用", "Liberty"]
        },
        "actions": {
            "front": {"sc": "客户沟通：承保能力来源", "tc": "客戶溝通：承保能力來源"},
            "midback": {"sc": "研究：保司组织变动", "tc": "研究：保司組織變動"},
            "lead": {"sc": "团队简报：对接入口变化", "tc": "團隊簡報：對接入口變化"},
            "cross": {"sc": "跨境特殊险安排", "tc": "跨境特殊險安排"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "source": {"sc": "Insurance Asia 2026-10-27", "tc": "Insurance Asia 2026-10-27",
                   "name": "insuranceasia", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "iasia-bocg-insurance-am-best-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27T06:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/bank-china-group-insurance-stays-stable-despite-investment-concentration",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 66,
        "boards": ["insurer", "market"],
        "themes": ["保险公司财务", "信用评级", "投资集中度"],
        "title": {
            "sc": "中银集团保险展望稳定　三成投资压在与关联公司的非流动资产",
            "tc": "中銀集團保險展望穩定　三成投資壓在與關聯公司的非流動資產"
        },
        "summary": {
            "sc": "AM Best 指中银集团保险财务表现可维持稳定，现金与易变现资产足以完全覆盖净保险负债，2025 年资本充足处于最高水平；非寿险市占 4.2%、排第六，2021 年起连续五年承保获利但利润率偏薄。约三分之一投资为关联公司非流动资产，构成集中度与流动性风险。[EN原文]",
            "tc": "AM Best 指中銀集團保險財務表現可維持穩定，現金與易變現資產足以完全覆蓋淨保險負債，2025 年資本充足處於最高水平；非壽險市佔 4.2%、排第六，2021 年起連續五年承保獲利但利潤率偏薄。約三分之一投資為關聯公司非流動資產，構成集中度與流動性風險。[EN原文]"
        },
        "why": {
            "sc": "评級机构看本地险企，真正的分水岭往往不是承保利润（普遍薄），而是投资端结构与流动性。这条给了具体比例，可用来说明「财务稳健」要看资产能不能变现，而不只看偿付能力比率。",
            "tc": "評級機構看本地險企，真正的分水嶺往往不是承保利潤（普遍薄），而是投資端結構與流動性。這條給了具體比例，可用來說明「財務穩健」要看資產能不能變現，而不只看償付能力比率。"
        },
        "tags": {
            "sc": ["保险公司财务", "信用评级", "投资集中度", "中银保险"],
            "tc": ["保險公司財務", "信用評級", "投資集中度", "中銀保險"]
        },
        "actions": {
            "front": {"sc": "客户沟通：保司财务怎么看", "tc": "客戶溝通：保司財務怎麼看"},
            "midback": {"sc": "研究：本地险企资产结构", "tc": "研究：本地險企資產結構"},
            "lead": {"sc": "团队简报：评级要点", "tc": "團隊簡報：評級要點"},
            "cross": {"sc": "中资保司跨境业务", "tc": "中資保司跨境業務"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia 2026-10-27", "tc": "Insurance Asia 2026-10-27",
                   "name": "insuranceasia", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "iasia-prudential-ai-operations-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27T16:26:00+08:00",
        "originalUrl": "https://insuranceasia.com/videos/prudential-embeds-ai-across-insurance-operations",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 72,
        "boards": ["tech", "insurer"],
        "themes": ["AI应用", "核保效率", "代理赋能"],
        "title": {
            "sc": "保诚把 AI 铺到代理、营运与健康　香港 AI 核保问答由数天变数分钟",
            "tc": "保誠把 AI 鋪到代理、營運與健康　香港 AI 核保問答由數天變數分鐘"
        },
        "summary": {
            "sc": "保诚集团首席 AI 业务官吴（Priscilla Ng）称把 AI 当业务工具而非独立科技项目：代理端用于整合客户资料、识别需求、备会与减行政工作，并以转化率与顾问产能衡量成效；香港已推出 AI 核保聊天机器人，财务顾问查核保指引与客户资料要求由数天缩短至数分钟。[EN原文]",
            "tc": "保誠集團首席 AI 業務官吳（Priscilla Ng）稱把 AI 當業務工具而非獨立科技項目：代理端用於整合客戶資料、識別需求、備會與減行政工作，並以轉化率與顧問產能衡量成效；香港已推出 AI 核保聊天機器人，財務顧問查核保指引與客戶資料要求由數天縮短至數分鐘。[EN原文]"
        },
        "why": {
            "sc": "大保司把 AI 落在「核保问答」这类高频卡点上，效果可量化成顾问时间。对我们最有借鉴价值的不是模型本身，而是它把 AI 绑到具体业务指标（转化、产能）——这正是团队里做 AI 赋能最常缺的一环。",
            "tc": "大保司把 AI 落在「核保問答」這類高頻卡點上，效果可量化成顧問時間。對我們最有借鑑價值的不是模型本身，而是它把 AI 綁到具體業務指標（轉化、產能）——這正是團隊裡做 AI 賦能最常缺的一環。"
        },
        "tags": {
            "sc": ["AI应用", "核保效率", "代理赋能", "保诚"],
            "tc": ["AI應用", "核保效率", "代理賦能", "保誠"]
        },
        "actions": {
            "front": {"sc": "客户沟通：核保流程提速", "tc": "客戶溝通：核保流程提速"},
            "midback": {"sc": "研究：AI 与业务指标挂钩", "tc": "研究：AI 與業務指標掛鈎"},
            "lead": {"sc": "团队简报：AI 赋能案例", "tc": "團隊簡報：AI 賦能案例"},
            "cross": {"sc": "跨境核保标准", "tc": "跨境核保標準"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 3, "cross": 1},
        "source": {"sc": "Insurance Asia 2026-10-27", "tc": "Insurance Asia 2026-10-27",
                   "name": "insuranceasia", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "iasia-china-life-overseas-ai-investment-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27T12:17:00+08:00",
        "originalUrl": "https://insuranceasia.com/videos/china-life-insurance-overseas-embeds-ai-in-investment-operations",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 68,
        "boards": ["tech", "insurer"],
        "themes": ["AI应用", "资产负债管理", "投资"],
        "title": {
            "sc": "中国人寿海外「星河」项目：AI 做投资分析与合规筛查　不碰配置决策",
            "tc": "中國人壽海外「星河」項目：AI 做投資分析與合規篩查　不碰配置決策"
        },
        "summary": {
            "sc": "中国人寿（海外）副总裁康乐称目标已非最大化收益，而是在支撑长期负债前提下取得风险调整后回报；「星河」项目以 AI 把组合表现与负债、财务数据结合，自动化部分数据处理、合规筛查与报表，但明言 AI 不设风险偏好、不做资产配置，治理责任仍在人。[EN原文]",
            "tc": "中國人壽（海外）副總裁康樂稱目標已非最大化收益，而是在支撐長期負債前提下取得風險調整後回報；「星河」項目以 AI 把組合表現與負債、財務數據結合，自動化部分數據處理、合規篩查與報表，但明言 AI 不設風險偏好、不做資產配置，治理責任仍在人。[EN原文]"
        },
        "why": {
            "sc": "「AI 做分析、人做决策」是金融机构目前最稳的分工写法，这条给了可直接引用的边界表述。做 AI 培训或对内治理草案时，比自创一套说法更容易被合规接受。",
            "tc": "「AI 做分析、人做決策」是金融機構目前最穩的分工寫法，這條給了可直接引用的邊界表述。做 AI 培訓或對內治理草案時，比自創一套說法更容易被合規接受。"
        },
        "tags": {
            "sc": ["AI应用", "资产负债管理", "投资", "治理边界"],
            "tc": ["AI應用", "資產負債管理", "投資", "治理邊界"]
        },
        "actions": {
            "front": {"sc": "客户沟通：AI 与决策责任", "tc": "客戶溝通：AI 與決策責任"},
            "midback": {"sc": "合规：AI 使用边界表述", "tc": "合規：AI 使用邊界表述"},
            "lead": {"sc": "团队简报：AI 治理框架", "tc": "團隊簡報：AI 治理框架"},
            "cross": {"sc": "跨境投资配置", "tc": "跨境投資配置"}
        },
        "rolesImpact": {"front": 1, "midback": 3, "lead": 2, "cross": 1},
        "source": {"sc": "Insurance Asia 2026-10-27", "tc": "Insurance Asia 2026-10-27",
                   "name": "insuranceasia", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "ibm-anthropic-ipo-ai-liability-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/cyber/anthropic-just-warned-its-ai-could-end-humanity--and-asiapacific-insurers-are-using-it-594963.aspx",
        "sourceKey": "insurancebusinessmag",
        "sourceTier": "media",
        "score": 72,
        "boards": ["tech", "market"],
        "themes": ["AI责任", "网络保险", "D&O"],
        "title": {
            "sc": "Anthropic 招股书自认 AI 或带来存续风险　三类伤害对应三条险种却无干净答案",
            "tc": "Anthropic 招股書自認 AI 或帶來存續風險　三類傷害對應三條險種卻無乾淨答案"
        },
        "summary": {
            "sc": "Anthropic 递交上市文件，明言技术若缺乏适当防护可能对人类构成灾难性或存续风险，并称无法确定系统行为在何处、如何承担责任，点名模型输出伤害、自主 AI 代理引发的网络安全事件等风险。文章指输出伤害可能落到专业/产品责任或 D&O，AI 代理网络事件则未必落在既有 cyber 保单内。[EN原文]",
            "tc": "Anthropic 遞交上市文件，明言技術若缺乏適當防護可能對人類構成災難性或存續風險，並稱無法確定系統行為在何處、如何承擔責任，點名模型輸出傷害、自主 AI 代理引發的網絡安全事件等風險。文章指輸出傷害可能落到專業/產品責任或 D&O，AI 代理網絡事件則未必落在既有 cyber 保單內。[EN原文]"
        },
        "why": {
            "sc": "AI 责任从研讨会议题变成招股书里的法律文字，意味争议会真的进法庭。对企业客户谈 D&O 与 cyber 时，「你的保单是否写于 AI 代理成为威胁之前」是个有杀伤力的问题，也提醒我们别随口承诺 AI 相关风险已被完整覆盖。",
            "tc": "AI 責任從研討會議題變成招股書裡的法律文字，意味爭議會真的進法庭。對企業客戶談 D&O 與 cyber 時，「你的保單是否寫於 AI 代理成為威脅之前」是個有殺傷力的問題，也提醒我們別隨口承諾 AI 相關風險已被完整覆蓋。"
        },
        "tags": {
            "sc": ["AI责任", "网络保险", "D&O", "科技风险"],
            "tc": ["AI責任", "網絡保險", "D&O", "科技風險"]
        },
        "actions": {
            "front": {"sc": "客户沟通：AI 风险的保障边界", "tc": "客戶溝通：AI 風險的保障邊界"},
            "midback": {"sc": "研究：AI 责任条款", "tc": "研究：AI 責任條款"},
            "lead": {"sc": "团队简报：新险种缺口", "tc": "團隊簡報：新險種缺口"},
            "cross": {"sc": "跨境科技企业保障", "tc": "跨境科技企業保障"}
        },
        "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 2},
        "source": {"sc": "Insurance Business Asia 2026-10-27", "tc": "Insurance Business Asia 2026-10-27",
                   "name": "insurancebusinessmag", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "ibm-south-korea-whole-life-shift-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/south-korea-insurance-slowdown-signals-product-shift-for-asiapacific-brokers-594949.aspx",
        "sourceKey": "insurancebusinessmag",
        "sourceTier": "media",
        "score": 68,
        "boards": ["market", "product"],
        "themes": ["产品转型", "人口老化", "监管"],
        "title": {
            "sc": "韩国保险增速腰斩　终身寿由身故给付转向生前给付",
            "tc": "韓國保險增速腰斬　終身壽由身故給付轉向生前給付"
        },
        "summary": {
            "sc": "韩国保险研究院预测 2027 年保险业仅增 3.5%（2026 年约 8%），寿险与非寿险合计保费约 299 万亿韩元。终身寿首年保费上半年跌 5.7%，监管 9 月叫停「700 终身寿」；韩华、三星、教保相继加入抗癌保障、可补充医疗账户与退休提领功能。[EN原文]",
            "tc": "韓國保險研究院預測 2027 年保險業僅增 3.5%（2026 年約 8%），壽險與非壽險合計保費約 299 萬億韓元。終身壽首年保費上半年跌 5.7%，監管 9 月叫停「700 終身壽」；韓華、三星、教保相繼加入抗癌保障、可補充醫療賬戶與退休提領功能。[EN原文]"
        },
        "why": {
            "sc": "韩国是把「终身寿加生前给付」推到极致的市场，它遇到的监管叫停与资本压力，对香港同类产品设计有前视价值。做产品比较或培训时，可用它说明为什么监管会盯住「缴几年就能全退」这类结构。",
            "tc": "韓國是把「終身壽加生前給付」推到極致的市場，它遇到的監管叫停與資本壓力，對香港同類產品設計有前視價值。做產品比較或培訓時，可用它說明為什麼監管會盯住「繳幾年就能全退」這類結構。"
        },
        "tags": {
            "sc": ["产品转型", "人口老化", "监管", "韩国"],
            "tc": ["產品轉型", "人口老化", "監管", "韓國"]
        },
        "actions": {
            "front": {"sc": "客户沟通：生前给付设计", "tc": "客戶溝通：生前給付設計"},
            "midback": {"sc": "研究：产品监管趋势", "tc": "研究：產品監管趨勢"},
            "lead": {"sc": "团队简报：区域产品比较", "tc": "團隊簡報：區域產品比較"},
            "cross": {"sc": "亚洲产品联动", "tc": "亞洲產品聯動"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 2, "cross": 1},
        "source": {"sc": "Insurance Business Asia 2026-10-27", "tc": "Insurance Business Asia 2026-10-27",
                   "name": "insurancebusinessmag", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "iasia-marsh-hkland-climate-resilience-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27T05:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/climate-resilient-buildings-curb-losses-insurers-tighten-cover",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 70,
        "boards": ["product", "market"],
        "themes": ["气候风险", "财产险", "ESG"],
        "title": {
            "sc": "Marsh 与置地：气候韧性设计令风暴潮预期损失降 84%",
            "tc": "Marsh 與置地：氣候韌性設計令風暴潮預期損失降 84%"
        },
        "summary": {
            "sc": "Marsh 与香港置地联合发布《Building Value That Lasts》，以上海西岸中環 170 万平方米项目为样本：工程韧性措施令风暴潮年均预期损失降 84%、暴雨洪涝降 88%，风电损失降 36%。两方指不足一成气候披露量化了调适回报，呼吁发展商、贷款人与险企在设计早期共建指标。[EN原文]",
            "tc": "Marsh 與香港置地聯合發布《Building Value That Lasts》，以上海西岸中環 170 萬平方米項目為樣本：工程韌性措施令風暴潮年均預期損失降 84%、暴雨洪澇降 88%，風電損失降 36%。兩方指不足一成氣候披露量化了調適回報，呼籲發展商、貸款人與險企在設計早期共建指標。[EN原文]"
        },
        "why": {
            "sc": "「减损措施能不能换保费」过去只能凭经验讲，这份报告给了量化口径。对持有商业物业或做项目险的客户，谈续保涨价时的筹码不是抱怨市场，而是拿出可核的韧性指标。",
            "tc": "「減損措施能不能換保費」過去只能憑經驗講，這份報告給了量化口徑。對持有商業物業或做項目險的客戶，談續保漲價時的籌碼不是抱怨市場，而是拿出可核的韌性指標。"
        },
        "tags": {
            "sc": ["气候风险", "财产险", "ESG", "减损"],
            "tc": ["氣候風險", "財產險", "ESG", "減損"]
        },
        "actions": {
            "front": {"sc": "客户沟通：物业韧性议价", "tc": "客戶溝通：物業韌性議價"},
            "midback": {"sc": "研究：气候调适回报", "tc": "研究：氣候調適回報"},
            "lead": {"sc": "团队简报：商业物业风险", "tc": "團隊簡報：商業物業風險"},
            "cross": {"sc": "大湾区资产保障", "tc": "大灣區資產保障"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 1, "cross": 2},
        "source": {"sc": "Insurance Asia 2026-10-27", "tc": "Insurance Asia 2026-10-27",
                   "name": "insuranceasia", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
]


def key_of(it):
    p = it.get('publishedAt') or ''
    return (p + 'T23:59:59+08:00') if len(p) == 10 else p


d = json.load(open(PATH, encoding='utf-8'))
items = d['items']
existing_ids = {i['id'] for i in items}
existing_urls = {(i.get('originalUrl') or '').split('?')[0] for i in items}

added = []
for it in new_items:
    if it['id'] in existing_ids:
        print('skip dup id', it['id'])
        continue
    if (it['originalUrl'].split('?')[0]) in existing_urls:
        print('skip dup url', it['id'])
        continue
    k = key_of(it)
    pos = len(items)
    for idx, cur in enumerate(items):
        if key_of(cur) < k:
            pos = idx
            break
    items.insert(pos, it)
    added.append(it['id'])

n = len(items)
d['items'] = items
meta = d.setdefault('meta', {})
meta['generatedAt'] = INGEST
meta['itemCount'] = n
meta['windowNote'] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}
json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

lc = json.load(open('data/last-check.json', encoding='utf-8'))
lc['lastCheck'] = INGEST
for k in lc.get('sources', {}):
    lc['sources'][k]['last'] = INGEST
json.dump(lc, open('data/last-check.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('added', len(added), added)
print('total', n, 'lastCheck', lc['lastCheck'])
for it in items[:12]:
    print(it['publishedAt'][:16], '|', it['id'], '|', it['title']['sc'][:44])
