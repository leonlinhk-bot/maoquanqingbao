#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 00:23（深夜补采，承接 09-29 18:08 未提交批次）增量采集。

窗口：2026-09-29 18:10 → 2026-09-30 00:55（周二深夜 / 周三凌晨）
核验说明（逐源）：
- HKMA：新闻稿页实抓（116KB），9/29 第 6 条 = 第四批数码绿色债券（政府新闻公报 20:10 代发）
  → 入库；半年度报告(16:30)、HKICL 伪冒网站(17:10) 已于 18:08 批次入库；外汇基金票据投标结果(16:00)不取。
- IA：官网 press_releases / circulars 直连返回 403（Cloudflare），经搜索交叉核验，新闻稿最新仍为 24/9
  （富卫 AML 罚款，已入库）、演辞最新 8/9 → 窗口内无新增。
- NFRA：官网列表页为 JS 渲染；经 doubao 检索核验，9/29 仅内贸险通知（16:20，已入库），
  科技保险交流推进会为 9/28（已入库）→ 窗口内无新增。
- HKFI：官网媒体室 404/最新 16/9 → 无新增。
- family_office(FSTB)：新闻公报页实抓，9/29 最后一则为「财库局率业界考察北都(14:30)」，已在库 → 无新增。
- 保司：AIA 最新 24/9、AXA 最新 23/9、宏利 ILAS 通知最新 17/9、保诚/永明页面 JS 渲染，
  经检索最新仍为月中 → 窗口内无新增。
- insuranceasianews(WP API)：最新 29/9 14:35（日本 AIG），在 18:08 窗口之前 → 无新增。
- insurancebusinessmag(Atom)：最新 29/9 14:50 → 无新增。
- insuranceasia：RSS 404，经站点 /news 实抓，最新条目为 18:30 前后，未能逐条取到分钟级时间戳 → 本批不取。
- artemis：RSS 实抓，窗口内新增 3 条（18:30 / 19:42 / 21:30）→ 全部入库。
- scmp：RSS 实抓，窗口内 2 条（20:00 AI 采用率、22:12 一手物业卖方罚款）→ 入库（pending，未核原文）；
  17:00–18:00 三则（豪宅、花旗、PIMCO）已于 18:08 批次入库。
