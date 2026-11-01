#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每月家办与跨境政策扫描 2026-11-01：插入 3 条新条目 + 回写 last-check / collect-progress。

窗口：2026-10-01 → 2026-11-01（承接 2026-10-01 月度扫描，collect-progress lastMonth=2026-09）
覆盖主题：①跨境信托（明示信托实益拥有权透明度公众咨询 Q4 2026）②港府五年规划下的
家族财富管理路线图 ③与新加坡家办竞争（新加坡 carried interest 免税或延伸至 13O/13U）。
"""
import json, datetime
import zhconv

TZ = datetime.timezone(datetime.timedelta(hours=8))
now_iso = datetime.datetime.now(TZ).strftime("%Y-%m-%dT%H:%M:%S+08:00")

FIX = {'轉帳': '轉賬', '鏈接': '連結', '裏面': '裡面', '面向': '面向',
       '帳戶': '賬戶', '資産': '資產', '賦予': '賦予'}


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
    # ======================= ① 明示信托实益拥有权透明度公众咨询（Q4 2026） =======================
    item(id='legco-express-trust-beneficial-ownership-consultation-20261005', score=85, verifyStatus='verified',
         sourceTier='official', sourceKey='legco', contentKind='press',
         publishedAt='2026-10-05T00:00:00+08:00',
         title=T('财库局10月5日向立法会提交文件：2026年第四季就加强公司及明示信托实益拥有权透明度的立法建议展开公众咨询——拟在公司注册处记录个别公司实益拥有人、要求明示信托保存并提供实益拥有人资料、加强会计师作为信托或公司服务提供者的监管'),
         summary=T('财经事务及库务局向立法会财经事务委员会提交资料文件（2026年10月5日会议，就《香港第一个五年规划》及《2026年施政报告》作简报），落实施政报告承诺：将于2026年第四季就加强公司及明示信托实益拥有权透明度的立法建议展开公众咨询，落实打击洗钱及恐怖分子资金筹集的最新国际标准。文件第52至53段明确三项建议：①在公司注册处记录个别公司实益拥有人；②要求明示信托保存和提供实益拥有人资料；③加强会计师作为信托或公司服务提供者的监管。该咨询已列入《施政报告》指定项目指标第6项（2026年第四季展开）。'),
         why=T('这是明示信托披露义务从「施政报告一句话」落到「具体建议+时间表」的关键一步，直接关系跨境信托架构的合规设计：香港明示信托未来须保存并提供实益拥有人资料，意味着高净值客户跨境信托架构的透明度成本将显著上升，架构师须提前评估「披露义务升级」对保密性与合规成本的影响；会计师作为信托或公司服务提供者的监管强化，也会改变跨境财富架构的专业服务分工。对服务内地高净值客户的团队，这是继内地离岸信托个税新规（21号公告）后，跨境信托合规收紧的又一信号。'),
         actions={'front': T('客户问及跨境信托时，说明香港明示信托披露义务将向最新反洗钱国际标准靠拢，不提供规避实益拥有权申报的安排'),
                  'midback': T('把明示信托实益拥有权透明度公众咨询列入跨境信托合规跟踪清单，Q4 关注咨询文件出台及披露细则'),
                  'lead': T('跨境传承方案设计时预留「实益拥有人披露」的合规与成本空间，纳入高客服务议题'),
                  'cross': T('香港与内地两地信托披露规则从严评估，中介不提供规避申报或避税安排')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 3},
         source={'sc': '立法会财经事务委员会资料文件 CB(1)1126/2026(03)（财库局就《香港第一个五年规划》及《2026年施政报告》作简报）2026-10-05', 'lang': 'zh'},
         boards=['family', 'reg'], themes=['trust', 'compliance', 'aml', 'family-office'],
         tags=tg('明示信托', '实益拥有权', '反洗钱', '公众咨询', '跨境信托'),
         originalUrl='https://www.legco.gov.hk/yr2026/chinese/panels/fa/papers/fa20261005cb1-1126-3-c.pdf'),

    # ======================= ② 香港首個五年規劃的家族財富管理路線圖 =======================
    item(id='capital-hk-5yrplan-family-wealth-roadmap-20261004', score=60, verifyStatus='verified',
         sourceTier='media', sourceKey='capitalhk', contentKind='news',
         publishedAt='2026-10-04T00:00:00+08:00',
         title=T('《香港第一个五年规划（2026-2030）》如何重塑家族财富管理：人民币成为家族资产配置独立维度、企业出海对接家族财富管理、港星协同互补——香港昇世匯盈CEO冼健岷解读'),
         summary=T('《资本杂志》10月4日封面故事引香港昇世匯盈首席执行官冼健岷分析《五年规划》对财富管理业的影响：政策意义不在单一产品或资金规模，而在把优势转化为完整资产生态圈。随着离岸人民币股债及流动性工具扩充，人民币已具备成为家族整体资产配置中独立维度的条件，高净值客户需求将从「买人民币产品」转向「货币与资产负债匹配」的跨货币综合架构（人民币、港元、美元统筹）。企业出海与家族财富管理密不可分，内地企业走向国际初期衍生融资财资需求，随后延伸至企业主个人及家族层面的海外资产统筹、跨区风险控制与跨代传承，是重要增长引擎。政府资本（100亿元创科产业引导基金等）催化耐心资本，让家族办公室参与从早期投资到上市退出的完整链条。港星并非零和博弈，香港核心定位是管理跨境资本及财富。'),
         why=T('这条把《五年规划》从「创科/北都」的宏观叙事拉回财富管理实务，提供两个前瞻议题：一是「人民币作为家族资产配置独立维度」——客户资产配置讨论将超越单一产品，转向多币种的资产负债匹配；二是「企业出海×家族财富管理」——内地企业主跨境扩张衍生的家族资产统筹与跨代传承需求，是港险高净值业务的结构性增量来源。港星协同互补的判断，为家办选址提供了「非零和」的理性框架。'),
         actions={'front': T('高净值客户配置讨论可引入「多币种资产负债匹配」框架，不把人民币资产当作单一产品推销'),
                  'midback': T('把「企业出海衍生的家族财富管理需求」列为获客线索，纳入业务开发议题'),
                  'lead': T('人民币资产维度与跨代传承是高客议题，纳入季度财富管理趋势观察'),
                  'cross': T('跨境多币种架构按属地规则个案确认，不提供规避外汇或税务监管的安排')},
         rolesImpact={'front': 2, 'midback': 1, 'lead': 2, 'cross': 2},
         source={'sc': '《资本杂志》（Capital HK）封面故事「香港第一個五年規劃．對接國家發展戰略」2026-10-04', 'lang': 'zh'},
         boards=['family', 'market'], themes=['family-office', 'wealth-management', 'rmb', 'market'],
         tags=tg('五年规划', '家族办公室', '人民币资产', '企业出海', '财富管理'),
         originalUrl='https://www.capital-hk.com/interview/cover-story/Coverstory_Capital_102026'),

    # ======================= ③ 新加坡 carried interest 免税或延伸至单一家办结构（13O/13U） =======================
    item(id='sg-carried-interest-family-office-13o13u-202609', score=70, verifyStatus='pending',
         sourceTier='pro', sourceKey='altassetasia', contentKind='news',
         publishedAt='2026-09-30T00:00:00+08:00',
         title=T('新加坡 carried interest（附带权益）免税拟2027课税年度生效，或延伸至13O/13U单一家办投资团队——与香港6月税改正面竞争，两地争夺基金经理与家办的多线竞争升温'),
         summary=T('Alt Asset Asia 专题分析：新加坡金管局与财政部8月19日公布「资产管理中心」一揽子措施，拟对合资格基金管理服务的利润相关回报（即 carried interest，附带权益）免税，预计2027课税年度生效、细则待2027年预算案公布。关键点在于「合资格基金」涵盖《所得税法》第13D、13O、13OA、13U、13V条——13O与13U正是单一家办最常用的基金结构，意味着免税可能延伸至家办内部投资团队的表现挂钩薪酬，而非仅限第三方基金经理（MAS尚未确认家办结构的具体适用方式）。这是对香港6月《2026年税务（修订）（关于基金、家族投资控权工具及附带权益的优惠税制）条例草案》的直接回应，两地附带权益税制从「香港先行」转为「同频竞争」。'),
         why=T('这条修正了「新加坡只收紧或放宽13O/13U门槛」的单一视角：carried interest免税是新的竞争维度。对跨境财富团队而言，一是存量或拟设新加坡家办基金须留意2027课税年度起的税制变化；二是两地附带权益税制同步宽松，客户在港新之间的选址考量将从「税率高低」转向「连接内地」与「分散风险」的功能定位，与既有GFCI40、13O/13U口径形成完整对标链条。'),
         actions={'front': T('客户问及港新家办税制时，引用两地附带权益税制最新进展，不沿用「新加坡严管」过时口径'),
                  'midback': T('把新加坡carried interest免税与香港6月条例草案并列更新到区域政策对照表'),
                  'lead': T('附带权益税制是基金经理与家办选址的关键变量，纳入客户提案'),
                  'cross': T('存量新加坡家办基金按2027课税年度对照MAS新规评估，跨境架构个案确认')},
         rolesImpact={'front': 1, 'midback': 1, 'lead': 2, 'cross': 2},
         source={'sc': 'Alt Asset Asia 专题分析（据MAS 2026-08-19新闻稿「加强新加坡资产管理中心竞争力措施」）2026年9月', 'lang': 'zh'},
         boards=['family'], themes=['family-office', 'benchmark', 'offshore', 'taxation'],
         tags=tg('新加坡', '附带权益', 'carried interest', '13O', '13U', '家办竞争'),
         originalUrl='https://altassetasia.com/singapores-new-carried-interest-tax-break-raises-the-stakes-in-its-hong-kong-rivalry/'),
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
    cp['lastMonth'] = '2026-10'
    cp['done'] = cp.get('done', []) + added
    json.dump(cp, open(cp_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f"collect-progress.json lastMonth -> {cp['lastMonth']}, done={len(cp['done'])}")


if __name__ == '__main__':
    main()
