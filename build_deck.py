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
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
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
#supa{position:fixed;left:22px;bottom:34px;z-index:40;font-size:.66rem;letter-spacing:.04em;color:var(--accent);font-family:"JetBrains Mono",monospace;opacity:.85;}
#namegate{position:fixed;inset:0;z-index:200;display:none;align-items:center;justify-content:center;background:rgba(6,10,30,.86);backdrop-filter:blur(8px);}
.ng-card{background:var(--bg2);border:1px solid var(--line);border-radius:22px;padding:38px 42px;text-align:center;max-width:440px;width:90%;box-shadow:0 30px 80px rgba(0,0,0,.6);}
.ng-emoji{font-size:3.2rem;margin-bottom:10px;}
.ng-title{font-size:1.7rem;font-weight:900;margin-bottom:10px;}
.ng-sub{font-size:1rem;color:var(--ink2);margin-bottom:22px;line-height:1.7;}
.ng-sub span{color:var(--ink3);font-size:.88rem;}
#ng-input{width:100%;padding:15px 18px;border-radius:12px;border:1px solid var(--line);background:rgba(255,255,255,.06);color:var(--ink);font-size:1.15rem;text-align:center;outline:none;font-family:inherit;}
#ng-input:focus{border-color:var(--accent);}
#ng-btn{margin-top:18px;width:100%;padding:15px;border:none;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#06122b;font-size:1.15rem;font-weight:900;cursor:pointer;}
#ng-btn:hover{filter:brightness(1.08);}
.ng-foot{margin-top:16px;font-size:.78rem;color:var(--ink4);font-family:"JetBrains Mono",monospace;}

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
.cover-qr{position:absolute;right:64px;bottom:84px;z-index:3;display:flex;flex-direction:column;align-items:center;gap:9px;background:rgba(10,14,39,.5);backdrop-filter:blur(8px);border:1px solid rgba(0,212,255,.38);border-radius:18px;padding:18px 20px 15px;text-align:center;}
.cover-qr-card{background:#fff;border-radius:12px;padding:11px;line-height:0;box-shadow:0 10px 34px rgba(0,0,0,.45);}
.cover-qr-card img{width:190px;height:190px;display:block;}
.cover-qr-zh{color:var(--accent);font-weight:700;font-size:clamp(.95rem,1.35vw,1.16rem);}
.cover-qr-vi{color:var(--ink2);font-size:clamp(.8rem,1.05vw,.96rem);}
@media (max-width:1100px){.cover-qr{position:static;margin:18px auto 0;right:auto;bottom:auto;}.cover-qr-card img{width:150px;height:150px;}}

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

/* ---- 暖身投票 ---- */
.poll-q{font-size:clamp(1.1rem,1.9vw,1.5rem);font-weight:700;margin-bottom:18px;text-align:center;}
.poll-list{display:flex;flex-direction:column;gap:12px;max-width:680px;margin:8px auto 0;}
.poll-opt{border:1px solid var(--line);border-radius:14px;padding:14px 18px;background:rgba(255,255,255,.03);cursor:pointer;transition:.15s;}
.poll-opt:hover{border-color:var(--accent);}
.poll-opt.active{border-color:var(--accent2);background:rgba(255,0,110,.12);}
.poll-row{display:flex;justify-content:space-between;align-items:center;gap:12px;font-size:clamp(1rem,1.5vw,1.2rem);font-weight:700;}
.poll-pct{font-family:"JetBrains Mono",monospace;color:var(--accent);font-size:.92rem;display:none;font-weight:500;}
.poll-bar-wrap{display:none;margin-top:9px;height:9px;border-radius:6px;background:rgba(255,255,255,.08);overflow:hidden;}
.poll-bar-fill{height:100%;width:0;border-radius:6px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width .5s ease;}
.poll-foot{text-align:center;margin-top:14px;font-size:.85rem;color:var(--ink3);font-family:"JetBrains Mono",monospace;}
/* ---- 課文精讀 ---- */
.read-wrap{display:grid;grid-template-columns:1.5fr 1fr;gap:28px;align-items:start;}
.read-passage{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:14px;padding:22px 26px;font-size:clamp(1.05rem,1.65vw,1.4rem);line-height:2;color:var(--ink);}
.read-passage .hl{color:var(--accent);font-weight:700;} .read-passage .hl2{color:var(--warn);font-weight:700;}
.gloss{display:flex;flex-direction:column;gap:9px;}
.gloss-item{background:rgba(0,212,255,.06);border:1px solid rgba(0,212,255,.22);border-radius:10px;padding:10px 15px;}
.gloss-item b{color:var(--accent);font-size:clamp(1rem,1.35vw,1.16rem);} .gloss-item span{display:block;color:var(--ink2);font-size:clamp(.84rem,1.15vw,1rem);margin-top:2px;}
.read-say{margin-top:6px;font-size:clamp(.9rem,1.25vw,1.06rem);color:var(--accent2);line-height:1.6;}
/* ---- 生詞表 II ---- */
.voca2{display:grid;grid-template-columns:1fr 1fr;gap:4px 30px;}
.vrow{display:flex;gap:14px;align-items:baseline;padding:12px 0;border-bottom:1px solid var(--line);}
.vw{color:var(--accent);font-weight:700;font-size:clamp(1.05rem,1.5vw,1.3rem);white-space:nowrap;}
.vm{color:var(--ink2);font-size:clamp(.88rem,1.25vw,1.08rem);}
/* ---- 文化 / 口說 ---- */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:22px;}
.info-card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px 24px;}
.info-card h3{font-size:clamp(1.1rem,1.6vw,1.35rem);margin-bottom:12px;color:var(--accent);}
.info-card ul{list-style:none;display:flex;flex-direction:column;gap:10px;}
.info-card li{font-size:clamp(.95rem,1.4vw,1.18rem);line-height:1.7;color:var(--ink2);padding-left:20px;position:relative;}
.info-card li:before{content:"›";position:absolute;left:0;color:var(--accent2);font-weight:900;}
.speak-frames{display:flex;flex-direction:column;gap:12px;}
.frame{background:rgba(0,212,255,.07);border:1px dashed rgba(0,212,255,.4);border-radius:10px;padding:13px 18px;font-size:clamp(1rem,1.45vw,1.22rem);color:var(--ink);}
.frame b{color:var(--accent);}
/* ---- 休息 ---- */
.break-box{text-align:center;display:flex;flex-direction:column;align-items:center;gap:16px;}
.break-emoji{font-size:4.5rem;}
.break-timer{font-family:"JetBrains Mono",monospace;font-size:clamp(3rem,8vw,6rem);font-weight:800;color:var(--accent);line-height:1;}
.break-sub{font-size:clamp(1rem,1.55vw,1.32rem);color:var(--ink2);line-height:1.7;}
/* ---- MG5 三選一 ---- */
#mg5-body .opts{grid-template-columns:repeat(3,1fr);}
#mg5-body .q{margin-bottom:7px;}

