#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-01 00:5x（周四，国庆）增量采集（承接 09-30 22:50 批次）。

窗口：2026-09-30 22:50 → 2026-10-01 00:55
逐源核验（14 信源）：
- IA：press_releases / circulars 页仍为 Cloudflare 保护（Just a moment...，Googlebot UA 亦被拦）；
  站内最新 IA 条目为《监管通讯》第13期（30/9 09:00，已入库）→ 窗口内无新增。
- HKMA：新闻稿页实抓，30/9 最新为 16:30 三则统计（货币统计／住宅按揭／外汇基金资产负债表，已入库）；
  30/9 17:05 HKICL 警示亦已入库 → 窗口内无新增。
- 保司（AIA/宏利/保诚/安盛/永明）：官网新闻室窗口内无新稿（宏利新闻室返回 403；永明/保诚页最新条目早于窗口）。
- insuranceasia(RSS)：最新 30/9 06:00 → 无新增。
- insuranceasianews(WP API)：最新 30/9 14:51（已入库）→ 无新增。
- insurancebusinessmag(Atom)：窗口内 2 则 → 取 1 则（印度 CCI 批准 BNP Paribas Cardif 收购 IndiaFirst Life 26%）；
  「The return to office is complete」与本域无关 → 不取。
- scmp(RSS)：窗口内 2 则，取 1 则（黄金周银行礼遇／20% 境外投资收益征税）；New World Development 亏损非本域 → 不取。
- artemis(RSS)：最新 30/9 21:00（Stone Ridge，已入库）→ 无新增。
- NFRA：官网 JS 不可直连，经检索 + 站内比对，补录 30/9 生效的《金融产品网络营销管理办法》（公告〔2026〕第9号），
  该办法将「境外机构未经许可面向境内居民提供金融产品服务」列为非法金融活动，直接约束港险内地网络导流。
