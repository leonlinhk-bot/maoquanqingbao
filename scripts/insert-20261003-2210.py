# -*- coding: utf-8 -*-
import json, datetime

NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).replace(microsecond=0).isoformat()

def item(**kw):
    base = {
        "clusterCount": 1,
        "score": 65,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "contentKind": "news",
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 1},
        "boards": ["market"],
        "themes": ["apac"],
        "tags": {"sc": [], "tc": []},
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False,
        "ingestedAt": NOW,
    }
    base.update(kw)
    return base

items = []

# 1) InsuranceAsia News Full Capacity weekly briefing (Oct 3)
items.append(item(
    id="ian-fullcapacity-weekly-apac-20261003",
    score=68,
    sourceTier="media",
    sourceKey="insuranceasianews",
    publishedAt="2026-10-03T08:00:00+08:00",
    originalUrl="https://insuranceasianews.com/irdais-reform-push-needs-a-finer-touch/",
    title={
        "sc": "亚太原保险周报（Full Capacity 10月3日）：新加坡 SG Re 获金管局原则批准设立再保险经纪；Tokio Marine 就 Greensill 案与瑞信实体和解；韩国 Lotte 损害保险10月中启动公开出售；伊藤忠增持美国保险科技 Moter [EN原文]",
        "tc": "亞太原保險週報（Full Capacity 10月3日）：新加坡 SG Re 獲金管局原則批准設立再保險經紀；Tokio Marine 就 Greensill 案與瑞信實體和解；韓國 Lotte 損害保險10月中啟動公開出售；伊藤忠增持美國保險科技 Moter [EN原文]",
    },
    summary={
        "sc": "InsuranceAsia News 10月3日刊出每周简报《Full Capacity》：①新加坡——韩国经纪集团 Simon Global 旗下 SG Re 获新加坡金管局原则批准（in-principle approval），将以亚洲区内条约再保险为主，重点日本、韩国与东南亚；②和解——Tokio Marine 就 Greensill Capital 倒闭相关诉讼与瑞信（Credit Suisse）实体达成和解，此前澳洲 IAG 旗下 IAL 已披露和解；③并购——JKL Partners 在与新韩金融集团独家谈判破裂后，拟于10月中对 Lotte 损害保险启动公开出售；同周 Marsh 完成收购日本能源商 Eneos 的保险中介业务，改以 EMIS Insurance Services 运作、Hiroyuki Hata 任社长；④资本——伊藤忠（Itochu）增持美国保险科技 Moter Technologies，其保险版图另含今年成立的开曼自保再保 Guna Re 及泰国 Thaivivat 20% 股权；⑤监管——印度 IRDAI 拟对中介报酬设产品级硬上限、五年内削减逾三成费用（EoM）上限，印度经纪协会 IBAI 与律所 JSA 认为将压缩小城镇服务人力、并把不当销售推向地下。 [EN原文]",
        "tc": "InsuranceAsia News 10月3日刊出每週簡報《Full Capacity》：①新加坡——韓國經紀集團 Simon Global 旗下 SG Re 獲新加坡金管局原則批准（in-principle approval），將以亞洲區內條約再保險爲主，重點日本、韓國與東南亞；②和解——Tokio Marine 就 Greensill Capital 倒閉相關訴訟與瑞信（Credit Suisse）實體達成和解，此前澳洲 IAG 旗下 IAL 已披露和解；③併購——JKL Partners 在與新韓金融集團獨家談判破裂後，擬於10月中對 Lotte 損害保險啟動公開出售；同週 Marsh 完成收購日本能源商 Eneos 的保險中介業務，改以 EMIS Insurance Services 運作、Hiroyuki Hata 任社長；④資本——伊藤忠（Itochu）增持美國保險科技 Moter Technologies，其保險版圖另含今年成立的開曼自保再保 Guna Re 及泰國 Thaivivat 20% 股權；⑤監管——印度 IRDAI 擬對中介報酬設產品級硬上限、五年內削減逾三成費用（EoM）上限，印度經紀協會 IBAI 與律所 JSA 認爲將壓縮小城鎮服務人力、並把不當銷售推向地下。 [EN原文]",
    },
    why={
        "sc": "这条周报把本周亚洲最值得跟进的三条主线压在一处，对香港团队有直接可迁移价值：一是分销成本监管正在从「渠道费率上限」走向「产品级硬上限＋费用审计」，与香港收窄转介费、佣金首年分摊的思路同源，前线的报酬结构与服务年限会被继续绑定；二是韩国大型险企 Lotte 损害保险进入公开出售，说明亚洲保险资产仍在换手，客户问到「公司会不会换股东」时应以公开披露为准而不是品牌印象；三是再保经纪、自保与 ILS 通道继续扩容（SG Re 获批、伊藤忠自保再保），与香港推动 ILS 与专属自保的政策方向一致，是经纪渠道可以留意的增量信息面。",
        "tc": "這條週報把本週亞洲最值得跟進的三條主線壓在一處，對香港團隊有直接可遷移價值：一是分銷成本監管正在從「渠道費率上限」走向「產品級硬上限＋費用審計」，與香港收窄轉介費、佣金首年分攤的思路同源，前線的報酬結構與服務年限會被繼續綁定；二是韓國大型險企 Lotte 損害保險進入公開出售，說明亞洲保險資產仍在換手，客戶問到「公司會不會換股東」時應以公開披露爲準而不是品牌印象；三是再保經紀、自保與 ILS 通道繼續擴容（SG Re 獲批、伊藤忠自保再保），與香港推動 ILS 與專屬自保的政策方向一致，是經紀渠道可以留意的增量信息面。",
    },
    actions={
        "front": {"sc": "客户问及亚洲险企股东或股权变动时，只引述监管与公司公开披露信息，不作兑付能力或回报承诺", "tc": "客戶問及亞洲險企股東或股權變動時，只引述監管與公司公開披露資訊，不作兌付能力或回報承諾"},
        "midback": {"sc": "把「中介报酬监管收紧」列为代理人与经纪培训的固定专题，说明报酬与长期服务绑定的趋势", "tc": "把「中介報酬監管收緊」列爲代理人與經紀培訓的固定專題，說明報酬與長期服務綁定的趨勢"},
        "lead": {"sc": "跟踪区内保险资产换手与再保资本扩容，评估对经纪渠道合作方与产品供给的影响", "tc": "跟蹤區內保險資產換手與再保資本擴容，評估對經紀渠道合作方與產品供給的影響"},
        "cross": {"sc": "团队涉新加坡、印度、韩国业务时，以当地监管原文与公司公告为准，不引用二手摘要作合规依据", "tc": "團隊涉新加坡、印度、韓國業務時，以當地監管原文與公司公告爲準，不引用二手摘要作合規依據"},
    },
    rolesImpact={"front": 1, "midback": 2, "lead": 2, "cross": 2},
    boards=["insurer", "market"],
    themes=["manda", "distribution", "reg", "capital", "apac", "people"],
    tags={"sc": ["亚太原保险", "新加坡SG Re", "Tokio Marine", "Greensill", "Lotte损害保险", "IRDAI", "分销成本", "伊藤忠"], "tc": ["亞太原保險", "新加坡SG Re", "Tokio Marine", "Greensill", "Lotte損害保險", "IRDAI", "分銷成本", "伊藤忠"]},
    source={"sc": "InsuranceAsia News 2026-10-03 08:00（每周简报 Full Capacity）[EN原文]", "tc": "InsuranceAsia News 2026-10-03 08:00（每週簡報 Full Capacity）[EN原文]", "lang": "en"},
))