@media (max-width:900px){
  .slide{padding:54px 24px;}
  .split,.split8,.split10,.task,.bottom13,.read-wrap,.two-col,.voca2{grid-template-columns:1fr;gap:20px;}
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
<div id="supa"></div>
<div id="namegate"><div class="ng-card">
  <div class="ng-emoji">🐟</div>
  <div class="ng-title">歡迎上課！</div>
  <div class="ng-sub">請輸入你的名字，老師才看得到你的參與。<br><span>Nhập tên của bạn để bắt đầu</span></div>
  <input id="ng-input" placeholder="你的名字 / Tên" maxlength="20" autocomplete="off">
  <button id="ng-btn" onclick="enterName()">開始上課 →</button>
  <div class="ng-foot">場次 · <span id="ng-session"></span></div>
</div></div>

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
    <div class="cover-qr">
      <div class="cover-qr-card"><img id="coverQR" alt="掃我加入課程 / Quét mã QR" src=""></div>
      <div class="cover-qr-zh">📱 手機掃我，一起上課</div>
      <div class="cover-qr-vi">Quét mã QR để tham gia</div>
    </div>
  </div>
</section>

<!-- 暖身投票 -->
<section class="slide" data-section="引起動機">
  <div class="slide-inner">
    <div class="kicker">暖身 · 即時投票</div>
    <h2 class="slide-title">你吃過鰻魚飯嗎？</h2>
    <p class="sub" style="text-align:center">拿手機掃封面 QR、點一個答案，看看全班的結果！</p>
    <div class="poll-list" id="poll">
      <div class="poll-opt" onclick="vote(0)"><div class="poll-row"><span>😋 常常吃</span><span class="poll-pct"></span></div><div class="poll-bar-wrap"><div class="poll-bar-fill"></div></div></div>
      <div class="poll-opt" onclick="vote(1)"><div class="poll-row"><span>🙂 吃過幾次</span><span class="poll-pct"></span></div><div class="poll-bar-wrap"><div class="poll-bar-fill"></div></div></div>
      <div class="poll-opt" onclick="vote(2)"><div class="poll-row"><span>🤔 沒吃過</span><span class="poll-pct"></span></div><div class="poll-bar-wrap"><div class="poll-bar-fill"></div></div></div>
      <div class="poll-opt" onclick="vote(3)"><div class="poll-row"><span>❓ 不知道那是什麼</span><span class="poll-pct"></span></div><div class="poll-bar-wrap"><div class="poll-bar-fill"></div></div></div>
    </div>
    <div class="poll-foot">已有 <span id="poll-total">0</span> 人投票</div>
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

<!-- 生詞表 II -->
<section class="slide" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker accent">生詞 · 再加幾個</div>
    <h2 class="slide-title">這些詞也要會</h2>
    <p class="sub">配合等一下的課文，先認識這幾個比較難的詞。</p>
    <div class="voca2">
      <div class="vrow"><span class="vw">胚胎幹細胞</span><span class="vm">能長成各種組織的細胞</span></div>
      <div class="vrow"><span class="vw">仰賴</span><span class="vm">依靠、依賴</span></div>
      <div class="vrow"><span class="vw">供不應求</span><span class="vm">東西太少，不夠賣</span></div>
      <div class="vrow"><span class="vw">節節下降</span><span class="vm">數量一直不斷地減少</span></div>
      <div class="vrow"><span class="vw">過度捕撈</span><span class="vm">抓太多，超過自然能恢復的量</span></div>
      <div class="vrow"><span class="vw">標榜</span><span class="vm">公開宣傳自己有某個優點</span></div>
    </div>
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

<!-- MG5 生詞克漏字 -->
<section class="slide" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker accent">生詞練習 · 形成性評量 ⑤</div>
    <h2 class="slide-title">生詞填填看</h2>
    <p class="sub">選出最適合的生詞，把句子填完整。</p>
    <div class="mg" id="mg5">
      <div id="mg5-body"></div>
      <div class="mg-bar"><span id="mg5-score">完成 0 / 4</span><button class="mg-reset" onclick="initMG5()">重做</button></div>
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

<!-- 精讀1 危機 -->
<section class="slide" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker accent">課文精讀 ① · 讀讀看</div>
    <h2 class="slide-title">原文：鰻魚的危機</h2>
    <div class="read-wrap">
      <div class="read-passage">鰻魚的繁殖過程相當複雜，牠們在河川中生長，成熟後<span class="hl">洄游</span>到海洋中產卵，一生<b>只產一次卵</b>。長年以來，鰻魚養殖幾乎完全<span class="hl">仰賴</span>野生<span class="hl">捕撈</span>鰻苗，導致自然資源<span class="hl2">過度消耗</span>，野生鰻苗數量<span class="hl2">節節下降</span>。</div>
      <div class="gloss">
        <div class="gloss-item"><b>洄游</b><span>在河流和海洋之間來回游</span></div>
        <div class="gloss-item"><b>仰賴</b><span>依靠、依賴</span></div>
        <div class="gloss-item"><b>節節下降</b><span>一直不斷地減少</span></div>
        <div class="read-say">🔊 跟老師唸一次，再用自己的話說：為什麼鰻魚越來越少？</div>
      </div>
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

<!-- 精讀2 解方 -->
<section class="slide" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker accent">課文精讀 ② · 讀讀看</div>
    <h2 class="slide-title">原文：科技的解方</h2>
    <div class="read-wrap">
      <div class="read-passage">Forsea Foods 利用鰻魚受精卵的<span class="hl">胚胎幹細胞</span>製成<span class="hl">類器官</span>，這些類器官可<b>自行生成</b>培植肉，組織結構<b>就如同真正的魚肉</b>。就像其他培植肉，這種鰻魚肉<span class="hl2">不使用抗生素或激素</span>。</div>
      <div class="gloss">
        <div class="gloss-item"><b>胚胎幹細胞</b><span>能長成各種組織的細胞</span></div>
        <div class="gloss-item"><b>類器官</b><span>實驗室培養、像真器官的組織</span></div>
        <div class="gloss-item"><b>自行生成</b><span>自己長出來</span></div>
        <div class="read-say">🔊 唸唸看，再回答：培植肉跟野生鰻魚有什麼不一樣？</div>
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

<!-- 精讀3 未來 -->
<section class="slide" data-section="維持注意">
  <div class="slide-inner">
    <div class="kicker accent">課文精讀 ③ · 讀讀看</div>
    <h2 class="slide-title">原文：不只有鰻魚</h2>
    <div class="read-wrap">
      <div class="read-passage">美國的 Wildtype <span class="hl">標榜</span>能培植出「壽司級鮭魚」；以色列的 Steakholder Foods 正培植石斑魚肉；新加坡的 Shiok Meats 則<b>瞄準</b>蝦子、龍蝦和螃蟹。這或許是更<span class="hl">永續</span>的選擇，<b>但消費者是否接受，仍是一大<span class="hl2">考驗</span></b>。</div>
      <div class="gloss">
        <div class="gloss-item"><b>標榜</b><span>公開宣傳自己有某個優點</span></div>
        <div class="gloss-item"><b>瞄準</b><span>把目標放在……</span></div>
        <div class="gloss-item"><b>考驗</b><span>困難的測試、挑戰</span></div>
        <div class="read-say">🔊 哪一種人造海鮮你最想試試？為什麼？</div>
      </div>
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

<!-- 休息 -->
<section class="slide" data-section="維持注意">
  <div class="slide-inner center">
    <div class="break-box">
      <div class="break-emoji">☕</div>
      <div class="kicker">休息一下 · Nghỉ giải lao</div>
      <div class="break-timer" id="breakTimer">10:00</div>
      <div class="break-sub">十分鐘後我們繼續：讀懂了嗎 → 你會吃嗎 → 寫作。<br>回來前先想一想：<b>你會不會吃人造鰻魚？</b></div>
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

<!-- 文化連結 -->
<section class="slide" data-section="喚起行動">
  <div class="slide-inner">
    <div class="kicker accent2">文化連結</div>
    <h2 class="slide-title">鰻魚飯與你</h2>
    <div class="two-col">
      <div class="info-card">
        <h3>🍱 鰻魚飯的文化</h3>
        <ul>
          <li>在日本，夏天最熱的「土用丑日」要吃鰻魚補體力。</li>
          <li>鰻魚飯是很多亞洲國家的高級料理，價格不便宜。</li>
          <li>正因為大家都愛吃，野生鰻魚才被抓得越來越少。</li>
        </ul>
      </div>
      <div class="info-card">
        <h3>🇻🇳 換你想一想</h3>
        <ul>
          <li>你或你的家人，吃過鰻魚嗎？什麼時候？</li>
          <li>在越南，有沒有快要消失、越來越少的食物或動物？</li>
          <li>如果牠快不見了，你希望用科技把牠「養出來」嗎？</li>
        </ul>
      </div>
    </div>
    <p class="note" style="text-align:center;margin-top:14px">把你的答案記下來——等一下寫作可以用！</p>
  </div>
</section>

<!-- 口說活動 -->
<section class="slide" data-section="喚起行動">
  <div class="slide-inner">
    <div class="kicker accent2">口說活動 · 兩人一組</div>
    <h2 class="slide-title">問問你的同學</h2>
    <p class="sub">兩個人一組，輪流問和答。請用完整的句子回答。</p>
    <div class="speak-frames">
      <div class="frame">A：你會吃人造鰻魚嗎？<b>為什麼</b>？</div>
      <div class="frame">B：我（會／不會）吃，<b>因為</b>……</div>
      <div class="frame">A：你覺得人造肉<b>最大的好處</b>是什麼？</div>
      <div class="frame">B：我覺得最大的好處是……，<b>例如</b>……</div>
    </div>
    <p class="note" style="text-align:center;margin-top:14px">說完換你寫：把剛剛說的，等一下寫進作文。</p>
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
      <div class="cta">寫好後貼到 <b>Edcafe</b> 作業，<br>系統會<b>自動批改</b>，馬上給你分數與建議！</div>
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
  if(slides[cur].querySelector('#breakTimer'))startBreak();
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

/* ---------------- Supabase 記錄（insert-only 公開金鑰；?session=班級 分班；連不上不影響遊戲）---------------- */
var SUPA_URL='https://qmldcjkllisvfgegkfsz.supabase.co';
var SUPA_ANON='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFtbGRjamtsbGlzdmZnZWdrZnN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzExMjM5ODYsImV4cCI6MjA4NjY5OTk4Nn0.Bfj0W7HN_n_vcjGe5502Chamk0YV-de8a0fxF4Nyczk';
var _qs=new URLSearchParams(location.search);
var SESSION=_qs.get('session')||(new Date().toISOString().slice(0,10).replace(/-/g,'')+'_VN1');
var PRESENT=_qs.get('present')==='1'||_qs.get('nolog')==='1';
var STU_NAME=_qs.get('name')||localStorage.getItem('eel_student_name')||null;
if(_qs.get('name'))localStorage.setItem('eel_student_name',_qs.get('name'));
var STU_ID=localStorage.getItem('eel_student_id');
if(!STU_ID){STU_ID='S-'+Math.random().toString(36).slice(2,8).toUpperCase();localStorage.setItem('eel_student_id',STU_ID);}
var _logged={};
function recordGame(game_id,game_name,score,wrong,total,meta){
  if(PRESENT||_logged[game_id])return; _logged[game_id]=true;
  try{fetch(SUPA_URL+'/rest/v1/interactions',{method:'POST',
    headers:{'apikey':SUPA_ANON,'Authorization':'Bearer '+SUPA_ANON,'Content-Type':'application/json','Prefer':'return=minimal'},
    body:JSON.stringify({course_code:'cultivated-eel',session_id:SESSION,student_id:STU_ID,student_name:STU_NAME,game_id:game_id,game_name:game_name,score:score,wrong:wrong,total:total,duration_ms:0,client_meta:meta||{}})
  }).then(function(r){var se=document.getElementById('supa');if(se&&r.ok)se.textContent='📡 已記錄 · '+SESSION;}).catch(function(e){console.warn('supa log failed',e);});}catch(e){}
}
/* ---- Supabase realtime client（給暖身投票用）---- */
var sb=null,RT_OK=false;
try{ if(typeof supabase!=='undefined'){ sb=supabase.createClient(SUPA_URL,SUPA_ANON); RT_OK=true; } }catch(e){}

/* ---- 暖身即時投票（沿用 poll_counts 表 + poll_vote RPC）---- */
var POLL_KEY=SESSION+'_eelwarmup';
var myVote=localStorage.getItem('eel_vote_'+POLL_KEY); myVote=(myVote===null)?null:parseInt(myVote);
var pv=[0,0,0,0];
function renderPollBars(c){
  var total=c.reduce(function(a,b){return a+b;},0);
  var pt=document.getElementById('poll-total'); if(pt)pt.textContent=total;
  document.querySelectorAll('#poll .poll-opt').forEach(function(o,j){
    var wrap=o.querySelector('.poll-bar-wrap'),fill=o.querySelector('.poll-bar-fill'),pct=o.querySelector('.poll-pct');
    if(total>0){wrap.style.display='block';pct.style.display='block';}
    var p=total?Math.round(c[j]/total*100):0; fill.style.width=p+'%'; pct.textContent=p+'%（'+c[j]+'）';
    o.classList.toggle('active',myVote===j);
  });
}
function subscribePoll(){
  if(!RT_OK)return;
  sb.from('poll_counts').select('opt0,opt1,opt2,opt3').eq('session_key',POLL_KEY).maybeSingle().then(function(res){
    var d=res&&res.data; if(d)renderPollBars([d.opt0||0,d.opt1||0,d.opt2||0,d.opt3||0]);
  });
  sb.channel('poll_'+POLL_KEY).on('postgres_changes',{event:'*',schema:'public',table:'poll_counts',filter:'session_key=eq.'+POLL_KEY},function(payload){var r=payload.new||{};renderPollBars([r.opt0||0,r.opt1||0,r.opt2||0,r.opt3||0]);}).subscribe();
}
function vote(i){
  if(PRESENT)return; var prev=myVote; if(prev===i)return;
  myVote=i; localStorage.setItem('eel_vote_'+POLL_KEY,i);
  if(RT_OK){ sb.rpc('poll_vote',{p_session:POLL_KEY,p_old:(prev==null?-1:prev),p_new:i}).then(function(res){if(res&&res.error)console.warn('vote rpc',res.error);}); document.querySelectorAll('#poll .poll-opt').forEach(function(o,j){o.classList.toggle('active',j===i);}); }
  else{ if(prev!=null&&pv[prev]>0)pv[prev]--; pv[i]++; renderPollBars(pv); }
}

/* ---- 休息倒數 10 分鐘 ---- */
var breakStarted=false;
function startBreak(){
  if(breakStarted)return; var el=document.getElementById('breakTimer'); if(!el)return; breakStarted=true;
  var t=600;
  var iv=setInterval(function(){ t--; var m=Math.floor(t/60),s=t%60; el.textContent=m+':'+(s<10?'0':'')+s; if(t<=0){clearInterval(iv);el.textContent='時間到 🔔';} },1000);
}

/* ---- 上課輸入名字（老師 present 模式跳過；學生輸入後遊戲/投票紀錄帶名字）---- */
function enterName(){var v=document.getElementById('ng-input').value.trim();if(!v){document.getElementById('ng-input').focus();return;}STU_NAME=v;localStorage.setItem('eel_student_name',v);var g=document.getElementById('namegate');if(g)g.style.display='none';}
function maybeGate(){var g=document.getElementById('namegate');if(!g)return;var s=document.getElementById('ng-session');if(s)s.textContent=SESSION;if(!PRESENT && !STU_NAME){g.style.display='flex';var i=document.getElementById('ng-input');if(i){i.addEventListener('keydown',function(e){if(e.key==='Enter')enterName();});setTimeout(function(){i.focus();},150);}}}

(function(){var se=document.getElementById('supa');if(se)se.textContent=PRESENT?'':('📡 連線中 · '+SESSION);
  var join=location.origin+location.pathname+'?session='+encodeURIComponent(SESSION);
  var q=document.getElementById('coverQR');if(q)q.src='https://api.qrserver.com/v1/create-qr-code/?size=360x360&margin=12&data='+encodeURIComponent(join);
})();

/* ---------------- MG1 生詞配對 ---------------- */
const MG1=[
  {w:'瀕危',m:'快要消失、有滅絕的危險'},
  {w:'洄游',m:'魚在河流和海洋之間來回游'},
  {w:'捕撈',m:'用工具在水裡抓魚'},
  {w:'永續',m:'能長久維持，不會用光資源'},
  {w:'類器官',m:'實驗室培養、像真器官的組織'},
];
function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
let mg1sel=null,mg1done=0,mg1wrong=0;
function initMG1(){
  mg1sel=null;mg1done=0;mg1wrong=0;
  const wc=document.getElementById('mg1-words'),mc=document.getElementById('mg1-means');
  wc.innerHTML='';mc.innerHTML='';
  shuffle(MG1).forEach(o=>{const d=document.createElement('div');d.className='pair word';d.textContent=o.w;d.dataset.w=o.w;
    d.onclick=()=>{if(d.classList.contains('done'))return;document.querySelectorAll('#mg1-words .pair').forEach(p=>p.classList.remove('sel'));d.classList.add('sel');mg1sel=o.w;};wc.appendChild(d);});
  shuffle(MG1).forEach(o=>{const d=document.createElement('div');d.className='pair';d.textContent=o.m;d.dataset.w=o.w;
    d.onclick=()=>{if(d.classList.contains('done'))return;if(!mg1sel){return;}
      if(mg1sel===o.w){d.classList.add('done');const wd=document.querySelector('#mg1-words .pair[data-w="'+o.w+'"]');wd.classList.remove('sel');wd.classList.add('done');mg1sel=null;mg1done++;
        document.getElementById('mg1-score').textContent='完成 '+mg1done+' / 5'+(mg1done===5?'　🎉 全對！':'');
        if(mg1done===5)recordGame('cultivated_eel_vocab_match','生詞配對',5,mg1wrong,5,{wrong:mg1wrong});}
      else{mg1wrong++;d.classList.add('bad');setTimeout(()=>d.classList.remove('bad'),350);}};mc.appendChild(d);});
  document.getElementById('mg1-score').textContent='完成 0 / 5';
}

/* ---------------- MG2 閱讀理解 ---------------- */
const MG2=[
  {q:'近十年，野生鰻魚的數量減少了多少？',o:['約 10–15%','約一半','約 90–95%','幾乎沒變'],a:2,f:'文章說野生鰻魚十年來減少了 90% 到 95%。'},
  {q:'開發人造鰻魚肉的 Forsea Foods 是哪一國的公司？',o:['日本','以色列','美國','新加坡'],a:1,f:'Forsea Foods 是以色列的食品新創公司。'},
  {q:'培植鰻魚肉主要是用什麼做出來的？',o:['鰻魚的胚胎幹細胞（類器官）','大豆蛋白','麵粉和澱粉','野生鰻苗'],a:0,f:'用受精卵的胚胎幹細胞做成類器官，再長出培植肉。'},
  {q:'下列哪一項「不是」這種培植肉的特點？',o:['不使用抗生素','不使用激素','組織像真的魚肉','需要大量野生鰻魚'],a:3,f:'培植肉正是為了「不再依賴野生鰻魚」而開發的。'},
];
let mg2score=0,mg2answered=0;
function initMG2(){
  mg2score=0;mg2answered=0;const b=document.getElementById('mg2-body');b.innerHTML='';
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
        document.getElementById('mg2-score').textContent='得分 '+mg2score+' / 4';
        mg2answered++;if(mg2answered===4)recordGame('cultivated_eel_reading_quiz','閱讀小測驗',mg2score,4-mg2score,4,{});};
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
    b.onclick=()=>{document.querySelectorAll('#mg3-stance button').forEach(x=>x.classList.remove('on'));b.classList.add('on');mg3stance=b.dataset.s;document.getElementById('mg3-after').classList.remove('hidden');mg3render();recordGame('cultivated_eel_stance','思辨立場',0,0,1,{stance:mg3stance});};});
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
          mg4done++;document.getElementById('mg4-score').textContent='完成 '+mg4done+' / 3'+(mg4done===3?'　🎉':'');
          if(mg4done===3)recordGame('cultivated_eel_cloze','句型克漏字',3,0,3,{});}
        else{btn.classList.add('wrong');setTimeout(()=>btn.classList.remove('wrong'),350);}};
      opts.appendChild(btn);});
    q.appendChild(opts);b.appendChild(q);
  });
  document.getElementById('mg4-score').textContent='完成 0 / 3';
}

