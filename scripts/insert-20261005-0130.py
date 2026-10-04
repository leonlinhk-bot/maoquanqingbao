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

# 1) InsuranceAsia News (Oct 5): Ex-Lloyds CEO John Neal joins LUSYi
items.append(item(
    id="ian-john-neal-lusyi-chairman-20261005",
    score=70,
    sourceTier="pro",
    sourceKey="insuranceasianews",
    publishedAt="2026-10-05",
    originalUrl="https://insuranceasianews.com/ex-lloyds-chief-john-neal-joins-software-developer-lusyi/",
    title={
        "sc": "前劳合社（Lloyd's）行政总裁 John Neal 加入软件开发商 LUSYi 出任非执行主席：离开劳合社后首项新任命 [EN原文]",
        "tc": "前勞合社（Lloyd's）行政總裁 John Neal 加入軟件開發商 LUSYi 出任非執行主席：離開勞合社後首項新任命 [EN原文]",
    },
    summary={
        "sc": "InsuranceAsia News 10月5日报道（记者 Roshan Nambiar）：据 LinkedIn 帖文，劳合社（Lloyd's）前行政总裁 John Neal 已加入软件开发商 LUSYi，出任非执行主席（non-executive chairman），为其离开劳合社并暂休一段时间后的首项新任命。原文为订阅内容，可公开部分以此为准。 [EN原文]",
        "tc": "InsuranceAsia News 10月5日報道（記者 Roshan Nambiar）：據 LinkedIn 帖文，勞合社（Lloyd's）前行政總裁 John Neal 已加入軟件開發商 LUSYi，出任非執行主席（non-executive chairman），爲其離開勞合社並暫休一段時間後的首項新任命。原文爲訂閱內容，可公開部分以此爲準。 [EN原文]",
    },
    why={
        "sc": "伦敦市场最高层人物转投科技公司，是「保险人才流动跨出传统承保与经纪边界」的又一例：一是大型市场机构的前任掌舵人开始进入软件／科技公司并担任非执行董事角色，反映数据、平台与技术治理已成为董事会层面的专业要求，而非仅是科技部门议题；二是这类人事消息常被客户与团队当作行业风向提问，处理原则是只引述公开报道与公司披露，不延伸解读为产品、偿付或投资优势。",
        "tc": "倫敦市場最高層人物轉投科技公司，是「保險人才流動跨出傳統承保與經紀邊界」的又一例：一是大型市場機構的前任掌舵人開始進入軟件／科技公司並擔任非執行董事角色，反映數據、平台與技術治理已成爲董事會層面的專業要求，而非僅是科技部門議題；二是這類人事消息常被客戶與團隊當作行業風向提問，處理原則是只引述公開報道與公司披露，不延伸解讀爲產品、償付或投資優勢。",
    },
    actions={
        "front": {"sc": "客户问及行业人事变动时，只引述公开报道，不作产品优劣或公司稳健性论据", "tc": "客戶問及行業人事變動時，只引述公開報道，不作產品優劣或公司穩健性論據"},
        "midback": {"sc": "把同業高层流动纳入行业动态简报，用于观察治理与技术要求的长期变化", "tc": "把同業高層流動納入行業動態簡報，用於觀察治理與技術要求的長期變化"},
        "lead": {"sc": "留意保险科技公司引入传统保险高管的趋势，评估对合作方与技术路线判断的启示", "tc": "留意保險科技公司引入傳統保險高管的趨勢，評估對合作方與技術路線判斷的啓示"},
        "cross": {"sc": "涉境外主体人事信息一律以原文报道与公司公告为准，不引用二手摘要", "tc": "涉境外主體人事資訊一律以原文報道與公司公告爲準，不引用二手摘要"},
    },
    rolesImpact={"front": 1, "midback": 1, "lead": 2, "cross": 1},
    boards=["tech", "insurer"],
    themes=["people", "insurtech", "tech", "leadership", "uk"],
    tags={"sc": ["John Neal", "劳合社Lloyd's", "LUSYi", "非执行主席", "保险科技", "人事变动"], "tc": ["John Neal", "勞合社Lloyd's", "LUSYi", "非執行主席", "保險科技", "人事變動"]},
    source={"sc": "InsuranceAsia News 2026-10-05 [EN原文]", "tc": "InsuranceAsia News 2026-10-05 [EN原文]", "lang": "en"},
))

