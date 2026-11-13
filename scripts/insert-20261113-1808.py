#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-13 18:08 采集的 5 条（窗口 2026-11-12 18:08 → 2026-11-13 18:08）"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIVE = os.path.join(BASE, "data", "live-items.json")
NOW = "2026-11-13T18:08:00+08:00"


def mk(**kw):
    return {
        "id": kw["id"],
        "clusterCount": 1,
        "score": kw["score"],
        "verifyStatus": kw.get("verifyStatus", "pending"),
        "sourceTier": kw["sourceTier"],
        "sourceKey": kw["sourceKey"],
        "title": {"sc": kw["t_sc"], "tc": kw["t_tc"]},
        "summary": {"sc": kw["s_sc"], "tc": kw["s_tc"]},
        "why": {"sc": kw["w_sc"], "tc": kw["w_tc"]},
        "actions": {
            "front": {"sc": kw["a_front"][0], "tc": kw["a_front"][1]} if kw.get("a_front") else {},
            "midback": {"sc": kw["a_mid"][0], "tc": kw["a_mid"][1]} if kw.get("a_mid") else {},
            "lead": {"sc": kw["a_lead"][0], "tc": kw["a_lead"][1]} if kw.get("a_lead") else {},
            "cross": {"sc": kw["a_cross"][0], "tc": kw["a_cross"][1]} if kw.get("a_cross") else {},
        },
        "rolesImpact": {
            "front": kw["r"][0], "midback": kw["r"][1],
            "lead": kw["r"][2], "cross": kw["r"][3],
        },
        "source": {"sc": kw["src"], "lang": kw["lang"]},
        "boards": kw["boards"],
        "themes": kw["themes"],
        "tags": {"sc": kw["tags_sc"], "tc": kw["tags_tc"]},
        "contentKind": kw["kind"],
        "publishedAt": kw["pub"],
        "originalUrl": kw["url"],
        "ingestedAt": NOW,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False,
        "summaryShort": {"sc": kw["s_sc"][:80], "tc": kw["s_tc"][:80]},
    }


ITEMS = []

# 1. 亚洲保险论坛 2026 闭幕（IA 官方新闻稿）
ITEMS.append(mk(
    id="ia-aif-2026-concludes-20261113",
    score=88, sourceTier="official", sourceKey="ia", verifyStatus="verified",
    t_sc="亚洲保险论坛 2026 闭幕　4,500 人参与创历届新高　保监局：业界须由「赔付复原」转向「预防适应」",
    t_tc="亞洲保險論壇 2026 閉幕　4,500 人參與創歷屆新高　保監局：業界須由「賠付復原」轉向「預防適應」",
    s_sc="保监局主办的第九届亚洲保险论坛 11 月 13 日闭幕，主题为「多重危机下的韧性蓝图」，线上线下合计 4,500 人参与，创历届新高。保监局主席致辞指，风险交织叠加下业界须由传统的「赔付与复原」转向「预防与适应」，资产管理、气候准备、数字基建与承保纪律是韧性蓝图的四大支柱；财政司司长陈茂波介绍国家「十五五」规划下巩固香港国际风险管理中心的政策举措；国家金融监管总局副局长丛林表示将继续支持香港强化国际风险管理中心地位、推动大湾区保险互联互通、支持更多内地机构在港发行巨灾债券。",
    s_tc="保監局主辦的第九屆亞洲保險論壇 11 月 13 日閉幕，主題為「多重危機下的韌性藍圖」，線上線下合計 4,500 人參與，創歷屆新高。保監局主席致辭指，風險交織疊加下業界須由傳統的「賠付與復原」轉向「預防與適應」，資產管理、氣候準備、數字基建與承保紀律是韌性藍圖的四大支柱；財政司司長陳茂波介紹國家「十五五」規劃下鞏固香港國際風險管理中心的政策舉措；國家金融監管總局副局長叢林表示將繼續支持香港強化國際風險管理中心地位、推動大灣區保險互聯互通、支持更多內地機構在港發行巨災債券。",
    w_sc="论坛是本周香港监管叙事的收口：IAIS 年会讲全球规则，AIF 讲产业落地，两场都把「资产密集型再保、另类投资、巨灾债券」放在同一张议程上——这三样正是香港想从「卖保单的市场」升级为「管风险的中心」的具体抓手。",
    w_tc="論壇是本週香港監管敘事的收口：IAIS 年會講全球規則，AIF 講產業落地，兩場都把「資產密集型再保、另類投資、巨災債券」放在同一張議程上——這三樣正是香港想從「賣保單的市場」升級為「管風險的中心」的具體抓手。",
    a_front=("把「预防与适应」翻译成客户语言：先做风险查勘与体检，再谈保额", "把「預防與適應」翻譯成客戶語言：先做風險查勘與體檢，再談保額"),
    a_mid=("四大支柱（资产管理／气候准备／数字基建／承保纪律）可做团队培训框架", "四大支柱（資產管理／氣候準備／數字基建／承保紀律）可做團隊培訓框架"),
    a_lead=("资产密集型再保与巨灾债券是下一阶段政策主线，提前建立对接认知", "資產密集型再保與巨災債券是下一階段政策主線，提前建立對接認知"),
    a_cross=("巨灾债券与另类风险转移，可作家办固定收益替代的观察方向", "巨災債券與另類風險轉移，可作家辦固定收益替代的觀察方向"),
    r=(1, 2, 3, 2),
    src="保监局", lang="en",
    boards=["reg", "market"], themes=["aif", "risk-management", "catastrophe-bond"],
    tags_sc=["亚洲保险论坛", "巨灾债券", "资产密集型再保", "风险管理中心", "十五五"],
    tags_tc=["亞洲保險論壇", "巨災債券", "資產密集型再保", "風險管理中心", "十五五"],
    kind="press", pub="2026-11-13",
    url="https://www.ia.org.hk/en/infocenter/press_releases/20261113.html",
))

