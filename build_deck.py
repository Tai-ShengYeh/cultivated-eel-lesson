# -*- coding: utf-8 -*-
"""
build_deck.py  —  唯一 source of truth
以 foodNEXT〈培植肉拯救瀕危魚類 人造鰻魚飯預計2025年上市〉製作
A2–B1 華文文獻閱讀與寫作 SOIL HTML 教學簡報（13頁 + 4 minigame）。
改 HTML 一律改這支腳本後重跑，不要直接改輸出 HTML。
"""
from PIL import Image
import base64, io, os

BASE = r"D:\course\食品營養華語文獻閱讀\week_cultivated_eel"
GEN  = os.path.join(BASE, "slides", "generated")

def embed(name, target_w, q=80):
    p = os.path.join(GEN, name)
    img = Image.open(p).convert("RGB")
    w, h = img.size
    if w > target_w:
        img = img.resize((target_w, int(h * target_w / w)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=q, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return "data:image/jpeg;base64," + b64

COVER  = embed("slide-1-cover.png", 1280)
CRISIS = embed("slide-6-crisis.png", 900)
LAB    = embed("slide-7-lab.png", 900)
CHOICE = embed("slide-10-choice.png", 1100)

HTML = r'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>人造鰻魚飯？｜食品營養華語 · 文獻閱讀與寫作</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
html,body{font-size:18px;}
*{margin:0;padding:0;box-sizing:border-box;}
:root{
  --bg:#0a0e27; --bg2:#11163a;
  --ink:#eef3ff; --ink2:#b8c5e0; --ink3:#7a8bb8; --ink4:#4a5680;
  --accent:#00d4ff; --accent2:#ff006e;
  --ok:#27e0a0; --warn:#ffb800; --bad:#ff4d6d;
  --card:rgba(255,255,255,.05); --line:rgba(255,255,255,.12);
}
body{
  background:radial-gradient(1200px 700px at 75% -10%, #18204d 0%, var(--bg) 55%) , var(--bg);
  color:var(--ink); font-family:"Noto Sans TC",system-ui,sans-serif;
  height:100vh; overflow:hidden; -webkit-font-smoothing:antialiased;
}
.mono{font-family:"JetBrains Mono",monospace;}
b,strong{font-weight:700;}
.hl{color:var(--accent);} .hl2{color:var(--warn);} .ok-t{color:var(--ok);}
.accent{color:var(--accent);} .accent2{color:var(--accent2);}

/* ---------- chrome ---------- */
#progress{position:fixed;top:0;left:0;height:3px;width:0;z-index:50;
  background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width .5s ease;}
#sectag{position:fixed;top:16px;left:22px;z-index:40;font-family:"JetBrains Mono",monospace;
  font-size:.72rem;letter-spacing:.18em;color:var(--ink3);text-transform:uppercase;}
#pageinfo{position:fixed;right:22px;bottom:16px;z-index:40;font-family:"JetBrains Mono",monospace;
  font-size:.8rem;color:var(--ink3);}
#pageinfo b{color:var(--accent);font-size:1rem;}
#hint{position:fixed;left:22px;bottom:16px;z-index:40;font-size:.7rem;color:var(--ink4);}

/* ---------- slides ---------- */
.slide{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  padding:64px 88px;opacity:0;pointer-events:none;transform:translateY(16px);
  transition:opacity .5s ease, transform .5s ease;overflow:hidden;}
.slide.active{opacity:1;pointer-events:auto;transform:none;}
.slide-inner{width:100%;max-width:1320px;}
.center{text-align:center;display:flex;flex-direction:column;align-items:center;gap:18px;}
.kicker{font-family:"JetBrains Mono",monospace;font-size:clamp(.72rem,1vw,.86rem);
  letter-spacing:.16em;color:var(--accent);text-transform:uppercase;margin-bottom:10px;}
.kicker.accent2{color:var(--accent2);}
.slide-title{font-size:clamp(1.7rem,3.4vw,2.7rem);font-weight:900;line-height:1.12;margin-bottom:14px;}
.sub{font-size:clamp(.95rem,1.45vw,1.18rem);color:var(--ink2);margin-bottom:18px;line-height:1.7;}
.tiny{font-size:.82rem;color:var(--ink3);}
.lead{font-size:clamp(1.05rem,1.7vw,1.4rem);color:var(--ink);line-height:1.7;}
.lead.big{font-size:clamp(1.2rem,2.1vw,1.7rem);}
.note{font-size:clamp(.92rem,1.3vw,1.08rem);color:var(--ink3);}

/* ---------- cover ---------- */
.cover{position:absolute;inset:0;}
.cover-bg{position:absolute;inset:0;background-size:cover;background-position:center;}
.cover-shade{position:absolute;inset:0;
  background:linear-gradient(90deg,rgba(10,14,39,.92) 0%,rgba(10,14,39,.6) 45%,rgba(10,14,39,.15) 100%),
             linear-gradient(0deg,rgba(10,14,39,.85) 0%,rgba(10,14,39,0) 55%);}
.cover-inner{position:absolute;left:88px;bottom:96px;max-width:760px;}
.cover-title{font-size:clamp(2.6rem,6vw,5rem);font-weight:900;line-height:1.02;
  letter-spacing:.01em;text-shadow:0 4px 40px rgba(0,212,255,.25);}