# 2) SCMP: Ping An Bank AI governance rules (Oct 3)
items.append(item(
    id="scmp-pingan-bank-ai-management-rules-20261003",
    score=66,
    verifyStatus="pending",
    sourceTier="media",
    sourceKey="scmp",
    publishedAt="2026-10-03T11:00:00+08:00",
    originalUrl="https://www.scmp.com/business/banking-finance/article/3369577/more-chinese-banks-likely-adopt-ai-rules-after-ping-move-analysts",
    title={
        "sc": "南华早报：平安银行成首家正式制定人工智能管理制度的中国上市银行，分析师预期更多内地机构跟进 [EN原文]",
        "tc": "南華早報：平安銀行成首家正式制定人工智能管理制度的中國上市銀行，分析師預期更多內地機構跟進 [EN原文]",
    },
    summary={
        "sc": "南华早报10月3日11:00（香港时间）报道：平安银行在9月30日（周三）公告中表示，董事会已批准人工智能管理办法，成为首家正式就 AI 使用建立治理规则的中国上市银行；此举回应监管要求银行加强对 AI 应用的监督。报道指出完整规则尚未公开披露，分析师认为该行的做法为内地金融机构提供了可追随的早期基准，也界定了行业在 AI 应用上可以走到多远。 [EN原文]",
        "tc": "南華早報10月3日11:00（香港時間）報導：平安銀行在9月30日（週三）公告中表示，董事會已批准人工智能管理辦法，成爲首家正式就 AI 使用建立治理規則的中國上市銀行；此舉回應監管要求銀行加強對 AI 應用的監督。報導指出完整規則尚未公開披露，分析師認爲該行的做法爲內地金融機構提供了可追隨的早期基準，也界定了行業在 AI 應用上可以走到多遠。 [EN原文]",
    },
    why={
        "sc": "香港保险业正以 GenA.I. 沙盒++、保监局「人工智能促进计划」与《监管通讯》对聊天机械人的要求，把 AI 治理责任落到持牌人层级。内地出现「董事会层级 AI 管理办法」的样本，对团队有两层提示：一是 AI 治理会像合规手册一样成为董事会议题与可审计对象，不再只是科技部门事项；二是「谁对 AI 输出内容负责」的两地监管口径正在趋同——前线用 AI 生成话术、建议书或客户沟通材料时，人工复核与留痕将成为基本要求。",
        "tc": "香港保險業正以 GenA.I. 沙盒++、保監局「人工智能促進計劃」與《監管通訊》對聊天機械人的要求，把 AI 治理責任落到持牌人層級。內地出現「董事會層級 AI 管理辦法」的樣本，對團隊有兩層提示：一是 AI 治理會像合規手冊一樣成爲董事會議題與可審計對象，不再只是科技部門事項；二是「誰對 AI 輸出內容負責」的兩地監管口徑正在趨同——前線用 AI 生成話術、建議書或客戶溝通材料時，人工覆核與留痕將成爲基本要求。",
    },
    actions={
        "front": {"sc": "用 AI 生成客户材料时保留人工复核与修改记录，未经核对的 AI 输出不得直接对外发送", "tc": "用 AI 生成客戶材料時保留人工覆核與修改記錄，未經核對的 AI 輸出不得直接對外發送"},
        "midback": {"sc": "在内部规范中明确 AI 使用边界、审批路径、留痕与客户资料处理要求", "tc": "在內部規範中明確 AI 使用邊界、審批路徑、留痕與客戶資料處理要求"},
        "lead": {"sc": "把 AI 治理纳入管理层汇报项，明确责任人、问责口径与抽查机制", "tc": "把 AI 治理納入管理層匯報項，明確責任人、問責口徑與抽查機制"},
        "cross": {"sc": "涉及跨境客户资料时遵守两地数据与 AI 使用规定，不跨境传输未授权数据", "tc": "涉及跨境客戶資料時遵守兩地數據與 AI 使用規定，不跨境傳輸未授權數據"},
    },
    rolesImpact={"front": 2, "midback": 3, "lead": 2, "cross": 2},
    boards=["tech", "reg"],
    themes=["ai", "governance", "reg", "china", "tech"],
    tags={"sc": ["平安银行", "AI管理制度", "AI治理", "银行保险", "内地监管", "留痕"], "tc": ["平安銀行", "AI管理制度", "AI治理", "銀行保險", "內地監管", "留痕"]},
    source={"sc": "南华早报 SCMP 2026-10-03 11:00（香港时间）[EN原文]", "tc": "南華早報 SCMP 2026-10-03 11:00（香港時間）[EN原文]", "lang": "en"},
))