# 2. 张云正：专属自保很快到双位数
ITEMS.append(mk(
    id="ian-hk-captives-double-digits-20261113",
    score=76, sourceTier="pro", sourceKey="insuranceasianews", verifyStatus="pending",
    t_sc="张云正：香港专属自保数目「很快到双位数」　称市场开始发出正面讯号",
    t_tc="張雲正：香港專屬自保數目「很快到雙位數」　稱市場開始發出正面訊號",
    s_sc="保监局行政总监张云正表示，注册于香港的专属自保公司（captive）总数「很快会达到双位数」，并称已开始从市场收到正面讯号。香港今年 7 月迎来两家新自保公司，政策上同时推进专属自保与保险相连证券两条线，以扩大风险管理中心的工具箱。（原文设付费墙，本条仅据导语与公开表态，未及全文细节）",
    s_tc="保監局行政總監張雲正表示，註冊於香港的專屬自保公司（captive）總數「很快會達到雙位數」，並稱已開始從市場收到正面訊號。香港今年 7 月迎來兩家新自保公司，政策上同時推進專屬自保與保險相連證券兩條線，以擴大風險管理中心的工具箱。（原文設付費牆，本條僅據導語與公開表態，未及全文細節）",
    w_sc="自保数量是「区域风险管理中心」最硬的实物指标——比论坛主题演讲更能验证政策是否真把人留住了。对做企业客户与跨境架构的团队，自保已从概念讨论进入「香港能不能落地」阶段。",
    w_tc="自保數量是「區域風險管理中心」最硬的實物指標——比論壇主題演講更能驗證政策是否真把人留住了。對做企業客戶與跨境架構的團隊，自保已從概念討論進入「香港能不能落地」階段。",
    a_front=("企业客户谈自保，先问风险自留规模与再保安排，而不是先谈保费", "企業客戶談自保，先問風險自留規模與再保安排，而不是先談保費"),
    a_mid=("自保与 PCC 制度差异，可做企业风险架构培训一页纸", "自保與 PCC 制度差異，可做企業風險架構培訓一頁紙"),
    a_lead=("双位数目标意味着政策 KPI 已定，跟踪落地节奏与配套优惠", "雙位數目標意味著政策 KPI 已定，跟蹤落地節奏與配套優惠"),
    a_cross=("家族企业自保＋家办架构的组合，是跨境客户的新话题", "家族企業自保＋家辦架構的組合，是跨境客戶的新話題"),
    r=(1, 2, 3, 2),
    src="InsuranceAsia News", lang="zh+en",
    boards=["reg", "family"], themes=["captive", "risk-management", "policy"],
    tags_sc=["专属自保", "captive", "保险相连证券", "风险管理中心", "企业风险"],
    tags_tc=["專屬自保", "captive", "保險相連證券", "風險管理中心", "企業風險"],
    kind="news", pub="2026-11-13T11:26:00+08:00",
    url="https://insuranceasianews.com/hong-kong-captives-gaining-momentum-as-ia-eyes-double-digit-count/",
))