.cover-title:after{content:"";display:block;width:88px;height:5px;margin-top:18px;
  background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:3px;}
.cover-sub{margin-top:22px;font-size:clamp(1.1rem,2vw,1.55rem);color:var(--ink2);line-height:1.6;}
.cover-src{margin-top:26px;font-size:.82rem;color:var(--ink3);font-family:"JetBrains Mono",monospace;}

/* ---------- stats ---------- */
.stat-row{display:flex;gap:54px;align-items:center;justify-content:center;flex-wrap:wrap;margin:6px 0 4px;}
.stat-big{display:flex;flex-direction:column;align-items:center;gap:8px;}
.stat-big .num{font-size:clamp(2.6rem,6vw,4.6rem);font-weight:900;color:var(--accent);line-height:1;}
.stat-big.alt .num{color:var(--accent2);}
.stat-big .cap{font-size:clamp(.85rem,1.2vw,1rem);color:var(--ink2);line-height:1.5;}
.spark{margin:2px auto 0;display:block;}

/* ---------- chips ---------- */
.chips3{display:flex;align-items:center;gap:14px;flex-wrap:wrap;justify-content:center;margin:6px 0;}
.chip{padding:10px 20px;border:1px solid var(--line);border-radius:999px;background:var(--card);
  font-weight:700;font-size:clamp(1rem,1.6vw,1.3rem);}
.arrow{color:var(--accent);font-weight:900;font-size:1.4rem;}

/* ---------- map ---------- */
.map6{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;}
.map-step{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px 22px;
  position:relative;}
.map-step .mn{position:absolute;top:-14px;left:18px;width:30px;height:30px;border-radius:50%;
  background:linear-gradient(135deg,var(--accent),var(--accent2));color:#06122b;font-weight:900;
  display:flex;align-items:center;justify-content:center;font-size:.95rem;}
.map-step b{font-size:clamp(1.05rem,1.6vw,1.3rem);}
.map-step p{margin-top:6px;color:var(--ink2);font-size:clamp(.85rem,1.2vw,1rem);}

/* ---------- split (image + text) ---------- */
.split{display:grid;grid-template-columns:1fr 1.05fr;gap:40px;align-items:center;}
.split.rev .split-img{order:2;}
.split-img img{width:100%;max-height:62vh;object-fit:cover;border-radius:18px;
  border:1px solid var(--line);box-shadow:0 20px 60px rgba(0,0,0,.45);}
.split-txt{display:flex;flex-direction:column;gap:16px;}
.big-list{list-style:none;display:flex;flex-direction:column;gap:16px;}
.big-list li{position:relative;padding-left:30px;font-size:clamp(1rem,1.55vw,1.32rem);line-height:1.65;color:var(--ink);}
.big-list li:before{content:"";position:absolute;left:0;top:.55em;width:12px;height:12px;border-radius:50%;
  background:linear-gradient(135deg,var(--accent),var(--accent2));}
.vocab-strip{display:flex;gap:10px;flex-wrap:wrap;margin-top:4px;}
.vocab-strip span{font-family:"JetBrains Mono",monospace;font-size:.82rem;color:var(--accent);
  border:1px dashed rgba(0,212,255,.4);padding:5px 12px;border-radius:8px;}
.firm{margin-top:6px;font-size:clamp(.95rem,1.4vw,1.15rem);color:var(--ink2);
  background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 18px;}

/* ---------- table page 8 ---------- */
.split8{display:grid;grid-template-columns:1.5fr 1fr;gap:36px;align-items:start;}
.tbl{width:100%;border-collapse:collapse;font-size:clamp(.88rem,1.2vw,1.08rem);}
.tbl th,.tbl td{text-align:left;padding:13px 14px;border-bottom:1px solid var(--line);}
.tbl thead th{color:var(--ink3);font-family:"JetBrains Mono",monospace;font-size:.8rem;
  letter-spacing:.08em;cursor:pointer;user-select:none;}
.tbl thead th:hover{color:var(--accent);}
.tbl tbody tr:hover{background:rgba(255,255,255,.03);}
.tbl td b{color:var(--accent);}
.data-cards{display:flex;flex-direction:column;gap:14px;}
.dc{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent2);
  border-radius:12px;padding:14px 18px;}
.dc .dn{font-size:clamp(1.6rem,2.6vw,2.2rem);font-weight:900;color:var(--accent2);}
.dc .du{margin-left:8px;font-size:.95rem;color:var(--ink2);}
.dc .dl{display:block;margin-top:4px;font-size:.82rem;color:var(--ink3);}

/* ---------- writing scaffold ---------- */
.steps4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:22px;}
.step4{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px 18px;position:relative;}
.step4 .sn{width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,var(--accent2),var(--accent));
  color:#06122b;font-weight:900;display:flex;align-items:center;justify-content:center;margin-bottom:12px;}
.step4 b{font-size:clamp(1.05rem,1.6vw,1.3rem);}
.step4 p{margin-top:8px;color:var(--ink2);font-size:clamp(.85rem,1.2vw,1.02rem);line-height:1.6;}
.model{background:rgba(0,212,255,.08);border:1px solid rgba(0,212,255,.3);border-radius:14px;
  padding:18px 22px;font-size:clamp(.98rem,1.45vw,1.2rem);line-height:1.8;}
