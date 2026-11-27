#!/usr/bin/env python3
"""
生成 data/docs.json —— 监管文档库索引

输入：data/_ia_docs/latest.json（ia-doc-watch.py 抓到的列表）
     + 本文件里的 DOC_META（每份的「要做什么」、场景、主题、半衰期、角色影响）
输出：data/docs.json

设计要点（详见 skill hk-intel-site-ops）：
  · 文档不按时间排，按「场景 + 主题」组织；halflife 记录衰减速度
  · demand 写「要做什么」而不是「讲了什么」——这是整张卡片的价值所在
  · status/replaces 支持版本链（旧文档标红但不删，可直接下载）
"""
import json
import os
import re

try:
    import opencc
    _cc = opencc.OpenCC("s2hk")
except ImportError:
    _cc = None


def tc(s):
    return _cc.convert(s) if _cc else s


# ── 场景（页面第一视图）────────────────────────────────────
SCENARIOS = {
    "annual":         {"sc": "每年必做", "tc": "每年必做"},
    "incident-prep":  {"sc": "出事前准备", "tc": "出事前準備"},
    "daily-sign":     {"sc": "日常签单动作", "tc": "日常簽單動作"},
    "hni-cross":      {"sc": "高客与跨境", "tc": "高客與跨境"},
    "team-mgmt":      {"sc": "团队管理", "tc": "團隊管理"},
    "claims-service": {"sc": "理赔与保全", "tc": "理賠與保全"},
    "corporate":      {"sc": "公司层面", "tc": "公司層面"},
}

