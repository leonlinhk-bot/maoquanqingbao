import json, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
NOW = now.isoformat(timespec="seconds")

items_new = [
    {
        "id": "insuranceasia-hk-nonlife-capital-reform-20261117",
        "clusterCount": 1,
        "score": 79,
        "verifyStatus": "verified",
        "sourceTier": "pro",
        "sourceKey": "insuranceasia",
        "contentKind": "news",
        "title": {
            "sc": "AM Best：香港非寿险资本新规年底生效　巨灾与准备金资本要求下调、离岸再保可获减免 [EN原文]",
            "tc": "AM Best：香港非壽險資本新規年底生效　巨災與準備金資本要求下調、離岸再保可獲減免 [EN原文]",
        },
        "summary": {
            "sc": "AM Best 11 月 9 日报告：香港非寿险新资本规则 12 月 31 日生效，下调巨灾与准备金风险资本要求，合资格离岸再保业务经监管批准可获减免。2025 年非寿险毛保费 1,085 亿港元升 8%，但整体承保利润跌 12.5% 至 29 亿港元；意外及健康险占 36.6%，医疗通胀约 10%。",
            "tc": "AM Best 11 月 9 日報告：香港非壽險新資本規則 12 月 31 日生效，下調巨災與準備金風險資本要求，合資格離岸再保業務經監管批准可獲減免。2025 年非壽險毛保費 1,085 億港元升 8%，但整體承保利潤跌 12.5% 至 29 億港元；意外及健康險佔 36.6%，醫療通脹約 10%。",
        },
        "why": {
            "sc": "这是今年底最实质的一次监管口径变化：巨灾风险资本要求下调，直接改变产险与再保在港配置业务的成本，也决定未来哪些跨境再保安排会被搬来香港。同一份报告里还有两个对前线更有用的数字——医疗通胀仍在 10% 左右、意外及健康险综合成本率才刚从 102.3% 修回 95.1%，说明「保费涨了但利润没回来」的压力还在；而大埔宏福苑火灾后，高座数维修与高风险工地的核保明显收紧。做企业险与医疗险的人，报价与条款谈判前应先把这两条放进判断。",
            "tc": "這是今年底最實質的一次監管口徑變化：巨災風險資本要求下調，直接改變產險與再保在港配置業務的成本，也決定未來哪些跨境再保安排會被搬來香港。同一份報告裡還有兩個對前線更有用的數字——醫療通脹仍在 10% 左右、意外及健康險綜合成本率才剛從 102.3% 修回 95.1%，說明「保費漲了但利潤沒回來」的壓力還在；而大埔宏福苑火災後，高座數維修與高風險工地的核保明顯收緊。做企業險與醫療險的人，報價與條款談判前應先把這兩條放進判斷。",
        },
        "actions": {
            "front": {"sc": "谈医疗险续保时，用「医疗通胀约 10%、行业综合成本率 95.1%」解释加费逻辑，而不是只说公司调整", "tc": "談醫療險續保時，用「醫療通脹約 10%、行業綜合成本率 95.1%」解釋加費邏輯，而不是只說公司調整"},
            "midback": {"sc": "把新资本规则生效日（12 月 31 日）列入产险与再保客户的年度检视节点", "tc": "把新資本規則生效日（12 月 31 日）列入產險與再保客戶的年度檢視節點"},
            "lead": {"sc": "招募与培训话术：香港正把制度成本往下调，做跨境风险管理的窗口在开", "tc": "招募與培訓話術：香港正把制度成本往下調，做跨境風險管理的窗口在開"},
            "cross": {"sc": "与家办、企业客户谈自保与再保安排时，可引为香港资本成本改善的依据", "tc": "與家辦、企業客戶談自保與再保安排時，可引為香港資本成本改善的依據"},
        },
        "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 2},
        "boards": ["reg", "market"],
        "themes": ["capital-requirement", "medical-inflation", "non-life"],
        "tags": {
            "sc": ["AM Best", "资本要求", "非寿险", "医疗通胀", "离岸再保"],
            "tc": ["AM Best", "資本要求", "非壽險", "醫療通脹", "離岸再保"],
        },
        "featured": False,
        "evergreen": False,
        "publishedAt": "2026-11-17T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/in-focus/hong-kong-capital-reforms-could-ease-non-life-insurers-burdens",
        "source": {
            "sc": "InsuranceAsia（引 AM Best 2026-11-09 报告）",
            "tc": "InsuranceAsia（引 AM Best 2026-11-09 報告）",
            "lang": "en",
            "name": "InsuranceAsia",
            "date": "2026-11-17",
        },
    },
    {
        "id": "ibm-cyber-mfa-bypass-renewal-20261120",
        "clusterCount": 1,
        "score": 68,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "contentKind": "news",
        "title": {
            "sc": "Beazley：黑客四招绕过 MFA　网络险续保问卷只问「有没有开」已不够 [EN原文]",
            "tc": "Beazley：黑客四招繞過 MFA　網絡險續保問卷只問「有沒有開」已不夠 [EN原文]",
        },
        "summary": {
            "sc": "Beazley Security 第三季威胁报告记录四种绕过多重验证（MFA）的手法：盗取已登录会话、设备码钓鱼、信息窃取程序截取令牌、注册攻击者设备保留访问权。勒索案源自漏洞利用的占比由第二季 14% 翻倍至 28%，公开漏洞约 3.7 万个、按季增近八成；ClickFix 感染后两至三周才部署勒索。亚太网络险保费同期仍在走软。",
            "tc": "Beazley Security 第三季威脅報告記錄四種繞過多重驗證（MFA）的手法：盜取已登入會話、設備碼釣魚、資訊竊取程式截取令牌、註冊攻擊者設備保留存取權。勒索案源自漏洞利用的佔比由第二季 14% 翻倍至 28%，公開漏洞約 3.7 萬個、按季增近八成；ClickFix 感染後兩至三週才部署勒索。亞太網絡險保費同期仍在走軟。",
        },
        "why": {
            "sc": "保单与问卷之间的落差，最后是要在理赔时才结算的。客户在投保表上勾了「已启用 MFA」，但攻击者现在根本不去破它，而是直接偷已登录的会话——这类个案一旦报赔，核保时的陈述就会被逐条翻出来。对做中小企业与专业事务所客户的人，这是续保前最值得花十分钟的一条：不是加保额，而是把「你的 MFA 是不是抗钓鱼、覆盖不覆盖管理员账号与云控制台」问清楚并留底。",
            "tc": "保單與問卷之間的落差，最後是要在理賠時才結算的。客戶在投保表上勾了「已啟用 MFA」，但攻擊者現在根本不去破它，而是直接偷已登入的會話——這類個案一旦報賠，核保時的陳述就會被逐條翻出來。對做中小企業與專業事務所客戶的人，這是續保前最值得花十分鐘的一條：不是加保額，而是把「你的 MFA 是不是抗釣魚、覆蓋不覆蓋管理員帳號與雲控制台」問清楚並留底。",
        },
        "actions": {
            "front": {"sc": "企业客户续保前，把「MFA 是否抗钓鱼、覆盖哪些账号」写进风险问卷留底", "tc": "企業客戶續保前，把「MFA 是否抗釣魚、覆蓋哪些帳號」寫進風險問卷留底"},
            "midback": {"sc": "整理一页「网络险投保陈述自查表」，供团队在续保前与客户逐项核对", "tc": "整理一頁「網絡險投保陳述自查表」，供團隊在續保前與客戶逐項核對"},
            "lead": {"sc": "培训要点：网络险卖的是核保纪律，不是保费价格", "tc": "培訓要點：網絡險賣的是核保紀律，不是保費價格"},
            "cross": {"sc": "与律所、会计师事务所客户谈专业责任险时，一并检视其网络安全陈述", "tc": "與律所、會計師事務所客戶談專業責任險時，一併檢視其網絡安全陳述"},
        },
        "rolesImpact": {"front": 3, "midback": 2, "lead": 1, "cross": 2},
        "boards": ["tech", "product"],
        "themes": ["cyber", "underwriting", "sme"],
        "tags": {
            "sc": ["网络保险", "MFA", "勒索软件", "投保陈述", "Beazley"],
            "tc": ["網絡保險", "MFA", "勒索軟件", "投保陳述", "Beazley"],
        },
        "featured": False,
        "evergreen": False,
        "publishedAt": "2026-11-20T18:09:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/cyber/cyberattack-tactics-are-outpacing-what-renewal-forms-ask-598222.aspx",
        "source": {
            "sc": "Insurance Business Asia（引 Beazley Security Q3 报告）",
            "tc": "Insurance Business Asia（引 Beazley Security Q3 報告）",
            "lang": "en",
            "name": "Insurance Business Asia",
            "date": "2026-11-20",
        },
    },
]

p = REPO / "data" / "live-items.json"
d = json.loads(p.read_text(encoding="utf-8"))
existing_ids = {i.get("id") for i in d["items"]}
existing_urls = {i.get("originalUrl") for i in d["items"]}
added = 0
for it in items_new:
    if it["id"] in existing_ids:
        print("SKIP dup id:", it["id"])
        continue
    if it["originalUrl"] in existing_urls:
        print("SKIP dup url:", it["originalUrl"])
        continue
    it["ingestedAt"] = NOW
    d["items"].insert(0, it)
    added += 1

d["meta"]["generatedAt"] = NOW
d["meta"]["itemCount"] = len(d["items"])
n = len(d["items"])
d["meta"]["windowNote"] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"added={added} total={n}")

# 回写各信源检查时间
lc_path = REPO / "data" / "last-check.json"
lc = json.loads(lc_path.read_text(encoding="utf-8"))
lc["lastCheck"] = NOW
for k, v in lc.get("sources", {}).items():
    if isinstance(v, dict):
        v["last"] = NOW
lc_path.write_text(json.dumps(lc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("last-check updated ->", NOW, "sources:", len(lc.get("sources", {})))
