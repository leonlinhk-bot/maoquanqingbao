#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 21:08/22:45（周三）增量采集（当日第二批）。

窗口：2026-09-30 18:08 → 22:45（承接 18:08 批次）
逐源核验（14 信源）：
- IA：press_releases 为 JS 表格，经 doubao 缓存快照核对最新条目为 24/9/2026（AML 罚则）→ 窗口内无新闻稿新增；
  通函页 30/9 早间《监管通讯》第13期已由 18:08 批次入库 → 无新增。
- HKMA：新闻稿页实抓，30/9 共 8 则，最新为 17:05（HKICL 伪冒网站）→ 窗口内无新增。
- 保司：AIA 最新 24/9、AXA 最新 23/9、宏利（403 未取）与保诚/永明页最新条目均早于本窗口 → 无新增。
- NFRA：官网直连不可达（000），经 doubao 交叉核验最新文件为 9/29（内贸险协同、安责险事故预防）→ 30/9 无新文件。
- HKFI：media-release 页返回 404（改版）→ 无新增；FSTB 首页无保险/家办核心新稿。
- insuranceasia(RSS)：最新条目 30/9 06:00 → 窗口内无新增。
- insuranceasianews(WP API)：最新条目 30/9 14:51（18:08 批次已入库）→ 无新增。
- insurancebusinessmag(Atom)：窗口内 4 则 → 取 3 则（保监局 RO 任期与操守风险、Willis D&F 增长主管与临时再保需求、
  亚洲/新兴市场人事汇总）；「回归办公室完成度」一则与本域无关 → 不取。