.model b{color:var(--accent);}

/* ---------- minigame shared ---------- */
.mg{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px 24px;}
.mg-bar{display:flex;align-items:center;justify-content:space-between;margin-top:16px;
  font-family:"JetBrains Mono",monospace;font-size:1rem;color:var(--accent);}
.mg-reset{background:transparent;border:1px solid var(--line);color:var(--ink2);border-radius:9px;
  padding:7px 16px;cursor:pointer;font-size:.85rem;font-family:inherit;}
.mg-reset:hover{border-color:var(--accent);color:var(--accent);}

/* MG1 matching */
.mg1-cols{display:grid;grid-template-columns:.7fr 1.3fr;gap:18px;}
.mg1-col{display:flex;flex-direction:column;gap:12px;}
.pair{padding:14px 18px;border:1px solid var(--line);border-radius:12px;background:rgba(255,255,255,.03);
  cursor:pointer;font-size:clamp(.95rem,1.35vw,1.18rem);transition:.15s;line-height:1.5;}
.pair.word{font-weight:700;text-align:center;}
.pair:hover{border-color:var(--accent);}
.pair.sel{border-color:var(--accent);background:rgba(0,212,255,.12);}
.pair.done{border-color:var(--ok);background:rgba(39,224,160,.12);color:var(--ok);cursor:default;pointer-events:none;}
.pair.bad{border-color:var(--bad);animation:shake .3s;}
@keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}

/* MG2 / MG4 questions */
.q{margin-bottom:14px;}
.q:last-child{margin-bottom:0;}
.q-t{font-size:clamp(.98rem,1.4vw,1.18rem);font-weight:700;margin-bottom:9px;line-height:1.45;}
.q-t .qn{color:var(--accent);margin-right:8px;}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:9px;}
.opt{padding:10px 14px;border:1px solid var(--line);border-radius:11px;background:rgba(255,255,255,.03);
  cursor:pointer;font-size:clamp(.88rem,1.25vw,1.06rem);transition:.15s;text-align:left;color:var(--ink);}
/* MG2：4 題排成 2×2，避免直向溢出 */
#mg2-body{display:grid;grid-template-columns:1fr 1fr;gap:6px 30px;align-items:start;}
#mg2-body .q{margin-bottom:6px;}
/* MG4：3 個連接詞選項排成一列 */
#mg4-body .opts{grid-template-columns:repeat(3,1fr);}
#mg4-body .q{margin-bottom:12px;}
.opt:hover{border-color:var(--accent);}
.opt.right{border-color:var(--ok);background:rgba(39,224,160,.15);color:var(--ok);font-weight:700;}
.opt.wrong{border-color:var(--bad);background:rgba(255,77,109,.12);color:var(--bad);}
.opt.lock{pointer-events:none;}
.fb{margin-top:8px;font-size:.92rem;color:var(--ink3);min-height:1.2em;}
.fb.good{color:var(--ok);} .fb.no{color:var(--warn);}

/* MG3 stance */
.split10{display:grid;grid-template-columns:.85fr 1.15fr;gap:34px;align-items:center;}
.split-img.sm img{width:100%;max-height:50vh;object-fit:cover;border-radius:16px;border:1px solid var(--line);}
.q3{font-size:clamp(1.05rem,1.6vw,1.32rem);font-weight:700;margin-bottom:16px;line-height:1.5;}
.stance{display:flex;gap:12px;flex-wrap:wrap;}
.stance button{flex:1;min-width:120px;padding:16px 14px;border:1px solid var(--line);border-radius:14px;
  background:rgba(255,255,255,.03);color:var(--ink);font-size:clamp(1rem,1.5vw,1.2rem);font-weight:700;
  cursor:pointer;transition:.15s;font-family:inherit;}