# 2) Business Standard (Oct 4): IBAI warns on IRDAI distribution reforms
items.append(item(
    id="bs-ibai-irdai-distribution-letter-20261004",
    score=62,
    sourceTier="media",
    sourceKey="businessstandard",
    publishedAt="2026-10-05T01:11:00+08:00",
    originalUrl="https://www.business-standard.com/finance/insurance/ibai-warns-irdai-distribution-overhaul-may-put-1-mn-livelihoods-at-risk-126100400432_1.html",
    title={
        "sc": "印度经纪协会 IBAI 致函总理与财长：IRDAI 拟设30多个佣金子上限、整体费用上限削三分之一，或危及100万个从业岗位 [EN原文]",
        "tc": "印度經紀協會 IBAI 致函總理與財長：IRDAI 擬設30多個佣金子上限、整體費用上限削三分之一，或危及100萬個從業崗位 [EN原文]",
    },
    summary={
        "sc": "Business Standard 10月4日22:41（印度时间）报道：代表印度798家持牌保险经纪的印度保险经纪协会（IBAI）在10月2日致总理莫迪与财长西塔拉曼的信中警告，IRDAI 拟推行的分销改革——跨产品与渠道设逾30个佣金子上限、并把险企整体费用（EoM）上限削减三分之一——可能令2023年监管修订所纠正的不当做法复活，五年内危及至少100万个就业岗位。IBAI 引用 IRDAI 2024-25 数据指分销体系供养逾830万从业者，其中经纪机构保荐了272万销售点（PoS）人员中的148万；协会警告佣金子上限会促使险企与分销商改以额外佣金（overriding）等替代渠道支付，重演2023年前15家险企涉约8.24亿卢比虚假增值税进项抵扣的合规问题，并要求在公布影响评估前不要公告新规。 [EN原文]",
        "tc": "Business Standard 10月4日22:41（印度時間）報道：代表印度798家持牌保險經紀的印度保險經紀協會（IBAI）在10月2日致總理莫迪與財長西塔拉曼的信中警告，IRDAI 擬推行的分銷改革——跨產品與渠道設逾30個佣金子上限、並把險企整體費用（EoM）上限削減三分之一——可能令2023年監管修訂所糾正的不當做法復活，五年內危及至少100萬個就業崗位。IBAI 引用 IRDAI 2024-25 數據指分銷體系供養逾830萬從業者，其中經紀機構保薦了272萬銷售點（PoS）人員中的148萬；協會警告佣金子上限會促使險企與分銷商改以額外佣金（overriding）等替代渠道支付，重演2023年前15家險企涉約8.24億盧比虛假增值稅進項抵扣的合規問題，並要求在公佈影響評估前不要公告新規。 [EN原文]",
    },
    why={
        "sc": "分销成本监管的逻辑在亚洲同源：由「渠道费率上限」走向「产品级硬上限＋费用审计」，与香港收窄转介费、首年佣金分摊与摊回机制的方向一致。这条对香港团队的实用价值有二：一是报酬结构受监管约束后，代理人／经纪的留存与服务年限会被进一步绑定，团队规划人力与产能时要把这一点计入；二是监管最担心的并非价格本身，而是被压价后「改以其他名目支付」，即返佣、回赠或以费用外补贴换取业务——这正是香港合规口径下的高危区。",
        "tc": "分銷成本監管的邏輯在亞洲同源：由「渠道費率上限」走向「產品級硬上限＋費用審計」，與香港收窄轉介費、首年佣金分攤與攤回機制的方向一致。這條對香港團隊的實用價值有二：一是報酬結構受監管約束後，代理人／經紀的留存與服務年限會被進一步綁定，團隊規劃人力與產能時要把這一點計入；二是監管最擔心的並非價格本身，而是被壓價後「改以其他名目支付」，即返傭、回贈或以費用外補貼換取業務——這正是香港合規口徑下的高危區。",
    },
    actions={
        "front": {"sc": "不向客户承诺或暗示任何佣金、回赠或费用补贴安排，报酬事宜一律按公司合规口径处理", "tc": "不向客戶承諾或暗示任何佣金、回贈或費用補貼安排，報酬事宜一律按公司合規口徑處理"},
        "midback": {"sc": "把「以其他名目支付报酬」列入自查清单，检查佣金以外的资金往来与留痕", "tc": "把「以其他名目支付報酬」列入自查清單，檢查佣金以外的資金往來與留痕"},
        "lead": {"sc": "在人力与产能规划中计入报酬监管收紧趋势，评估对留存与服务年限的影响", "tc": "在人力與產能規劃中計入報酬監管收緊趨勢，評估對留存與服務年限的影響"},
        "cross": {"sc": "涉印度等海外市场内容仅作行业背景，不作当地展业或产品比较依据", "tc": "涉印度等海外市場內容僅作行業背景，不作當地展業或產品比較依據"},
    },
    rolesImpact={"front": 1, "midback": 2, "lead": 2, "cross": 1},
    boards=["reg", "market"],
    themes=["distribution", "commission", "reg", "conduct", "india"],
    tags={"sc": ["IBAI", "IRDAI", "佣金子上限", "费用上限EoM", "分销改革", "额外佣金", "印度经纪"], "tc": ["IBAI", "IRDAI", "佣金子上限", "費用上限EoM", "分銷改革", "額外佣金", "印度經紀"]},
    source={"sc": "Business Standard 2026-10-04 22:41 IST（香港时间 10-05 01:11）[EN原文]", "tc": "Business Standard 2026-10-04 22:41 IST（香港時間 10-05 01:11）[EN原文]", "lang": "en"},
))