# ── 通函：(文件名词根, demand简, 场景, 主题, 半衰期, (前线,中后台,管理层,跨境)) ──
CIRCULARS = [
    ("cir_dd_20.11.2026",
     "对照 GL20 逐项核六项内控：备份与复原要能证明、演练与渗透测试要有记录、第三方与集团依赖要画得出来；适用机构善用 CISP 情报平台",
     ["incident-prep"], ["cyber", "compliance"], "long", (2, 3, 3, 2)),
    ("Cir_dd_5.11.2026",
     "经纪公司改经 IIC 平台电子提交财务报表，硬本并行至 2027 年 10 月",
     ["annual"], ["reporting", "compliance"], "long", (1, 3, 1, 0)),
    ("Cir_dd_29.7.2026",
     "四机构首轮网络测绘成果：认清你与同业共用的第三方与单点故障面——最大节点是云、数据中心与网安方案供应商",
     ["incident-prep"], ["cyber", "third-party-risk"], "long", (1, 3, 3, 2)),
    ("Cir_dd_29.05.2026",
     "读 13 主题查察发现（附件近 1,800 行）：财务需要分析、保费收取、冷静期交付、理赔、孤儿保单五项最贴日常，逐条对照留痕",
     ["team-mgmt"], ["conduct", "compliance"], "long", (3, 3, 3, 2)),
    ("Cir_dd_13.05.2026",
     "招聘与入职阶段做银行—保险跨行业背景查核，确认对方在职纪录",
     ["team-mgmt"], ["recruitment", "conduct"], "long", (1, 3, 2, 0)),
    ("Cir_dd_31032026",
     "按新程序申报 CPD（2025-2026 考核期起适用），留意申报时点与留证",
     ["annual"], ["cpd", "compliance"], "long", (3, 2, 2, 1)),
    ("Cir_dd_14102025",
     "经纪公司负责人的强制 CPD 培训：具体场次、考核期与豁免情形",
     ["annual"], ["cpd", "compliance"], "long", (1, 2, 3, 0)),
    ("Cir_dd_20.11.2025",
     "中介入职流程须纳入背景查核计划，评估适当人选资格",
     ["team-mgmt"], ["recruitment", "conduct"], "long", (1, 3, 2, 0)),
    ("Cir_dd_11072025",
     "按修订后 GL24 执行持牌中介持续专业培训",
     ["annual"], ["cpd", "compliance"], "long", (3, 2, 2, 1)),
    ("Cir_dd_01092025",
     "转介费监管期望：转介不得变相成销售，须披露身份与记录报酬；按此检视转介安排",
     ["team-mgmt"], ["commission", "conduct"], "long", (2, 3, 3, 1)),
    ("Cir_dd_30.7.2025",
     "佣金摊分实务守则：报酬结构不得诱导短期销售或前期冲量",
     ["team-mgmt"], ["commission", "conduct"], "long", (2, 3, 3, 1)),
    ("Cir_dd_6.6.2025",
     "2024-2025 考核期 CPD 合规申报的具体要求与格式",
     ["annual"], ["cpd", "compliance"], "medium", (3, 2, 2, 1)),
    ("Cir_dd_07032025",
     "中介管理控能关键人员 CPD 试点首轮安排",
     ["annual"], ["cpd", "compliance"], "medium", (0, 2, 3, 0)),
    ("Circular_First_run_of_RO-CPD",
     "经纪负责人 CPD 试点首轮安排与参与方式",
     ["annual"], ["cpd", "compliance"], "medium", (1, 2, 3, 0)),
    ("Circular_ROCPD_20250711",
     "经纪公司负责人强制 CPD 的生效要求与责任",
     ["annual"], ["cpd", "compliance"], "long", (1, 2, 3, 0)),
    ("Circular_10072026",
     "演示利率上限的复核机制解读：产品演示数字须按此口径，超上限的说明要有依据",
     ["daily-sign"], ["product", "illustration"], "long", (2, 2, 2, 1)),
    ("Circular_28022025",
     "利益演示利率上限实务守则：分红与万能演示数字不得超上限",
     ["daily-sign"], ["product", "illustration"], "long", (3, 2, 2, 1)),
    ("Circular_20082026",
     "保费融资业务观察：检视宣传口径（勿写杠杆倍数、勿只讲「付一成」）与负担能力评估是否计入房贷等既有债务",
     ["daily-sign"], ["premium-financing", "conduct"], "long", (3, 3, 3, 2)),
    ("Cir_dd_05.06.2026",
     "按金管局口径检视报酬结构，避免奖励设计变相鼓励销售误导",
     ["corporate"], ["remuneration", "governance"], "long", (0, 2, 2, 0)),
    ("Circular_dd_20260305",
     "生成式 AI 的使用边界：沙盒扩围、风险治理、问责与人工复核要求",
     ["incident-prep"], ["ai", "compliance"], "long", (2, 3, 3, 2)),
    ("20260224_KPIM_Handbook",
     "中介管理控能关键人员（KPIM）按手册履职，明确管控职责与汇报线",
     ["team-mgmt"], ["governance", "conduct"], "long", (0, 3, 3, 0)),
    ("Cir_dd_29.05.2026_Annex", None, None, None, None, None),  # 占位，附件不单独成条
    ("20260930_Circular_Conduct_In_Focus_Issue_13",
     "读第 13 期监管通讯：经纪公司负责人任期过短被视作操守风险，另有营销选择性数据与伪造文件个案",
     ["team-mgmt"], ["conduct", "compliance"], "medium", (2, 2, 2, 1)),
    ("20260327_Circular_Conduct_In_Focus_Issue_12",
     "读第 12 期监管通讯的查察与执法要点",
     ["team-mgmt"], ["conduct", "compliance"], "medium", (2, 2, 2, 1)),
    ("20250930_Circular_Conduct_In_Focus_Issue_11",
     "读第 11 期监管通讯的执法与操守个案",
     ["team-mgmt"], ["conduct", "compliance"], "medium", (2, 2, 2, 1)),
    ("20250328_Circular_Conduct_In_Focus_Issue_10",
     "读第 10 期监管通讯的执法与操守要点",
     ["team-mgmt"], ["conduct", "compliance"], "medium", (2, 2, 2, 1)),
    ("Circular_20260831_Integrity_Management_Policy",
     "建立诚信管理政策，附件含政策范本与实施要求",
     ["team-mgmt"], ["conduct", "governance"], "long", (1, 2, 2, 1)),
    ("Circular_19092025",
     "保险产品命名要求：名称不得暗示保证收益或误导投保人",
     ["daily-sign"], ["product", "conduct"], "long", (2, 2, 2, 1)),
    ("Circular_20250313_IUL",
     "指数型万能寿险（IUL）联合通函：面向专业投资者以外客户的销售限制与披露要求",
     ["hni-cross"], ["product", "hni"], "long", (2, 2, 3, 3)),
    ("Circular_20250206",
     "理赔管理发现与建议：理赔时限、进度沟通与拒赔理由说明的实操要求",
     ["claims-service"], ["claims", "conduct"], "long", (2, 3, 2, 1)),
    ("Circular_20250808_First_Year_Public_Disclosure",
     "采用风险资本制度首年的公开披露要求",
     ["corporate"], ["capital", "reporting"], "medium", (0, 1, 2, 0)),
    ("Circular_20250620_GL36",
     "估值与资本要求（GL36）的适用与计算",
     ["corporate"], ["capital", "actuarial"], "long", (0, 1, 2, 0)),
    ("Circular_20250919_GL34",
     "分红基金治理与管理（GL34）：分红政策的公平性与持份者沟通",
     ["corporate"], ["product", "governance"], "long", (1, 2, 3, 1)),
    ("Circular_20260206_GL16_and_GL34",
     "承保长期业务与分红基金治理按修订后的 GL16/GL34 执行",
     ["corporate"], ["product", "actuarial"], "long", (1, 2, 2, 1)),
    ("cir_20250523",
     "非香港险企迁册来港的指引与释义（公司层面决策参考）",
     ["corporate"], ["corporate", "cross-border"], "long", (0, 1, 2, 1)),
    ("Circular__06062025",
     "集团监管制度下的申报模板（指定保险控股公司适用）",
     ["corporate"], ["reporting", "group"], "long", (0, 1, 2, 0)),
    ("20261002_Circulars_DPP_and_EAP",
     "纪律审裁小组与专家顾问小组的委任与续任名单（机构无需动作）",
     ["corporate"], ["enforcement"], "medium", (0, 0, 1, 0)),
]