.stance button:hover{border-color:var(--accent2);}
.stance button.on{border-color:var(--accent2);background:rgba(255,0,110,.15);color:#ffd0e4;}
.reasons{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 14px;}
.rchip{padding:9px 16px;border:1px solid var(--line);border-radius:999px;background:rgba(255,255,255,.03);
  cursor:pointer;font-size:clamp(.85rem,1.2vw,1.02rem);transition:.15s;}
.rchip:hover{border-color:var(--accent);}
.rchip.on{border-color:var(--accent);background:rgba(0,212,255,.15);color:var(--accent);}
.stem{background:rgba(0,212,255,.08);border:1px solid rgba(0,212,255,.3);border-radius:12px;
  padding:14px 18px;font-size:clamp(.98rem,1.4vw,1.18rem);line-height:1.7;min-height:1em;}
.stem b{color:var(--accent);}
.hidden{display:none;}

/* MG4 cloze filled */
.cloze{font-size:clamp(.98rem,1.45vw,1.2rem);line-height:1.55;margin-bottom:7px;}
.cloze .blank{color:var(--ink4);border-bottom:2px dashed var(--ink4);padding:0 22px;}
.cloze.filled{color:var(--ok);} .cloze.filled b{color:var(--ok);}

/* ---------- task page 13 ---------- */
.task{display:grid;grid-template-columns:1.25fr 1fr;gap:28px;align-items:start;margin-bottom:20px;}
.prompt{background:rgba(255,0,110,.08);border:1px solid rgba(255,0,110,.32);border-radius:16px;
  padding:22px 24px;font-size:clamp(1.05rem,1.6vw,1.35rem);line-height:1.7;}
.prompt .wc{display:inline-block;margin-top:10px;font-size:.85rem;color:var(--accent2);
  font-family:"JetBrains Mono",monospace;border:1px solid rgba(255,0,110,.4);padding:3px 10px;border-radius:7px;}
.rubric{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 20px;}
.rubric .rh{font-weight:700;color:var(--accent);margin-bottom:10px;font-size:clamp(.95rem,1.3vw,1.1rem);}
.rrow{display:flex;justify-content:space-between;gap:12px;padding:8px 0;border-bottom:1px solid var(--line);
  font-size:clamp(.85rem,1.2vw,1.02rem);}
.rrow:last-child{border-bottom:none;}
.rrow span:first-child{font-weight:700;color:var(--ink);} .rrow span:last-child{color:var(--ink3);text-align:right;}
.bottom13{display:grid;grid-template-columns:1.4fr 1fr;gap:24px;align-items:stretch;}
.extra{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 20px;}
.extra .eh{font-weight:700;margin-bottom:8px;color:var(--ink2);}
.extra ul{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:4px 18px;}
.extra li{font-size:.86rem;color:var(--ink3);padding-left:14px;position:relative;line-height:1.7;}
.extra li:before{content:"›";position:absolute;left:0;color:var(--accent);}
.cta{background:linear-gradient(135deg,rgba(0,212,255,.16),rgba(255,0,110,.16));
  border:1px solid rgba(0,212,255,.3);border-radius:14px;padding:18px 22px;display:flex;align-items:center;
  font-size:clamp(1rem,1.45vw,1.22rem);line-height:1.7;}
.cta b{color:var(--accent);}

@media (max-width:900px){
  .slide{padding:54px 24px;}
  .split,.split8,.split10,.task,.bottom13{grid-template-columns:1fr;gap:20px;}
  .map6,.steps4{grid-template-columns:1fr 1fr;}
  .opts{grid-template-columns:1fr;}
  .cover-inner{left:24px;right:24px;bottom:54px;}
}
</style>
</head>
<body>
<div id="progress"></div>
<div id="sectag">— 引起動機 —</div>
<div id="pageinfo"><b>1</b> / 13</div>
<div id="hint">← → 翻頁 · 點兩側翻頁 · F 全螢幕</div>

<!-- 1 封面 -->
<section class="slide active" data-slide="1" data-section="引起動機">
  <div class="cover">
    <div class="cover-bg" style="background-image:url('__COVER__')"></div>
    <div class="cover-shade"></div>
    <div class="cover-inner">
      <div class="kicker">食品營養華語 · 文獻閱讀與寫作　|　A2–B1</div>
      <h1 class="cover-title">人造鰻魚飯？</h1>
      <p class="cover-sub">用科技在實驗室養出鰻魚肉，<br>救救快要消失的鰻魚。</p>
      <div class="cover-src">改寫自 foodNEXT 食力《培植肉拯救瀕危魚類　人造鰻魚飯預計 2025 年上市》</div>
    </div>
  </div>
</section>

<!-- 2 痛點 -->
<section class="slide" data-slide="2" data-section="引起動機">
  <div class="slide-inner center">
    <div class="kicker">痛點 · 一個正在消失的味道</div>
    <h2 class="slide-title">鰻魚要消失了</h2>
    <div class="stat-row">
      <div class="stat-big">
        <span class="num">90–95%</span>
        <svg class="spark" width="150" height="40" viewBox="0 0 150 40"><polyline points="2,6 40,12 80,22 115,32 148,37" fill="none" stroke="#00d4ff" stroke-width="3" stroke-linecap="round"/></svg>
        <span class="cap">近 10 年<br>野生鰻魚數量減少</span>
      </div>
      <div class="stat-big alt">
        <span class="num">700+</span>
        <span class="cap">種可食用海洋物種<br>正面臨滅絕</span>
      </div>
    </div>
    <p class="lead">鰻魚飯是很多人的最愛，<b class="hl2">可是</b>野生鰻魚越來越少。<br>以後，我們還吃得到鰻魚飯嗎？</p>
  </div>
</section>

<!-- 3 命題 -->
<section class="slide" data-slide="3" data-section="引起動機">
  <div class="slide-inner center">
    <div class="kicker">核心命題</div>
    <h2 class="slide-title">科技能救牠嗎？</h2>
    <p class="lead big">有一家公司想用「<b class="hl">培植肉</b>」技術，<br>在實驗室裡養出鰻魚肉。</p>
    <div class="chips3">
      <span class="chip">① 瀕危</span><span class="arrow">→</span>
      <span class="chip">② 培植肉</span><span class="arrow">→</span>
      <span class="chip">③ 永續</span>
    </div>
    <p class="note">這節課，我們一起讀懂這篇文章，最後寫出自己的看法。</p>
  </div>
</section>

<!-- 4 MG1 生詞 -->
<section class="slide" data-slide="4" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker">生詞站 · 形成性評量 ①</div>
    <h2 class="slide-title">先學五個詞</h2>
    <p class="sub">點左邊一個<b class="hl">生詞</b>，再點右邊正確的<b class="hl">解釋</b>。配對成功會變成綠色。</p>
    <div class="mg" id="mg1">
      <div class="mg1-cols">
        <div class="mg1-col" id="mg1-words"></div>
        <div class="mg1-col" id="mg1-means"></div>
      </div>
      <div class="mg-bar"><span id="mg1-score">完成 0 / 5</span><button class="mg-reset" onclick="initMG1()">重來</button></div>
    </div>
  </div>
</section>

<!-- 5 文章地圖 -->
<section class="slide" data-slide="5" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker">閱讀地圖</div>
    <h2 class="slide-title">文章說什麼</h2>
    <p class="sub">這篇文章像一條線，從「問題」一路走到「未來」。</p>
    <div class="map6">
      <div class="map-step"><span class="mn">1</span><b>危機</b><p>野生鰻魚快沒了</p></div>
      <div class="map-step"><span class="mn">2</span><b>原因</b><p>洄游、過度捕撈</p></div>
      <div class="map-step"><span class="mn">3</span><b>解方</b><p>類器官培植肉</p></div>
      <div class="map-step"><span class="mn">4</span><b>商業</b><p>價格與餐廳合作</p></div>
      <div class="map-step"><span class="mn">5</span><b>未來</b><p>各國人造海鮮</p></div>
      <div class="map-step"><span class="mn">6</span><b>挑戰</b><p>大家敢不敢吃</p></div>
    </div>
  </div>
</section>

<!-- 6 危機 -->
<section class="slide" data-slide="6" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker">① 危機 · 為什麼</div>
    <h2 class="slide-title">為什麼瀕危</h2>
    <div class="split">
      <div class="split-img"><img src="__CRISIS__" alt="瀕危的野生鰻魚"></div>
      <div class="split-txt">
        <ul class="big-list">
          <li>鰻魚一生<b>只產一次卵</b>，要<b class="hl">洄游</b>到海洋裡產卵。</li>
          <li>養鰻魚幾乎完全<b class="hl">仰賴</b>（依靠）野生的小鰻魚。</li>
          <li>因為<b class="hl2">過度捕撈</b>，野生鰻苗的數量「節節下降」。</li>
        </ul>
        <div class="vocab-strip"><span>洄游</span><span>仰賴</span><span>過度捕撈</span><span>節節下降</span></div>
      </div>
    </div>
  </div>
</section>

<!-- 7 解方 -->
<section class="slide" data-slide="7" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker">② 解方 · 怎麼做</div>
    <h2 class="slide-title">肉怎麼長出來</h2>
    <div class="split rev">
      <div class="split-txt">
        <ul class="big-list">
          <li>用鰻魚受精卵的<b class="hl">胚胎幹細胞</b>，做成<b class="hl">類器官</b>。</li>
          <li>類器官會自己長出培植肉，組織<b>就像真的魚肉</b>。</li>
          <li><b class="ok-t">不用抗生素，也不用激素。</b></li>
        </ul>
        <div class="firm">🏢 以色列新創公司 <b>Forsea Foods</b>（2021 年成立，已募資 520 萬美元）</div>
      </div>
      <div class="split-img"><img src="__LAB__" alt="培植海鮮實驗室"></div>
    </div>
  </div>
</section>

<!-- 8 全球 -->
<section class="slide" data-slide="8" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker">③ 商業與未來</div>
    <h2 class="slide-title">不只有鰻魚</h2>
    <div class="split8">
      <div>
        <p class="sub">很多國家的公司，都在培植不同的海鮮。<span class="tiny">（點欄位標題可排序）</span></p>
        <table class="tbl" id="tbl8">
          <thead><tr><th data-k="co">公司</th><th data-k="ct">國家</th><th data-k="sf">培植的海鮮</th></tr></thead>
          <tbody></tbody>
        </table>
      </div>
      <div class="data-cards">
        <div class="dc"><span class="dn">250</span><span class="du">美元 / 公斤</span><span class="dl">和野生鰻魚差不多</span></div>
        <div class="dc"><span class="dn">520萬</span><span class="du">美元</span><span class="dl">Forsea 已募得投資</span></div>
        <div class="dc"><span class="dn">2025</span><span class="du">年上市</span><span class="dl">與東京餐廳合作</span></div>
      </div>
    </div>
  </div>
</section>

<!-- 9 MG2 閱讀測驗 -->
<section class="slide" data-slide="9" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker">閱讀測驗 · 形成性評量 ②</div>
    <h2 class="slide-title">閱讀小測驗</h2>
    <div class="mg" id="mg2">
      <div id="mg2-body"></div>
      <div class="mg-bar"><span id="mg2-score">得分 0 / 4</span><button class="mg-reset" onclick="initMG2()">重做</button></div>
    </div>
  </div>
</section>

<!-- 10 MG3 思辨立場 -->
<section class="slide" data-slide="10" data-section="喚起行動">
  <div class="slide-inner">
    <div class="kicker accent2">想一想 · 形成性評量 ③</div>
    <h2 class="slide-title">你會吃嗎？</h2>
    <div class="split10">
      <div class="split-img sm"><img src="__CHOICE__" alt="傳統與科技的抉擇"></div>
      <div class="mg" id="mg3">
        <p class="q3">如果有一天，人造鰻魚飯上市了，你會吃嗎？</p>
        <div class="stance" id="mg3-stance">
          <button data-s="會吃">😋 我會吃</button>
          <button data-s="不會吃">🙅 我不會</button>
          <button data-s="看情況才吃">🤔 看情況</button>
        </div>
        <div id="mg3-after" class="hidden">
          <p class="sub" style="margin:16px 0 8px">為什麼？點幾個你同意的理由（等一下寫作會用到）：</p>
          <div class="reasons" id="mg3-reasons"></div>
          <div class="stem" id="mg3-stem"></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 11 寫作鷹架 -->
<section class="slide" data-slide="11" data-section="喚起行動">
  <div class="slide-inner">
    <div class="kicker accent2">寫作鷹架</div>
    <h2 class="slide-title">論點怎麼寫</h2>
    <p class="sub">一段好的「看法」，可以用這四步寫出來：</p>
    <div class="steps4">
      <div class="step4"><span class="sn">1</span><b>立場</b><p>我認為……<br>我支持／反對……</p></div>
      <div class="step4"><span class="sn">2</span><b>理由</b><p>因為……<br>第一……第二……</p></div>
      <div class="step4"><span class="sn">3</span><b>例子</b><p>例如……<br>根據文章……</p></div>
      <div class="step4"><span class="sn">4</span><b>結論</b><p>總而言之……<br>所以……</p></div>
    </div>
    <div class="model">範例：<b>我認為</b>可以吃人造鰻魚，<b>因為</b>它能保護瀕危的鰻魚。<b>例如</b>文章說，野生鰻魚十年來已經少了九成。<b>所以</b>我支持這種新科技。</div>
  </div>
</section>

<!-- 12 MG4 句型克漏字 -->
<section class="slide" data-slide="12" data-section="喚起行動">
  <div class="slide-inner">
    <div class="kicker accent2">句型練習 · 形成性評量 ④</div>
    <h2 class="slide-title">換你造句</h2>
    <p class="sub">選出正確的<b class="hl">連接詞</b>，把句子填完整。</p>
    <div class="mg" id="mg4">
      <div id="mg4-body"></div>
      <div class="mg-bar"><span id="mg4-score">完成 0 / 3</span><button class="mg-reset" onclick="initMG4()">重做</button></div>
    </div>
  </div>
</section>

<!-- 13 寫作任務 -->
<section class="slide" data-slide="13" data-section="喚起行動">
  <div class="slide-inner">
    <div class="kicker accent2">今天的寫作任務 · CTA</div>
    <h2 class="slide-title">今天的作文</h2>
    <div class="task">
      <div class="prompt">✍️ 你支持用「培植肉」（人造肉）來保護瀕危的動物嗎？<br>請寫出你的<b>看法</b>和<b>理由</b>。<span class="wc">150–250 字</span></div>
      <div class="rubric">
        <div class="rh">評分量表（每項 0–20，共 100）</div>
        <div class="rrow"><span>內容理解</span><span>讀懂文章重點</span></div>
        <div class="rrow"><span>科學概念</span><span>正確用到培植肉概念</span></div>
        <div class="rrow"><span>結構組織</span><span>立場→理由→例子→結論</span></div>
        <div class="rrow"><span>語言表達</span><span>句型、連接詞、生詞</span></div>
        <div class="rrow"><span>思辨應用</span><span>有自己的觀點與判斷</span></div>
      </div>
    </div>
    <div class="bottom13">
      <div class="extra">
        <div class="eh">📚 延伸閱讀（其他培植肉主題）</div>
        <ul>
          <li>歐盟首款含 26% 培養肉主食犬糧</li>
          <li>新加坡上市 12 款培養肉寵物食品</li>
          <li>日本完成 200 公升培植肉放大測試</li>
          <li>亞洲首款培養肉寵物食品獲核准</li>
          <li>瑪氏啟動替代蛋白與油脂新創計畫</li>
        </ul>
      </div>
      <div class="cta">完成後，用 <b>LINE</b> 把作文傳給老師，<br>輸入「<b>批改</b>」就能得到分數與建議！</div>
    </div>
  </div>
</section>

<script>
/* ---------------- 導航 ---------------- */
const slides=[...document.querySelectorAll('.slide')];
const total=slides.length; let cur=0;
const prog=document.getElementById('progress');
const sectag=document.getElementById('sectag');
const pinfo=document.getElementById('pageinfo');
function show(n){
  cur=Math.max(0,Math.min(total-1,n));
  slides.forEach((s,i)=>s.classList.toggle('active',i===cur));
  prog.style.width=((cur+1)/total*100)+'%';
  sectag.textContent='— '+slides[cur].dataset.section+' —';
  pinfo.innerHTML='<b>'+(cur+1)+'</b> / '+total;
}
function next(){show(cur+1);} function prev(){show(cur-1);}
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){e.preventDefault();next();}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();prev();}
  else if(e.key==='Home'){show(0);} else if(e.key==='End'){show(total-1);}
  else if(e.key.toLowerCase()==='f'){if(!document.fullscreenElement)document.documentElement.requestFullscreen();else document.exitFullscreen();}
});
document.addEventListener('click',e=>{
  if(e.target.closest('.mg,button,a,.cover-inner,th'))return;
  const x=e.clientX,w=window.innerWidth;
  if(x>w*0.62)next(); else if(x<w*0.38)prev();
});