# 3) Insurance Business Asia (Oct 2): Allianz new CEOs at Partners / Direct
items.append(item(
    id="ibm-allianz-partners-direct-ceos-20261002",
    score=64,
    sourceTier="media",
    sourceKey="insurancebusinessmag",
    publishedAt="2026-10-02T15:54:00+08:00",
    originalUrl="https://www.insurancebusinessmag.com/asia/news/breaking-news/allianz-names-new-ceos-at-allianz-partners-and-allianz-direct-592079.aspx",
    title={
        "sc": "安联调整两家数字化业务CEO：Philipp Kroetz 转任安联世博（Allianz Partners）CEO，Laurent Floquet 接掌 Allianz Direct，11月1日生效 [EN原文]",
        "tc": "安聯調整兩家數字化業務CEO：Philipp Kroetz 轉任安聯世博（Allianz Partners）CEO，Laurent Floquet 接掌 Allianz Direct，11月1日生效 [EN原文]",
    },
    summary={
        "sc": "Insurance Business Asia 10月2日报道（记者 Jonalyn Cueto）：安联10月1日在慕尼黑公布两项数字化业务人事调动——原 Allianz Direct CEO Philipp Kroetz（46岁）将于2026年11月1日接任 Allianz Partners CEO，接替 Tomas Kunzmann；Allianz Partners 现任首席营运官 Laurent Floquet（49岁）同日接掌 Allianz Direct，其COO继任人另行公布，任命均待监管批准。安联指 Kroetz 任内把 Allianz Direct 客户数增至逾320万（五个欧洲市场）、2025年业务规模超15亿欧元（同比+23%、综合成本率95%），并以「60秒内AI理赔结案」及 ChatGPT 试探性报价为例，强调数字化与跨境（车险、家财、旅游、援助与健康）的战略优势；报道指对中介渠道而言，变化最大的是主要经业务伙伴与中介销售旅游险、援助与国际健康的 Allianz Partners。 [EN原文]",
        "tc": "Insurance Business Asia 10月2日報道（記者 Jonalyn Cueto）：安聯10月1日在慕尼黑公佈兩項數字化業務人事調動——原 Allianz Direct CEO Philipp Kroetz（46歲）將於2026年11月1日接任 Allianz Partners CEO，接替 Tomas Kunzmann；Allianz Partners 現任首席營運官 Laurent Floquet（49歲）同日接掌 Allianz Direct，其COO繼任人另行公佈，任命均待監管批准。安聯指 Kroetz 任內把 Allianz Direct 客戶數增至逾320萬（五個歐洲市場）、2025年業務規模超15億歐元（同比+23%、綜合成本率95%），並以「60秒內AI理賠結案」及 ChatGPT 試探性報價爲例，強調數字化與跨境（車險、家財、旅遊、援助與健康）的戰略優勢；報道指對中介渠道而言，變化最大的是主要經業務夥伴與中介銷售旅遊險、援助與國際健康的 Allianz Partners。 [EN原文]",
    },
    why={
        "sc": "这条把两件事放在一起看才有价值：一是保险公司正把「数字化直营」与「中介／伙伴分销」两类业务的管理层互相轮调，并在同一集团内拉近两者的技术与服务后台，说明直营与中介不再是两条互不相干的路线；二是官方叙述里出现「60秒AI理赔」与「ChatGPT 报价」两个指标，与本周 Manulife 在 ChatGPT 上线旅游险插件属同一趋势——保险的分销入口正在向通用AI助手迁移。对香港团队的提示是：流量入口会变，但持牌人的销售流程、适当性评估与留痕要求不变，工具可以快，合规环节不能省。",
        "tc": "這條把兩件事放在一起看才有價值：一是保險公司正把「數字化直營」與「中介／夥伴分銷」兩類業務的管理層互相輪調，並在同一集團內拉近兩者的技術與服務後台，說明直營與中介不再是兩條互不相干的路线；二是官方敘述裏出現「60秒AI理賠」與「ChatGPT 報價」兩個指標，與本週 Manulife 在 ChatGPT 上線旅遊險插件屬同一趨勢——保險的分銷入口正在向通用AI助手遷移。對香港團隊的提示是：流量入口會變，但持牌人的銷售流程、適當性評估與留痕要求不變，工具可以快，合規環節不能省。",
    },
    actions={
        "front": {"sc": "客户问及「AI 报价／AI 理赔」时，说明其适用范围与人工复核环节，不承诺时效或结果", "tc": "客戶問及「AI 報價／AI 理賠」時，說明其適用範圍與人工覆核環節，不承諾時效或結果"},
        "midback": {"sc": "在合作保司复核中加入「服务与分销模式变动」观察项，评估对中介渠道的影响", "tc": "在合作保司覆核中加入「服務與分銷模式變動」觀察項，評估對中介渠道的影響"},
        "lead": {"sc": "留意合作方技术平台与直营渠道的整合动向，评估渠道价值与客户体验的长期变化", "tc": "留意合作方技術平台與直營渠道的整合動向，評估渠道價值與客戶體驗的長期變化"},
        "cross": {"sc": "涉欧洲市场业务内容仅作行业参考，不用于本地产品比较或推介", "tc": "涉歐洲市場業務內容僅作行業參考，不用於本地產品比較或推介"},
    },
    rolesImpact={"front": 1, "midback": 1, "lead": 2, "cross": 1},
    boards=["insurer", "tech"],
    themes=["people", "digital", "distribution", "ai", "group"],
    tags={"sc": ["安联Allianz", "Allianz Partners", "Allianz Direct", "Philipp Kroetz", "Laurent Floquet", "AI理赔", "中介渠道"], "tc": ["安聯Allianz", "Allianz Partners", "Allianz Direct", "Philipp Kroetz", "Laurent Floquet", "AI理賠", "中介渠道"]},
    source={"sc": "Insurance Business Asia 2026-10-02 15:54（香港时间）[EN原文]", "tc": "Insurance Business Asia 2026-10-02 15:54（香港時間）[EN原文]", "lang": "en"},
))