# ── 指引：ref → (demand简, 场景, 主题, 半衰期, roles) ──
GUIDELINES = {
    "GL1": ("授权指引：申请经营保险业务的门槛与流程", ["corporate"], ["authorization"], "long", (0, 0, 1, 0)),
    "GL2": ("一般业务保险的估值规则", ["corporate"], ["actuarial", "capital"], "long", (0, 1, 1, 0)),
    "GL3": ("反洗钱与反恐融资：客户尽职审查、持续监察与可疑交易报告", ["daily-sign"], ["aml", "compliance"], "long", (2, 3, 2, 2)),
    "GL3A": ("对中介行使罚款权力的指引", ["corporate"], ["enforcement"], "long", (1, 1, 2, 0)),
    "GL4": ("「适当人选」准则（公司层面）：控股人、董事与管控人员的资格", ["corporate"], ["governance"], "long", (0, 1, 2, 0)),
    "GL5": ("经营保险业务的授权申请要求", ["corporate"], ["authorization"], "long", (0, 0, 1, 0)),
    "GL6": ("按揭担保业务的准备金要求", ["corporate"], ["actuarial", "capital"], "long", (0, 1, 1, 0)),
    "GL7": ("长期业务 G 类的准备金规定", ["corporate"], ["actuarial"], "long", (0, 1, 1, 0)),
    "GL8": ("互联网保险活动：网上销售与线上投保的管控、披露与留痕", ["daily-sign"], ["digital", "conduct"], "long", (2, 2, 2, 1)),
    "GL9": ("雇主责任业务的保险负债精算检讨", ["corporate"], ["actuarial"], "long", (0, 1, 1, 0)),
    "GL10": ("企业管治：董事会职责、制衡机制、举报与纠正程序", ["corporate"], ["governance"], "long", (0, 2, 3, 0)),
    "GL11": ("C 类相连长期业务的分类规则", ["corporate"], ["product"], "long", (0, 1, 1, 0)),
    "GL12": ("与关联公司安排再保险的监管要求", ["corporate"], ["reinsurance", "governance"], "long", (0, 1, 2, 0)),
    "GL13": ("保险公司的资产管理要求", ["corporate"], ["capital", "investment"], "long", (0, 1, 2, 0)),
    "GL14": ("外包：第三方服务的尽职调查、合约条款、监督与退出安排", ["incident-prep"], ["third-party-risk", "compliance"], "long", (1, 3, 3, 2)),
    "GL15": ("C 类业务的承保要求", ["corporate"], ["product", "underwriting"], "long", (0, 1, 1, 0)),
    "GL16": ("长期保险（非 C 类）的承保规定", ["corporate"], ["product", "underwriting"], "long", (0, 1, 1, 0)),
    "GL17": ("再保险安排的监管要求与自留额", ["corporate"], ["reinsurance"], "long", (0, 1, 1, 0)),
    "GL18": ("对公司行使罚款权力的指引", ["corporate"], ["enforcement"], "long", (0, 0, 1, 0)),
    "GL19": ("合资格延期年金（QDAP）的产品要求与销售", ["daily-sign"], ["product", "annuity"], "long", (2, 2, 2, 1)),
    "GL20": ("网络安全：治理、风险识别与评估、控制措施、事故响应与通报；网络韧性通函的核对基准", ["incident-prep"], ["cyber", "compliance"], "long", (2, 3, 3, 2)),
    "GL21": ("企业风险管理（ERM）：风险偏好框架、压力测试与情景分析", ["incident-prep"], ["risk", "governance"], "long", (1, 3, 3, 2)),
    "GL22": ("对管控人员行使罚款权力的指引", ["corporate"], ["enforcement"], "long", (0, 0, 1, 0)),
    "GL23": ("持牌保险中介的「适当人选」准则：学历、经验、品格与财务稳健", ["team-mgmt"], ["recruitment", "compliance"], "long", (2, 3, 2, 0)),
    "GL24": ("持牌中介持续专业培训（CPD）：时数、范畴与申报", ["annual"], ["cpd", "compliance"], "long", (3, 2, 2, 1)),
    "GL25": ("赠品提供：不得以赠品变相诱导投保，须符合价值与披露限制", ["daily-sign"], ["conduct", "product"], "long", (3, 2, 2, 1)),
    "GL26": ("投连险（ILAS）销售：适当性评估、风险披露与销售流程", ["daily-sign"], ["product", "conduct"], "long", (3, 2, 2, 2)),
    "GL27": ("长期保单替换：替换前须做比较、披露不利之处并留痕", ["daily-sign"], ["conduct", "product"], "long", (3, 2, 3, 2)),
    "GL28": ("利益演示：保证与非保证部分的呈现、乐观悲观情景与警示语", ["daily-sign"], ["product", "illustration"], "long", (3, 2, 2, 1)),
    "GL29": ("冷静期：保单交付、冷静期起算与退保权利", ["daily-sign"], ["conduct", "product"], "long", (3, 2, 2, 1)),
    "GL30": ("财务需要分析（FNA）：必须做、必须记录、必须与建议一致", ["daily-sign"], ["conduct", "compliance"], "long", (3, 3, 3, 2)),
    "GL31": ("医疗保险业务：核保、理赔、披露与产品设计", ["claims-service"], ["product", "claims"], "long", (2, 3, 2, 1)),
}


