from math import exp

TEAM_IDS = {
    "ATL": 1610612737, "BOS": 1610612738, "BKN": 1610612751, "CHA": 1610612766,
    "CHI": 1610612741, "CLE": 1610612739, "DAL": 1610612742, "DEN": 1610612743,
    "DET": 1610612765, "GSW": 1610612744, "HOU": 1610612745, "IND": 1610612754,
    "LAC": 1610612746, "LAL": 1610612747, "MEM": 1610612763, "MIA": 1610612748,
    "MIL": 1610612749, "MIN": 1610612750, "NOP": 1610612740, "NYK": 1610612752,
    "OKC": 1610612760, "ORL": 1610612753, "PHI": 1610612755, "PHX": 1610612756,
    "POR": 1610612757, "SAC": 1610612758, "SAS": 1610612759, "TOR": 1610612761,
    "UTA": 1610612762, "WAS": 1610612764,
}
TEAM_NAMES = {
    "ATL":"Atlanta Hawks","BOS":"Boston Celtics","BKN":"Brooklyn Nets","CHA":"Charlotte Hornets","CHI":"Chicago Bulls","CLE":"Cleveland Cavaliers","DAL":"Dallas Mavericks","DEN":"Denver Nuggets","DET":"Detroit Pistons","GSW":"Golden State Warriors","HOU":"Houston Rockets","IND":"Indiana Pacers","LAC":"LA Clippers","LAL":"Los Angeles Lakers","MEM":"Memphis Grizzlies","MIA":"Miami Heat","MIL":"Milwaukee Bucks","MIN":"Minnesota Timberwolves","NOP":"New Orleans Pelicans","NYK":"New York Knicks","OKC":"Oklahoma City Thunder","ORL":"Orlando Magic","PHI":"Philadelphia 76ers","PHX":"Phoenix Suns","POR":"Portland Trail Blazers","SAC":"Sacramento Kings","SAS":"San Antonio Spurs","TOR":"Toronto Raptors","UTA":"Utah Jazz","WAS":"Washington Wizards"
}
TEAM_COLORS = {
    "ATL":["#E03A3E","#C1D32F"],"BOS":["#007A33","#BA9653"],"BKN":["#111111","#777777"],"CHA":["#1D1160","#00788C"],"CHI":["#CE1141","#000000"],"CLE":["#860038","#FDBB30"],"DAL":["#00538C","#B8C4CA"],"DEN":["#0E2240","#FEC524"],"DET":["#C8102E","#1D42BA"],"GSW":["#1D428A","#FFC72C"],"HOU":["#CE1141","#000000"],"IND":["#002D62","#FDBB30"],"LAC":["#C8102E","#1D428A"],"LAL":["#552583","#FDB927"],"MEM":["#5D76A9","#12173F"],"MIA":["#98002E","#F9A01B"],"MIL":["#00471B","#EEE1C6"],"MIN":["#0C2340","#78BE20"],"NOP":["#0C2340","#C8102E"],"NYK":["#006BB6","#F58426"],"OKC":["#007AC1","#EF3B24"],"ORL":["#0077C0","#C4CED4"],"PHI":["#006BB6","#ED174C"],"PHX":["#1D1160","#E56020"],"POR":["#E03A3E","#000000"],"SAC":["#5A2D81","#63727A"],"SAS":["#C4CED4","#000000"],"TOR":["#CE1141","#000000"],"UTA":["#002B5C","#F9A01B"],"WAS":["#002B5C","#E31837"]
}

def headshot(pid):
    return f"https://cdn.nba.com/headshots/nba/latest/1040x760/{pid}.png"

def logo(team):
    return f"https://cdn.nba.com/logos/nba/{TEAM_IDS[team]}/primary/L/logo.svg"

