# -*- coding: utf-8 -*-
"""2026-09-22 21:08(实际22:15) 增量插入脚本 — 猫圈儿港险情报站"""
import json, shutil, os
from datetime import datetime, timezone, timedelta
import zhconv

HKT = timezone(timedelta(hours=8))
NOW = datetime.now(HKT)
NOW_ISO = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

def tc(s):
    return zhconv.convert(s, 'zh-hk')

def mk(id_, publishedAt, score, tier, key, src_label, lang, title_sc, summary_sc, why_sc,
       boards, themes, tags_sc, url, actions=None, roles=None, kind='news', verify='pending',
       role_label=True):
    a = {'front': {}, 'midback': {}, 'lead': {}, 'cross': {}}
    if actions:
        for k, v in actions.items():
            a[k] = {'sc': v, 'tc': tc(v)}
    it = {
        'clusterCount': 1,
        'score': score,
        'verifyStatus': verify,
        'sourceTier': tier,
        'actions': a,
        'rolesImpact': roles or {'front': 0, 'midback': 1, 'lead': 1, 'cross': 0},
        'source': {'sc': src_label, 'lang': lang},
        'contentKind': kind,
        'id': id_,
        'sourceKey': key,
        'title': {'sc': title_sc, 'tc': tc(title_sc)},
        'summary': {'sc': summary_sc, 'tc': tc(summary_sc)},
        'why': {'sc': why_sc, 'tc': tc(why_sc)},
        'boards': boards,
        'themes': themes,
        'tags': {'sc': tags_sc, 'tc': [tc(t) for t in tags_sc]},
        'publishedAt': publishedAt,
        'originalUrl': url,
    }
    if role_label:
        it['contentRole'] = {'sc': '本站导读', 'tc': '本站導讀'}
        it['featured'] = False
        it['evergreen'] = False
    return it

