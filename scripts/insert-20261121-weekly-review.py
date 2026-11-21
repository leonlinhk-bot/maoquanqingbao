#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""周末复核 2026-11-21：补「机构研究」缺口（本周 sourceTier=research 为 0）
真实原始日期，date-only 仅因信源只给日期。"""
import json
import shutil

BASE = '/Users/leonliang/maoquanqingbao'
LIVE = BASE + '/data/live-items.json'
NOW = '2026-11-21T18:00:00+08:00'

ITEMS = [
    {
        "id": "swissre-sigma-2026-05-searching-for-resilience",
        "clusterCount": 1,
        "score": 80,
        "verifyStatus": "verified",
        "sourceTier": "research",
        "sourceKey": "swissre",
        "title": {
            "sc": "瑞再 sigma 5/2026《Searching for resilience》：2027年全球经济增长2.8%但根基收窄，非寿险ROE料由12.7%降至10.3%",
            "tc": "瑞再 sigma 5/2026《Searching for resilience》：2027年全球經濟增長2.8%但根基收窄，非壽險ROE料由12.7%降至10.3%",
        },
        "summary": {
            "sc": "瑞再研究院发布 sigma 5/2026《Searching for resilience》，预测2027年全球实际GDP增长2.8%、2028年2.6%，增长主要靠AI基建投资、金融市场与高净值家庭消费等少数引擎支撑；非寿险保司ROE料由2026年的12.7%回落至10.3%，中期趋向约7.3%的资本成本。[EN原文]",
            "tc": "瑞再研究院發布 sigma 5/2026《Searching for resilience》，預測2027年全球實際GDP增長2.8%、2028年2.6%，增長主要靠AI基建投資、金融市場與高淨值家庭消費等少數引擎支撐；非壽險保司ROE料由2026年的12.7%回落至10.3%，中期趨向約7.3%的資本成本。[EN原文]",
        },
        "why": {
            "sc": "瑞再把「保险业资本与流动性充足」和「增长根基收窄」并置：承保端ROE从高点回落、定价动能让位于风险敞口增长，是理解未来两三年再保与直保定价周期的机构级基准；对讲分红险与投连险底层配置的IFA，这是一份可直接引用的全球承保/投资端背景。",
            "tc": "瑞再把「保險業資本與流動性充足」和「增長根基收窄」並置：承保端ROE從高點回落、定價動能讓位於風險敞口增長，是理解未來兩三年再保與直保定價週期的機構級基準；對講分紅險與投連險底層配置的IFA，這是一份可直接引用的全球承保/投資端背景。",
        },
        "actions": {
            "front": {"sc": "客户问「保险公司靠什么赚钱」，可用瑞再ROE回落趋势解释承保利润率走向", "tc": "客戶問「保險公司靠什麼賺錢」，可用瑞再ROE回落趨勢解釋承保利潤率走向"},
            "midback": {"sc": "归档瑞再sigma观点，作为承保/再保定价周期背景", "tc": "歸檔瑞再sigma觀點，作為承保/再保定價週期背景"},
            "lead": {"sc": "承保ROE回落=定价与资本纪律的行业主线", "tc": "承保ROE回落=定價與資本紀律的行業主線"},
            "cross": {"sc": "全球再保/承保周期=港险产品定价与分红能力的宏观注脚", "tc": "全球再保/承保週期=港險產品定價與分紅能力的宏觀註腳"},
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 3, "cross": 3},
        "source": {
            "sc": "Swiss Re Institute sigma 5/2026 · 2026年11月17日",
            "tc": "Swiss Re Institute sigma 5/2026 · 2026年11月17日",
            "name": "Swiss Re Institute sigma 5/2026",
            "date": "2026-11-17",
            "lang": "en",
            "note": "[EN原文]",
        },
        "boards": ["market", "insurer"],
        "themes": ["reinsurance", "insurer-strategy"],
        "tags": {
            "sc": ["瑞再", "sigma", "宏观经济", "非寿险ROE", "承保周期"],
            "tc": ["瑞再", "sigma", "宏觀經濟", "非壽險ROE", "承保週期"],
        },
        "contentKind": "research",
        "publishedAt": "2026-11-17",
        "originalUrl": "https://www.swissre.com/institute/research/sigma-research/sigma-2026-05-global-economic-insurance-outlook-searching-for-resilience.html",
    },
    {
        "id": "pimco-charting-year-ahead-2027",
        "clusterCount": 1,
        "score": 76,
        "verifyStatus": "verified",
        "sourceTier": "research",
        "sourceKey": "pimco",
        "title": {
            "sc": "PIMCO《Charting the Year Ahead》：AI集中度重塑市场，2027年须主动分散组合的「隐性集中」",
            "tc": "PIMCO《Charting the Year Ahead》：AI集中度重塑市場，2027年須主動分散組合的「隱性集中」",
        },
        "summary": {
            "sc": "PIMCO发布2027年度前瞻《Charting the Year Ahead》，指出多年科技股上涨使多数组合过度偏股，而AI基建在股票、信用、基建与地产间形成不易察觉的关联，看似均衡的组合实则风险高度集中；建议以总组合视角识别隐性集中，借相对价值、高质量信用与商品等拓宽收益来源。[EN原文]",
            "tc": "PIMCO發布2027年度前瞻《Charting the Year Ahead》，指出多年科技股上漲使多數組合過度偏股，而AI基建在股票、信用、基建與地產間形成不易察覺的關聯，看似均衡的組合實則風險高度集中；建議以總組合視角識別隱性集中，借相對價值、高質量信用與商品等拓寬收益來源。[EN原文]",
        },
        "why": {
            "sc": "PIMCO对「AI集中度」的警示，直指高净值客户资产配置的共性风险：指数里重仓科技，又在债券、私募里再次暴露于同一主题。做家办与传承配置的IFA可用这份机构级前瞻，帮客户识别「看起来分散、实则同源」的组合，并自然引出分散与再平衡的配置话题。",
            "tc": "PIMCO對「AI集中度」的警示，直指高淨值客戶資產配置的共性風險：指數裡重倉科技，又在債券、私募裡再次暴露於同一主題。做家辦與傳承配置的IFA可用這份機構級前瞻，幫客戶識別「看起來分散、實則同源」的組合，並自然引出分散與再平衡的配置話題。",
        },
        "actions": {
            "front": {"sc": "客户组合若科技仓位重，可借「隐性集中」话题做一次配置体检", "tc": "客戶組合若科技倉位重，可借「隱性集中」話題做一次配置體檢"},
            "midback": {"sc": "归档PIMCO年度前瞻，作为高客配置沟通素材", "tc": "歸檔PIMCO年度前瞻，作為高客配置溝通素材"},
            "lead": {"sc": "「分散不等于均衡」是2027年配置沟通的切入点", "tc": "「分散不等於均衡」是2027年配置溝通的切入點"},
            "cross": {"sc": "传承与家办配置里的AI相关敞口，可对照PIMCO的集中度框架复核", "tc": "傳承與家辦配置裡的AI相關敞口，可對照PIMCO的集中度框架覆核"},
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 2, "cross": 3},
        "source": {
            "sc": "PIMCO · 2026年11月",
            "tc": "PIMCO · 2026年11月",
            "name": "PIMCO Charting the Year Ahead",
            "date": "2026-11",
            "lang": "en",
            "note": "[EN原文]",
        },
        "boards": ["market", "family"],
        "themes": ["wealth", "ai"],
        "tags": {
            "sc": ["PIMCO", "年度前瞻", "AI集中", "资产配置", "分散投资"],
            "tc": ["PIMCO", "年度前瞻", "AI集中", "資產配置", "分散投資"],
        },
        "contentKind": "research",
        "publishedAt": "2026-11-17",
        "originalUrl": "https://www.pimco.com/gbl/en/insights/charting-the-year-ahead-investment-ideas-for-2027",
    },
    {
        "id": "blackrock-bii-weekly-ai-buildout-20261116",
        "clusterCount": 1,
        "score": 72,
        "verifyStatus": "verified",
        "sourceTier": "research",
        "sourceKey": "blackrock",
        "title": {
            "sc": "贝莱德投资研究所周评《AI: looking beyond the buildout》：短期战术中性、长期超配美股，利率走高下重新看好债券",
            "tc": "貝萊德投資研究所週評《AI: looking beyond the buildout》：短期戰術中性、長期超配美股，利率走高下重新看好債券",
        },
        "summary": {
            "sc": "贝莱德投资研究所（BII）11月16日周评指，美股估值是否高企取决于量度口径，AI盈利能否兑现仍是未解问题；BII长期战略超配美股但短期战术转中性，并因利率走高自2020年来首次对利率风险转正面、倾向通胀挂钩债券，同时看好亚洲与拉美的「AI稀缺」表达。[EN原文]",
            "tc": "貝萊德投資研究所（BII）11月16日週評指，美股估值是否高企取決於量度口徑，AI盈利能否兌現仍是未解問題；BII長期戰略超配美股但短期戰術轉中性，並因利率走高自2020年來首次對利率風險轉正面、傾向通脹掛鉤債券，同時看好亞洲與拉美的「AI稀缺」表達。[EN原文]",
        },
        "why": {
            "sc": "贝莱德BII把「长期看好AI」与「短期战术谨慎」拆开，是理解当前美股与利率环境的机构级框架；对讲投连险、投资相连产品底层权益配置的IFA，这份周评给出「战略与战术分层」的现成口径，也可借「重新看好债券」引出固收配置的再平衡话题。",
            "tc": "貝萊德BII把「長期看好AI」與「短期戰術謹慎」拆開，是理解當前美股與利率環境的機構級框架；對講投連險、投資相連產品底層權益配置的IFA，這份週評給出「戰略與戰術分層」的現成口徑，也可借「重新看好債券」引出固收配置的再平衡話題。",
        },
        "actions": {
            "front": {"sc": "客户问美股还能不能买，用「战略超配+战术中性」的框架回应", "tc": "客戶問美股還能不能買，用「戰略超配+戰術中性」的框架回應"},
            "midback": {"sc": "归档BII周评，作为权益/固收配置沟通素材", "tc": "歸檔BII週評，作為權益/固收配置溝通素材"},
            "lead": {"sc": "利率走高下的股债配置再平衡是团队统一话术", "tc": "利率走高下的股債配置再平衡是團隊統一話術"},
            "cross": {"sc": "投连险/投资相连产品的权益敞口，可对照BII战略战术框架复核", "tc": "投連險/投資相連產品的權益敞口，可對照BII戰略戰術框架覆核"},
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 2, "cross": 2},
        "source": {
            "sc": "BlackRock Investment Institute · 2026年11月16日",
            "tc": "BlackRock Investment Institute · 2026年11月16日",
            "name": "BlackRock Investment Institute Weekly Commentary",
            "date": "2026-11-16",
            "lang": "en",
            "note": "[EN原文]",
        },
        "boards": ["market"],
        "themes": ["wealth", "ai"],
        "tags": {
            "sc": ["贝莱德", "BII", "周评", "AI", "资产配置"],
            "tc": ["貝萊德", "BII", "週評", "AI", "資產配置"],
        },
        "contentKind": "research",
        "publishedAt": "2026-11-16",
        "originalUrl": "https://www.blackrock.com/us/individual/literature/market-commentary/weekly-investment-commentary-en-us-20261116-ai-looking-beyond-the-buildout.pdf",
    },
]


def main():
    d = json.load(open(LIVE, encoding='utf-8'))
    old = d['items']
    existing_ids = {i['id'] for i in old}
    existing_urls = {(i.get('originalUrl') or '').rstrip('/') for i in old}

    new = []
    for it in ITEMS:
        it['ingestedAt'] = NOW
        it['contentRole'] = {'sc': '本站导读', 'tc': '本站導讀'}
        it['featured'] = False
        it['evergreen'] = False
        it['summaryShort'] = {'sc': it['summary']['sc'][:80], 'tc': it['summary']['tc'][:80]}
        if it['id'] in existing_ids:
            print('SKIP dup id:', it['id'])
            continue
        if it['originalUrl'].rstrip('/') in existing_urls:
            print('SKIP dup url:', it['id'])
            continue
        assert len(it['boards']) >= 1, it['id']
        assert len(it['themes']) >= 2, it['id']
        assert it['originalUrl'].startswith('http'), it['id']
        slen = len(it['summary']['sc'])
        assert 50 <= slen <= 170, (it['id'], slen)
        existing_ids.add(it['id'])
        existing_urls.add(it['originalUrl'].rstrip('/'))
        new.append(it)

    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    print('inserting', len(new), 'items')
    d['items'] = new + old
    d.setdefault('meta', {})
    d['meta']['generatedAt'] = NOW
    d['meta']['itemCount'] = len(d['items'])
    d['meta']['windowNote'] = {'sc': f'本库{len(d["items"])}条。', 'tc': f'本庫{len(d["items"])}條。'}

    shutil.copy(LIVE, LIVE + '.bak-1121-1800')
    json.dump(d, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('total now:', len(d['items']))


if __name__ == '__main__':
    main()