/* ---------------- MG1 生詞配對 ---------------- */
const MG1=[
  {w:'瀕危',m:'快要消失、有滅絕的危險'},
  {w:'洄游',m:'魚在河流和海洋之間來回游'},
  {w:'捕撈',m:'用工具在水裡抓魚'},
  {w:'永續',m:'能長久維持，不會用光資源'},
  {w:'類器官',m:'實驗室培養、像真器官的組織'},
];
function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
let mg1sel=null,mg1done=0;
function initMG1(){
  mg1sel=null;mg1done=0;
  const wc=document.getElementById('mg1-words'),mc=document.getElementById('mg1-means');
  wc.innerHTML='';mc.innerHTML='';
  shuffle(MG1).forEach(o=>{const d=document.createElement('div');d.className='pair word';d.textContent=o.w;d.dataset.w=o.w;
    d.onclick=()=>{if(d.classList.contains('done'))return;document.querySelectorAll('#mg1-words .pair').forEach(p=>p.classList.remove('sel'));d.classList.add('sel');mg1sel=o.w;};wc.appendChild(d);});
  shuffle(MG1).forEach(o=>{const d=document.createElement('div');d.className='pair';d.textContent=o.m;d.dataset.w=o.w;
    d.onclick=()=>{if(d.classList.contains('done'))return;if(!mg1sel){return;}
      if(mg1sel===o.w){d.classList.add('done');const wd=document.querySelector('#mg1-words .pair[data-w="'+o.w+'"]');wd.classList.remove('sel');wd.classList.add('done');mg1sel=null;mg1done++;
        document.getElementById('mg1-score').textContent='完成 '+mg1done+' / 5'+(mg1done===5?'　🎉 全對！':'');}
      else{d.classList.add('bad');setTimeout(()=>d.classList.remove('bad'),350);}};mc.appendChild(d);});
  document.getElementById('mg1-score').textContent='完成 0 / 5';
}