# 3) Insurance Business Asia: Hanwha Life / Acuon / KDIC (Oct 2 23:34)
items.append(item(
    id="ibm-hanwha-acuon-kdic-capital-scrutiny-20261002",
    score=64,
    sourceTier="media",
    sourceKey="insurancebusinessmag",
    publishedAt="2026-10-02T23:34:00+08:00",
    originalUrl="https://www.insurancebusinessmag.com/asia/news/life-insurance/regulators-close-in-on-hanwha-lifes-acuon-deal-as-capital-questions-stack-up-592146.aspx",
    title={
        "sc": "监管与资本双重审视下的韩华生命：4400亿韩元收购 Acuon Capital 遇 KDIC 减持时间表；同期承诺2500亿韩元增资证券子公司并参与 KDB 人寿竞标 [EN原文]",
        "tc": "監管與資本雙重審視下的韓華生命：4400億韓元收購 Acuon Capital 遇 KDIC 減持時間表；同期承諾2500億韓元增資證券子公司並參與 KDB 人壽競標 [EN原文]",
    },
    summary={
        "sc": "Insurance Business Asia 10月2日23:34（香港时间）报道：韩华生命9月30日董事会批准以4,400亿韩元收购 Acuon Capital 50.54%控股权（卖方为 EQT Partners，Centroid Investment Partners 作为财务投资人参与），监管批准待定；Acuon Capital 2026上半年资产约4.6万亿韩元，全资持有 Acuon 储蓄银行（约5.1万亿韩元），韩华计划与其现有储蓄银行合并为约6.5万亿韩元规模。报道指出韩国存款保险公司（KDIC）持有韩华生命10%股权（源于1999至2001年向当时已无力偿债的大韩生命注入3.55万亿韩元公共资金），其债券清偿基金将于2027年底到期，出清该股权的安排已列入 KDIC 2026年预算，目标价5,000韩元/股，而报道时股价约4,845韩元、完全回收公共资金需接近10,000韩元；收购增加风险加权资产并压缩 K-ICS 偿付能力比率，被形容为 KDIC 的股价问题。同一日董事会另向韩华投资证券增资2,500亿韩元（韩华资产管理再出资2,500亿，合计5,000亿韩元；证券端另考虑最多4,000亿韩元混合资本工具）。韩华生命亦与兴国生命、韩国投资控股一同就 KDB 人寿提交最终报价，市场估算 KDB 人寿可能需最多1万亿韩元后续注资。韩国金融委员会已将韩华列为2026年八家非控股金融集团之一，须按集团口径报告资本充足性与集团风险管理。报道强调本次交易并未公布保险分销安排的变动。 [EN原文]",
        "tc": "Insurance Business Asia 10月2日23:34（香港時間）報導：韓華生命9月30日董事會批准以4,400億韓元收購 Acuon Capital 50.54%控股權（賣方爲 EQT Partners，Centroid Investment Partners 作爲財務投資人參與），監管批准待定；Acuon Capital 2026上半年資產約4.6萬億韓元，全資持有 Acuon 儲蓄銀行（約5.1萬億韓元），韓華計劃與其現有儲蓄銀行合併爲約6.5萬億韓元規模。報導指出韓國存款保險公司（KDIC）持有韓華生命10%股權（源於1999至2001年向當時已無力償債的大韓生命注入3.55萬億韓元公共資金），其債券清償基金將於2027年底到期，出清該股權的安排已列入 KDIC 2026年預算，目標價5,000韓元/股，而報導時股價約4,845韓元、完全回收公共資金需接近10,000韓元；收購增加風險加權資產並壓縮 K-ICS 償付能力比率，被形容爲 KDIC 的股價問題。同一日董事會另向韓華投資證券增資2,500億韓元（韓華資產管理再出資2,500億，合計5,000億韓元；證券端另考慮最多4,000億韓元混合資本工具）。韓華生命亦與興國生命、韓國投資控股一同就 KDB 人壽提交最終報價，市場估算 KDB 人壽可能需最多1萬億韓元後續注資。韓國金融委員會已將韓華列爲2026年八家非控股金融集團之一，須按集團口徑報告資本充足性與集團風險管理。報導強調本次交易並未公佈保險分銷安排的變動。 [EN原文]",
    },
    why={
        "sc": "对香港团队有两点实用意义：一是「母公司同期多线资本承诺」是评估险企长期支持能力的关键，客户往往只看品牌与评级，忽略同一集团在证券、储蓄银行与并购上同时占用资本；二是监管机构自身持股（如 KDIC 的10%）会形成额外的时间压力与信息披露动力，与香港近年强调股东适当性、集团监管与资本充足性披露的逻辑一致。评级机构已提示母公司资产负债表恶化可能带来负面评级行动，这是前线在高客沟通中值得留意的背景变量，但不可用作兑付或回报承诺。",
        "tc": "對香港團隊有兩點實用意義：一是「母公司同期多線資本承諾」是評估險企長期支持能力的關鍵，客戶往往只看品牌與評級，忽略同一集團在證券、儲蓄銀行與併購上同時佔用資本；二是監管機構自身持股（如 KDIC 的10%）會形成額外的時間壓力與信息披露動力，與香港近年強調股東適當性、集團監管與資本充足性披露的邏輯一致。評級機構已提示母公司資產負債表惡化可能帶來負面評級行動，這是前線在高客溝通中值得留意的背景變量，但不可用作兌付或回報承諾。",
    },
    actions={
        "front": {"sc": "客户问及韩资或亚洲系险企稳健性时，引述评级机构与监管公开信息，不作兑付或回报保证", "tc": "客戶問及韓資或亞洲系險企穩健性時，引述評級機構與監管公開資訊，不作兌付或回報保證"},
        "midback": {"sc": "把「母公司同期资本承诺」列入保司背景复核清单，与偿付能力、评级并列观察", "tc": "把「母公司同期資本承諾」列入保司背景覆核清單，與償付能力、評級並列觀察"},
        "lead": {"sc": "涉韩国或新兴市场公司业务件时，要求确认股东结构、集团支持安排与监管状态", "tc": "涉韓國或新興市場公司業務件時，要求確認股東結構、集團支持安排與監管狀態"},
        "cross": {"sc": "跨境配置客户只以当地监管披露与评级报告为依据，不作跨市场产品比较", "tc": "跨境配置客戶只以當地監管披露與評級報告爲依據，不作跨市場產品比較"},
    },
    rolesImpact={"front": 1, "midback": 2, "lead": 2, "cross": 2},
    boards=["insurer", "market"],
    themes=["manda", "capital", "korea", "reg", "group"],
    tags={"sc": ["韩华生命", "Acuon Capital", "KDIC", "K-ICS", "KDB人寿", "集团资本"], "tc": ["韓華生命", "Acuon Capital", "KDIC", "K-ICS", "KDB人壽", "集團資本"]},
    source={"sc": "Insurance Business Asia 2026-10-02 23:34（香港时间）[EN原文]", "tc": "Insurance Business Asia 2026-10-02 23:34（香港時間）[EN原文]", "lang": "en"},
))