BASE_PLAYERS = [
    # id, name, team, age, height, weight, pos, jersey, ppg, apg, rpg, usg, ts, mom, risk, defense, team_bonus, narrative, rookie, sixth
    (1628983,"Shai Gilgeous-Alexander","OKC",27,"6'6",195,"G",2,32.7,6.4,5.1,32.9,63.6,5.8,7.2,7.5,12.0,10.0,False,False),
    (203999,"Nikola Jokić","DEN",30,"6'11",284,"C",15,29.6,10.2,12.7,31.4,66.3,3.9,8.0,6.9,9.5,9.2,False,False),
    (1641705,"Victor Wembanyama","SAS",22,"7'4",235,"C",1,24.8,3.9,11.0,31.0,60.7,6.2,10.4,10.0,3.5,9.0,False,False),
    (1629029,"Luka Dončić","LAL",26,"6'7",230,"G",77,28.2,8.1,8.2,34.1,61.5,2.7,9.6,5.2,10.5,8.2,False,False),
    (203507,"Giannis Antetokounmpo","MIL",31,"6'11",243,"F",34,30.4,6.5,11.9,33.8,62.4,2.8,8.7,8.6,8.4,8.4,False,False),
    (203954,"Joel Embiid","PHI",31,"7'0",280,"C",21,29.8,4.7,10.5,35.5,61.0,1.1,12.5,8.4,6.4,8.8,False,False),
    (1630178,"Tyrese Maxey","PHI",25,"6'2",200,"G",0,25.9,6.1,3.5,29.0,58.1,4.4,7.1,4.8,6.4,6.5,False,False),
    (1628369,"Jayson Tatum","BOS",27,"6'8",210,"F",0,27.1,5.4,8.2,30.2,60.2,2.1,7.3,7.4,9.2,8.0,False,False),
    (1629630,"Ja Morant","MEM",26,"6'2",174,"G",12,25.0,7.4,4.3,31.6,56.0,3.5,11.2,4.5,5.8,6.2,False,False),
    (1630162,"Anthony Edwards","MIN",24,"6'4",225,"G",5,27.9,5.0,5.7,31.8,58.2,3.8,8.2,7.1,8.1,7.5,False,False),
    (1627759,"Jaylen Brown","BOS",29,"6'6",223,"G/F",7,25.4,3.8,5.8,29.4,57.1,3.1,7.5,7.0,9.2,6.8,False,False),
    (1631094,"Paolo Banchero","ORL",23,"6'10",250,"F",5,24.1,5.2,7.4,30.7,55.3,3.6,8.4,6.8,6.2,7.2,False,False),
    (1628368,"De'Aaron Fox","SAS",28,"6'3",185,"G",4,24.5,6.3,4.5,29.7,56.4,2.9,8.8,5.5,3.5,5.8,False,False),
    (1628378,"Donovan Mitchell","CLE",29,"6'3",215,"G",45,26.2,5.1,4.7,31.0,59.1,2.7,7.6,6.8,9.0,7.1,False,False),
    (201939,"Stephen Curry","GSW",37,"6'2",185,"G",30,25.0,6.0,4.2,30.5,62.8,1.5,9.4,4.3,7.4,8.0,False,False),
    (2544,"LeBron James","LAL",41,"6'9",250,"F",23,23.1,8.0,7.5,28.0,60.8,0.8,10.9,5.9,10.5,9.5,False,False),
    (1628973,"Jalen Brunson","NYK",29,"6'2",190,"G",11,26.8,7.3,3.6,31.0,59.4,3.1,7.7,5.2,8.2,6.9,False,False),
    (1630169,"Tyrese Haliburton","IND",25,"6'5",185,"G",0,19.9,10.7,3.7,25.5,60.1,3.8,7.8,5.3,7.6,6.0,False,False),
    (1627783,"Pascal Siakam","IND",31,"6'8",245,"F",43,21.7,4.0,7.3,25.6,58.5,1.9,6.2,7.1,7.6,5.3,False,False),
    (1630532,"Franz Wagner","ORL",24,"6'10",220,"F",22,21.5,4.0,5.5,27.2,57.0,3.4,6.9,6.5,6.2,6.2,False,False),
    (1631099,"Keegan Murray","SAC",25,"6'8",225,"F",13,15.2,2.0,5.5,20.0,57.2,2.2,5.9,6.7,5.7,4.5,False,False),
    (1631101,"Jabari Smith Jr.","HOU",22,"6'11",220,"F",10,14.8,1.6,8.7,20.6,56.5,3.0,6.1,7.3,6.8,6.2,False,False),
    (1631095,"Jalen Williams","OKC",24,"6'5",211,"G/F",8,21.0,5.3,5.5,25.8,61.7,4.2,5.8,7.6,12.0,7.4,False,False),
    (1641708,"Brandon Miller","CHA",23,"6'7",200,"F",24,21.2,3.6,5.0,26.2,57.7,4.8,7.0,5.2,3.0,6.9,False,False),
    (1641731,"Amen Thompson","HOU",23,"6'7",215,"G/F",1,14.5,4.4,8.2,19.3,59.8,5.1,6.4,8.3,6.8,8.4,False,False),
    (1630596,"Evan Mobley","CLE",24,"7'0",215,"F/C",4,18.6,3.2,9.3,22.3,61.4,2.5,5.7,9.2,9.0,6.5,False,False),
    (1630543,"Alperen Şengün","HOU",23,"6'11",243,"C",28,22.0,5.2,10.4,27.4,58.3,3.0,6.6,6.2,6.8,7.1,False,False),
    (1630595,"Cade Cunningham","DET",24,"6'6",220,"G",2,25.1,9.1,6.2,32.2,57.2,4.5,8.9,5.0,5.0,7.2,False,False),
    (1629636,"Darius Garland","CLE",26,"6'1",192,"G",10,21.0,7.0,2.8,26.5,58.8,2.8,6.7,4.7,9.0,5.4,False,False),
    (1642264,"Zaccharie Risacher","ATL",20,"6'8",200,"F",10,13.2,1.5,4.0,19.5,54.5,3.7,7.9,5.6,4.0,8.8,True,False),
    (1642262,"Alex Sarr","WAS",20,"7'0",205,"C",20,12.0,2.0,7.0,21.5,53.4,3.2,8.2,8.5,2.5,8.4,True,False),
    (1641706,"Scoot Henderson","POR",22,"6'3",202,"G",00,17.2,6.6,3.7,27.0,53.1,4.6,9.8,4.1,3.5,6.0,False,False),
    (1629008,"Michael Porter Jr.","BKN",27,"6'10",218,"F",1,18.5,1.8,6.8,22.8,60.0,2.0,6.5,4.6,4.2,4.8,False,False),
    (1626164,"Devin Booker","PHX",29,"6'5",206,"G",1,26.6,6.4,4.2,30.5,59.5,1.7,7.4,5.0,6.0,7.2,False,False),
    (203078,"Bradley Beal","PHX",32,"6'4",207,"G",3,18.1,4.2,3.9,23.6,57.5,0.8,8.5,4.8,6.0,5.6,False,False),
    (1627780,"Gary Trent Jr.","MIL",27,"6'5",204,"G",5,13.0,1.4,2.6,18.8,56.6,2.1,5.4,4.0,8.4,4.0,False,True),
]