ITEMS = [
    mk('ibm-allianz-captive-head-20260922', '2026-09-22T21:54:00+08:00', 68, 'media',
       'insurancebusinessmag', 'Insurance Business Asia（2026-09-22）', 'en',
       '安联聘请 AIG 老将执掌全球专属自保前端与解决方案业务 [EN原文]',
       '安联商业（Allianz Commercial）任命 Stephen Morton 为全球专属自保前端及自保解决方案主管，2027年3月1日生效，常驻巴黎并向另类风险转移（ART）全球主管 Lara Martiner 汇报，接替服务约七年后退休的 Brian McNamara。Morton 有逾30年保险经验，此前任 AIG 前端与跨国业务全球首席承保官。安联称该业务组合过去15年增长强劲，涵盖单一险种前端承保到多年期、多险种跨境结构；Martiner 引述全球自保市场约600亿美元保费、约6,000家自保公司。',
       '专属自保是香港「风险管理中心」定位下的政策抓手之一（五年规划已提出自保与 PCC 框架、ILS 投资者限制检讨）。国际集团承保团队换人，会直接影响跨国自保与前端方案的对接人与承保口径，值得在客户谈「自保+前端+再保」架构时同步留意。',
       ['insurer'], ['leadership', 'reinsurance'], ['安联', '专属自保', '前端承保', '人事', '另类风险转移'],
       'https://www.insurancebusinessmag.com/asia/news/breaking-news/allianz-taps-aig-veteran-to-lead-global-captive-solutions-business-590677.aspx',
       actions={'lead': '留意专属自保与 PCC/ILS 框架配套，评估自保客户方案的再保与前端对接渠道'},
       roles={'front': 0, 'midback': 1, 'lead': 2, 'cross': 1}, verify='verified'),

    mk('ibm-zurich-beazley-court-20260922', '2026-09-22T21:03:00+08:00', 74, 'media',
       'insurancebusinessmag', 'Insurance Business Asia（2026-09-22）', 'en',
       '伦敦高等法院放行苏黎世81亿英镑收购 Beazley，10月1日完成 [EN原文]',
       '英格兰及威尔士高等法院周二批准苏黎世收购劳合社专业险商 Beazley 的安排计划，庭上无人提出反对，董事会此前已一致支持。交易对价为每股1,310便士现金另加25便士股息（合计1,335便士），较1月中收市价820便士溢价59.8%，作价约81亿英镑（约109亿美元）。苏黎世9月14日确认监管批准齐备，交易将于10月1日生效，股东两周内收到现金。分析师称此为十余年来专业险最重大整合之一，可能引发同业竞争性回应，并推动网络风险建模与威胁情报投资。',
       'Beazley 的网络险与劳合社牌照是本次收购的核心资产。对做企业/高净值专业险渠道的团队，供应商集中度上升意味着承保口径与容量排布可能调整，续保年度宜提前确认条线策略。',
       ['insurer', 'market'], ['ma', 'cyber'], ['苏黎世', 'Beazley', '劳合社', '并购', '网络险'],
       'https://www.insurancebusinessmag.com/asia/news/breaking-news/zurichs-8-1bn-swoop-for-beazley-gets-the-green-light-from-londons-high-court-590666.aspx',
       actions={'midback': '关注并购完成后网络险与专业险条线的承保口径及授权变化'},
       roles={'front': 1, 'midback': 2, 'lead': 1, 'cross': 1}, verify='verified'),

    mk('ibm-el-nino-record-2026-losses-20260922', '2026-09-22T18:16:00+08:00', 72, 'media',
       'insurancebusinessmag', 'Insurance Business Asia（2026-09-22）', 'en',
       '「史上最强厄尔尼诺」成形：海温破150年纪录，损失已进账 [EN原文]',
       '2026–2027年厄尔尼诺关键海区海温较1991–2020年均值高3.05℃，超越2015年11月的3.02℃纪录。气候学家 Zeke Hausfather 预计11–12月或升至4.0℃；英国气象局称其为「19世纪以来最大」，世界气象组织称至少千年最强，NOAA 给出9月至明年1月持续概率≥90%。2026年已出现夏威夷飓风、美国洪水、智利风暴与秘鲁高温等事件，8月为有记录以来最热8月（较工业化前高1.65℃）。距峰值约8–10周。',
       '巨灾累积是承保端最真实的「尾部」问题：若巨灾模型按3.0℃校准，4.0℃情景下的超赔层与再保结构可能不足。财产、农业、能源及供应链客户在续保前值得重检分区限额、免赔与累积管理假设。',
       ['market'], ['catastrophe', 'reinsurance'], ['厄尔尼诺', '巨灾模型', '累积风险', '再保险', '气候变化'],
       'https://www.insurancebusinessmag.com/asia/news/breaking-news/the-strongest-el-nino-in-recorded-history-is-building--insurers-are-already-paying-the-price-590647.aspx',
       actions={'midback': '提醒财产/农业/能源客户在续保前检视分区限额、免赔与累积假设', 'lead': '评估再保结构与巨灾模型情景是否需要按更高海温情景重算'},
       roles={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1}, verify='verified'),

    mk('ibm-insurance-moves-canopius-hdi-20260921', '2026-09-21T23:42:00+08:00', 66, 'media',
       'insurancebusinessmag', 'Insurance Business Asia（2026-09-21）', 'en',
       '人事动向：Canopius 亚太补三席，HDI Global 推进北亚项目型业务 [EN原文]',
       '报道指 Canopius 在亚太新增三名人员，分别覆盖理赔、财产及信用风险条线；HDI Global 同步推进北亚的项目型业务（programmes）。同期区域人事动态还包括 Lockton 与 Manulife 的相关任命。亚洲专业险与项目险的承保团队正在重新排布，本地承保人才竞争随之升温。',
       '专业险团队补位往往先于承保口径调整；北亚项目型业务（programmes）活跃度提升，意味着大型企业客户的分层承保结构会有更多本地选项，值得在续保谈判前摸清各家的授权边界。',
       ['insurer'], ['talent', 'underwriting'], ['Canopius', 'HDI Global', '北亚', '项目型业务', '人事'],
       'https://www.insurancebusinessmag.com/asia/news/breaking-news/insurance-moves-lockton-canopius-manulife-hdi-global-590521.aspx',
       actions={'lead': '留意北亚项目型业务新容量的授权边界与承保偏好'},
       roles={'front': 1, 'midback': 1, 'lead': 2, 'cross': 1}, verify='pending'),

    mk('ian-aon-jane-drummond-global-cco-20260922', '2026-09-22T21:30:00+08:00', 70, 'pro',
       'insuranceasianews', 'InsuranceAsia News（2026-09-22）', 'en',
       '怡安擢升亚太首席商务官 Jane Drummond 为全球首席商务官 [EN原文]',
       '怡安（Aon）宣布将现任亚太区首席商务官 Jane Drummond 擢升为全球首席商务官，自1月1日起生效。该任命是亚太区人才进入集团全球决策层的最新一例；Aon 近期在亚洲区亦有多项人事与业务布局。',
       '经纪渠道的决策权进一步向全球总部集中，对香港复杂风险方案的全球协调、再保安排与跨境客户服务节奏有间接影响；对前线而言，意味着复杂个案（跨境架构、大额企业险）的解决路径可能更依赖区域—全球联动。',
       ['insurer'], ['talent', 'channel'], ['怡安', '保险经纪', '人事', '亚太', '全球总部'],
       'https://insuranceasianews.com/aon-promotes-jane-drummond-to-global-chief-commercial-officer/',
       actions={'lead': '留意经纪渠道全球条线负责人更替对复杂风险方案协调节奏的影响'},
       roles={'front': 1, 'midback': 0, 'lead': 2, 'cross': 1}, verify='pending'),

    mk('ian-oneglobal-fraction-hk-crypto-20260922', '2026-09-22T07:42:00+08:00', 74, 'pro',
       'insuranceasianews', 'InsuranceAsia News（2026-09-22）', 'en',
       'Oneglobal 完成收购香港加密资产专业经纪 Fraction [EN原文]',
       '国际经纪集团 Oneglobal 宣布完成对香港加密资产专业经纪商 Fraction 的收购，金额未披露。该交易归入金融责任险（financial lines）与香港市场条线，反映香港虚拟资产生态在牌照与稳定币制度落地后，对专业责任、托管与合规类保险安排的需求上升；Oneglobal 借此扩充香港及亚太专业险团队。',
       '数字资产相关责任险是香港专业险少见的增量赛道，但承保能力高度依赖少数再保方。团队若接触持牌虚拟资产平台或家族办公室客户，宜先确认可用容量与免责边界，避免口头承诺。',
       ['insurer', 'market'], ['ma', 'cyber'], ['虚拟资产', '专业责任险', 'Oneglobal', '香港', '并购'],
       'https://insuranceasianews.com/oneglobal-completes-takeover-of-hong-kong-crypto-specialist-fraction/',
       actions={'front': '接触虚拟资产/家办客户前先确认数字资产责任险可用容量与免责范围'},
       roles={'front': 2, 'midback': 2, 'lead': 1, 'cross': 2}, verify='pending'),

    mk('ian-munich-re-specialty-property-df-20260922', '2026-09-22T18:00:00+08:00', 70, 'pro',
       'insuranceasianews', 'InsuranceAsia News（2026-09-22）', 'en',
       '慕尼黑再保险专业险增聘财产直接与临分承保人 Johnny Ng [EN原文]',
       '慕尼黑再保险专业险（Munich Re Specialty）任命 Johnny Ng 为财产险直接与临分（direct & facultative）承保人，常驻新加坡，从怡安（Aon）过档。该 Lloyd\'s 平台持续在亚洲补强财产险承保能力，反映亚太财产与临分需求仍在扩张。',
       '临分承保人到位通常先改善大额、非标财产风险的报价效率。对有大型财产或工程项目客户的中介，区域临分能力增强意味着个案安排路径更多元。',
       ['insurer'], ['talent', 'underwriting'], ['慕尼黑再保险', '临分', '财产险', '新加坡', '人事'],
       'https://insuranceasianews.com/munich-re-specialty-hires-johnny-ng-as-property-df-underwriter/',
       actions={'midback': '留意区域临分承保能力变化对非标财产个案报价节奏的影响'},
       roles={'front': 1, 'midback': 2, 'lead': 1, 'cross': 1}, verify='pending'),

    mk('ian-lockton-alex-bursak-credit-asia-20260922', '2026-09-22T12:56:00+08:00', 68, 'pro',
       'insuranceasianews', 'InsuranceAsia News（2026-09-22）', 'en',
       'Lockton 任命 Alex Bursak 为亚洲区信用险总监 [EN原文]',
       'Lockton 宣布任命 Alex Bursak 为亚洲区信用险（credit）总监。他由韦莱韬悦（WTW）过档，此前在安联贸易（Allianz Trade）亚太区任职逾八年，其中两年出任雅加达印尼区总经理。这是 Lockton 近期在亚洲的又一项人事布局。',
       '信用与贸易险条线的人才流动往往伴随产品与服务升级。对做贸易融资、应收账款保障客户的中介，区域信用险专业度提升意味着更细分的额度与条款设计空间。',
       ['insurer'], ['talent', 'underwriting'], ['Lockton', '信用险', '安联贸易', '亚洲', '人事'],
       'https://insuranceasianews.com/lockton-appoints-alex-bursak-as-regional-credit-director-for-asia/',
       actions={'midback': '留意信用险条线专业力量变化对贸易融资类客户方案的影响'},
       roles={'front': 1, 'midback': 2, 'lead': 1, 'cross': 1}, verify='pending'),

    mk('ian-policystreet-cuo-hannover-re-20260922', '2026-09-22T10:55:00+08:00', 72, 'pro',
       'insuranceasianews', 'InsuranceAsia News（2026-09-22）', 'en',
       '马来西亚数字保险商 PolicyStreet 延揽 Hannover Re 的 Firdaus Kasman 任首席承保官 [EN原文]',
       '马来西亚数字保险平台 PolicyStreet 任命 Firdaus Kasman 为首席承保官（CUO），他此前任职于汉诺威再保险（Hannover Re）。该任命显示东南亚 insurtech 正从流量与分销竞争，转向补强精算定价与承保核心能力。',
       '数字渠道平台补强承保核心，意味着其与再保方的定价与条款谈判能力上升，长期将改变东南亚嵌入式保险的费率与条款供给。对以东南亚为延伸市场的团队，可关注其后续产品结构与再保支持。',
       ['tech', 'insurer'], ['insurtech', 'talent'], ['PolicyStreet', 'insurtech', '承保', '东南亚', '人事'],
       'https://insuranceasianews.com/policystreet-snaps-up-hannover-res-firdaus-kasman-as-new-cuo/',
       actions={'lead': '观察东南亚数字渠道平台承保能力提升对区域费率与条款供给的影响'},
       roles={'front': 0, 'midback': 1, 'lead': 2, 'cross': 1}, verify='pending'),

    mk('scmp-mainland-insurers-hk-etf-inflows-20260922', '2026-09-22T12:20:00+08:00', 74, 'media',
       'scmp', 'South China Morning Post（2026-09-22）', 'en',
       '内地险资获准经互联互通买港股 ETF 满月：多只 ETF 成交放量',
       '南华早报报道，内地41万亿元人民币（约6.1万亿美元）的保险业资金正成为港股新变量：国家金融监督管理总局上月批准保险公司经「股票通」（互联互通）机制投资香港上市 ETF，市场观察人士以周一多只港股 ETF 成交放量作为险资入场的迹象。若配置持续，将改变港股流动性与 ETF 生态结构。',
       '险资跨境配置是内地资金「出海」的又一合规通道，也间接影响以港股资产为底层的储蓄型与投资型产品的外部环境。销售端可用作解释资产端环境的背景信息，但不应延伸为任何收益表述。',
       ['market'], ['cross-border', 'capital'], ['内地险资', '港股ETF', '互联互通', '跨境配置', '流动性'],
       'https://www.scmp.com/business/china-business/article/3368329/hong-kong-stocks-eye-fresh-inflows-mainland-chinas-insurers-sitting-us6-trillion',
       actions={'front': '用于向客户解释资产端宏观环境，严格避免衍生收益承诺', 'lead': '留意险资跨境配置政策口径对投资型产品的间接影响'},
       roles={'front': 1, 'midback': 1, 'lead': 2, 'cross': 2}, verify='verified'),
]

path = 'data/live-items.json'
shutil.copy(path, path + '.bak-0922-2115')
d = json.load(open(path))
before = len(d['items'])
existing = {it.get('id') for it in d['items']}
new = [it for it in ITEMS if it['id'] not in existing]
dup = [it['id'] for it in ITEMS if it['id'] in existing]
d['items'] = new + d['items']
d['meta']['generatedAt'] = NOW_ISO
d['meta']['itemCount'] = len(d['items'])
d['meta']['asOf'] = NOW_ISO
note = '本库%d条。' % len(d['items'])
d['meta']['windowNote'] = {'sc': note, 'tc': tc(note)}
json.dump(d, open(path, 'w'), ensure_ascii=False, indent=1)
print('before=%d after=%d new=%d skipped_dups=%s' % (before, len(d['items']), len(new), dup))
for it in new:
    print(' +', it['publishedAt'], it['sourceKey'], it['id'], '| sum_len', len(it['summary']['sc']))