# 4) Artemis: casualty ILS exit mechanisms (Oct 2 21:00)
items.append(item(
    id="artemis-casualty-ils-exit-mechanisms-srs-20261002",
    score=70,
    sourceTier="pro",
    sourceKey="artemis",
    publishedAt="2026-10-02T21:00:00+08:00",
    originalUrl="https://www.artemis.bm/news/dependable-exit-mechanisms-the-key-breakthrough-in-casualty-ils-strategic-risk-solutions/",
    title={
        "sc": "Artemis：Strategic Risk Solutions 称「可靠的退出机制」是伤亡类 ILS 放量的关键突破，须在设计之初嵌入资本终局性 [EN原文]",
        "tc": "Artemis：Strategic Risk Solutions 稱「可靠的退出機制」是傷亡類 ILS 放量的關鍵突破，須在設計之初嵌入資本終局性 [EN原文]",
    },
    summary={
        "sc": "Artemis 10月2日报道：独立自保与再保管理服务商 Strategic Risk Solutions（SRS）认为，伤亡类（casualty）ILS 能否规模化，取决于平台能否提供可靠的退出机制，让投资者自成立之初就获得资本终局性。SRS 引用数据指 2026年中全球另类再保资本达创纪录1,445亿美元，其中巨灾债市场逾656亿美元、抵押再保侧挂车（sidecar）创纪录230亿美元。SRS 指出伤亡侧挂车仍属早期阶段但具战略意义：百慕达近期活动源于投资者对更长存续期伤亡风险的需求，同时新增产能也加剧了伤亡再保定价竞争。与财产巨灾不同，伤亡理赔须多年发展，准备金不确定性、社会通胀、诉讼趋势与对最终损失的判断差异会令抵押品释放与通勤（commutation）长期延后，对投资者形成「回报吸引但资本承诺期限难测」的根本张力。SRS 主张以 reinsurance-to-close、损失组合转移（LPT）、不利进展保障（ADC）、权益转让与买断投资人权益等机制，把不确定的长尾清算情景转化为清晰的资本释放路径，并把治理与问责、数据与准备金、抵押品与流动性、生命周期与退出准备列为平台四项设计纪律；文中并以 Enstar 在前端承保方案内嵌退出终局性、以及与 Artex 合作提供 ILS 退出方案为例。 [EN原文]",
        "tc": "Artemis 10月2日報導：獨立自保與再保管理服務商 Strategic Risk Solutions（SRS）認爲，傷亡類（casualty）ILS 能否規模化，取決於平台能否提供可靠的退出機制，讓投資者自成立之初就獲得資本終局性。SRS 引用數據指 2026年中全球另類再保資本達創紀錄1,445億美元，其中巨災債市場逾656億美元、抵押再保側掛車（sidecar）創紀錄230億美元。SRS 指出傷亡側掛車仍屬早期階段但具戰略意義：百慕達近期活動源於投資者對更長存續期傷亡風險的需求，同時新增產能也加劇了傷亡再保定價競爭。與財產巨災不同，傷亡理賠須多年發展，準備金不確定性、社會通脹、訴訟趨勢與對最終損失的判斷差異會令抵押品釋放與通勤（commutation）長期延後，對投資者形成「回報吸引但資本承諾期限難測」的根本張力。SRS 主張以 reinsurance-to-close、損失組合轉移（LPT）、不利進展保障（ADC）、權益轉讓與買斷投資人權益等機制，把不確定的長尾清算情景轉化爲清晰的資本釋放路徑，並把治理與問責、數據與準備金、抵押品與流動性、生命週期與退出準備列爲平台四項設計紀律；文中並以 Enstar 在前端承保方案內嵌退出終局性、以及與 Artex 合作提供 ILS 退出方案爲例。 [EN原文]",
    },
    why={
        "sc": "ILS 与另类资本正从财产巨灾向伤亡长尾延伸，这与香港推动保险相连证券（ILS）与专属自保、以及内地险企赴港发行巨灾债与侧挂车的政策方向同源。对经纪与高客团队而言，重点不是向客户销售 ILS，而是理解「资本市场的参与者在关心什么」——长尾风险的定价透明度、退出机制与资本终局性。这与分红保单中「非保证利益如何被长期资产管理与资本约束支撑」属于同一套讨论框架，有助于团队在客户面前把「非保证」讲清楚。",
        "tc": "ILS 與另類資本正從財產巨災向傷亡長尾延伸，這與香港推動保險相連證券（ILS）與專屬自保、以及內地險企赴港發行巨災債與側掛車的政策方向同源。對經紀與高客團隊而言，重點不是向客戶銷售 ILS，而是理解「資本市場的參與者在關心什麼」——長尾風險的定價透明度、退出機制與資本終局性。這與分紅保單中「非保證利益如何被長期資產管理與資本約束支撐」屬於同一套討論框架，有助於團隊在客戶面前把「非保證」講清楚。",
    },
    actions={
        "front": {"sc": "向高客解释分红与非保证利益时，区分资产端策略与保证承诺，不用资本市场收益率类比保单回报", "tc": "向高客解釋分紅與非保證利益時，區分資產端策略與保證承諾，不用資本市場收益率類比保單回報"},
        "midback": {"sc": "在培训材料中加入「资本与退出机制」基础概念，帮助前线理解产品背后的资产逻辑", "tc": "在培訓材料中加入「資本與退出機制」基礎概念，幫助前線理解產品背後的資產邏輯"},
        "lead": {"sc": "关注香港 ILS 与专属自保政策进展，评估对经纪渠道与高客服务的溢出机会", "tc": "關注香港 ILS 與專屬自保政策進展，評估對經紀渠道與高客服務的溢出機會"},
        "cross": {"sc": "涉投资与资本市场内容仅作行业背景，不构成投资建议或产品推介", "tc": "涉投資與資本市場內容僅作行業背景，不構成投資建議或產品推介"},
    },
    rolesImpact={"front": 1, "midback": 1, "lead": 2, "cross": 1},
    boards=["market"],
    themes=["ils", "casualty", "capital", "reinsurance", "bermuda"],
    tags={"sc": ["伤亡ILS", "退出机制", "资本终局性", "另类再保资本", "侧挂车", "Enstar"], "tc": ["傷亡ILS", "退出機制", "資本終局性", "另類再保資本", "側掛車", "Enstar"]},
    source={"sc": "Artemis.bm 2026-10-02 21:00（香港时间）[EN原文]", "tc": "Artemis.bm 2026-10-02 21:00（香港時間）[EN原文]", "lang": "en"},
))