# 4) Manulife (Sep 28): first in Canada to offer travel insurance quotes in ChatGPT
items.append(item(
    id="manulife-chatgpt-coverme-travel-plugin-20260928",
    score=78,
    sourceTier="insurer",
    sourceKey="manulife",
    publishedAt="2026-09-28T18:00:00+08:00",
    originalUrl="https://www.theglobeandmail.com/investing/markets/markets-news/Newswire.ca/4828321/manulife-becomes-the-first-in-canada-to-offer-travel-insurance-quotes-in-chatgpt/",
    title={
        "sc": "宏利（Manulife）在 ChatGPT 上线 CoverMe 旅游保险插件：加拿大首例，也是集团全球首个 ChatGPT 插件 [EN原文]",
        "tc": "宏利（Manulife）在 ChatGPT 上線 CoverMe 旅遊保險插件：加拿大首例，也是集團全球首個 ChatGPT 插件 [EN原文]",
    },
    summary={
        "sc": "宏利（Manulife）2026年9月28日（多伦多时间上午5:00）发布：推出 ChatGPT 内的 CoverMe 旅游保险插件，加拿大用户可借此探索旅游保险并获取个性化报价。公司称该插件是加拿大首例同类插件，也是宏利在全球的首个 ChatGPT 插件，结合其在旅游险的市场地位与「成为AI驱动组织」的目标，让客户在原本用于行程研究与规划的数字化场景中完成保障探索。（该内容经 Newswire.ca 转载，非媒体自采报道。） [EN原文]",
        "tc": "宏利（Manulife）2026年9月28日（多倫多時間上午5:00）發佈：推出 ChatGPT 內的 CoverMe 旅遊保險插件，加拿大用戶可藉此探索旅遊保險並獲取個性化報價。公司稱該插件是加拿大首例同類插件，也是宏利在全球的首個 ChatGPT 插件，結合其在旅遊險的市場地位與「成爲AI驅動組織」的目標，讓客戶在原本用於行程研究與規劃的數字化場景中完成保障探索。（該內容經 Newswire.ca 轉載，非媒體自採報道。） [EN原文]",
    },
    why={
        "sc": "旅行社群的入口正从「搜索＋官网」转向通用AI助手：宏利把报价能力直接嵌入 ChatGPT，是保司争取「对话式入口」的第一批动作之一。对香港团队有三层含义：一是客户会比过去更早、更快地拿到「看起来像报价」的信息，前线需要能解释报价与承保条件、除外责任的差别；二是内容生产与AI可见度正在成为保司的品牌资产，团队的公开内容同样会被AI引用，措辞必须可溯源、不得夸大；三是无论入口如何变化，持牌人层面的需求分析、适当性与披露仍是不可替代的一环。",
        "tc": "旅行社群的入口正從「搜索＋官網」轉向通用AI助手：宏利把報價能力直接嵌入 ChatGPT，是保司爭取「對話式入口」的第一批動作之一。對香港團隊有三層含義：一是客戶會比過去更早、更快地拿到「看起來像報價」的信息，前線需要能解釋報價與承保條件、除外責任的差別；二是內容生產與AI可見度正在成爲保司的品牌資產，團隊的公開內容同樣會被AI引用，措辭必須可溯源、不得誇大；三是無論入口如何變化，持牌人層面的需求分析、適當性與披露仍是不可替代的一環。",
    },
    actions={
        "front": {"sc": "客户拿着AI生成的报价询问时，先解释报价不等于承保条件，逐项核对保障范围与除外责任", "tc": "客戶拿着AI生成的報價詢問時，先解釋報價不等於承保條件，逐項核對保障範圍與除外責任"},
        "midback": {"sc": "检视对外公开内容的措辞与可溯源性，避免被AI引用时产生夸大或误导性表述", "tc": "檢視對外公開內容的措辭與可溯源性，避免被AI引用時產生誇大或誤導性表述"},
        "lead": {"sc": "把「对话式入口与AI报价」列入渠道环境观察，评估对客户获取与顾问价值定位的影响", "tc": "把「對話式入口與AI報價」列入渠道環境觀察，評估對客戶獲取與顧問價值定位的影響"},
        "cross": {"sc": "涉境外产品与服务内容仅作趋势参考，不作本地替代方案比较", "tc": "涉境外產品與服務內容僅作趨勢參考，不作本地替代方案比較"},
    },
    rolesImpact={"front": 2, "midback": 1, "lead": 2, "cross": 1},
    boards=["tech", "insurer", "product"],
    themes=["ai", "distribution", "digital", "travel", "canada"],
    tags={"sc": ["宏利Manulife", "CoverMe", "ChatGPT插件", "旅游保险", "AI报价", "对话式入口"], "tc": ["宏利Manulife", "CoverMe", "ChatGPT插件", "旅遊保險", "AI報價", "對話式入口"]},
    source={"sc": "Manulife 公告（Newswire.ca／The Globe and Mail 转载）2026-09-28 [EN原文]", "tc": "Manulife 公告（Newswire.ca／The Globe and Mail 轉載）2026-09-28 [EN原文]", "lang": "en"},
))