# ── 跨机构文档（HKMA / PCPD）—— 手工维护，补「高客与跨境」场景 ──
# 这些源没有稳定的列表页可 diff（HKMA brdr 是 docId 系统、PCPD 站点改版过），
# 所以按「已知文档」维护，新增时手工添一条。
EXTERNAL_DOCS = [
    dict(
        org="pcpd", type="guideline", ref="跨境轉移指引", date="2014-12-01",
        title_sc="保障个人资料：跨境资料转移指引（含建议合约条文范本）",
        title_tc="保障個人資料：跨境資料轉移指引（含建議合約條文範本）",
        demand="客户资料只要离开香港（含集团海外系统、云端、内地合作方），须先确认符合《私隐条例》第 33 条例外；实务上以书面同意＋建议合约条文范本为准，并保留跨境资料清单",
        scenario=["hni-cross"], topics=["privacy", "cross-border", "compliance"],
        halflife="long", roles=(2, 3, 3, 3),
        url="https://www.pcpd.org.hk/tc_chi/resources_centre/publications/guidance/files/GN_crossborder_c.pdf",
    ),
    dict(
        org="pcpd", type="guideline", ref="大灣區標準合同", date="2023-12-01",
        title_sc="跨境资料转移指引：《粤港澳大湾区（内地、香港）个人信息跨境流动标准合同》",
        title_tc="跨境資料轉移指引：《粵港澳大灣區（內地、香港）個人信息跨境流動標準合同》",
        demand="客户资料转往大湾区内地城市时，可用《大湾区标准合同》替代逐份书面同意；须签署标准合同并完成合规备案与个人信息保护影响评估",
        scenario=["hni-cross"], topics=["privacy", "cross-border", "gba"],
        halflife="long", roles=(1, 3, 3, 3),
        url="https://www.pcpd.org.hk/tc_chi/resources_centre/publications/files/standard_contract_gba.pdf",
    ),
    dict(
        org="hkma", type="circular", ref="20260522-9-EN", date="2026-05-22",
        title_sc="金管局通函：投资账户开户与客户关系维护的应采管控（含内地投资者额外措施）",
        title_tc="金管局通函：投資帳戶開立與客戶關係維護的應採管控（含內地投資者額外措施）",
        demand="内地客户开投资账户须做额外措施：核实资金来源、禁止代客开户、识别可疑或伪造文件；跨境理财通南向通客户沿用现有安排、不适用该附件",
        scenario=["hni-cross"], topics=["onboarding", "cross-border", "aml"],
        halflife="long", roles=(2, 2, 3, 3),
        url="https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20260522-9-EN/20260522-9-EN.pdf",
    ),
]