# 5) Artemis: Plenum subordinated insurance debt (Oct 2 18:30)
items.append(item(
    id="artemis-plenum-insurance-subordinated-debt-20261002",
    score=68,
    sourceTier="pro",
    sourceKey="artemis",
    publishedAt="2026-10-02T18:30:00+08:00",
    originalUrl="https://www.artemis.bm/news/as-bonds-become-bonds-again-investors-should-look-to-insurance-debt-plenum/",
    title={
        "sc": "Artemis：Plenum 称「债券重回债券属性」，投资者应关注保险公司次级债，较政府债多约140个基点行业溢价 [EN原文]",
        "tc": "Artemis：Plenum 稱「債券重回債券屬性」，投資者應關注保險公司次級債，較政府債多約140個基點行業溢價 [EN原文]",
    },
    summary={
        "sc": "Artemis 10月2日报道：专业 ILS 管理人 Plenum Investments 在网志会中指出，政府债收益率升至历史吸引水平之际，保险公司次级债（subordinated insurance bonds）可提供约140个基点的额外利差，成为具吸引力的固定收益配置。管理合伙人 Daniel Grieger 称保险业存在「持续性的行业溢价」，RT1 相对 Tier 2 具结构性溢价，且当前 RT1 票息高于对应股息率；同时保险债供给相对有限，专业管理人更能捕捉该机会。合伙人 Rotger Franz 表示当前债市波动巨大、机会正在打开，保险业是少数因利率上升而净受益的行业之一，核心讯息是「无风险基准回归了」；文中指其欧洲保险债券基金欧元收益约5.8%、已有五年纪录。 [EN原文]",
        "tc": "Artemis 10月2日報導：專業 ILS 管理人 Plenum Investments 在網誌會中指出，政府債收益率升至歷史吸引水平之際，保險公司次級債（subordinated insurance bonds）可提供約140個基點的額外利差，成爲具吸引力的固定收益配置。管理合夥人 Daniel Grieger 稱保險業存在「持續性的行業溢價」，RT1 相對 Tier 2 具結構性溢價，且當前 RT1 票息高於對應股息率；同時保險債供給相對有限，專業管理人更能捕捉該機會。合夥人 Rotger Franz 表示當前債市波動巨大、機會正在打開，保險業是少數因利率上升而淨受益的行業之一，核心訊息是「無風險基準回歸了」；文中指其歐洲保險債券基金歐元收益約5.8%、已有五年紀錄。 [EN原文]",
    },
    why={
        "sc": "这条对香港保险团队的意义在「资产端叙事」：利率上行期，保险公司被债券投资者重新定价为净受益者，其次级资本工具存在持续行业溢价。这与香港风险为本资本制度的新一轮优化方向相呼应——为合资格基础设施投资提供优惠资本待遇、为指数型万用寿险引入匹配调整（MA）、下调一般业务部分风险因子，制度目标都是提升资产端效率与资负匹配。对前线而言，可借此理解「公司质量」的判断维度不止保费规模，还包括资本工具结构、融资成本与资产配置能力；但任何资本市场收益率都不得用来类比保单回报。",
        "tc": "這條對香港保險團隊的意義在「資產端敘事」：利率上行期，保險公司被債券投資者重新定價爲淨受益者，其次級資本工具存在持續行業溢價。這與香港風險爲本資本制度的新一輪優化方向相呼應——爲合資格基礎設施投資提供優惠資本待遇、爲指數型萬用壽險引入匹配調整（MA）、下調一般業務部分風險因子，制度目標都是提升資產端效率與資負匹配。對前線而言，可藉此理解「公司質量」的判斷維度不止保費規模，還包括資本工具結構、融資成本與資產配置能力；但任何資本市場收益率都不得用來類比保單回報。",
    },
    actions={
        "front": {"sc": "不用债券利差或基金收益率类比保单回报，客户沟通只描述保证与非保证利益结构", "tc": "不用債券利差或基金收益率類比保單回報，客戶溝通只描述保證與非保證利益結構"},
        "midback": {"sc": "在培训中加入「险企资产端与偿付能力」基础，帮助前线理解公司质量判断维度", "tc": "在培訓中加入「險企資產端與償付能力」基礎，幫助前線理解公司質量判斷維度"},
        "lead": {"sc": "在保司复核中增加「资本工具结构与融资成本」观察项，作为公司质量的辅助指标", "tc": "在保司覆核中增加「資本工具結構與融資成本」觀察項，作爲公司質量的輔助指標"},
        "cross": {"sc": "涉资本市场与基金内容仅作行业背景，不向客户作投资建议", "tc": "涉資本市場與基金內容僅作行業背景，不向客戶作投資建議"},
    },
    rolesImpact={"front": 1, "midback": 1, "lead": 2, "cross": 1},
    boards=["market"],
    themes=["invest", "capital", "rates", "insurance-debt", "europe"],
    tags={"sc": ["保险次级债", "RT1", "行业溢价", "利率上行", "资负匹配", "Plenum"], "tc": ["保險次級債", "RT1", "行業溢價", "利率上行", "資負匹配", "Plenum"]},
    source={"sc": "Artemis.bm 2026-10-02 18:30（香港时间）[EN原文]", "tc": "Artemis.bm 2026-10-02 18:30（香港時間）[EN原文]", "lang": "en"},
))

path = 'data/live-items.json'
d = json.load(open(path))
existing_ids = {it['id'] for it in d['items']}
added = []
for it in items:
    if it['id'] in existing_ids:
        print('SKIP duplicate id:', it['id'])
        continue
    added.append(it)

d['items'] = added + d['items']
d['meta']['generatedAt'] = NOW
d['meta']['itemCount'] = len(d['items'])
n = len(d['items'])
d['meta']['windowNote'] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}

json.dump(d, open(path, 'w'), ensure_ascii=False, indent=1)
print('added', len(added), 'total', n, 'generatedAt', NOW)
for it in added:
    print(' +', it['id'], it['publishedAt'], it['sourceKey'], it['sourceTier'], it['verifyStatus'])
