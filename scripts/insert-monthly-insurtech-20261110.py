#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每月AI与保险科技落地扫描 2026-11-10：插入 5 条新条目 + 回写 insurtech 信源 last-check。"""
import json, datetime

TZ = datetime.timezone(datetime.timedelta(hours=8))
now = datetime.datetime.now(TZ)
now_iso = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")

NEW_ITEMS = [
    {
        "id": "fwd-hk-ai-claims-35s-award-20261030",
        "clusterCount": 1,
        "score": 78,
        "verifyStatus": "pending",
        "sourceTier": "insurer",
        "sourceKey": "fwd-hk",
        "title": {
            "sc": "富卫香港AI理赔转型夺香港保险业大奖年度大奖 合资格个案最快35秒完成审批",
            "tc": "富衛香港AI理賠轉型奪香港保險業大獎年度大獎 合資格個案最快35秒完成審批"
        },
        "summary": {
            "sc": "富卫香港「AI驱动理赔转型」项目于香港保险业大奖2026获「杰出理赔管理大奖」年度大奖，连续两年在理赔管理获奖。其一站式数字平台结合自动化理赔流程、光学字符辨识与AI规则引擎，符合自动化处理条件的理赔最快35秒完成审批，并以欺诈、浪费及滥用风险侦测加强理赔风控，另设理赔大使提供人手支援。富卫同届共获八项殊荣，香港专属代理团队年内增逾一成、突破5,000人。",
            "tc": "富衛香港「AI驅動理賠轉型」項目於香港保險業大獎2026獲「傑出理賠管理大獎」年度大獎，連續兩年在理賠管理獲獎。其一站式數碼平台結合自動化理賠流程、光學字符辨識與AI規則引擎，符合自動化處理條件的理賠最快35秒完成審批，並以欺詐、浪費及濫用風險偵測加強理賠風控，另設理賠大使提供人手支援。富衛同屆共獲八項殊榮，香港專屬代理團隊年內增逾一成、突破5,000人。"
        },
        "why": {
            "sc": "香港保司把AI理赔跑到「秒级审批」并连续两年获行业奖，是理赔流程AI化最可直接对标的本地案例：哪些个案可自动、哪些必须留人手，界线已由实践画出。",
            "tc": "香港保司把AI理賠跑到「秒級審批」並連續兩年獲行業獎，是理賠流程AI化最可直接對標的本地案例：哪些個案可自動、哪些必須留人手，界線已由實踐畫出。"
        },
        "actions": {
            "front": {"sc": "向客户说明AI快赔与理赔大使分工", "tc": "向客戶說明AI快賠與理賠大使分工"},
            "midback": {"sc": "理赔自动化边界对标", "tc": "理賠自動化邊界對標"},
            "lead": {"sc": "本地保司AI落地节奏参考", "tc": "本地保司AI落地節奏參考"},
            "cross": {}
        },
        "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 1},
        "source": {"sc": "富卫香港（Media OutReach）", "lang": "zh"},
        "boards": ["insurer", "tech"],
        "themes": ["ai", "claims", "insurtech"],
        "tags": {
            "sc": ["富卫", "AI理赔", "35秒", "香港保险业大奖", "保险科技"],
            "tc": ["富衛", "AI理賠", "35秒", "香港保險業大獎", "保險科技"]
        },
        "contentKind": "press",
        "publishedAt": "2026-10-30",
        "originalUrl": "https://businessfocus.io/article/364792/",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "kalepa-series-b-470m-20261105",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "pending",
        "sourceTier": "pro",
        "sourceKey": "kalepa",
        "title": {
            "sc": "AI核保平台Kalepa完成7,500万美元B轮 估值4.7亿美元、一年营收增两倍",
            "tc": "AI核保平台Kalepa完成7,500萬美元B輪 估值4.7億美元、一年營收增兩倍"
        },
        "summary": {
            "sc": "纽约AI核保平台Kalepa 11月5日宣布完成7,500万美元B轮，由Updata Partners领投，IA Ventures与Inspired Capital跟投，投后估值4.7亿美元、累计融资9,100万美元。平台覆盖核保、定价、运营与组合管理，客户包括W.R. Berkley、Bowhead Specialty与AmRisc；公司称使用方每名核保人保费收入增30%至60%、报价时间减58%，过去一年营收与客户数均增两倍，并计划2027年团队翻倍。",
            "tc": "紐約AI核保平台Kalepa 11月5日宣布完成7,500萬美元B輪，由Updata Partners領投，IA Ventures與Inspired Capital跟投，投後估值4.7億美元、累計融資9,100萬美元。平台覆蓋核保、定價、營運與組合管理，客戶包括W.R. Berkley、Bowhead Specialty與AmRisc；公司稱使用方每名核保人保費收入增30%至60%、報價時間減58%，過去一年營收與客戶數均增兩倍，並計劃2027年團隊翻倍。"
        },
        "why": {
            "sc": "核保是保险AI商业化最实的场景：Kalepa已连续两年经营现金流为正、按人头产出可量化，说明「AI帮核保人做更多单」比「AI替代核保人」更早跑通。",
            "tc": "核保是保險AI商業化最實的場景：Kalepa已連續兩年經營現金流為正、按人頭產出可量化，說明「AI幫核保人做更多單」比「AI替代核保人」更早跑通。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "核保工具产出指标参考", "tc": "核保工具產出指標參考"},
            "lead": {"sc": "保险AI融资与估值观察", "tc": "保險AI融資與估值觀察"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 0},
        "source": {"sc": "Kalepa / Reuters", "lang": "en"},
        "boards": ["tech", "market"],
        "themes": ["insurtech", "funding", "underwriting"],
        "tags": {
            "sc": ["Kalepa", "AI核保", "保险科技", "融资", "估值"],
            "tc": ["Kalepa", "AI核保", "保險科技", "融資", "估值"]
        },
        "contentKind": "news",
        "publishedAt": "2026-11-05",
        "originalUrl": "https://kalepa.com/news-posts/kalepa-raises-75-million-series-b",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "covergo-series-b1-6m-20261029",
        "clusterCount": 1,
        "score": 74,
        "verifyStatus": "pending",
        "sourceTier": "pro",
        "sourceKey": "covergo",
        "title": {
            "sc": "港产AI原生保险平台CoverGo完成600万美元B1轮 营收较A轮增十倍、已EBITDA收支平衡",
            "tc": "港產AI原生保險平台CoverGo完成600萬美元B1輪 營收較A輪增十倍、已EBITDA收支平衡"
        },
        "summary": {
            "sc": "总部设于香港与旧金山的AI原生保险平台CoverGo 10月29日完成600万美元B1轮首关，由Betatron Venture Group领投，累计融资逾3,000万美元。公司称自2022年A轮以来营收增十倍并达EBITDA收支平衡，现服务15个国家25家机构客户，包括安盛、保柏、忠意、永明、保诚、MSIG与达信；资金将用于开发AI代理能力并扩张市场，目标是让险企逐步淘汰旧核心系统。",
            "tc": "總部設於香港與舊金山的AI原生保險平台CoverGo 10月29日完成600萬美元B1輪首關，由Betatron Venture Group領投，累計融資逾3,000萬美元。公司稱自2022年A輪以來營收增十倍並達EBITDA收支平衡，現服務15個國家25家機構客戶，包括安盛、保柏、忠意、永明、保誠、MSIG與達信；資金將用於開發AI代理能力並擴張市場，目標是讓險企逐步淘汰舊核心系統。"
        },
        "why": {
            "sc": "香港本土保险科技以「AI原生核心系统」切入，客户名单已含多家在港活跃保司；对判断本地保司换核心系统的节奏与供应商格局，是难得的一手信号。",
            "tc": "香港本土保險科技以「AI原生核心系統」切入，客戶名單已含多家在港活躍保司；對判斷本地保司換核心系統的節奏與供應商格局，是難得的一手信號。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "核心系统AI化供应商图谱", "tc": "核心系統AI化供應商圖譜"},
            "lead": {"sc": "香港保险科技生态观察", "tc": "香港保險科技生態觀察"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 0},
        "source": {"sc": "CoverGo", "lang": "en"},
        "boards": ["tech", "insurer"],
        "themes": ["insurtech", "funding", "ai"],
        "tags": {
            "sc": ["CoverGo", "保险科技", "AI原生", "融资", "香港"],
            "tc": ["CoverGo", "保險科技", "AI原生", "融資", "香港"]
        },
        "contentKind": "press",
        "publishedAt": "2026-10-29",
        "originalUrl": "https://covergo.com/news/covergo-raises-us6-million-in-series-b1-funding-to-accelerate-global-adoption-of-its-ai-insurance-platform/",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "guidewire-agentic-insurance-platform-20261027",
        "clusterCount": 1,
        "score": 72,
        "verifyStatus": "pending",
        "sourceTier": "pro",
        "sourceKey": "guidewire",
        "title": {
            "sc": "Guidewire发布「代理式保险」平台 AI代理直接跑在核心系统上、内建权限边界与审计轨迹",
            "tc": "Guidewire發布「代理式保險」平台 AI代理直接跑在核心系統上、內建權限邊界與審計軌跡"
        },
        "summary": {
            "sc": "保险核心系统商Guidewire 10月27日在Connections大会发布「代理式保险」平台：AI代理与核心应用跑在同一平台、直接取用险企既有数据与流程，并以内建控制划定可访问范围、保留可更新的审计轨迹。承保侧含UnderwritingCenter、PricingCenter与ProNavigator；理赔侧Concierge让客户以语音或聊天自助报案、把损失资料整理后直送ClaimCenter。Agentic Framework支持自建代理、选模型、设护栏、评估表现与监控成本。",
            "tc": "保險核心系統商Guidewire 10月27日在Connections大會發布「代理式保險」平台：AI代理與核心應用跑在同一平台、直接取用險企既有數據與流程，並以內建控制劃定可訪問範圍、保留可更新的審計軌跡。承保側含UnderwritingCenter、PricingCenter與ProNavigator；理賠側Concierge讓客戶以語音或聊天自助報案、把損失資料整理後直送ClaimCenter。Agentic Framework支持自建代理、選模型、設護欄、評估表現與監控成本。"
        },
        "why": {
            "sc": "核心系统商把代理式AI从外挂插件改为平台内建能力，并主打「权限边界＋审计轨迹」的治理叙事——这是保司采购AI时必问的两件事，值得作为选型框架参考。",
            "tc": "核心系統商把代理式AI從外掛插件改為平台內建能力，並主打「權限邊界＋審計軌跡」的治理敘事——這是保司採購AI時必問的兩件事，值得作為選型框架參考。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "核心系统AI治理能力对标", "tc": "核心系統AI治理能力對標"},
            "lead": {"sc": "代理式AI平台化趋势", "tc": "代理式AI平台化趨勢"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 3, "lead": 2, "cross": 0},
        "source": {"sc": "Guidewire", "lang": "en"},
        "boards": ["tech", "product"],
        "themes": ["agentic-ai", "insurtech", "core-system"],
        "tags": {
            "sc": ["代理式AI", "Guidewire", "核心系统", "理赔", "审计轨迹"],
            "tc": ["代理式AI", "Guidewire", "核心系統", "理賠", "審計軌跡"]
        },
        "contentKind": "press",
        "publishedAt": "2026-10-27",
        "originalUrl": "https://www.guidewire.com/about/press-center/press-releases/20261027/guidewire-delivers-the-open-secure-and-complete-core-platform-for-agentic-insurance",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "al-wathba-agentic-ai-production-20261109",
        "clusterCount": 1,
        "score": 75,
        "verifyStatus": "pending",
        "sourceTier": "insurer",
        "sourceKey": "al-wathba-insurance",
        "title": {
            "sc": "阿布扎比Al Wathba保险代理式AI投产 案件处理时间减半、质检覆盖率升至100%",
            "tc": "阿布扎比Al Wathba保險代理式AI投產 案件處理時間減半、質檢覆蓋率升至100%"
        },
        "summary": {
            "sc": "阿布扎比Al Wathba Insurance 11月9日宣布代理式AI已在案件管理投产：AI代理读取、分类、补充并分流客户案件，收集相关资料并建议后续行动，重大决定仍由员工把关。案件处理时间缩短50%，质检由人工抽检20%至30%提升到覆盖全部在范围内案件，AI并实时进行客户满意度调查。平台由Magure的MagOneAI与Core42 Compass提供，数据留在阿联酋境内、提示与输出不留存，后续将扩展至医疗核保支援与首勘通知分流。",
            "tc": "阿布扎比Al Wathba Insurance 11月9日宣布代理式AI已在案件管理投產：AI代理讀取、分類、補充並分流客戶案件，收集相關資料並建議後續行動，重大決定仍由員工把關。案件處理時間縮短50%，質檢由人工抽檢20%至30%提升到覆蓋全部在範圍內案件，AI並實時進行客戶滿意度調查。平台由Magure的MagOneAI與Core42 Compass提供，數據留在阿聯酋境內、提示與輸出不留存，後續將擴展至醫療核保支援與首勘通知分流。"
        },
        "why": {
            "sc": "这是少见把「代理式AI+100%质检覆盖」写成可核数字的投产案例：AI做量、人做判断，质检从抽检变全检——正好回应「AI上线后如何监控AI」的治理难题。",
            "tc": "這是少見把「代理式AI＋100%質檢覆蓋」寫成可核數字的投產案例：AI做量、人做判斷，質檢從抽檢變全檢——正好回應「AI上線後如何監控AI」的治理難題。"
        },
        "actions": {
            "front": {"sc": "理解AI分流与人工把关分工", "tc": "理解AI分流與人工把關分工"},
            "midback": {"sc": "AI质检全检模式参考", "tc": "AI質檢全檢模式參考"},
            "lead": {"sc": "代理式AI投产节奏观察", "tc": "代理式AI投產節奏觀察"},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 3, "lead": 2, "cross": 1},
        "source": {"sc": "Al Wathba Insurance（American Bazaar）", "lang": "en"},
        "boards": ["tech", "insurer"],
        "themes": ["agentic-ai", "claims", "ai-governance"],
        "tags": {
            "sc": ["代理式AI", "案件管理", "质检", "数据本地化", "阿联酋"],
            "tc": ["代理式AI", "案件管理", "質檢", "數據本地化", "阿聯酋"]
        },
        "contentKind": "press",
        "publishedAt": "2026-11-09",
        "originalUrl": "https://americanbazaaronline.com/2026/11/09/al-wathba-insurance-launches-agentic-ai-cuts-case-turnaround-time-by-50-491881/",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]

# --- 1. live-items.json ---
path = "data/live-items.json"
data = json.load(open(path, encoding="utf-8"))
existing_ids = {it["id"] for it in data["items"]}
existing_urls = {it.get("originalUrl", "") for it in data["items"]}
added = []
for it in NEW_ITEMS:
    if it["id"] in existing_ids or it["originalUrl"] in existing_urls:
        print("SKIP (dup):", it["id"])
        continue
    data["items"].insert(0, it)
    added.append(it["id"])

data["meta"]["itemCount"] = len(data["items"])
data["meta"]["generatedAt"] = now_iso
data["meta"]["windowNote"] = {
    "sc": f"本库{len(data['items'])}条。含11月10日月度AI与保险科技扫描+{len(added)}条。",
    "tc": f"本庫{len(data['items'])}條。含11月10日月度AI與保險科技掃描+{len(added)}條。"
}
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"INSERTED {len(added)} items; total now {len(data['items'])}")
for a in added:
    print(" +", a)

# --- 2. last-check.json ---
lc_path = "data/last-check.json"
lc = json.load(open(lc_path, encoding="utf-8"))
if "insurtech" in lc.get("sources", {}):
    lc["sources"]["insurtech"]["last"] = now_iso
lc["lastCheck"] = now_iso
json.dump(lc, open(lc_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"last-check.json insurtech.last -> {now_iso}")