def norm(s):
    """把文件名/ref 归一化，便于匹配"""
    s = re.sub(r"\.pdf$", "", s, flags=re.I)
    s = re.sub(r"_(Eng|Chi|ENG|中文|English)$", "", s, flags=re.I)
    return s.lower()


def clean_title(s):
    """清理列表页标题：HTML 实体 + 「中文譯本: …」/「Attachment: …」这类后缀

    列表页原文形如：
      Conduct in Focus - September 2026 中文譯本 : 監管通訊- 2026年9月
      Reference Checking Schemes … 中文譯本: 保險中介人背景查核計劃 Attachment: …
    这些后缀是列表页的排版产物，不是文档标题的一部分。
    """
    import html as _html
    s = _html.unescape(s or "")
    s = re.sub(r"\s*中文[譯译]本\s*[:：].*$", "", s)
    s = re.sub(r"\s*Attachment\s*[:：].*$", "", s, flags=re.I)
    s = re.sub(r"\s+", " ", s).strip(" -–—:")
    return s


def main():
    src = json.load(open("data/_ia_docs/latest.json"))
    out = []

    # 通函
    circ_map = {}
    for d in src:
        if d["kind"] != "circular":
            continue
        fn = d["pdf"].split("/")[-1]
        circ_map[norm(fn)] = d

    used = set()
    for root, demand, scen, topics, half, roles in CIRCULARS:
        if demand is None:
            continue
        key = norm(root)
        match = None
        for fn, d in circ_map.items():
            if fn.startswith(key) or key in fn:
                match = d
                used.add(fn)
                break
        if not match:
            print(f"  [!] 未匹配: {root}")
            continue
        out.append({
            "id": "ia-cir-" + re.sub(r"[^a-z0-9]+", "-", key).strip("-"),
            "org": "ia",
            "type": "circular",
            "ref": None,
            "publishedAt": to_iso(match.get("date")),
            "title": {"sc": clean_title(match["subject"]), "tc": tc(clean_title(match["subject"]))},
            "demand": {"sc": demand, "tc": tc(demand)},
            "scenario": scen,
            "topics": topics,
            "halflife": half,
            "status": "active",
            "replaces": None,
            "supersededBy": None,
            "rolesImpact": dict(zip(["front", "midback", "lead", "cross"], roles)),
            "sourceUrl": match["pdf"],
            "attachments": match.get("attachments") or [],
        })

    # 指引
    gl_map = {}
    for d in src:
        if d["kind"] == "guideline":
            gl_map[d["ref"]] = d
    for ref, (demand, scen, topics, half, roles) in GUIDELINES.items():
        d = gl_map.get(ref)
        if not d:
            print(f"  [!] 未匹配指引: {ref}")
            continue
        out.append({
            "id": "ia-gl-" + ref.lower().replace("gl", ""),
            "org": "ia",
            "type": "guideline",
            "ref": ref,
            "publishedAt": None,
            "title": {"sc": clean_title(d["subject"]), "tc": tc(clean_title(d["subject"]))},
            "demand": {"sc": demand, "tc": tc(demand)},
            "scenario": scen,
            "topics": topics,
            "halflife": half,
            "status": "active",
            "replaces": None,
            "supersededBy": None,
            "rolesImpact": dict(zip(["front", "midback", "lead", "cross"], roles)),
            "sourceUrl": d["pdf"],
            "attachments": d.get("attachments") or [],
        })

    # 跨机构文档（HKMA / PCPD）
    for e in EXTERNAL_DOCS:
        out.append({
            "id": f"{e['org']}-{e['type']}-" + re.sub(r"[^a-z0-9]+", "-", e["ref"].lower()).strip("-"),
            "org": e["org"],
            "type": e["type"],
            "ref": e["ref"],
            "publishedAt": e["date"],
            "title": {"sc": e["title_sc"], "tc": e["title_tc"]},
            "demand": {"sc": e["demand"], "tc": tc(e["demand"])},
            "scenario": e["scenario"],
            "topics": e["topics"],
            "halflife": e["halflife"],
            "status": "active",
            "replaces": None,
            "supersededBy": None,
            "rolesImpact": dict(zip(["front", "midback", "lead", "cross"], e["roles"])),
            "sourceUrl": e["url"],
            "attachments": [],
        })

    # 排序：场景内按日期倒序，指引排后面
    out.sort(key=lambda x: (x["type"] != "circular", x["publishedAt"] or "0000", x["id"]))

    doc = {
        "meta": {
            "updatedAt": "2026-11-27T18:00:00+08:00",
            "total": len(out),
            "disclaimer": {
                "sc": "本库仅为公开监管文件的索引与导读，供专业参考，不构成法律或合规意见，也不构成任何销售或投资建议。文件内容以监管机构发布的原文为准；如导读与原文有出入，一律以原文为准。使用前请自行核对最新版本——监管文件会更新、取代或撤销，本库虽尽力标注状态，但无法保证实时。",
                "tc": tc("本库仅为公开监管文件的索引与导读，供专业参考，不构成法律或合规意见，也不构成任何销售或投资建议。文件内容以监管机构发布的原文为准；如导读与原文有出入，一律以原文为准。使用前请自行核对最新版本——监管文件会更新、取代或撤销，本库虽尽力标注状态，但无法保证实时。"),
            },
        },
        "scenarios": SCENARIOS,
        "docs": out,
    }
    json.dump(doc, open("data/docs.json", "w"), ensure_ascii=False, indent=1)
    print(f"\n生成 data/docs.json：{len(out)} 条（通函 {sum(1 for x in out if x['type']=='circular')} + 指引 {sum(1 for x in out if x['type']=='guideline')}）")


def to_iso(s):
    """'20 November 2026' → '2026-11-20'"""
    if not s:
        return None
    m = re.match(r"(\d{1,2})\s+(\w+)\s+(\d{4})", s.strip())
    if not m:
        return None
    day, mon, yr = m.groups()
    months = {m2: i for i, m2 in enumerate(
        ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"], 1)}
    mn = months.get(mon.capitalize())
    if not mn:
        return None
    return f"{yr}-{mn:02d}-{int(day):02d}"


if __name__ == "__main__":
    main()