/* ---------------- MG2 閱讀理解 ---------------- */
const MG2=[
  {q:'近十年，野生鰻魚的數量減少了多少？',o:['約 10–15%','約一半','約 90–95%','幾乎沒變'],a:2,f:'文章說野生鰻魚十年來減少了 90% 到 95%。'},
  {q:'開發人造鰻魚肉的 Forsea Foods 是哪一國的公司？',o:['日本','以色列','美國','新加坡'],a:1,f:'Forsea Foods 是以色列的食品新創公司。'},
  {q:'培植鰻魚肉主要是用什麼做出來的？',o:['鰻魚的胚胎幹細胞（類器官）','大豆蛋白','麵粉和澱粉','野生鰻苗'],a:0,f:'用受精卵的胚胎幹細胞做成類器官，再長出培植肉。'},
  {q:'下列哪一項「不是」這種培植肉的特點？',o:['不使用抗生素','不使用激素','組織像真的魚肉','需要大量野生鰻魚'],a:3,f:'培植肉正是為了「不再依賴野生鰻魚」而開發的。'},
];
let mg2score=0;
function initMG2(){
  mg2score=0;const b=document.getElementById('mg2-body');b.innerHTML='';
  MG2.forEach((it,qi)=>{
    const q=document.createElement('div');q.className='q';
    q.innerHTML='<div class="q-t"><span class="qn">Q'+(qi+1)+'</span>'+it.q+'</div>';
    const opts=document.createElement('div');opts.className='opts';
    it.o.forEach((t,oi)=>{const btn=document.createElement('button');btn.className='opt';btn.textContent=t;
      btn.onclick=()=>{if(opts.classList.contains('answered'))return;opts.classList.add('answered');
        opts.querySelectorAll('.opt').forEach(x=>x.classList.add('lock'));
        const fb=q.querySelector('.fb');
        if(oi===it.a){btn.classList.add('right');mg2score++;fb.className='fb good';fb.textContent='✓ 答對了！'+it.f;}
        else{btn.classList.add('wrong');opts.children[it.a].classList.add('right');fb.className='fb no';fb.textContent='✗ 正確答案已標綠。'+it.f;}
        document.getElementById('mg2-score').textContent='得分 '+mg2score+' / 4';};
      opts.appendChild(btn);});
    q.appendChild(opts);const fb=document.createElement('div');fb.className='fb';q.appendChild(fb);b.appendChild(q);
  });
  document.getElementById('mg2-score').textContent='得分 0 / 4';
}