# 3. IAIS：另类资本与私募信贷尚未构成系统性忧虑
ITEMS.append(mk(
    id="ian-iais-alt-capital-private-credit-20261113",
    score=74, sourceTier="pro", sourceKey="insuranceasianews", verifyStatus="pending",
    t_sc="IAIS：向另类资本与私募信贷的转移「尚未构成系统性忧虑」　但须警惕结构性转变",
    t_tc="IAIS：向另類資本與私募信貸的轉移「尚未構成系統性憂慮」　但須警惕結構性轉變",
    s_sc="国际保险监督官协会（IAIS）表示，保险业向另类资本与私募信贷的转移目前「尚未构成系统性忧虑」，但监管者必须对「结构性转变」以及在压力情景下的风险传导方式保持警惕；同时认为对人工智能的监管指引应「赋能而非约束」创新。相关表态于香港举行的 IAIS 2026 年会期间释出。",
    s_tc="國際保險監督官協會（IAIS）表示，保險業向另類資本與私募信貸的轉移目前「尚未構成系統性憂慮」，但監管者必須對「結構性轉變」以及在壓力情景下的風險傳導方式保持警惕；同時認為對人工智能的監管指引應「賦能而非約束」創新。相關表態於香港舉行的 IAIS 2026 年會期間釋出。",
    w_sc="这句话等于给「私募信贷＋资产密集型再保」的扩张暂时开了绿灯：它决定未来两年香港这类架构的监管松紧，也决定高客产品底层资产的可用范围。「暂时不构成系统性风险」不等于「没有流动性风险」。",
    w_tc="這句話等於給「私募信貸＋資產密集型再保」的擴張暫時開了綠燈：它決定未來兩年香港這類架構的監管鬆緊，也決定高客產品底層資產的可用範圍。「暫時不構成系統性風險」不等於「沒有流動性風險」。",
    a_front=("客户问「另类资产安全吗」，先讲监管口径：未被判定系统性风险 ≠ 无流动性风险", "客戶問「另類資產安全嗎」，先講監管口徑：未被判定系統性風險 ≠ 無流動性風險"),
    a_mid=("私募信贷与资产密集型再保的培训可直接引 IAIS 口径", "私募信貸與資產密集型再保的培訓可直接引 IAIS 口徑"),
    a_lead=("关注 IAIS 后续是否把「结构性转变」量化成资本要求", "關注 IAIS 後續是否把「結構性轉變」量化成資本要求"),
    a_cross=("家办配置私募信贷时，同步看保险侧资本要求与再保对手方", "家辦配置私募信貸時，同步看保險側資本要求與再保對手方"),
    r=(1, 2, 3, 2),
    src="InsuranceAsia News", lang="zh+en",
    boards=["reg", "market"], themes=["iais", "private-credit", "alternative-capital"],
    tags_sc=["IAIS", "私募信贷", "另类资本", "资产密集型再保", "AI监管"],
    tags_tc=["IAIS", "私募信貸", "另類資本", "資產密集型再保", "AI監管"],
    kind="news", pub="2026-11-13",
    url="https://insuranceasianews.com/shift-towards-alternative-capital-private-credit-not-yet-systemically-concerning-iais/",
))