/* ---------------- MG5 生詞克漏字 ---------------- */
var MG5=[
  {q:'野生鰻魚的數量越來越少，可以說數量＿＿＿。',o:['節節下降','供不應求','胚胎幹細胞'],a:0},
  {q:'以前養鰻魚幾乎完全＿＿＿野生的小鰻魚。',o:['標榜','仰賴','洄游'],a:1},
  {q:'鰻魚太受歡迎、常常＿＿＿，所以價格很高。',o:['供不應求','過度捕撈','永續'],a:0},
  {q:'科學家用受精卵的＿＿＿，做成類器官。',o:['胚胎幹細胞','適口性','洄游'],a:0},
];
var mg5done=0;
function initMG5(){
  mg5done=0;var b=document.getElementById('mg5-body');b.innerHTML='';
  MG5.forEach(function(it,qi){
    var q=document.createElement('div');q.className='q';
    q.innerHTML='<div class="q-t"><span class="qn">'+(qi+1)+'</span>'+it.q+'</div>';
    var opts=document.createElement('div');opts.className='opts';
    it.o.forEach(function(t,oi){var btn=document.createElement('button');btn.className='opt';btn.textContent=t;
      btn.onclick=function(){if(opts.classList.contains('answered'))return;
        if(oi===it.a){opts.classList.add('answered');opts.querySelectorAll('.opt').forEach(function(x){x.classList.add('lock');});btn.classList.add('right');mg5done++;document.getElementById('mg5-score').textContent='完成 '+mg5done+' / 4'+(mg5done===4?'　🎉':'');if(mg5done===4)recordGame('cultivated_eel_vocab_fill','生詞填空',4,0,4,{});}
        else{btn.classList.add('wrong');setTimeout(function(){btn.classList.remove('wrong');},350);}};
      opts.appendChild(btn);});
    q.appendChild(opts);b.appendChild(q);
  });
  document.getElementById('mg5-score').textContent='完成 0 / 4';
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
/* 深層連結：網址加 #p4 可直接跳到第 4 頁（供越南班週課索引連到指定段落）*/
function gotoHash(){var m=(location.hash||'').match(/p(\d+)/);if(m){var n=+m[1];if(n>=1&&n<=total)show(n-1);}}
window.addEventListener('hashchange',gotoHash);
initMG1();initMG2();initMG3();initMG4();initMG5();renderT8();subscribePoll();maybeGate();show(0);gotoHash();
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
