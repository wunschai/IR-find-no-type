# TMU 圖書館論文爬蟲工具

這是一個用於爬取臺北醫學大學機構典藏系統 （http://libir.tmu.edu.tw） 論文資料的工具。包含兩個主要程式：
- `IR_find_notype.py`: 搜尋不包含特定文字的論文
- `IR_find_hiden.py`: 搜尋包含特定文字的論文
本工具使用 `requests` 和 `BeautifulSoup` 進行網頁爬蟲，並將結果儲存到 CSV 檔案中。
主要撰寫過程使用 ChatGPT 4o 和 VSCode 進行撰寫。感謝Cursor的幫助。

## 安裝需求

使用前請先安裝必要的 Python 套件：

```bash
pip install requests beautifulsoup4 pandas
```

## 使用說明

### IR_find_notype.py（排除特定文字的論文）

這個程式會搜尋並列出不包含指定文字的論文網址。

1. 執行程式：
    ```bash
    python IR_find_notype.py
    ```

2
2. 依照提示輸入：
   - 要排除的文字（每行一個，輸入空行結束）
   - 起始 ID
   - 結束 ID

3. 結果會儲存在 `notype_results.csv` 檔案中

### IR_find_hiden.py（搜尋包含特定文字的論文）

這個程式會搜尋並列出包含指定文字的論文網址。

1. 執行程式：
    ```bash
    python IR_find_hiden.py
    ```

2. 依照提示輸入：
   - 要搜尋的文字（每行一個，輸入空行結束）
   - 起始 ID
   - 結束 ID

3. 結果會儲存在 `hiden_results.csv` 檔案中

## 注意事項

- 請確保網路連線穩定，否則可能會導致爬蟲失敗。
- 請勿過度頻繁地使用爬蟲工具，以免對伺服器造成負擔。
- 請遵守相關法律法規，不得用於非法用途。    

## 範例使用

### 排除特定類型論文：
 ```
請輸入要排除的文字（每行一個，輸入空行結束）：
碩士 
博士 
學位
[按 Enter 鍵]
請輸入起始ID: 1
請輸入結束ID: 100
 ```
### 搜尋特定類型論文：
```
請輸入要指定的文字（每行一個，輸入空行結束）：
隱私
限制
[按 Enter 鍵]
請輸入起始ID: 1
請輸入結束ID: 100
```