/* ---------------- MG3 思辨立場 ---------------- */
const MG3R=['可以保護瀕危的鰻魚','比較環保、永續','不用抗生素和激素','我擔心食品安全','我喜歡傳統的味道','價格可能太貴'];
let mg3stance=null,mg3reasons=new Set();
function mg3render(){
  const stem=document.getElementById('mg3-stem');
  if(!mg3stance){stem.innerHTML='';return;}
  const rs=[...mg3reasons];
  stem.innerHTML='我<b>'+mg3stance+'</b>人造鰻魚，因為'+(rs.length?'<b>'+rs.join('</b>、<b>')+'</b>。':'……（再選幾個理由）');
}
function initMG3(){
  mg3stance=null;mg3reasons.clear();
  document.getElementById('mg3-after').classList.add('hidden');
  document.querySelectorAll('#mg3-stance button').forEach(b=>{b.classList.remove('on');
    b.onclick=()=>{document.querySelectorAll('#mg3-stance button').forEach(x=>x.classList.remove('on'));b.classList.add('on');mg3stance=b.dataset.s;document.getElementById('mg3-after').classList.remove('hidden');mg3render();};});
  const rc=document.getElementById('mg3-reasons');rc.innerHTML='';
  MG3R.forEach(t=>{const c=document.createElement('div');c.className='rchip';c.textContent=t;
    c.onclick=()=>{if(c.classList.toggle('on'))mg3reasons.add(t);else mg3reasons.delete(t);mg3render();};rc.appendChild(c);});
}