# 4. 微软 365 全球断线 → 云集中风险与网络险条款
ITEMS.append(mk(
    id="ibm-microsoft365-outage-cloud-concentration-20261113",
    score=68, sourceTier="media", sourceKey="insurancebusinessmag", verifyStatus="verified",
    t_sc="微软 365 全球断线、Outlook 宕机报告逾 13 万　云集中风险重回经纪视野：理赔卡在两条条款",
    t_tc="微軟 365 全球斷線、Outlook 宕機報告逾 13 萬　雲集中風險重回經紀視野：理賠卡在兩條條款",
    s_sc="美东时间 11 月 12 日中午起，微软 365 的 Exchange Online、Teams、SharePoint、Copilot 与 Defender XDR 出现全球性故障，Outlook 宕机报告一度超过 13 万条。微软称大批服务器异常离线致负载转移到其余系统，并非流量激增，亦无攻击迹象。对经纪而言关键在两条条款：网络营业中断的等待期（多为 8 至 12 小时，短时故障永不触发），以及第三方供应商系统故障是否落入承保范围；安联商业险数据显示，供应商／云端／IT 外包导致的连带营业中断已占逾 100 万欧元网络险赔案金额约 15%。",
    s_tc="美東時間 11 月 12 日中午起，微軟 365 的 Exchange Online、Teams、SharePoint、Copilot 與 Defender XDR 出現全球性故障，Outlook 宕機報告一度超過 13 萬條。微軟稱大批伺服器異常離線致負載轉移到其餘系統，並非流量激增，亦無攻擊跡象。對經紀而言關鍵在兩條條款：網絡營業中斷的等待期（多為 8 至 12 小時，短時故障永不觸發），以及第三方供應商系統故障是否落入承保範圍；安聯商業險數據顯示，供應商／雲端／IT 外包導致的連帶營業中斷已佔逾 100 萬歐元網絡險賠案金額約 15%。",
    w_sc="云集中风险不是新话题，但它每年用一次真实断线提醒：客户的「业务中断」多数发生在自己管不到的供应商机房里。这类事件最适合做企业客户的保单缺口体检，而不是等理赔时才发现等待期太长。",
    w_tc="雲集中風險不是新話題，但它每年用一次真實斷線提醒：客戶的「業務中斷」多數發生在自己管不到的供應商機房裡。這類事件最適合做企業客戶的保單缺口體檢，而不是等理賠時才發現等待期太長。",
    a_front=("企业客户谈网络险，先问「供应商断电你停几小时才赔」", "企業客戶談網絡險，先問「供應商斷電你停幾小時才賠」"),
    a_mid=("等待期与第三方故障条款，纳入保单复核清单", "等待期與第三方故障條款，納入保單覆核清單"),
    a_lead=("关注云集中风险的结构化再保与参数型产品演进", "關注雲集中風險的結構化再保與參數型產品演進"),
    a_cross=("家办旗下运营公司的 IT 外包依赖度，属投前尽调项", "家辦旗下運營公司的 IT 外包依賴度，屬投前盡調項"),
    r=(2, 2, 2, 1),
    src="Insurance Business Asia", lang="zh+en",
    boards=["tech", "market"], themes=["cyber", "cloud-concentration", "business-interruption"],
    tags_sc=["网络险", "云集中风险", "业务中断", "等待期", "第三方故障"],
    tags_tc=["網絡險", "雲集中風險", "業務中斷", "等待期", "第三方故障"],
    kind="news", pub="2026-11-13",
    url="https://www.insurancebusinessmag.com/asia/news/breaking-news/microsoft-email-teams-goes-out-globally-puts-cloud-concentration-risk-back-on-brokers-radar-597216.aspx",
))

