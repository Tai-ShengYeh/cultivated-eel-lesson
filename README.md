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

## 13 頁結構（SOIL 三段式）

引起動機：① 封面 ② 鰻魚要消失了（90–95%）③ 科技能救牠嗎
維持注意：④🎮生詞配對 ⑤ 文章地圖 ⑥ 為什麼瀕危 ⑦ 肉怎麼長出來 ⑧ 各國人造海鮮（可排序表）⑨🎮閱讀小測驗
喚起行動：⑩🎮你會吃嗎（思辨立場）⑪ 論點怎麼寫 ⑫🎮句型克漏字 ⑬ 寫作任務＋5維度量表

## 4 個內嵌 Minigame（形成性評量）

1. **生詞配對**（第4頁）— 5 生詞配解釋，配對成功變綠、即時計分
2. **閱讀小測驗**（第9頁）— 4 題選擇，答對綠／答錯標出正解＋回饋，0–4 分
3. **思辨立場**（第10頁）— 選立場→勾理由→自動組出可用於作文的句子
4. **句型克漏字**（第12頁）— 3 題連接詞（為了／不但…而且／雖然…但是），答對整句填入

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