LEAGUE_ZONE_AVG = {
    "Paint": 61, "Free Throw": 44, "Left Midrange": 42, "Right Midrange": 42,
    "Left Corner 3": 38, "Right Corner 3": 38, "Left Wing 3": 36, "Right Wing 3": 36, "Above Break 3": 35
}

def compute_archetype(ppg, apg, rpg):
    if apg >= 8: return "Playmaker"
    if ppg >= 28 and apg < 6: return "Elite Scorer"
    if rpg >= 10 and ppg < 20: return "Rim Anchor"
    if ppg >= 20 and rpg >= 8: return "All-Around Big"
    if ppg >= 18 and apg >= 5: return "Two-Way Engine"
    if ppg >= 15: return "Scoring Wing"
    if rpg >= 8: return "Stretch Big"
    return "Role Contributor"

def zones_for_player(p):
    arch = p[4] if len(p) > 4 else ""
    # base shaped by statistical role, not random
    pid,name,team,age,height,weight,pos,jersey,ppg,apg,rpg,usg,ts,mom,*rest = p
    paint = 56 + min(10, rpg*.45) + (3 if "C" in pos or "F" in pos else 0)
    ft = 39 + min(8, ppg*.1) + max(0, ts-56)*.15
    mid_l = 39 + min(8, ppg*.09) + (2 if age > 28 else 0)
    mid_r = mid_l - .6 + (mom*.15)
    corner_l = 34 + max(0, ts-55)*.22 + (1.5 if pos in ["F","G/F"] else 0)
    corner_r = 33.5 + max(0, ts-55)*.20 + (1.2 if pos in ["F","G/F"] else 0)
    wing_l = 34 + max(0, ts-55)*.20 + min(3, usg*.04)
    wing_r = 34 + max(0, ts-55)*.18 + min(3, usg*.04)
    above = 33 + max(0, ts-55)*.22 + (3 if apg >= 7 else 1)
    vals = {"Paint":paint,"Free Throw":ft,"Left Midrange":mid_l,"Right Midrange":mid_r,"Left Corner 3":corner_l,"Right Corner 3":corner_r,"Left Wing 3":wing_l,"Right Wing 3":wing_r,"Above Break 3":above}
    return [{"zone": z, "fg_pct": round(v,1), "league_avg": LEAGUE_ZONE_AVG[z], "diff": round(v-LEAGUE_ZONE_AVG[z],1), "volume": round(28 + abs(v-LEAGUE_ZONE_AVG[z])*6 + (ppg/2),1)} for z,v in vals.items()]

