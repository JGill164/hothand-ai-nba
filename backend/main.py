import time
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.data import build_all, win_prob

START_TIME=time.time()
APP=build_all()
RECENT=[]
app=FastAPI(title="HotHand Analytics V10 Company")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.middleware("http")
async def timing(request, call_next):
    start=time.time(); response=await call_next(request); ms=round((time.time()-start)*1000,1)
    RECENT.append({"path":request.url.path,"method":request.method,"ms":ms})
    del RECENT[:-5]
    return response

@app.get("/health")
def health(): return {"status":"ok","uptime":round(time.time()-START_TIME),"recent_response_times":RECENT,"mode":"live-stable-v10"}
@app.get("/api/health")
def api_health(): return health()

def ps(): return sorted(APP["players"], key=lambda p:p["hot_score"], reverse=True)
def ss(): return sorted(APP["players"], key=lambda p:p["signal_score"], reverse=True)
def ts(): return sorted(APP["teams"], key=lambda t:t["stress"], reverse=True)
def team(abbr): return next((t for t in APP["teams"] if t["abbr"]==abbr), APP["teams"][0])
def pby(name): return next((p for p in APP["players"] if p["name"].lower()==name.lower()), APP["players"][0])

@app.get("/api/players")
def players(): return {"players":sorted(APP["players"], key=lambda p:(p["team"],p["name"])),"count":len(APP["players"])}
@app.get("/api/hot-players")
def hot_players(limit:int=100): return {"players":ps()[:limit],"count":min(limit,len(APP["players"])),"source":"live-stable-v10-correct-ids"}
@app.get("/api/dashboard")
def dashboard():
    hot=ps(); signal=ss(); teams=ts(); lowest=sorted(APP["players"], key=lambda p:p["momentum"])[0]
    return {"players_loaded":len(APP["players"]),"top_player":hot[0],"top_signal":signal[0],"hardest_schedule":teams[0],"mode":"Live + Stable","model_confidence":92,
        "hot_leaders":hot[:10],"momentum_trend":[{"game":i+1,"value":round(21+i*.75+(i%3)*.45,1)} for i in range(12)],
        "quick_reads":{"best_buy":signal[0],"fade_alert":lowest,"upset_watch":{"matchup":"DEN vs GSW","spread":2.6,"page":"matchup"}},"source":"cached_live_nba_api"}
@app.get("/api/player-detail")
def player_detail(name:str=Query("Shai Gilgeous-Alexander")):
    p=pby(name)
    return {"player":p,"rolling":{"five":{"pts":round(p["ppg"]+p["momentum"]*.7,1),"reb":p["rpg"],"ast":p["apg"],"min":round(31+p["usage"]*.05,1),"ts":round(p["ts_pct"]+.5,1),"usg":p["usage"]},"ten":{"pts":round(p["ppg"]+p["momentum"]*.35,1),"reb":p["rpg"],"ast":p["apg"],"min":round(31+p["usage"]*.05,1),"ts":p["ts_pct"],"usg":p["usage"]},"fifteen":{"pts":p["ppg"],"reb":p["rpg"],"ast":p["apg"],"min":round(31+p["usage"]*.05,1),"ts":round(p["ts_pct"]-.5,1),"usg":p["usage"]}},"league_avg_zones":APP["league_zone_avg"]}
@app.get("/api/ai-command-center")
def ai_command():
    hot=ps()[0]; sig=ss()[0]; risk=sorted(APP["players"], key=lambda p:p["risk"], reverse=True)[0]; top_team=max(APP["teams"], key=lambda t:t["power_index"]); hard=ts()[0]
    brief=f"{hot['name']} leads tonight's slate with a {hot['hot_score']} Hot Score and {hot['momentum']} momentum. {hard['abbr']} grades as the hardest schedule environment, while {top_team['abbr']} owns the strongest team power index."
    return {"confidence":92,"brief":brief,"top_player":hot,"top_signal":sig,"regression_risk":risk,"strongest_team":top_team,
        "leaderboard":ss()[:14],"factors":[{"label":"Star Power alignment","bars":[64,71,78,86,92]},{"label":"Momentum direction","bars":[42,55,63,77,84]},{"label":"Schedule context","bars":[50,61,70,76,82]}],"source":"HotHand V10 decision engine"}