- govhk(info.gov.hk RSS)：30/9 18:20 后 15 则均为食安／警务／立法会简报等 → 无保险相关。
- HKFI：media-release 及备用路径均 404（改版）→ 无可取内容；FSTB 首页窗口内无保险／家办新稿。
- insurtech / family_office：窗口内无新增。
本批 3 条覆盖 nfra / insurancebusinessmag / scmp 三类信源（3 个 sourceKey）。
"""
import json, shutil, os
import zhconv

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-10-01T00:55:00+08:00'

FIX = {'轉帳': '轉賬', '鏈接': '連結', '裏面': '裡面'}


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
    # ======================= 内地网络营销新规生效（港险导流直接相关） =======================
    item(id='nfra-financial-product-online-marketing-effective-20260930', score=86, verifyStatus='verified',
         sourceTier='official', sourceKey='nfra', contentKind='circular',
         publishedAt='2026-09-30T00:00:00+08:00',
         title=T('人民银行等八部门《金融产品网络营销管理办法》9月30日起施行：保险纳入统一网络营销规范，禁止夸大保险责任或保险产品收益、禁止将保险收益与存款及资管产品简单类比；「境外机构未经许可面向境内居民提供金融产品服务」明确列为非法金融活动，任何机构和个人不得为其提供网络营销服务或便利；公众号、直播、短视频营销须由持牌从业人员在经审核内容及授权账号内进行并全程可回溯',
                 '人民銀行等八部門《金融產品網絡營銷管理辦法》9月30日起施行：保險納入統一網絡營銷規範，禁止誇大保險責任或保險產品收益、禁止將保險收益與存款及資管產品簡單類比；「境外機構未經許可面向境內居民提供金融產品服務」明確列為非法金融活動，任何機構和個人不得為其提供網絡營銷服務或便利；公眾號、直播、短視頻營銷須由持牌從業人員在經審核內容及授權賬號內進行並全程可回溯'),
         summary=T('中国人民银行、工业和信息化部、市场监管总局、金融监管总局、中国证监会、国家知识产权局、国家网信办、国家外汇局联合发布的《金融产品网络营销管理办法》（公告〔2026〕第9号，2026年4月21日发布）自2026年9月30日起施行。办法把保险纳入「金融产品」范围（含存款、贷款、证券、资管产品、保险、贵金属、外汇、期货、衍生品、支付、投资顾问或咨询等），对通过互联网对金融产品进行商业性宣传推介——包括展示介绍产品信息、为消费者购买提供转接渠道——统一规范。要点一：第六条把「境外机构未经许可面向境内居民提供金融产品服务」与非法集资、非法证券期货活动、非法外汇保证金交易等并列为非法金融活动，明确任何机构和个人不得为其提供网络营销服务或者便利。要点二：第十二项禁止性行为（第十条）包括使用虚假或引人误解的内容、引用不真实或未经核实的数据资料、夸大保险责任或保险产品收益、将保险产品收益与存款及资产管理产品等金融产品简单类比，以及使用「低风险」「低门槛」「秒到账」「高收益」「无成本」等诱导性用语。要点三：第十六条要求通过公众号、直播、短视频营销金融产品的，须在金融机构自营平台或其合法开设的第三方平台账号进行，营销人员须为具备资格的金融机构从业人员并获机构授权；机构须加强合规审查与可回溯管理、保存视频音频图文资料供查验；平台须核验从业主体资质、在账号主页展示资质材料，对不符合者暂停服务或关闭账号，并加强巡查、发现违规立即停止信息发布并向监管部门报告。要点四：第十八、十九条限制未取得相应资质者在网站、应用程序及账号名称、商标中使用「保险」「理财」「资产管理」「投资顾问或咨询」等涉金融字样。要点五：第二十条至二十五条要求第三方平台恪守技术服务本位，不得介入或变相介入销售合同签订、资金划转、适当性测评，不得就金融产品与消费者互动咨询，不得以「投资者教育」「课程培训」等形式变相开展网络营销并收取费用，不得转委托。违规者由金融管理部门依职责采取出具警示函、监管谈话、责令整改、行政处罚等措施，涉嫌犯罪移送司法机关；金融监管总局依职责负责银行、保险领域的监督管理。', None),
         why=T('这条对内地获客链条的约束是结构性的：把「境外机构未经许可面向境内居民提供金融产品服务」写进非法金融活动定义，并禁止任何主体为其提供网络营销服务或便利，等于在制度层面覆盖了内地社交平台上的港险导流内容、以「投资者教育／课程培训」包装的变相营销，以及无资质账号使用「保险」字样揽客等做法。配合第十六条的账号资质核验、内容前置审核与可回溯留存，营销链条上机构、从业人员、平台三方责任都被点名，平台还有主动巡查与报告义务，违规成本从「内容下架」升级为可处罚、可追责。对服务内地客户的团队而言，这是继经纪转介费基准（2025年10月起）与分红险首年佣金不超过70%（2026年1月起）之后，第三条直接改变获客方式的规则，值得与现有转介管理、内容合规流程一并复核。', None),
         actions={'front': T('不在内地社交平台宣传推介境外保险；不参与以「投资者教育」「课程培训」为名的变相营销与付费导流'),
                  'midback': T('逐一核验内容渠道与账号资质，确保宣传内容经公司审核、从业人员持牌且可回溯留档'),
                  'lead': T('把网络营销合规纳入渠道管理制度，明确平台、账号、内容的授权、审查与终止合作机制'),
                  'cross': T('涉及内地客户的内容一律不做境内网络营销；跨境展业边界按两地规则从严把握')},
         rolesImpact={'front': 3, 'midback': 3, 'lead': 3, 'cross': 3},
         source={'sc': '中国人民银行等八部门公告〔2026〕第9号（2026年4月21日发布，2026年9月30日起施行）',
                 'tc': '中國人民銀行等八部門公告〔2026〕第9號（2026年4月21日發布，2026年9月30日起施行）', 'lang': 'zh'},
         boards=['reg', 'compliance'], themes=['reg', 'compliance', 'channel', 'cross-border'],
         tags=tg('网络营销', '境外保险', '投资者教育', '账号资质', '内容可回溯', '八部门公告'),
         originalUrl='https://www.csrc.gov.cn/csrc/c100028/c7628276/content.shtml'),

    # ======================= 印度寿险外资并购与分销结构 =======================
    item(id='ibm-indiafirst-life-bnp-paribas-cardif-cci-20260930', score=76, verifyStatus='verified',
         sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
         publishedAt='2026-09-30T23:12:00+08:00',
         title=T('印度竞争委员会（CCI）批准法国巴黎银行保险部门BNP Paribas Cardif向Warburg Pincus收购IndiaFirst Life 26%股权：交割后Bank of Baroda持股65%、Cardif 26%、Union Bank of India 9%；印度已于2026年2月放开寿险外资100%持股，但银行保险占新单逾33%，外资选择以少数股权换取银行渠道；印度保险经纪协会同日就IRDAI分销经济草案（佣金上限收紧、费用限额拟降三分一）发声 [EN原文]',
                 '印度競爭委員會（CCI）批准法國巴黎銀行保險部門BNP Paribas Cardif向Warburg Pincus收購IndiaFirst Life 26%股權：交割後Bank of Baroda持股65%、Cardif 26%、Union Bank of India 9%；印度已於2026年2月放開壽險外資100%持股，但銀行保險佔新單逾33%，外資選擇以少數股權換取銀行渠道；印度保險經紀協會同日就IRDAI分銷經濟草案（佣金上限收緊、費用限額擬降三分一）發聲 [EN原文]'),
         summary=T('Insurance Business Asia 9月30日23:12报道：印度竞争委员会（CCI）已批准BNP Paribas Cardif向私募股权公司Warburg Pincus收购IndiaFirst Life Insurance 26%股权，交易的最后一道监管障碍清除（据《经济时报》）。Cardif为法国巴黎银行集团保险部门，2026年7月签订具约束力协议；交易完成后IndiaFirst Life股东结构为Bank of Baroda持股65%、BNP Paribas Cardif持股26%、Union Bank of India持股9%。IndiaFirst Life于2009年由Bank of Baroda发起成立；彭博2026年3月报道该交易隐含估值约3.5亿美元。Cardif行政总裁Pauline Leclerc-Glorieux表示，该交易将推进其与高潜力市场强机构合作的国际增长策略。报道指出一个反差：按《Sabka Bima Sabki Raksha（保险法修订）法案2025》（2026年2月5日生效），印度已允许寿险公司外资持股100%，但Cardif仍选择少数股权。原因是分销结构：据Magi Research and Consultants研究，银行保险（bancassurance）占印度全部新寿险保单逾33%，与Bank of Baroda既有分行网络结盟可即时获得分销覆盖，包括独立渠道难以开拓的半城市化与农村市场。基本面上，IRDAI 2025年12月年度报告显示印度寿险渗透率连续第三年下滑，2025财年降至GDP的2.7%（前一财年2.8%）；瑞士再保险数据显示印度按名义保费为全球第十大保险市场；印度保险经纪协会（IBAI）与麦肯锡2025年7月报告指每两名印度成年人中仅一人持有任何寿险，并预测市场可由2024年的11万亿卢比增至2030年的25万亿卢比。IBAI（代表印度798家持牌保险经纪）于2026年9月30日就IRDAI分销经济草案发声，警告收紧佣金上限及拟将保险公司整体费用限额削减三分之一的建议，可能会损害委任经纪比较产品并协助理赔的客户；IBAI并指截至2025年3月31日，经纪机构保荐了印度27.18万名销售点人员中的14.81万名，其中不少在小城镇营运。', None),
         why=T('这条把「外资开放」与「渠道结构」的真实取舍摆在一起：印度已允许外资100%持股，但Cardif仍以26%少数股权换取Bank of Baroda的分行与客群，说明在银行保险占新单逾三成的市场里，分销通道比控股权更值钱。对区域分销格局的含义是双向的：银行渠道进一步集中，独立经纪的相对空间会受压，而IBAI同日的发声正反映这一张力——佣金上限与费用限额收紧会先压缩靠佣金生存的中介。对关注亚洲市场准入与分销经济性的团队，这是判断「牌照放开是否等于机会放开」的具体案例；印度渗透率降至2.7%、半数成年人无寿险，也说明增量空间在保障缺口而非存量争夺。', None),
         actions={'front': T('客户问及亚洲市场比较时，只引用公开的监管批准与持股结构，不作任何市场或产品推荐'),
                  'midback': T('把印度等新兴市场的分销结构与佣金监管变化纳入区域市场观察，季度更新'),
                  'lead': T('引用须标注为媒体报道与公开研究（CCI/IRDAI/IBAI），勿延伸为本公司立场'),
                  'cross': T('南亚与东南亚市场的牌照、佣金与分销限制各异，客户涉当地业务须按属地规则个案确认')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Insurance Business Asia 2026-09-30 23:12（综合 CCI／IRDAI／IBAI／瑞士再保险）[EN原文]',
                 'tc': 'Insurance Business Asia 2026-09-30 23:12（綜合 CCI／IRDAI／IBAI／瑞士再保險）[EN原文]', 'lang': 'en'},
         boards=['insurer', 'market'], themes=['distribution', 'capital', 'market', 'reg'],
         tags=tg('印度寿险', 'BNP Paribas Cardif', 'IndiaFirst Life', '银行保险', '外资持股', '分销经济'),
         originalUrl='https://www.insurancebusinessmag.com/asia/news/life-insurance/competition-watchdog-clears-french-insurers-stake-in-indiafirst-life-591806.aspx'),

    # ======================= 黄金周跨境销售场景（20%境外收益征税后首个长假） =======================
    item(id='scmp-golden-week-bank-lures-crossborder-levy-20260930', score=60, verifyStatus='pending',
         sourceTier='media', sourceKey='scmp', contentKind='news',
         publishedAt='2026-09-30T23:39:00+08:00',
         title=T('香港银行在内地收紧跨境投资规则、并对境外投资或保险收益征收20%税项后的首个黄金周，继续以免门槛礼遇争取内地访客：汇丰为新高端客户提供最高8.8万港元（约11,215美元）优惠，并附国庆烟花晚宴、北京中国网球公开赛或韩国流行歌手演唱会门票等体验 [EN原文]',
                 '香港銀行在內地收緊跨境投資規則、並對境外投資或保險收益徵收20%稅項後的首個黃金周，繼續以免門檻禮遇爭取內地訪客：滙豐為新高端客戶提供最高8.8萬港元（約11,215美元）優惠，並附國慶煙花晚宴、北京中國網球公開賽或韓國流行歌手演唱會門票等體驗 [EN原文]'),
         summary=T('《南华早报》9月30日23:39报道：在「十一黄金周」——即北京收紧跨境投资规则、并就对境外投资或保险收益征收20%税项之后的第一个黄金周——香港商业银行继续向内地访客提供优惠以争取业务。报道示例：汇丰银行为新高端客户提供最高8.8万港元（约11,215美元）优惠，并搭配体验类礼遇，包括国庆烟花晚宴，以及北京中国网球公开赛或韩国流行歌手演唱会门票等（据该行资料）。报道聚焦银行在跨境理财与高端客户获取上的竞争安排，涉及内地客户在港的资产配置与服务选择。', None),
         why=T('这是20%境外投资／保险收益征税与跨境投资规则收紧之后的第一个黄金周，银行仍以高额礼遇与稀缺体验争客，说明内地客户在港配置资产的需求并未因税务与合规收紧而消失，竞争反而从产品条款延伸到服务与体验的「软性差异」。对保险渠道而言，同一批客群、同一段时间窗，银行以存款、理财与保险多重产品包揽，中介若只比产品条件，容易被银行的综合服务与礼遇比下去；同时跨境销售的税务申报与合规边界在这段时间更受关注，任何回佣、返点或代客安排都属高风险。这条适合作为黄金周期间的客户沟通背景，而非产品推荐依据。', None),
         actions={'front': T('不比较或转述个别银行的优惠金额与礼遇；客户问及黄金周赴港安排时，只说明须亲身在港完成销售流程'),
                  'midback': T('黄金周期间强化客户沟通与留痕：投资声明、风险披露、税务提示逐项到位'),
                  'lead': T('把跨境客户服务标准与礼遇竞争区分开，不以费用或回赠类安排争取客户'),
                  'cross': T('内地客户的境外收益与保险收益税务申报属客户自身责任，中介不得提供规避建议')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 1, 'cross': 2},
         source={'sc': 'South China Morning Post 2026-09-30 23:39（据 RSS 摘要，全文受订阅限制，待复核）[EN原文]',
                 'tc': 'South China Morning Post 2026-09-30 23:39（據 RSS 摘要，全文受訂閱限制，待覆核）[EN原文]', 'lang': 'en'},
         boards=['market', 'family'], themes=['cross-border', 'market', 'taxation', 'channel'],
         tags=tg('黄金周', '跨境理财', '20%税项', '汇丰', '高端客户', '赴港投保'),
         originalUrl='https://www.scmp.com/business/banking-finance/article/3369382/hong-kong-banks-set-golden-week-lures-mainland-chinese-visitors-despite-new-levies'),
]


def main():
    path = os.path.join(BASE, 'data', 'live-items.json')
    data = json.load(open(path, encoding='utf-8'))
    existing = {it.get('id') for it in data['items']}
    new = [it for it in NEW if it['id'] not in existing]
    dup = [it['id'] for it in NEW if it['id'] in existing]
    if dup:
        print('跳过已存在:', dup)
    # 同 sourceKey 同标题重复保护：按 originalUrl 去重
    urls = {it.get('originalUrl') for it in data['items']}
    new = [it for it in new if it['originalUrl'] not in urls]
    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    data['items'] = new + data['items']
    data['meta']['generatedAt'] = NOW
    data['meta']['itemCount'] = len(data['items'])
    n = len(data['items'])
    data['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
    shutil.copy(path, os.path.join(BASE, 'data/live-items.json.bak-1001-0055'))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'写入完成: 新增 {len(new)} 条, 合计 {n} 条')
    for it in new:
        print(' +', it['publishedAt'], it['id'])


if __name__ == '__main__':
    main()