# 5. 新加坡：财务顾问渠道首超银行
ITEMS.append(mk(
    id="ibm-singapore-fa-overtake-banks-20261113",
    score=66, sourceTier="media", sourceKey="insurancebusinessmag", verifyStatus="verified",
    t_sc="新加坡寿险渠道洗牌：财务顾问首超银行　贡献九个月加权新保费增长近三分之二",
    t_tc="新加坡壽險渠道洗牌：財務顧問首超銀行　貢獻九個月加權新保費增長近三分之二",
    s_sc="新加坡寿险协会 11 月 12 日数据：2026 年前九个月，财务顾问渠道加权新保费升 27.9% 至 20.7 亿新元、市占 37.9%，首次超过银行的 17.9 亿新元（32.7%）；行业加权新保费升 15% 至 54.7 亿新元，但第三季增速降至 4.2%。增长主要来自投连险（ILP），其占比由 43% 升至 46%。新加坡金管局已确认将为 ILP 引入标准化产品资料概要，并重申适当性评估与提前退保损失披露责任；线上直销保单数则跌 29.5%。",
    s_tc="新加坡壽險協會 11 月 12 日數據：2026 年前九個月，財務顧問渠道加權新保費升 27.9% 至 20.7 億新元、市佔 37.9%，首次超過銀行的 17.9 億新元（32.7%）；行業加權新保費升 15% 至 54.7 億新元，但第三季增速降至 4.2%。增長主要來自投連險（ILP），其佔比由 43% 升至 46%。新加坡金管局已確認將為 ILP 引入標準化產品資料概要，並重申適當性評估與提前退保損失披露責任；線上直銷保單數則跌 29.5%。",
    w_sc="同一件事在两地被讲成两个故事：香港讲银保与高客，新加坡的独立顾问渠道正在反超银行。对 IFA 这是有利证据——顾问渠道的份额可以被专业度抢回来，前提是产品结构（ILP）与适当性说明跟得上监管。",
    w_tc="同一件事在兩地被講成兩個故事：香港講銀保與高客，新加坡的獨立顧問渠道正在反超銀行。對 IFA 這是有利證據——顧問渠道的份額可以被專業度搶回來，前提是產品結構（ILP）與適當性說明跟得上監管。",
    a_front=("与客户谈投连险，先说费用与提前退保损失，再谈回报", "與客戶談投連險，先說費用與提前退保損失，再談回報"),
    a_mid=("ILP 适当性与产品资料概要是新加坡先行版，可预判香港口径", "ILP 適當性與產品資料概要是新加坡先行版，可預判香港口徑"),
    a_lead=("关注顾问渠道份额回升的可复制条件：专业度而非激励", "關注顧問渠道份額回升的可複製條件：專業度而非激勵"),
    a_cross=None,
    r=(2, 2, 3, 0),
    src="Insurance Business Asia", lang="zh+en",
    boards=["market", "insurer"], themes=["distribution", "ilp", "regulation"],
    tags_sc=["渠道结构", "投连险", "财务顾问", "适当性", "新加坡"],
    tags_tc=["渠道結構", "投連險", "財務顧問", "適當性", "新加坡"],
    kind="news", pub="2026-11-13",
    url="https://www.insurancebusinessmag.com/asia/news/life-insurance/financial-advisers-overtake-banks-in-singapore-life-insurance-sales-597188.aspx",
))


def main():
    data = json.load(open(LIVE, encoding="utf-8"))
    items = data["items"]
    existing_ids = {i["id"] for i in items}
    existing_urls = {i.get("originalUrl") for i in items}

    added, skipped = [], []
    for it in ITEMS:
        if it["id"] in existing_ids:
            skipped.append((it["id"], "id dup"))
            continue
        if it["originalUrl"] in existing_urls:
            skipped.append((it["id"], "url dup"))
            continue
        added.append(it)

    if not added:
        print("no new items")
        return

    data["items"] = added + items
    n = len(data["items"])
    data["meta"]["itemCount"] = n
    data["meta"]["generatedAt"] = NOW
    data["meta"]["windowNote"] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}

    json.dump(data, open(LIVE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"inserted {len(added)} items -> total {n}")
    for it in added:
        print("  +", it["publishedAt"], it["sourceKey"], it["title"]["sc"][:60])
    for s in skipped:
        print("  skip", s)


if __name__ == "__main__":
    main()
