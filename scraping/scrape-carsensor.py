from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from bs4 import BeautifulSoup
import re
import csv

# ブラウザーを起動
options = Options()
options.add_argument('--headless')
# Chromeのドライバを得る
browser = webdriver.Chrome(chrome_options=options)

url = "https://www.carsensor.net/usedcar/search.php?SKIND=1"
makers_list = [] #メーカーを保存するリスト
makers_code = [] #メーカーのコードを保存するリスト
cartype_list = [] #車種を保存するリスト

# 暗黙的な待機を最大3秒行う(サーバーの負担軽減)
browser.implicitly_wait(3)
# URLを読み込む
browser.get(url)
# htmlを取得
html = browser.page_source
# 「メーカー 車種」選択ボタンをクリック
browser.find_element_by_id('shashuAnc').click()
# HTMLを解析する --- (※3)
soup = BeautifulSoup(html, "html.parser")
# メーカー名を取得
makers = soup.find_all("a","js_makerMenu",href="#")
makers_count = 0
# 除外する項目
skip_list = ["こだわらない","国産車その他","輸入車その他"]

r = re.compile("[A-Z]{2}") #任意の連続する２つのアルファベット == maker_code

for maker in makers:
  #メーカーコードの取得
  maker_code = r.findall("%s" %maker)

  #テキスト部分の抽出
  maker = maker.text
  # 正規表現で余分なものを取る
  maker = re.sub(r'\(\d*\)', "", maker) #(数字)
  maker = re.sub(r'\s', "", maker) #空白
  #除外項目をスキップ
  if not maker in skip_list:
    makers_list.append([])
    makers_code.append([])

    makers_list[makers_count].append(str(makers_count+1))
    makers_list[makers_count].append(maker)
    makers_list[makers_count].append(maker_code[0])

    makers_code[makers_count].append(maker_code[0])

    makers_count += 1

    #車種名を取得する
    #



# #csvに書き込み(メーカー名)
# with open('index_makers.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator='\n')
#     writer.writerows(makers_list)

# 画面をキャプチャしてファイルに保存 --- (※4)
    #browser.save_screenshot("website.png")

# ブラウザを終了
browser.quit()