def decorate(row):
    pid,name,team,age,height,weight,pos,jersey,ppg,apg,rpg,usg,ts,mom,risk,defense,team_bonus,narrative,rookie,sixth = row
    arch = compute_archetype(ppg,apg,rpg)
    production = round(ppg + apg*.9 + rpg*.75,1)
    consistency = round(max(42,min(96, 70 + (ts-54)*1.7 + team_bonus*.4 - risk*.8)),1)
    volatility = round(max(2.0, 12 - consistency*.07 + risk*.25),1)
    hot_score = round(ppg*.78 + apg*1.15 + rpg*.72 + usg*.28 + ts*.18 + mom*2.1 + team_bonus*.35 - risk*.3,1)
    signal_score = round(hot_score + mom*2.2 + consistency*.13 - risk*.55 + team_bonus*.4,1)
    expected = round(24 + max(0, 27-abs(age-27))*1.05 - max(0, age-32)*1.25,1)
    delta = round(production - expected,1)
    clutch = round(ppg*.75 + apg*1.2 + consistency*.42 + mom*1.8,1)
    mvp = round(ppg*1.4 + apg*.95 + rpg*.65 + ts*.23 + team_bonus*2.35 + narrative*3.2 + mom*1.6 - risk*.35,1)
    dpoy = round(defense*8.8 + rpg*1.7 + team_bonus*.8 + narrative*.35,1)
    sixth_score = round((ppg+apg+rpg)*1.5 + mom*3 + (8 if sixth else 0),1)
    mip = round(max(0,mom)*8.5 + max(0, signal_score-50)*.75 + max(0, 26-age)*.8,1)
    roty = round((ppg*1.25+rpg*.85+apg*.95+mom*2.2+defense*2.5)*(1.15 if rookie else .18),1)
    decision = "BUY SIGNAL" if signal_score >= 68 else "OVERPERFORM ALERT" if signal_score >= 58 else "HOLD" if signal_score >= 48 else "FADE"
    return {
        "id":pid,"name":name,"team":team,"team_name":TEAM_NAMES[team],"team_logo_url":logo(team),"team_colors":TEAM_COLORS[team],
        "headshot_url":headshot(pid),"image":headshot(pid),"age":age,"height":height,"weight":weight,"position":pos,"jersey":jersey,
        "archetype":arch,"ppg":round(ppg,1),"apg":round(apg,1),"rpg":round(rpg,1),"usage":round(usg,1),"ts_pct":round(ts,1),"momentum":round(mom,1),"risk":round(risk,1),"defense_score":round(defense,1),"team_bonus":team_bonus,
        "production":production,"expected_production":expected,"aging_delta":delta,"hot_score":hot_score,"signal_score":signal_score,"consistency":consistency,"volatility":volatility,"clutch_proxy":clutch,"decision":decision,
        "award_mvp_score":mvp,"award_dpoy_score":dpoy,"award_6moy_score":sixth_score,"award_mip_score":mip,"award_roty_score":roty,
        "projection":{"pts":round(ppg + mom*.42 + max(0,signal_score-60)*.04,1),"reb":round(rpg + .25 + mom*.05,1),"ast":round(apg + .18 + mom*.06,1),"confidence":round(max(48,min(96,50+signal_score*.55-risk*.5)),1)},
        "shot_zones":zones_for_player(row),
        "intel":[
            f"{name} projects as a {decision.lower()} because usage ({round(usg,1)}), momentum ({round(mom,1)}), and efficiency ({round(ts,1)} TS%) are aligned.",
            f"Best scoring zone: {max(zones_for_player(row), key=lambda z:z['diff'])['zone']} at {max(zones_for_player(row), key=lambda z:z['diff'])['fg_pct']}%.",
            "Risk rises if pace slows or role compresses." if risk>8 else "Risk profile is clean for a stable role projection."
        ],
        "reason": f"{name} combines production, role, momentum, and team context into a {round(signal_score,1)} signal score."
    }