- scmp(RSS)：窗口内 1 则（DFI 出售美心权益换星巴克业务）→ 非保险核心，不取。
- artemis(RSS)：窗口内 2 则（Stone Ridge 巨灾债基金 50 亿美元、巴西 SUSEP 巨灾融资改革）→ 全取。
- govhk(info.gov.hk RSS)：18:08 后 13 则，均为食安/警务/立法会简报等 → 无保险相关。
- insurtech / family_office：窗口内无新增。
本批 5 条覆盖 ia 衍生分析 / ibm / artemis 三类信源（4 个 sourceKey：insurancebusinessmag、artemis）。
"""
import json, shutil, os
import zhconv

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-09-30T22:50:00+08:00'

FIX = {'轉帳': '轉賬', '鏈接': '連結', '裏面': '裡面', '數據': '數據'}


def tc(s):
    out = zhconv.convert(s, 'zh-tw')
    for a, b in FIX.items():
        out = out.replace(a, b)
    return out


def T(sc, tcv=None):
    return {'sc': sc, 'tc': tcv if tcv else tc(sc)}


def item(**kw):
    d = {
        'clusterCount': 1, 'score': 65, 'verifyStatus': 'pending',
        'sourceTier': 'media', 'sourceKey': '', 'contentKind': 'news',
        'actions': {'front': {}, 'midback': {}, 'lead': {}, 'cross': {}},
        'rolesImpact': {'front': 0, 'midback': 0, 'lead': 0, 'cross': 0},
        'boards': [], 'themes': [], 'tags': {'sc': [], 'tc': []},
        'contentRole': {'sc': '本站导读', 'tc': '本站導讀'},
        'featured': False, 'evergreen': False, 'ingestedAt': NOW,
    }
    d.update(kw)
    return d


def tg(*words):
    return {'sc': list(words), 'tc': [tc(w) for w in words]}


NEW = [
    # ======================= 保监局操守监管（深度数据） =======================
    item(id='ibm-broker-ro-tenure-conduct-risk-20260930', score=78, verifyStatus='verified',
         sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
         publishedAt='2026-09-30T21:14:00+08:00',
         title=T('保险商业（亚洲）解读保监局《监管通讯》第13期数据：2019年9月至2026年6月共批出3,201名负责人员，平均在任3.8年；长期业务机构51.4%任命不足两年，经纪公司负责人员平均仅2.3年（代理机构3.3年）低于三年牌照期基准；3家经纪公司因转介管控失效被加设续牌条件 [EN原文]',
                 '保險商業（亞洲）解讀保監局《監管通訊》第13期數據：2019年9月至2026年6月共批出3,201名負責人員，平均在任3.8年；長期業務機構51.4%任命不足兩年，經紀公司負責人員平均僅2.3年（代理機構3.3年）低於三年牌照期基準；3家經紀公司因轉介管控失效被加設續牌條件 [EN原文]'),
         summary=T('Insurance Business Asia 9月30日21:14报道，援引保险业监管局《监管通讯》（Conduct in Focus）第13期（2026年9月30日发表）的负责人员（RO）任命与任期数据：2019年9月23日至2026年6月30日期间，保监局共批准3,201名RO任命，涵盖持牌保险代理机构与持牌保险经纪公司；整体平均在任3.8年。经营长期业务的实体中，51.4%的RO任命任期不足两年；经纪公司RO平均在任2.3年，低于代理机构的3.3年，而实体牌照的标准年期为三年。保监局以在任超过三年作为管理稳定的基准，任期过短或重复任命可能反映治理不足、资源投放不够或授予RO的权限有限，出现此类模式的机构会面对督导检视或现场检查。经营长期业务（尤其采用转介分销）的经纪公司RO人选，获批前更可能被安排面试，内容涵盖对公司业务模式的认识、治理经验及对适用监管要求的掌握。3家经纪公司因未能管控转介活动被加设牌照续期条件，包括禁止接受新转介业务；保监局行为监管代理主管Alan Wu在7月12日评论中表示，这些行动并非一次性举措，市场若再现同类违规，将适时采取相称而果断的监管行动以回复市场秩序。报道并指保监局把「自荐转介」（客户或家人与经纪订立转介协议、把费用实质回流为回佣）定性为无纪录回佣，属禁止行为；合规格的转介模式下，无牌转介人只可介绍客户、不得从事任何受规管活动，所有顾问工作须由持牌中介人完成；按2025年9月1日通函，转介费超过所收佣金50%会触发额外披露要求与审视。CPD方面，2025年7月11日通函订明RO强制持续专业培训要求（2025年8月1日生效）若不合规，会影响适当人选资格，并令有关经纪公司受更严格审视。投诉方面，保监局2026年上半年接获652宗投诉，同比增加10%，最大类别为「业务或营运」、升9%，主要与中介人流失引致的代理人委任失效有关。此外，报道指数码广告中选择性呈现实绩（例如只涵盖产品首两年的履行比率）违反《操守守则》一般原则1及《保险业条例》第90条，中介人须在销售前识别并纠正已被扭曲的客户期望，屡次引致误解的宣传须修订或撤回。', None),
         why=T('这批数字把「负责人员在任年资」变成可量化的监管风向标：经纪公司RO平均仅2.3年、长期业务机构逾半任命撑不过两年，都会直接触发面试、督导检视甚至续牌条件。对经纪与管理层而言，这不是抽象原则，而是「谁担任RO、担任多久、有没有实权与资源」的治理问题；频繁换人的机构已被系统性标记。转介方面，「自荐转介」被明确定性为无纪录回佣、转介费超过佣金50%触发额外披露，加上3家经纪公司被禁接新转介业务，说明该渠道的合规成本正在刚性上升。上半年投诉652宗、升10%且集中于代理人委任失效，也提示中介人流失本身已成投诉来源，团队稳定性与继承安排值得提前布局。', None),
         actions={'front': T('不得向客户提供或承诺任何形式回佣；转介客户须由持牌中介人完成所有顾问工作，无牌转介人只可介绍'),
                  'midback': T('核查RO任命年期、权限与资源是否合理，转介费占佣金比例超过50%的个案须补做额外披露并留痕'),
                  'lead': T('把RO在任年期与代理委任安排列入治理自查，避免出现频繁更换RO的监管关注模式'),
                  'cross': T('跨境转介与费用安排须逐笔留痕，内地访客客户的转介不得以任何名义变相回佣')},
         rolesImpact={'front': 3, 'midback': 3, 'lead': 3, 'cross': 2},
         source={'sc': 'Insurance Business Asia 2026-09-30 21:14（援引保监局《监管通讯》第13期）[EN原文]',
                 'tc': 'Insurance Business Asia 2026-09-30 21:14（援引保監局《監管通訊》第13期）[EN原文]', 'lang': 'en'},
         boards=['reg', 'compliance'], themes=['reg', 'compliance', 'channel', 'talent'],
         tags=tg('负责人员', '在任年期', '监管通讯', '自荐转介', '续牌条件', '投诉统计'),
         originalUrl='https://www.insurancebusinessmag.com/asia/news/breaking-news/broker-leadership-churn-emerges-as-conduct-risk-signal-in-hong-kong-ia-report-591783.aspx'),

    # ======================= 再保市场（临时再保需求与费率） =======================
    item(id='ibm-willis-df-growth-leader-fac-demand-20260930', score=60, verifyStatus='verified',
         sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
         publishedAt='2026-09-30T19:39:00+08:00',
         title=T('Willis委任Andy Chang为全球直接与临时再保（D&F）增长主管：调查指60%保险公司未来两年将增用临时再保、仅13%减少；美加1月物业临时再保费率跌25%至30%，穆迪称为逾十年最急 [EN原文]',
                 'Willis委任Andy Chang為全球直接與臨時再保（D&F）增長主管：調查指60%保險公司未來兩年將增用臨時再保、僅13%減少；美加1月物業臨時再保費率跌25%至30%，穆迪稱為逾十年最急 [EN原文]'),
         summary=T('Insurance Business Asia 9月30日19:39报道：Willis（WTW旗下）委任Andy Chang为全球直接与临时再保（direct & facultative, D&F）业务增长主管；Chang来自Aon，最近出任另类分销主管，将常驻迈阿密并向全球D&F主管Garret Gaughan汇报。报道指临时再保已不再只是处理问题风险的最后一着：Willis本月发表的《2026年临时再保全球调查》显示，受访的380名高级保险管理层中，60%计划在未来两年增加使用临时再保，仅13%预期减少；「资本管理」以52%成为首要驱动（2024年为44%），「全球扩张」被56%视为主要机遇（两年前为39%），意味着保险公司正以临时再保额度支持进入新地域与风险类别，而非单纯补足合约缺口，而这需要布局关系与跨境技术知识。费率方面，据Gallagher Re《2026年1月全球临时再保市场报告》，美国及加拿大1月续保的物业临时再保平均费率下跌25%至30%，即使受灾账目亦见双位数减幅；穆迪形容该等环境为逾十年来最急的定价跌幅。Chang的任命紧随Willis于2025年11月为英国D&F团队作出的三项高级任命。', None),
         why=T('需求上升与费率急跌同时出现，是当前再保市场最值得注意的组合：保险公司把临时再保当作扩张工具（六成拟增用、全球扩张由39%升至56%），说明分出意愿强、承保能力被主动调用；但美加物业临时再保费率一年内跌25%至30%、穆迪称为逾十年最急，意味着额度充裕而定价压力极大，反过来会传导到原保险的续保条件与自留水平。对经纪人而言，客户在续保谈判中的议价空间与结构选择（自留、分层、参数补充）比过去更依赖对再保端条件的掌握，这条信息属于续保周期的先行指标。', None),
         actions={'front': T('客户讨论续保条件时，只引用公开的再保费率与调查数据，不作个别保单的费率承诺'),
                  'midback': T('把临时再保需求与费率走势列入下一个续保周期的定价与自留假设更新'),
                  'lead': T('引用一律标注Willis调查与Gallagher Re报告及时间点，避免与自家议价结果混用'),
                  'cross': T('跨境安排的临时再保须按各地分出与监管规则处理，不可直接套用美加定价结论')},
         rolesImpact={'front': 1, 'midback': 3, 'lead': 2, 'cross': 1},
         source={'sc': 'Insurance Business Asia 2026-09-30 19:39 [EN原文]', 'tc': 'Insurance Business Asia 2026-09-30 19:39 [EN原文]', 'lang': 'en'},
         boards=['market'], themes=['reinsurance', 'pricing', 'talent', 'market'],
         tags=tg('临时再保', 'D&F', 'Willis', '资本管理', '再保费率', '全球扩张'),
         originalUrl='https://www.insurancebusinessmag.com/asia/news/breaking-news/willis-appoints-dandf-growth-leader-as-fac-demand-surges-591766.aspx'),

    # ======================= 亚洲/新兴市场人事变动 =======================
    item(id='ibm-insurance-moves-antarah-mclarens-markel-irdai-20260930', score=56, verifyStatus='verified',
         sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
         publishedAt='2026-09-30T22:27:00+08:00',
         title=T('亚洲及新兴市场保险人事汇总：Ardonagh旗下MGA Antarah委任Antonio El Hokayem为中东非洲行政总裁；McLarens中东区10月1日换帅；Markel合并新加坡与马来西亚并委任Kevin Leung掌东南亚；菲律宾保险委员会与印度IRDAI新任高管 [EN原文]',
                 '亞洲及新興市場保險人事匯總：Ardonagh旗下MGA Antarah委任Antonio El Hokayem為中東非洲行政總裁；McLarens中東區10月1日換帥；Markel合併新加坡與馬來西亞並委任Kevin Leung掌東南亞；菲律賓保險委員會與印度IRDAI新任高管 [EN原文]'),
         summary=T('Insurance Business Asia 9月30日22:27汇总多项区域人事变动。Ardonagh Group旗下MGA子公司Antarah委任Antonio El Hokayem为中东及非洲行政总裁（待常规监管批准）；他自2022年起在Gallagher任职，曾任中东及非洲金融线总监及沙特阿拉伯专业险主管，此前在Zurich任金融线核保师。Antarah为劳合社认可承保代理（coverholder），以承保授权与劳合社承保能力经营多险种，集团CEO David Ross指该区对专业方案需求持续，El Hokayem表示将探索科技与AI辅助核保。理赔服务机构McLarens委任Ollie Waterman为中东区总监，10月1日生效，接替将于2026年底退休的Malcolm Addy；Waterman为特许公估师，2022年迁往迪拜，负责McLarens在中东的物业及意外、建造工程、海事及专业线，并与伦敦及欧洲中东非洲团队衔接。Markel Insurance把新加坡与马来西亚业务合并为统一东南亚架构，委任Kevin Leung为东南亚董事总经理（即时生效）；Leung原任亚太区首席核保官（2023年加入Markel，此前任职Swiss Re、Catlin、ACE Group及AIG，具逾25年经验），马来西亚业务仍由Jasminder Kaur担任国家主管，Leung向亚太董事总经理Sucheng Chang汇报。菲律宾保险委员会（IC）委任Nikolai Buncio为副保险专员，主管财务审查组（Financial Examination Group），他于9月7日到任，此前为澳新银行交易银行部高级总监，曾任职德意志银行马尼拉、渣打、富国及美国银行。印度方面，LIC高管Dinesh Pant出任IRDAI全职精算委员，并因此在IRDAI增设第五名全职委员，同时令LIC在职董事总经理减至两名（LIC另有MD及CEO职位）。', None),
         why=T('人事流向往往先于业务重心变化：区域架构「合并新加坡与马来西亚」、中东与东盟层面统一管理、以及监管机构从银行体系引入财务审查与精算主管，反映的是承保能力与监管能力同时被重新配置。对关注服务网络与人员稳定性的团队，这类变动是判断区域资源投放与对接效率的先行指标——尤其在 Markel 这类以专业险为主的承保主体上，亚太核保官升任区域负责人意味着承保权更贴近市场。', None),
         actions={'front': T('客户问及区域服务网络时，只说明公开的人事与架构安排，不代述服务或对接承诺'),
                  'midback': T('把主要保司与经纪的亚洲区管理层与架构变动列入合作方服务能力观察'),
                  'lead': T('引用须标注为媒体公开报道，勿据此推断任何合作、佣金或业务安排'),
                  'cross': T('中东与东盟市场分销与牌照要求各异，客户涉当地业务须按属地规则个案确认')},
         rolesImpact={'front': 0, 'midback': 1, 'lead': 2, 'cross': 1},
         source={'sc': 'Insurance Business Asia 2026-09-30 22:27 [EN原文]', 'tc': 'Insurance Business Asia 2026-09-30 22:27 [EN原文]', 'lang': 'en'},
         boards=['insurer'], themes=['talent', 'career', 'market'],
         tags=tg('人事任命', '中东非洲', '东南亚', 'Markel', 'McLarens', 'IRDAI'),
         originalUrl='https://www.insurancebusinessmag.com/asia/news/breaking-news/insurance-moves-antarah-mclarens-markel-insurance-commission-irdai-591790.aspx'),

    # ======================= ILS / 巨灾债资金端 =======================
    item(id='artemis-stone-ridge-cat-bond-fund-5bn-20260930', score=60, verifyStatus='verified',
         sourceTier='media', sourceKey='artemis', contentKind='news',
         publishedAt='2026-09-30T21:00:00+08:00',
         title=T('Artemis：Stone Ridge高收益再保风险溢价基金规模达50亿美元里程碑，旗下互惠巨灾债与ILS基金合计约76亿美元、一年增近30%，为2018年以来高位 [EN原文]',
                 'Artemis：Stone Ridge高收益再保風險溢價基金規模達50億美元里程碑，旗下互惠巨災債與ILS基金合計約76億美元、一年增近30%，為2018年以來高位 [EN原文]'),
         summary=T('Artemis 9月30日报道：Stone Ridge Asset Management旗下规模最大、以巨灾债为主的Stone Ridge High Yield Reinsurance Risk Premium Fund（约81%资产为巨灾债）规模已达约50亿美元，创该策略历来最大规模；此前官方报告日为4月30日约44.4亿美元、6月30日约46亿美元、7月31日约47.4亿美元，8月底约49亿美元，即本周内触及50亿美元水平，2026年至今增逾9亿美元，12个月内增逾11.5亿美元。另一只Stone Ridge Reinsurance Risk Premium Interval Fund投资ILS全谱（sidecar、私人定额分出、抵押再保，巨灾债占比较低），7月31日约15.8亿美元，本周约16.6亿美元，一年增约3.6亿美元；该基金2018年曾达60亿美元，因2017至2019年损失事件收缩，自2023年起稳步增长，反映投资者对私募ILS与抵押再保信心回升。连同多策略Stone Ridge Diversified Alternatives Fund中的巨灾债与ILS部分，Stone Ridge旗下互惠巨灾债、ILS与再保基金合计AUM约76亿美元，较一年前增长近30%，处于2018年以来高位。', None),
         why=T('资金端规模往往领先费率变化：Stone Ridge互惠ILS基金一年增近30%、主基金触及50亿美元新高，Interval基金从2018年腰斩后持续回补，说明在无重大灾损的窗口里资本正加速流入再保风险转移。对理解财产险与再保的条件有直接意义——资本越充裕，定价与条款压力越大；一旦大灾发生，这条链会迅速反向。与同日Pioneer ILS基金规模数据相互印证，可作为再保周期判断的资金端证据。', None),
         actions={'front': T('客户问及ILS或再保相关资产时，须说明这属公开基金规模数据、非任何产品的回报承诺'),
                  'midback': T('把ILS基金规模与资本流入列入再保定价与财产险条件的季度观察'),
                  'lead': T('引用一律标注来源（Artemis.bm）与时间点，避免与自家产品规模或回报混用'),
                  'cross': T('ILS与sidecar属专业投资者范畴，跨境客户的参与资格与分销限制按属地规则处理')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Artemis.bm 2026-09-30 [EN原文]', 'tc': 'Artemis.bm 2026-09-30 [EN原文]', 'lang': 'en'},
         boards=['market'], themes=['ils', 'capital', 'market'],
         tags=tg('巨灾债', 'ILS基金', 'Stone Ridge', '再保资本', 'sidecar', 'AUM'),
         originalUrl='https://www.artemis.bm/news/stone-ridge-cat-bond-fund-hits-5bn-aum-milestone-total-mutual-ils-assets-now-7-6bn/'),

    # ======================= 新兴市场巨灾风险融资 =======================
    item(id='artemis-brazil-susep-lrs-catbond-proposals-20260930', score=62, verifyStatus='verified',
         sourceTier='media', sourceKey='artemis', contentKind='news',
         publishedAt='2026-09-30T18:30:00+08:00',
         title=T('Artemis：巴西SUSEP公布自然灾害风险融资改革方案——拟完善LRS（保险风险凭证）制度、引入巨灾债与参数保险，长期设想主权巨灾债与南美区域风险共担；当地自然灾害经济损失投保比例仅约9%，远低于全球约45% [EN原文]',
                 'Artemis：巴西SUSEP公布自然災害風險融資改革方案——擬完善LRS（保險風險憑證）制度、引入巨災債與參數保險，長期設想主權巨災債與南美區域風險共擔；當地自然災害經濟損失投保比例僅約9%，遠低於全球約45% [EN原文]'),
         summary=T('Artemis 9月30日报道：巴西私营保险监管机构SUSEP公布自然灾害财务与保险保障工作组成果文件，提出多项建议及后续探讨方向，包括设立自然灾害基金、本地及主权层面的巨灾风险转移、更广泛采用参数保险、扩大使用巴西本土ILS工具「保险风险凭证」（Letra de Risco de Seguro, LRS），以及更多利用资本市场支持的再保。SUSEP指出，目前巴西自然灾害经济损失平均仅约9%由保险承担，远低于全球约45%的水平，灾后主要依赖公共财政资源，令公众、企业与政府承担损失。方案拟建立分层级的巨灾与灾难风险融资体系，把更多风险转移至保险、再保与资本市场，并由公私协调配合减灾与适应措施；风险分层路径为每一层风险配置不同的风险转移与融资工具，包括参数触发机制。文件设想的推进路径由参数保险试点起步，经沙盒鼓励风险转移创新，再推进至主权风险转移，同时需要监管工作完善LRS制度并把巨灾债引入巴西。长期愿景包括巴西巨灾风险池、南美洲区域风险共担、类似世界银行发行的主权巨灾债，以及以税务诱因鼓励投保巨灾保险。SUSEP并建议进一步完善LRS结构以把自然灾害风险转移至资本市场，可能需要额外监管修订；政府亦可成为常设主权巨灾债计划的受益人，为留存于政府或公共资产负债表的峰值风险提供融资支持。', None),
         why=T('这是新兴市场把灾害风险「金融化」的完整路线图：投保比例仅约9%对全球约45%，缺口之大意味着未来数年的增量需求会落在参数保险、LRS与主权巨灾债三条线上。对ILS市场而言，更多主权与本地ILS工具意味着可投资标的与分散化来源增加；对关注发展中国家保障缺口的读者，这份文件提供了监管方自认的目标与路径，而非第三方推测。', None),
         actions={'front': T('客户问及新兴市场自然灾害保障时，只引用SUSEP公开的投保比例与方案方向，不作产品推介'),
                  'midback': T('把新兴市场参数保险与主权巨灾债动向列入ILS与另类风险转移的市场观察'),
                  'lead': T('引用须标注为监管机构建议文件（SUSEP工作组成果），非已生效法规'),
                  'cross': T('新兴市场风险转移工具的参与资格与分销限制按属地规则处理，勿直接对应本地产品')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Artemis.bm 2026-09-30 [EN原文]', 'tc': 'Artemis.bm 2026-09-30 [EN原文]', 'lang': 'en'},
         boards=['reg', 'market'], themes=['ils', 'reg', 'catastrophe', 'cat-risk'],
         tags=tg('巴西', 'SUSEP', 'LRS', '参数保险', '巨灾债', '保障缺口'),
         originalUrl='https://www.artemis.bm/news/brazils-susep-proposes-lrs-reforms-cat-bonds-parametrics-for-catastrophe-protection/'),
]


def main():
    path = os.path.join(BASE, 'data', 'live-items.json')
    data = json.load(open(path, encoding='utf-8'))
    existing = {it.get('id') for it in data['items']}
    new = [it for it in NEW if it['id'] not in existing]
    dup = [it['id'] for it in NEW if it['id'] in existing]
    if dup:
        print('跳过已存在:', dup)
    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    data['items'] = new + data['items']
    data['meta']['generatedAt'] = NOW
    data['meta']['itemCount'] = len(data['items'])
    n = len(data['items'])
    data['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
    shutil.copy(path, os.path.join(BASE, 'data/live-items.json.bak-0930-2245'))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'写入完成: 新增 {len(new)} 条, 合计 {n} 条')
    for it in new:
        print(' +', it['publishedAt'], it['id'])


if __name__ == '__main__':
    main()
