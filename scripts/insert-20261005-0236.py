# -*- coding: utf-8 -*-
import json, datetime

NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).replace(microsecond=0).isoformat()

item = {
    "id": "ia-flmi-exam-policy-validity-20261003",
    "clusterCount": 1,
    "score": 78,
    "verifyStatus": "verified",
    "sourceTier": "media",
    "sourceKey": "epochtimes",
    "title": {
        "sc": "保监局就FLMI考试作弊案最新表态：涉案中介人处理的保单效力与持有人权益不受影响，将按个案检视牌照资格",
        "tc": "保監局就FLMI考試作弊案最新表態：涉案中介人處理保單效力與持有人權益不受影響，將按個案檢視牌照資格",
    },
    "summary": {
        "sc": "《明報》10月3日向保监局及警方跟进查询（大纪元时报香港同日转载）：警方与保监局8月捣破「寿险管理师」（FLMI）资格考试作弊团伙，涉案考试中心位于观塘、由「大中华自媒体协会」营运约一年半，至少250人经该考场取得FLMI资格。保监局表示案件仍在调查、不作进一步评论，但会按个案情况检视有关中介人的牌照资格并采取相应监管行动，同时表明「有关保险中介人处理的保单，效力及保单持有人的权益将不受影响」。",
        "tc": "《明報》10月3日向保監局及警方跟進查詢（大紀元時報香港同日轉載）：警方與保監局8月搗破「壽險管理師」（FLMI）資格考試作弊團伙，涉案考試中心位於觀塘、由「大中華自媒體協會」營運約一年半，至少250人經該考場取得FLMI資格。保監局表示案件仍在調查、不作進一步評論，但會按個案情況檢視有關中介人的牌照資格並採取相應監管行動，同時表明「有關保險中介人處理的保單，效力及保單持有人的權益將不受影響」。",
    },
    "why": {
        "sc": "这条把「监管执法」与「客户权益」两件事分清楚了，是前线最需要的一句话：持牌资格被复核，不等于客户手上的保单失效。实务价值有三：一是团队内部与客户沟通时要区分「人员资格／执法」与「保单效力／索偿权益」两个层面，避免混为一谈引发不必要的恐慌；二是「资格学历」的取得路径已被监管全面检视，招聘与推荐新人时的资格核查、学历与考试记录留痕必须做实；三是提醒中介资格合规是长期的事——用不正当途径取得的资格，风险不会在入职时结束，而是可能在数年后的复核中被追诉。",
        "tc": "這條把「監管執法」與「客戶權益」兩件事分清楚了，是前線最需要的一句話：持牌資格被覆核，不等於客戶手上的保單失效。實務價值有三：一是團隊內部與客戶溝通時要區分「人員資格／執法」與「保單效力／索償權益」兩個層面，避免混為一談引發不必要的恐慌；二是「資格學歷」的取得路徑已被監管全面檢視，招聘與推薦新人時的資格核查、學歷與考試記錄留痕必須做實；三是提醒中介資格合規是長期的事——用不正當途徑取得的資格，風險不會在入職時結束，而是可能在數年後的覆核中被追訴。",
    },
    "actions": {
        "front": {
            "sc": "客户或团队问及此事时，只引述保监局公开表态：保单效力与保单持有人权益不受影响，不作额外解读",
            "tc": "客戶或團隊問及此事時，只引述保監局公開表態：保單效力與保單持有人權益不受影響，不作額外解讀",
        },
        "midback": {
            "sc": "复核从业人员资格与学历的取得记录，确保招聘与推荐环节留痕完整",
            "tc": "覆核從業人員資格與學歷的取得記錄，確保招聘與推薦環節留痕完整",
        },
        "lead": {
            "sc": "把「资格学历合规」列入团队长期合规议题，明确所引用的投考与取证路径要求",
            "tc": "把「資格學歷合規」列入團隊長期合規議題，明確所引用的投考與取證路徑要求",
        },
        "cross": {
            "sc": "涉在查案件只转述监管与警方公开信息，不对涉案人员或机构作定性评论",
            "tc": "涉在查案件只轉述監管與警方公開資訊，不對涉案人員或機構作定性評論",
        },
    },
    "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
    "boards": ["reg"],
    "themes": ["enforcement", "licensing", "conduct", "client-protection", "hk"],
    "tags": {
        "sc": ["保监局", "FLMI", "LOMA", "考试作弊", "保单效力", "牌照资格复核", "客户权益"],
        "tc": ["保監局", "FLMI", "LOMA", "考試作弊", "保單效力", "牌照資格覆核", "客戶權益"],
    },
    "source": {
        "sc": "大纪元时报（香港）转载《明报》2026-10-03 16:18 报道",
        "tc": "大紀元時報（香港）轉載《明報》2026-10-03 16:18 報道",
        "lang": "zh",
    },
    "contentKind": "news",
    "publishedAt": "2026-10-03T16:18:00+08:00",
    "originalUrl": "https://hk.epochtimes.com/news/2026-10-03/43787560",
    "ingestedAt": NOW,
    "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
    "featured": False,
    "evergreen": False,
}

path = 'data/live-items.json'
d = json.load(open(path))
ids = {it['id'] for it in d['items']}
if item['id'] in ids:
    print('SKIP duplicate id:', item['id'])
else:
    d['items'] = [item] + d['items']
    d['meta']['generatedAt'] = NOW
    d['meta']['itemCount'] = len(d['items'])
    n = len(d['items'])
    d['meta']['windowNote'] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}
    json.dump(d, open(path, 'w'), ensure_ascii=False, indent=1)
    print('added 1, total', n, 'generatedAt', NOW)
    print(' +', item['id'], item['publishedAt'], item['sourceKey'])
