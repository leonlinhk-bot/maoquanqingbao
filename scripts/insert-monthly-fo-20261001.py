#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每月家办与跨境政策扫描 2026-10-01：插入 4 条新条目 + 回写 last-check / collect-progress。

窗口：2026-09-01 → 2026-10-01（承接 2026-09-01 月度扫描，collect-progress lastMonth=2026-08）
覆盖主题：港府施政报告（家办/财富管理/明示信托透明度）、新港家办竞争（GFCI40/BCG）、
新加坡13O/13U放宽、离岸信托新规(CRS2.0)跨境合规。
"""
import json, datetime
import zhconv

TZ = datetime.timezone(datetime.timedelta(hours=8))
now_iso = datetime.datetime.now(TZ).strftime("%Y-%m-%dT%H:%M:%S+08:00")

FIX = {'轉帳': '轉賬', '鏈接': '連結', '裏面': '裡面', '面向': '面向'}


def tc(s):
    out = zhconv.convert(s, 'zh-tw')
    for a, b in FIX.items():
        out = out.replace(a, b)
    return out


def T(sc, tcv=None):
    return {'sc': sc, 'tc': tcv if tcv else tc(sc)}


def tg(*words):
    return {'sc': list(words), 'tc': [tc(w) for w in words]}


def item(**kw):
    d = {
        'clusterCount': 1, 'score': 70, 'verifyStatus': 'verified',
        'sourceTier': 'pro', 'sourceKey': '', 'contentKind': 'news',
        'actions': {'front': {}, 'midback': {}, 'lead': {}, 'cross': {}},
        'rolesImpact': {'front': 0, 'midback': 0, 'lead': 0, 'cross': 0},
        'boards': [], 'themes': [], 'tags': {'sc': [], 'tc': []},
        'contentRole': {'sc': '本站导读', 'tc': '本站導讀'},
        'featured': False, 'evergreen': False, 'ingestedAt': now_iso,
    }
    d.update(kw)
    return d


NEW = [
    # ======================= 行政长官2026年施政报告（家办/财富管理/明示信托） =======================
    item(id='fstb-policy-address-2026-wealth-fo-trust-20260916', score=86, verifyStatus='verified',
         sourceTier='official', sourceKey='fstb', contentKind='press',
         publishedAt='2026-09-16T13:02:00+08:00',
         title=T('《行政长官2026年施政报告》9月16日发表：香港跃居全球最大跨境财富管理中心，将在优化基金、单一家族办公室及附带权益优惠税制的条例草案获立法会通过后加强推广；2026年内提交REIT私有化或重组条例草案；财库局年内就加强公司及明示信托实益拥有权透明度的立法建议咨询公众，落实打击洗钱及恐怖分子资金筹集最新国际标准'),
         summary=T('行政长官2026年施政报告9月16日发表（全文13:02刊出）。第三章「国际资产及财富管理中心」一节指香港今年跃居全球最大跨境财富管理中心，将持续构建更具吸引力的资产及财富管理生态圈：在《2026年税务（修订）（关于基金、单一家族办公室及附带权益的优惠税制）条例草案》获立法会通过后加强推广，吸引基金和家族办公室落户香港及更多环球资金在港管理；于2026年内提交便利房託基金（REIT）私有化或重组的条例草案，2027年上半年提交为准备上市的房託基金宽免转让非住宅物业印花税的条例草案，证监会精简程序吸引优质海外房託基金来港双重上市并争取尽快把房託基金纳入互联互通；同时推动内地保险资金透过互联互通投资香港ETF。第52段明确，财库局将于2026年内就加强公司及明示信托实益拥有权透明度的立法建议咨询公众。另设「国际风险管理中心」一节，保监局今年已为三间专属自保保险公司批出授权、总数增至九间，继续推广保险相连证券（ILS）并研究修改法例引入「受保护单元公司」（PCC）。'),
         why=T('施政报告是家办与跨境财富架构的年度政策基准，三个点直接关系业务：一是基金/家办/附带权益税制草案通过后进入推广期，客户架构设计可按「草案通过后」情景测算（措施拟追溯至2025/26课税年度生效）；二是房託基金私有化、印花税宽免与纳入互联互通，为以REIT持有资产的家办提供退出、重组与流动性空间；三是明示信托实益拥有权透明度立法咨询，意味着跨境信托架构的披露义务将向最新反洗钱国际标准靠拢，高净值客户的信托设计须提前评估透明度成本。ILS、PCC与专属自保的推进则为跨境财富的风险管理端提供新工具。'),
         actions={'front': T('客户问及香港家办政策时，只引用施政报告公开表述，不代述税制草案尚未通过的细节或作税务承诺'),
                  'midback': T('把明示信托实益拥有权透明度立法咨询列入跨境信托架构的合规跟踪清单，预留披露义务升级的预案'),
                  'lead': T('REIT私有化/重组与印花税宽免是家办客户资产退出与重组的政策窗口，纳入高客服务议题'),
                  'cross': T('内地高净值客户的信托与家办架构须按两地税务与披露规则从严评估，中介不提供规避建议')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 3},
         source={'sc': '财经事务及库务局（行政长官2026年施政报告第三章，政府新闻网全文）2026-09-16 13:02', 'lang': 'zh'},
         boards=['family', 'reg'], themes=['family-office', 'taxation', 'trust', 'fo-ecosystem'],
         tags=tg('施政报告', '家族办公室', '附带权益', '房託基金', '明示信托', '财富管理'),
         originalUrl='https://www.policyaddress.gov.hk/2026/tc/chapter3.html'),

    # ======================= 新港家办竞争：GFCI40 + BCG全球财富报告 =======================
    item(id='hk-sg-gfci40-wealth-competition-20260916', score=70, verifyStatus='verified',
         sourceTier='pro', sourceKey='163', contentKind='news',
         publishedAt='2026-09-16T00:00:00+08:00',
         title=T('第40期全球金融中心指数：香港756分 vs 新加坡755分仅差1分；香港跨境财富管理2.95万亿美元首超瑞士成全球第一、上半年IPO集资额约为新加坡31倍；新加坡以逾2000间单一家办与基金业7.5%年均增速反击，人才战上香港扩大附带权益免税、新加坡金管局推出免税＋对冲基金资本＋高管签证三招应对'),
         summary=T('网易号「中金洞察」9月16日分析第40期全球金融中心指数（GFCI 40）发布结果：纽约761、伦敦757、香港756、新加坡755，前四大金融中心最大分差仅6分，香港与新加坡仅差1分，香港守住亚太区首位。硬数据方面，波士顿咨询《2026年全球财富报告》显示香港2025年财富管理规模同比增10.7%至2.95万亿美元，首超瑞士（2.94万亿）成为全球最大跨境财富管理中心；新加坡增10.3%至2.1万亿美元居全球第三。IPO差距悬殊：2026年上半年香港85家公司上市、集资约2104亿港元，新加坡仅5宗、约8.68亿美元，香港约为新加坡31倍。香港6月人民币清算量升至53.2万亿元创纪录。新加坡则以超过2000间单一家族办公室、基金业五年7.5%年均增速、约7万亿新元资管规模反制。人才战方面，香港6月扩大附带权益优惠税制适用范围，新加坡金管局随即推出三招：拟免除投资专业人士基金管理服务利润相关税款、设立对冲基金管理人资本支持计划、放宽高级基金管理人员签证要求。分析指两地是「连接」与「分散」两种模式的分野，亚太金融中心平均评分升1.48%为全球最大增幅。'),
         why=T('这条把「新港竞争」从印象落到可核对的数字：1分的GFCI分差、2.95万亿对2.1万亿的跨境财富体量、31倍的IPO集资差距，以及两地同步推出的税制与人才优惠。对港险高净值客群而言，家办与身份规划的选址决策受两地政策节奏直接影响——香港主打「连接内地」的制度嵌套，新加坡主打「分散风险」的信任溢价。客户在两地之间的架构与身份安排，需按「谁更适合谁」而非「谁更好」来规划，这条提供了最新的对标数据与政策清单。'),
         actions={'front': T('两地政策对比可作高净值客户选址话术素材，只引用公开数据、不作市场或产品推荐'),
                  'midback': {},
                  'lead': T('家办架构选址的长期判断依据，纳入季度区域竞争观察'),
                  'cross': T('跨境财富与身份规划客户重点跟进，两地架构差异按属地规则个案确认')},
         rolesImpact={'front': 1, 'midback': 0, 'lead': 2, 'cross': 2},
         source={'sc': '网易号「中金洞察」（据GFCI40／BCG2026全球财富报告／上证报／21世纪经济报道等公开数据）2026-09-16', 'lang': 'zh'},
         boards=['family', 'market'], themes=['family-office', 'benchmark', 'offshore', 'market'],
         tags=tg('全球金融中心指数', '新加坡', '家办竞争', '跨境财富', '附带权益', '人才战'),
         originalUrl='https://www.163.com/dy/article/L7HRORLM0518X2UP.html'),

    # ======================= 新加坡13O/13U单一家办税收优惠放宽 =======================
    item(id='sg-mas-13o-13u-fo-tax-relax-20260801', score=72, verifyStatus='verified',
         sourceTier='pro', sourceKey='hankunlaw', contentKind='news',
         publishedAt='2026-08-04T00:00:00+08:00',
         title=T('新加坡MAS发布基金税收激励通函：13O/13U单一家办条件全面放宽——IP招聘给宽限期（13O申请时仅需1名、13U仅需2名）、本地开支阶梯门槛大幅放宽（2.5亿新元以下降至20万新元）、资本部署精简为三选项、取消实物贵金属5%上限，2026年8月1日起生效'),
         summary=T('汉坤律师事务所8月4日解读：新加坡金管局（MAS）金融中心发展署2026年7月31日发布基金税收激励计划通函（FDD Cir 05-2026），对13O、13OA及13U计划作多项修订，其中针对单一家族办公室（SFO）的申请条件放宽与取消实物贵金属5%上限已于2026年8月1日生效。五大变化：①专业投资人士（IP）招聘给宽限期——13O申请时仅需雇1名IP、13U仅需2名（均可为家庭成员），在奖励首个课税年度基期结束前分别补齐至2名、3名（含至少1名非家庭成员）即可；②最低资产规模条件简化——只需在申请时及每个基期结束申报达标（13O为2000万新元、13U为5000万新元），无需全年持续跟踪；③本地开支（LBE）阶梯门槛大幅放宽——资产低于2.5亿新元最低本地开支降至20万新元、2.5亿至20亿新元为50万、20亿新元以上为100万；④资本部署要求（CDR）精简为三大选项（MAS批准交易所上市投资、MAS持牌机构分销产品、有实质经营的新加坡非上市公司）；⑤取消实物贵金属5%上限，其合格收入全额免税。13D/13O/13OA/13U税务优惠延至2029年12月31日到期前接受审核。'),
         why=T('这是对「新加坡收紧家办」印象的重要修正：2026年8月起新加坡实为「简合规、放宽落地」，与香港6月扩大附带权益免税形成同频竞争。对高净值客户而言，两地都在降低家办设立与运营的摩擦成本，真正的差异化不在门槛高低，而在「连接内地」与「分散风险」的功能定位。跨境财富团队据此可为客户提供更准确的选址对标，避免沿用「新加坡严管」的过时口径；存量新加坡家办基金亦须按8月1日后基期对照MAS新条件评估。'),
         actions={'front': T('客户问及新港家办选择时，引用13O/13U最新条件，不沿用「新加坡严管」的过时口径'),
                  'midback': T('把MAS 13O/13U新政与香港基金/家办税制草案并列更新到区域政策对照表'),
                  'lead': T('新加坡放宽IP招聘与本地开支，是家办选址对标的关键变量，纳入客户提案'),
                  'cross': T('存量新加坡家办基金须按8月1日后基期对照MAS新条件评估，跨境架构个案确认')},
         rolesImpact={'front': 1, 'midback': 1, 'lead': 2, 'cross': 2},
         source={'sc': '汉坤律师事务所（据MAS FDD Cir 05-2026，2026年8月4日解读）', 'lang': 'zh'},
         boards=['family'], themes=['family-office', 'benchmark', 'offshore', 'taxation'],
         tags=tg('新加坡', '13O', '13U', 'MAS', '单一家办', '税务优惠'),
         originalUrl='https://hankunlaw.com/portal/article/index/cid/8/id/17048.html'),

    # ======================= 离岸信托新规(CRS2.0)跨境财富合规 =======================
    item(id='offshore-trust-crs2-crossborder-compliance-20260902', score=64, verifyStatus='pending',
         sourceTier='pro', sourceKey='allbrightlaw', contentKind='news',
         publishedAt='2026-09-04T00:00:00+08:00',
         title=T('「离岸信托新规下的跨境财富合规与信托价值重塑」研讨会9月2日在沪举行：聚焦海外信托合规与税务影响、A股股权置入信托的监管障碍、香港家办与信托制度优势及CRS穿透与追税现状'),
         summary=T('锦天城律师事务所9月4日发布活动纪要：9月2日下午，其婚姻家事与私人财富管理、银行与金融、税法专业委员会及香港办公室联合举办「离岸信托新规下的跨境财富合规与信托价值重塑」专题研讨会。开场致辞聚焦海外信托合规性及税务影响，探讨新规背景下海外信托的存续价值与架构调整，以及A股上市公司股权置入信托的现实需求与监管障碍；《香港家办与信托：制度优势与CRS框架下的落地实务》主题分享系统阐释家办与信托的基础架构与法律逻辑，梳理香港信托制度的法律基石与优势，并聚焦CRS穿透与追税现状。研讨会在强监管与税务透明化背景下，就高净值客户境外资产架构的合规路径与存续价值展开讨论。'),
         why=T('这条是跨境信托主题的行业信号：CRS2.0/离岸信托新规下，多层嵌套架构面临穿透式审查、受托人/委托人/受益人身份信息须逐一申报，跨境资产配置的灰色空间被压缩。对服务内地高净值客户的团队而言，「境外资产架构合规化」正从可选项变为必选项，香港家办＋信托的制度组合价值反而凸显——香港信托在CRS框架下的落地实务，是跨境传承与风险隔离方案的核心卖点，值得作为高客议题持续跟踪。'),
         actions={'front': T('客户问及境外信托时，说明新规下披露义务升级，不提供规避申报或避税建议'),
                  'midback': T('把CRS2.0/离岸信托新规列入跨境财富合规清单，信托架构涉及的身份申报与受益所有人披露逐笔留痕'),
                  'lead': T('香港家办＋信托的制度组合是跨境传承方案的核心，纳入高客服务议题'),
                  'cross': T('跨境信托的受托人/委托人/受益人申报属客户义务，中介不得提供规避安排')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 3},
         source={'sc': '锦天城律师事务所「家富智享」研习系列活动纪要 2026-09-04', 'lang': 'zh'},
         boards=['family', 'reg'], themes=['trust', 'offshore', 'family-office', 'compliance'],
         tags=tg('离岸信托', 'CRS2.0', '跨境财富', '香港家办', '受益所有人', '税务透明'),
         originalUrl='https://www.allbrightlaw.com/CN/10482/66eed16b46d9b1c9.aspx'),
]


def main():
    path = 'data/live-items.json'
    data = json.load(open(path, encoding='utf-8'))
    existing_ids = {it.get('id') for it in data['items']}
    urls = {it.get('originalUrl') for it in data['items']}
    added = []
    for it in NEW:
        if it['id'] in existing_ids:
            print('SKIP (dup id):', it['id'])
            continue
        if it['originalUrl'] in urls:
            print('SKIP (dup url):', it['id'])
            continue
        data['items'].insert(0, it)
        added.append(it['id'])
    n = len(data['items'])
    data['meta']['itemCount'] = n
    data['meta']['generatedAt'] = now_iso
    data['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
    json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'INSERTED {len(added)} items; total now {n}')
    for a in added:
        print(' +', a)

    # last-check.json：仅更新 family_office 信源
    lc_path = 'data/last-check.json'
    lc = json.load(open(lc_path, encoding='utf-8'))
    lc['sources']['family_office']['last'] = now_iso
    lc['lastCheck'] = now_iso
    json.dump(lc, open(lc_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'last-check.json family_office.last -> {now_iso}')

    # collect-progress.json：月度扫描进度
    cp_path = 'data/collect-progress.json'
    try:
        cp = json.load(open(cp_path, encoding='utf-8'))
    except Exception:
        cp = {}
    cp['lastMonth'] = '2026-09'
    cp['done'] = cp.get('done', []) + added
    json.dump(cp, open(cp_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f"collect-progress.json lastMonth -> {cp['lastMonth']}, done={len(cp['done'])}")


if __name__ == '__main__':
    main()