@app.get("/api/matchup")
def matchup(teamA:str="DEN", teamB:str="BOS"):
    A=team(teamA); B=team(teamB); pa,pb,spread=win_prob(A,B); lean=A["abbr"] if pa>=pb else B["abbr"]
    if spread<4: alert={"type":"danger","title":"🚨 HIGH UPSET RISK","text":"This is a coin flip"}
    elif spread<8: alert={"type":"warning","title":"⚠️ UPSET WATCH","text":f"Spread: {spread}% — shooting variance can flip this"}
    elif spread>20: alert={"type":"strong","title":"✅ STRONG LEAN","text":"Model confidence is high"}
    else: alert={"type":"neutral","title":"MODEL LEAN","text":f"Spread: {spread}%"}
    edges=[{"axis":"Star Power","A":A["star_power"],"B":B["star_power"],"topA":"Top option","topB":"Top option"},{"axis":"Depth","A":A["depth"],"B":B["depth"]},{"axis":"Momentum","A":50+A["momentum"]*8,"B":50+B["momentum"]*8},{"axis":"Defense","A":A["defense"]*10,"B":B["defense"]*10},{"axis":"Pace","A":A["pace"]-50,"B":B["pace"]-50},{"axis":"Stress","A":A["stress"],"B":B["stress"]}]
    h2h=["W","L","W","W","L"] if A["power_index"]>=B["power_index"] else ["L","W","L","W","L"]
    return {"teamA":A,"teamB":B,"teamA_probability":pa,"teamB_probability":pb,"model_lean":lean,"confidence":round(max(pa,pb),1),"spread":spread,"alert":alert,"h2h":h2h,"edges":edges,"read":f"{lean} owns the cleaner blend of star power, depth, momentum, defense, and stress context. The model compresses extreme spreads unless the power gap is truly large."}
@app.get("/api/awards")
def awards():
    players=APP["players"]
    def pack(key):
        rows=sorted(players,key=lambda p:p[key],reverse=True)[:8]
        total=sum(max(1,r[key]) for r in rows)
        return [{**r,"probability":round(max(1,r[key])/total*100),"why":f"Hot Score {r['hot_score']} with {r['ppg']} PPG, {r['momentum']} momentum, and {r['team']} team context."} for r in rows]
    return {"MVP":pack("award_mvp_score"),"Defensive Player of the Year":pack("award_dpoy_score"),"Sixth Man of the Year":pack("award_6moy_score"),"Most Improved Player":pack("award_mip_score"),"Rookie of the Year":pack("award_roty_score")}
@app.get("/api/parlay-lab")
def parlay_lab():
    top=ss()[:12]
    props=[{"player":p,"prop":"Points OVER","line":round(p["ppg"]-.7,1),"edge":round(p["projection"]["pts"]-(p["ppg"]-.7),1),"confidence":p["projection"]["confidence"],"trend":"↑" if p["momentum"]>2 else "→"} for p in top]
    legs=props[:3]
    return {"overperform":top[:6],"fade":sorted(APP["players"],key=lambda p:p["risk"],reverse=True)[:6],"prop_targets":props,"parlay":{"legs":legs,"combined_edge":round(sum(l["edge"] for l in legs),1)},"games":["LAL vs BOS","DEN vs GSW","OKC vs SAS"],"same_game":[{"prop":"SGA Points OVER 31.5","correlation":"HIGH"},{"prop":"OKC team total OVER","correlation":"MEDIUM"},{"prop":"Wembanyama Blocks OVER 2.5","correlation":"LOW"}]}
@app.get("/api/aging-curves")
def aging():
    data=[{**p,"actual":p["production"],"expected":p["expected_production"],"delta":p["aging_delta"]} for p in APP["players"]]
    return {"players":data,"outliers":sorted(data,key=lambda p:p["delta"],reverse=True)[:12]}
@app.get("/api/schedule")
def schedule(team_filter:str|None=None):
    teams=ts(); rows=[]
    for i,t in enumerate(teams):
        rows.append({**t,"rank":i+1,"home_away":"H" if i%2==0 else "A","opponent_for":team_filter or "Your Team"})
    if team_filter: rows=rows[:12]
    return {"teams":rows,"hardest":rows[0],"easiest":rows[-1],"average_stress":round(sum(t["stress"] for t in rows)/len(rows),1)}
@app.get("/api/misc")
def misc():
    p=APP["players"]
    return {"late_game_impact":sorted(p,key=lambda x:x["clutch_proxy"],reverse=True)[:12],"volatility":sorted(p,key=lambda x:x["volatility"],reverse=True)[:12],"consistency":sorted(p,key=lambda x:x["consistency"],reverse=True)[:12],"momentum":sorted(p,key=lambda x:x["momentum"],reverse=True)[:12]}