/* ---------------- MG4 句型克漏字 ---------------- */
const MG4=[
  {parts:['','保護快要消失的鰻魚，科學家用類器官技術養出鰻魚肉。'],o:['為了','雖然','可是'],a:0,
   filled:'<b>為了</b>保護快要消失的鰻魚，科學家用類器官技術養出鰻魚肉。'},
  {parts:['人造鰻魚肉','不使用抗生素，','比較健康。'],o:['不但…而且…','因為…所以…','雖然…但是…'],a:0,
   filled:'人造鰻魚肉<b>不但</b>不使用抗生素，<b>而且</b>比較健康。'},
  {parts:['','有些人覺得奇怪，','培植肉可能是更永續的選擇。'],o:['雖然…但是…','不但…而且…','一邊…一邊…'],a:0,
   filled:'<b>雖然</b>有些人覺得奇怪，<b>但是</b>培植肉可能是更永續的選擇。'},
];
let mg4done=0;
function initMG4(){
  mg4done=0;const b=document.getElementById('mg4-body');b.innerHTML='';
  MG4.forEach((it,qi)=>{
    const q=document.createElement('div');q.className='q';
    const cz=document.createElement('div');cz.className='cloze';
    cz.innerHTML='<span class="qn" style="color:var(--accent);font-weight:700;margin-right:8px">句'+(qi+1)+'</span>'+it.parts[0]+'<span class="blank">？</span>'+it.parts.slice(1).join('<span class="blank">？</span>');
    q.appendChild(cz);
    const opts=document.createElement('div');opts.className='opts';
    it.o.forEach((t,oi)=>{const btn=document.createElement('button');btn.className='opt';btn.textContent=t;
      btn.onclick=()=>{if(opts.classList.contains('answered'))return;
        if(oi===it.a){opts.classList.add('answered');opts.querySelectorAll('.opt').forEach(x=>x.classList.add('lock'));btn.classList.add('right');
          cz.className='cloze filled';cz.innerHTML='<span class="qn" style="color:var(--ok);font-weight:700;margin-right:8px">句'+(qi+1)+'</span>'+it.filled;
          mg4done++;document.getElementById('mg4-score').textContent='完成 '+mg4done+' / 3'+(mg4done===3?'　🎉':'');}
        else{btn.classList.add('wrong');setTimeout(()=>btn.classList.remove('wrong'),350);}};
      opts.appendChild(btn);});
    q.appendChild(opts);b.appendChild(q);
  });
  document.getElementById('mg4-score').textContent='完成 0 / 3';
}

/* ---------------- 表格 8 ---------------- */
const T8=[
  {co:'Forsea Foods',ct:'以色列',sf:'鰻魚'},
  {co:'Wildtype',ct:'美國',sf:'壽司級鮭魚'},
  {co:'Steakholder Foods',ct:'以色列',sf:'石斑魚'},
  {co:'Shiok Meats',ct:'新加坡',sf:'蝦、龍蝦、螃蟹'},
  {co:'Cell4Food',ct:'葡萄牙',sf:'章魚'},
];
let t8dir=1,t8key='co';
function renderT8(){
  const tb=document.querySelector('#tbl8 tbody');
  const rows=T8.slice().sort((a,b)=>a[t8key].localeCompare(b[t8key],'zh-Hant')*t8dir);
  tb.innerHTML=rows.map(r=>'<tr><td><b>'+r.co+'</b></td><td>'+r.ct+'</td><td>'+r.sf+'</td></tr>').join('');
}
document.querySelectorAll('#tbl8 th').forEach(th=>{th.onclick=()=>{const k=th.dataset.k;if(k===t8key)t8dir*=-1;else{t8key=k;t8dir=1;}renderT8();};});

/* ---------------- init ---------------- */
initMG1();initMG2();initMG3();initMG4();renderT8();show(0);
</script>
</body>
</html>'''

HTML = (HTML.replace("__COVER__", COVER)
            .replace("__CRISIS__", CRISIS)
            .replace("__LAB__", LAB)
            .replace("__CHOICE__", CHOICE))

out = os.path.join(BASE, "eel_cultivated_meat.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print("OK written:", out)
print("size: %.2f MB" % (len(HTML.encode("utf-8")) / 1048576))
