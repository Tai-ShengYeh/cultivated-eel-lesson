# 人造鰻魚飯？｜培植肉 × 華文文獻閱讀與寫作

A2–B1 華語教學 SOIL HTML 簡報，以 foodNEXT 食力《培植肉拯救瀕危魚類　人造鰻魚飯預計2025年上市》改寫。
單一 `.html` 檔，4 張 AI 圖已 base64 內嵌，打開即用、可線上分享。

## 檔案

| 檔案 | 說明 |
|------|------|
| `eel_cultivated_meat.html` | **成品**（直接開啟或丟到 Firebase/GitHub Pages） |
| `build_deck.py` | **唯一 source of truth**。改內容請改這支再 `python build_deck.py` 重建，不要直接改 HTML |
| `slides/generated/*.png` | 4 張 FLUX 原圖（封面／瀕危鰻魚／培養實驗室／抉擇盤），備份用 |

## 重建

```bash
cd week_cultivated_eel
pip install Pillow          # 首次
python build_deck.py        # 產出 eel_cultivated_meat.html
```

## 22 頁結構（2 小時版 · SOIL 三段式）

引起動機：① 封面 ②🗳暖身投票 ③ 鰻魚要消失了（90–95%）④ 科技能救牠嗎
維持注意：⑤ 生詞表II ⑥🎮生詞配對 ⑦🎮生詞填空 ⑧ 文章地圖 ⑨ 精讀①危機 ⑩ 為什麼瀕危 ⑪ 精讀②解方 ⑫ 肉怎麼長出來 ⑬ 精讀③未來 ⑭ 各國人造海鮮（可排序表）⑮☕休息 ⑯🎮閱讀小測驗
喚起行動：⑰ 文化連結（鰻魚飯/越南）⑱ 口說活動（兩人訪問）⑲🎮你會吃嗎（思辨立場）⑳ 論點怎麼寫 ㉑🎮句型克漏字 ㉒ 寫作任務＋5維度量表

> 13 頁基礎版升級為 2 小時版（+暖身投票、課文精讀×3、生詞表II+生詞填空、文化/口說/休息頁）。

## 5 個內嵌 Minigame ＋ 暖身投票（形成性評量）

1. **暖身投票**（第2頁）— 你吃過鰻魚飯嗎？即時 poll，學生手機投票看長條圖（Supabase `poll_counts`+`poll_vote` RPC realtime）
2. **生詞配對**（第6頁）— 5 生詞配解釋，配對成功變綠、即時計分
3. **生詞填空**（第7頁）— 4 題選生詞填句（節節下降/仰賴/供不應求/胚胎幹細胞）
4. **閱讀小測驗**（第16頁）— 4 題選擇，答對綠／答錯標出正解＋回饋
5. **思辨立場**（第19頁）— 選立場→勾理由→自動組出可用於作文的句子
6. **句型克漏字**（第21頁）— 3 題連接詞（為了／不但…而且／雖然…但是），答對整句填入

## 操作

- `← →` 或 空白鍵翻頁；點畫面左右兩側翻頁
- `F` 全螢幕
- minigame 區點擊不會翻頁，可放心作答

## 課堂記錄（Supabase，比照 W14 麥當勞）

4 個遊戲完成時會寫一筆到 Supabase `interactions` 表（`course_code='cultivated-eel'`），
進 master dashboard。**純 insert 公開金鑰、連不上也不影響遊戲**。

- **分班**：網址加 `?session=班級`，例如
  `https://tai-shengyeh.github.io/cultivated-eel-lesson/?session=20260608_VN1`
  （不加時預設 `YYYYMMDD_VN1`）
- **學生**：自動產生匿名 `S-xxxxx`（存 localStorage）；可選 `?name=王小明` 帶名字
- **純投影/不記錄**：加 `?present=1`（或 `?nolog=1`）
- 左下角 `📡` 指示燈顯示連線/已記錄狀態
- 記錄欄位：`session_id / student_id / game_id / score / wrong / total / client_meta`
  （思辨立場存 `client_meta.stance`、生詞配對存 `client_meta.wrong`）

## 鏡像／延伸

- 可用 `slide-to-game-imports` 讀此 HTML 自動產 Kahoot/Wordwall/Gimkit 題庫
- 寫作任務搭配既有 LINE 批改 bot（輸入「批改」）與 Edcafe 5 維度量表
- 延伸閱讀：其他 5 篇培植肉主題（歐盟犬糧／新加坡寵食／日本量產／亞洲首款／瑪氏新創）