# 5) Prudential HK (Oct 4): Prudential Leadership Forum with Dr Maye Musk
items.append(item(
    id="pru-hk-leadership-forum-maye-musk-20261004",
    score=75,
    sourceTier="insurer",
    sourceKey="prudential",
    publishedAt="2026-10-04",
    originalUrl="https://www.media-outreach.com/news/hong-kong/2026/10/04/491738/dr-maye-musk-author-supermodel-and-dietitian-speaks-at-the-prudential-leadership-forum/",
    title={
        "sc": "保诚香港举办 Prudential Leadership Forum：梅伊·马斯克与保诚香港CEO林智刚、集团大中华区区域CEO Angel Ng 同场谈领导力、韧性与传承 [EN原文]",
        "tc": "保誠香港舉辦 Prudential Leadership Forum：梅伊·馬斯克與保誠香港CEO林智剛、集團大中華區區域CEO Angel Ng 同場談領導力、韌性與傳承 [EN原文]",
    },
    summary={
        "sc": "保诚香港（Prudential Hong Kong Limited）10月4日经 Media OutReach 发布：公司于10月3日举办「Prudential Leadership Forum」，主题为《Beyond Success: The Blueprint for Leadership, Resilience and Legacy》，邀请作家、超级名模及营养学博士梅伊·马斯克（Dr Maye Musk）主讲，与保诚香港行政总裁林智刚（Lawrence Lam）及保诚集团大中华区区域行政总裁（集团客户与财富）Angel Ng 同场交流领导力、韧性与传承。 [EN原文]",
        "tc": "保誠香港（Prudential Hong Kong Limited）10月4日經 Media OutReach 發佈：公司於10月3日舉辦「Prudential Leadership Forum」，主題爲《Beyond Success: The Blueprint for Leadership, Resilience and Legacy》，邀請作家、超級名模及營養學博士梅伊·馬斯克（Dr Maye Musk）主講，與保誠香港行政總裁林智剛（Lawrence Lam）及保誠集團大中華區區域行政總裁（集團客戶與財富）Angel Ng 同場交流領導力、韌性與傳承。 [EN原文]",
    },
    why={
        "sc": "保险公司把「传承」做成面向代理人与客户的品牌论坛，反映高客市场的沟通语言正从「产品收益」转向「跨代规划与家族治理」。对香港团队的可迁移点：一是客户对传承议题的兴趣需要真本事支撑（受益人安排、信托与保单架构、跨境税务与法务协同），论坛内容不能替代顾问流程与合规披露；二是同业品牌活动的公开信息可以作为客户沟通与团队选题的素材，但不得转述为产品推介、收益或回报承诺。",
        "tc": "保險公司把「傳承」做成面向代理人與客戶的品牌論壇，反映高客市場的溝通語言正從「產品收益」轉向「跨代規劃與家族治理」。對香港團隊的可遷移點：一是客戶對傳承議題的興趣需要真本事支撐（受益人安排、信託與保單架構、跨境稅務與法務協同），論壇內容不能替代顧問流程與合規披露；二是同業品牌活動的公開資訊可以作爲客戶溝通與團隊選題的素材，但不得轉述爲產品推介、收益或回報承諾。",
    },
    actions={
        "front": {"sc": "客户谈传承时引导至需求梳理与合规顾问流程，不以名人演讲内容作为销售理由", "tc": "客戶談傳承時引導至需求梳理與合規顧問流程，不以名人演講內容作爲銷售理由"},
        "midback": {"sc": "复核高客传承主题（受益人、信托、跨境）内容的合规与披露口径", "tc": "覆核高客傳承主題（受益人、信託、跨境）內容的合規與披露口徑"},
        "lead": {"sc": "可借鉴同业「传承／家族治理」客户活动的形式，内容与讲者须经合规审核", "tc": "可借鑑同業「傳承／家族治理」客戶活動的形式，內容與講者須經合規審核"},
        "cross": {"sc": "涉跨境传承与税务话题必须提示专业顾问参与，不提供税务或法律意见", "tc": "涉跨境傳承與稅務話題必須提示專業顧問參與，不提供稅務或法律意見"},
    },
    rolesImpact={"front": 1, "midback": 1, "lead": 2, "cross": 1},
    boards=["insurer", "family"],
    themes=["hnw", "legacy", "brand", "agency", "hk"],
    tags={"sc": ["保诚香港", "Prudential Leadership Forum", "梅伊·马斯克", "林智刚", "家族传承", "高客活动"], "tc": ["保誠香港", "Prudential Leadership Forum", "梅伊·馬斯克", "林智剛", "家族傳承", "高客活動"]},
    source={"sc": "Media OutReach（保诚香港发布）2026-10-04 [EN原文]", "tc": "Media OutReach（保誠香港發佈）2026-10-04 [EN原文]", "lang": "en"},
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