def build_all():
    players=[decorate(r) for r in BASE_PLAYERS]
    teams=[]
    for abbr in TEAM_IDS:
        roster=[p for p in players if p["team"]==abbr]
        idx=list(TEAM_IDS).index(abbr)
        if roster:
            star=max(x["hot_score"] for x in roster)
            depth=sum(x["hot_score"] for x in sorted(roster,key=lambda p:p["hot_score"],reverse=True)[:6])/min(6,len(roster))
            momentum=sum(x["momentum"] for x in roster)/len(roster)
            defense=sum(x["defense_score"] for x in roster)/len(roster)
        else:
            star=34+(idx%9)*2.3
            depth=31+(idx%11)*1.5
            momentum=((idx%7)-3)*.6
            defense=4+(idx%8)*.55
        power=round(star*.50+depth*.34+momentum*2.7+defense*2.15,1)
        stress=round(power*.88+defense*2.2,1)
        teams.append({"abbr":abbr,"name":TEAM_NAMES[abbr],"logo_url":logo(abbr),"colors":TEAM_COLORS[abbr],"power_index":power,"stress":stress,"star_power":round(star,1),"depth":round(depth,1),"momentum":round(momentum,1),"defense":round(defense,1),"pace":round(96+(idx%8)*1.4,1)})
    return {"players":players,"teams":teams,"league_zone_avg":LEAGUE_ZONE_AVG}

def win_prob(a,b):
    raw = (a["power_index"]-b["power_index"])*.72 + (a["star_power"]-b["star_power"])*.22 + (a["momentum"]-b["momentum"])*2.1 + (a["defense"]-b["defense"])*1.2
    prob=100/(1+exp(-raw/8.5))
    # compress unless true gap is huge
    gap=abs(a["power_index"]-b["power_index"])
    if gap < 20:
        prob=50+(prob-50)*.55
    return round(max(20,min(80,prob)),1), round(100-max(20,min(80,prob)),1), round(abs((max(20,min(80,prob)))-(100-max(20,min(80,prob)))),1)