- 注：GMT EIGHT 9/30「内地访客定义咨询」一则经核为 2026-03 明报旧闻再刊 → 不取（避免误导）。
本批 6 条覆盖 hkma / artemis / scmp。
"""
import json, shutil, os
import zhconv

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-09-30T00:55:00+08:00'

# zh-tw 转换再修正为港式用字（与库内既有用字保持一致）
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
    # ======================= 官方 / 监管 =======================
    item(id='hkma-hksar-fourth-digital-green-bonds-20260929', score=88, verifyStatus='verified',
         sourceTier='official', sourceKey='hkma', contentKind='press',
         publishedAt='2026-09-29T20:10:00+08:00',
         title=T('香港特区政府发售第四批数码绿色债券：约200亿港元等值、四币种，港元二年期3.80%、人民币五年期1.65%、美元三年期5.023%、欧元四年期3.734%；港元部分通过EnsembleTX引入代币化存款',
                 '香港特區政府發售第四批數碼綠色債券：約200億港元等值、四幣種，港元二年期3.80%、人民幣五年期1.65%、美元三年期5.023%、歐元四年期3.734%；港元部分透過EnsembleTX引入代幣化存款'),
         summary=T('香港特区政府9月29日宣布，在政府可持续债券计划下成功定价约200亿港元等值的第四批数码绿色债券，涵盖港元、人民币、美元及欧元。经网路路演后于9月28日定价：55亿港元二年期3.80%、75亿人民币五年期1.65%、2亿美元三年期5.023%、4.5亿欧元四年期3.734%。四个币种认购额为发行额约1.3至11.3倍，再度刷新全球最大数码债券发行纪录。除沿用传统结算与上次引入的代币化央行货币交收选项外，本次在港元债券一级发行结算流程中通过EnsembleTX引入代币化存款，为全球首批引入港元代币化存款的数码债券；并采用国际资本市场协会债券数据分类术语（BDT）2.0。',
                 None),
         why=T('这是本港债券市场基建的年度关键节点：四币种同时定价，为港元、人民币、美元、欧元四条收益率曲线留下官方新发债定价锚；代币化存款与BDT 2.0则指向结算与数据标准的迁移方向。对保险资金而言，绿色债券与数码债券的供给规模、期限结构与结算方式，会持续影响固定收益组合的可选标的与营运流程；对前线而言，是回应客户对「香港债市深度与美元资产」提问时可引用的官方事实。',
                 None),
         actions={'front': T('客户问香港债市与美元资产时，可引用「政府发行200亿等值四币种绿债、认购1.3–11.3倍」等公开事实，不作收益承诺或产品推荐'),
                  'midback': T('把数码债券／代币化存款的推进节点列入固定收益与营运流程观察清单'),
                  'lead': T('引用须标明为政府可持续债券计划下的发行，并注明各币种期限与票息为发行定价、非投资建议'),
                  'cross': T('人民币与欧元债的投资者基础扩大，对跨境客户的多币种资产讨论有参照意义，但须按属地规则处理')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 3, 'cross': 2},
         source={'sc': '香港特区政府新闻公报（代香港金融管理局发出） 2026-09-29 20:10', 'tc': '香港特區政府新聞公報（代香港金融管理局發出） 2026-09-29 20:10', 'lang': 'zh'},
         boards=['market'], themes=['market', 'capital', 'esg'],
         tags=tg('数码绿色债券', '可持续债券计划', '代币化存款', 'EnsembleTX', 'BDT 2.0', '债券市场基建'),
         originalUrl='https://www.info.gov.hk/gia/general/202609/29/P2026092900686.htm'),

    # ======================= 媒体 / 市场 =======================
    item(id='artemis-oecd-micro-catastrophe-bonds-20260929', score=62, verifyStatus='verified',
         sourceTier='media', sourceKey='artemis', contentKind='news',
         publishedAt='2026-09-29T21:30:00+08:00',
         title=T('OECD发展中心政策简报：小额巨灾债（micro-cat bonds）在新兴亚洲「微灾风险融资」中应用潜力上升，建议与微型保险、参数型保障一并纳入工具箱 [EN原文]',
                 'OECD發展中心政策簡報：小額巨災債（micro-cat bonds）在新興亞洲「微災風險融資」中應用潛力上升，建議與微型保險、參數型保障一併納入工具箱 [EN原文]'),
         summary=T('Artemis 9月29日报道：OECD发展中心由Kensuke Molnar-Tanaka与Prasiwi Ibrahim撰写的政策简报指出，新兴亚洲大部分自然灾害损失仍未投保，家庭、小微企业与地方政府在灾后普遍缺乏资金支持。简报认为「微灾风险融资」工具——包括微型灾害保险与小额巨灾债——可基于更细致的本地风险与需求知识，更快速回应社区实际损失，与国家层级的应急基金、参数型保险及巨灾债形成互补。简报并引用Artemis交易目录中「较小规模巨灾债发行日趋可行、且多为私募配售」的趋势，认为可将小额巨灾债按区域客制化，以匹配农户与小微企业的风险特征。',
                 None),
         why=T('这条把「巨灾风险转移」的成本下限往下推了一格：传统巨灾债的规模门槛，一直把小微主体与地方财政挡在外面；若小额、私募配售的结构可行，风险转移的适用半径会明显扩大。对香港而言，这与推动ILS生态（含PCC架构）的方向同源，可作为理解「保险相连证券如何下沉到区域与小微」的政策参照，也提醒参数型产品须同时管理基差风险。',
                 None),
         actions={'front': T('客户问参数型或新型保障时，先讲明「按指标触发、与实损可能不一致」的基差风险，不作赔付或收益承诺'),
                  'midback': T('把巨灾债下沉至区域/小微主体（含私募配售）列入风险转移产品形态观察'),
                  'lead': T('引用须标明为OECD政策简报观点，并注明来源与日期，勿改写为香港政策已落地'),
                  'cross': T('东南亚与新兴亚洲的微灾融资安排涉及跨境监管与分销要求，客户涉当地业务时须个案确认')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Artemis.bm 2026-09-29（引述 OECD 发展中心政策简报）[EN原文]', 'tc': 'Artemis.bm 2026-09-29（引述 OECD 發展中心政策簡報）[EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'ils', 'catastrophe'],
         tags=tg('巨灾债', 'OECD', '微灾风险融资', '参数型保险', '新兴亚洲', '风险转移'),
         originalUrl='https://www.artemis.bm/news/micro-catastrophe-bonds-show-growing-potential-for-use-in-disaster-risk-financing-oecd/'),

    item(id='artemis-euler-ils-moodys-cat-risk-analytics-20260929', score=60, verifyStatus='verified',
         sourceTier='media', sourceKey='artemis', contentKind='news',
         publishedAt='2026-09-29T19:42:00+08:00',
         title=T('瑞士ILS投资管理人Euler ILS Partners与Moody\'s签订多年期巨灾风险分析协议：经Moody\'s智能风险平台取用自然巨灾与网络风险模型及专项风险、敞口数据集 [EN原文]',
                 '瑞士ILS投資管理人Euler ILS Partners與Moody\'s簽訂多年期巨災風險分析協議：經Moody\'s智能風險平台取用自然巨災與網絡風險模型及專項風險、敞口數據集 [EN原文]'),
         summary=T('Artemis 9月29日报道：瑞士专业保险相连证券（ILS）投资管理人Euler ILS Partners与Moody\'s签署多年期协议，将使用其巨灾风险模型、分析工具与敞口数据集，支持承保、组合管理与ILS投资决策；Euler将经Moody\'s智能风险平台取用自然巨灾与网络风险模型、以及一系列专项风险与敞口数据集。Moody\'s董事Stefano Nicolini称该协议反映Euler对其建模科学性与方法透明度的信任；Euler首席投资官Niklaus Hilti指，在投资者要求更高透明度、一致性与风险评估信心的环境下，可信分析工具比以往更重要。',
                 None),
         why=T('ILS与巨灾债的定价权，长期高度依赖少数巨灾模型供应商；投资人端与模型方的多年期绑定，说明「风险量化能力」正从技术成本变成准入条件。对承保与产品端而言，这解释了为何新型风险（如网络）要进入证券化结构之前，先要有可被资本市场接受的模型与敞口口径——这也是参数型与ILS产品能否扩张的隐性约束。',
                 None),
         actions={'front': T('客户问「保单背后的风险如何被评估」时，答风险评估由专业模型与再保安排支撑，不代答个案细节'),
                  'midback': T('把巨灾/网络风险建模供应商生态列入资本与风险转移观察'),
                  'lead': T('不要把模型与数据分析协议解读为任何产品收益或保障范围的承诺'),
                  'cross': T('网络风险证券化仍处早期，跨境客户若涉相关安排须按属地监管要求个案确认')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Artemis.bm 2026-09-29 [EN原文]', 'tc': 'Artemis.bm 2026-09-29 [EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'ils', 'reinsurance'],
         tags=tg('ILS', '巨灾风险模型', 'Moody\'s', 'Euler ILS', '网络风险', '风险分析'),
         originalUrl='https://www.artemis.bm/news/euler-ils-partners-signs-multi-year-catastrophe-risk-analytics-agreement-with-moodys/'),

    item(id='artemis-ils-advisers-august-2026-return-20260929', score=62, verifyStatus='verified',
         sourceTier='media', sourceKey='artemis', contentKind='stats',
         publishedAt='2026-09-29T18:30:00+08:00',
         title=T('ILS Advisers基金指数：8月ILS基金平均回报1.39%为年内最佳单月，纯巨灾债基金1.42%、含私募ILS者1.34%；年内平均累计6.56% [EN原文]',
                 'ILS Advisers基金指數：8月ILS基金平均回報1.39%為年內最佳單月，純巨災債基金1.42%、含私募ILS者1.34%；年內平均累計6.56% [EN原文]'),
         summary=T('Artemis 9月29日报道：ILS Advisers基金指数显示，2026年8月ILS基金策略回报加速，平均回报1.39%，为年内最佳单月，也是该指数自2025年10月以来最强单月；年内平均累计回报升至6.56%，在再保市场趋软背景下仍略高于历史平均。纯巨灾债基金8月平均1.42%（7月为0.95%），含私募ILS（如抵押再保）的基金平均1.34%（7月为1.23%）。ILS Advisers指二级市场受强劲投资者需求与有限供给支撑，8月无重大损失事件，巨灾债价格升1.33%，瑞士再保险全球巨灾债指数总回报2.22%。已报告业绩的基金全部为正回报。',
                 None),
         why=T('这是ILS资产端表现的月度体温计：8月回报由「季节性与价格动力」共同推升，前提是当月无重大灾损。对理解再保与巨灾债的资金供给节奏有直接价值——回报偏高会吸引更多资本入场，进一步压低费率，最终传导到财产险与再保的定价条件；而一旦大灾发生，这条链条会迅速反转。',
                 None),
         actions={'front': T('客户问ILS或再保相关资产时，须说明这属公开基金指数数据、非任何产品的回报承诺，且历史表现不代表未来'),
                  'midback': T('把ILS基金月度回报与巨灾债价格变动列入资产端与再保条件观察'),
                  'lead': T('引用一律标注来源（ILS Advisers基金指数）与月份口径，避免与自家产品收益率混用'),
                  'cross': T('ILS属专业投资者范畴，跨境客户的参与资格与分销限制按属地规则处理')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Artemis.bm 2026-09-29（引述 ILS Advisers 基金指数）[EN原文]', 'tc': 'Artemis.bm 2026-09-29（引述 ILS Advisers 基金指數）[EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'ils'],
         tags=tg('ILS基金', '巨灾债', '月度回报', 'ILS Advisers', '二级市场', '再保险定价'),
         originalUrl='https://www.artemis.bm/news/ils-fund-gains-accelerate-cat-bonds-particularly-strong-average-august-return-1-39-ils-advisers/'),

    item(id='scmp-vertex-developer-disclosure-fine-20260929', score=62, verifyStatus='pending',
         sourceTier='media', sourceKey='scmp', contentKind='news',
         publishedAt='2026-09-29T22:12:00+08:00',
         title=T('南华早报：长沙湾新盘The Vertex发展商Twin City因11宗违反一手住宅物业销售条例、未在24小时内如实记录付款条款，被判罚款共77万港元 [EN原文]',
                 '南華早報：長沙灣新盤The Vertex發展商Twin City因11宗違反一手住宅物業銷售條例、未在24小時內如實記錄付款條款，被判罰款共77萬港元 [EN原文]'),
         summary=T('南华早报9月29日报道：长沙湾住宅项目The Vertex（原由中国恒大持有）的发展商Twin City Holdings，因未妥善记录与项目相关的交易资料，被罚款合共77万港元。据政府声明，该公司违反一手住宅物业销售条例，未披露交易中的付款条款细节（如价格折扣及其他财务优惠）；违规涉及该项目东、西翼共11个单位，发展商未能在签署临时买卖合约后24小时内，将所需付款资料记入项目成交纪录册，共被票控11项，由一手住宅物业销售监管局（SRPA）公布罚款总额。',
                 None),
         why=T('这条的价值不在物业本身，而在监管对「销售过程记录与披露」的执行力度：付款条款、折扣与优惠必须如实、及时入册，违规按宗票控并累积罚款。同一套执法逻辑在保险销售的披露与销售流程记录上同样适用，是提醒前线与合规部门「销售文件与优惠说明必须留痕」的现实案例。',
                 None),
         actions={'front': T('谈销售合规时可用「条款与优惠须如实、及时记录」的原则，但不引述个案判断或作法律意见'),
                  'midback': T('把销售过程留痕（优惠、付款条款、时点）列入自查清单，与保险销售文件要求对照'),
                  'lead': T('引用须标明来源为SCMP报道及SRPA公布，待本局／监管原文核实后再作正式引用'),
                  'cross': T('跨境客户若涉港澳两地物业与保险安排，文件与披露口径需分别按属地要求处理')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 1, 'cross': 1},
         source={'sc': '南华早报（SCMP）2026-09-29 [EN原文，待核原文]', 'tc': '南華早報（SCMP）2026-09-29 [EN原文，待核原文]', 'lang': 'en'},
         boards=['market'], themes=['reg', 'market', 'enforcement'],
         tags=tg('一手住宅销售', '销售监管局', '罚款', '披露要求', '销售留痕', '合规执法'),
         originalUrl='https://www.scmp.com/business/companies/article/3369241/vertex-developer-hit-hk770000-fine'),

    item(id='scmp-hk-ai-adoption-lags-mainland-accenture-20260929', score=60, verifyStatus='pending',
         sourceTier='media', sourceKey='scmp', contentKind='news',
         publishedAt='2026-09-29T20:00:00+08:00',
         title=T('南华早报：埃森哲称香港企业AI采用落后内地——仅约一成港企将生成式AI整合到多个业务职能，内地约两成一；归因旧有系统包袱与偏保守的企业心态 [EN原文]',
                 '南華早報：埃森哲稱香港企業AI採用落後內地——僅約一成港企將生成式AI整合到多個業務職能，內地約兩成一；歸因舊有系統包袱與偏保守的企業心態 [EN原文]'),
         summary=T('南华早报9月29日报道：埃森哲大中华区香港办公室主管Robert Hah受访指出，香港企业在AI采用上落后于内地同业，主因是根深蒂固的旧有系统与偏保守的企业心态拖慢数码转型。据埃森哲调查，仅10%受访香港企业已将生成式AI整合到多个业务职能，内地企业约21%。报道指内地企业级AI采用迅速，部分得益于模型成本下降与本地开发者生态（包括DeepSeek、阿里巴巴等）。',
                 None),
         why=T('对香港保险与企业服务而言，这条点出AI落地的真实瓶颈不是工具可得性，而是旧系统与决策文化：整合度低意味着竞争优势尚未形成，也意味着「先把流程与数据打通、再谈模型」仍是主线。可作为团队内部推动AI项目时对难度预期的客观参照，同时提示在AI与数据治理上加码的必要性。',
                 None),
         actions={'front': T('谈AI应用时，先讲清「流程与数据基础决定成效」，不夸大数据或替代人工的幅度'),
                  'midback': T('把「多职能整合度」而非「工具数量」列为AI项目推进的检视指标'),
                  'lead': T('引用调查数据须标明机构、口径与日期，属机构观点而非行业既定结论'),
                  'cross': T('跨境团队若两地并行，注意内地与香港在数据、模型与合规要求上的差异')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': '南华早报（SCMP）2026-09-29 [EN原文，待核原文]', 'tc': '南華早報（SCMP）2026-09-29 [EN原文，待核原文]', 'lang': 'en'},
         boards=['tech'], themes=['tech', 'ai'],
         tags=tg('AI采用', '埃森哲', '生成式AI', '旧有系统', '数码转型', '香港企业'),
         originalUrl='https://www.scmp.com/tech/policy/article/3369205/hong-kong-firms-lag-mainland-china-ai-adoption'),
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
    shutil.copy(path, os.path.join(BASE, 'data/live-items.json.bak-0930-0023'))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'写入完成: 新增 {len(new)} 条, 合计 {n} 条')
    for it in new:
        print(' +', it['publishedAt'], it['id'])


if __name__ == '__main__':
    main()
