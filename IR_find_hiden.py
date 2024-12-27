import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

class TMUCrawler:
    def __init__(self):
        self.base_url = "http://libir.tmu.edu.tw/handle/987654321"
        self.results = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_page_content(self, id_number):
        url = f"{self.base_url}/{id_number}"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.encoding = 'utf-8'
            
            if response.status_code == 200 and "無效的ID" not in response.text:
                return response.text
            return None
        except Exception as e:
            print(f"Error fetching ID {id_number}: {str(e)}")
            return None

    def check_content(self, html, include_texts):
        """檢查頁面內容是否包含任何指定文字"""
        if html is None:
            return True
        # 如果任何一個指定文字出現在頁面中，返回ture
        return any(text in html for text in include_texts)

    def crawl(self, start_id, end_id, exclude_texts):
        """按照ID順序爬取頁面"""
        for current_id in range(start_id, end_id + 1):
            print(f"Checking ID: {current_id}")
            
            html = self.get_page_content(current_id)
            
            if html and self.check_content(html, exclude_texts):
                url = f"{self.base_url}/{current_id}"
                self.results.append({
                    'id': current_id,
                    'url': url
                })
                print(f"Found valid page: {url}")
            
            #time.sleep(1)

    def save_results(self, filename='hiden_results.csv'):
        """保存結果到CSV文件"""
        df = pd.DataFrame(self.results)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Results saved to {filename}")
        print(f"Total valid URLs found: {len(self.results)}")

def get_include_texts():
    """獲取使用者輸入的指定文字列表"""
    include_texts = []
    print("請輸入要指定的文字（每行一個，輸入空行結束）：")
    while True:
        text = input().strip()
        if not text:  # 如果輸入空行，結束輸入
            break
        include_texts.append(text)
    return include_texts

def main():
    crawler = TMUCrawler()
    
    # 獲取使用者輸入的指定文字
    include_texts = get_include_texts()
    print(f"將指定包含以下文字的頁面：{include_texts}")
    
    # 設定爬取範圍
    start_id = int(input("請輸入起始ID: "))
    end_id = int(input("請輸入結束ID: "))
    
    # 開始爬蟲
    crawler.crawl(start_id, end_id, include_texts)
    
    # 保存結果
    crawler.save_results()

if __name__ == "__main__":
    main()