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
export_list = [] #出力を保存するリスト

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
# メーカー名/車種名を取得
makers = soup.find_all("a", "js_makerMenu", href="#")
cartypes = soup.find_all("a", class_="js_makerMenu", href=re.compile(r"javascript:void"))
row_index = 0

skip_list = ["こだわらない","国産車その他","輸入車その他"] # 除外する項目

r = re.compile("[A-Z]{2}") #任意の連続する２つのアルファベット == maker_code

for maker in makers:
  #メーカーコードの取得
  maker_code = r.findall("%s" %maker)

  # テキスト部分の抽出
  maker = maker.text
  # 正規表現で余分なものを取る
  maker = re.sub(r'\(\d*\)', "", maker) #(数字)
  maker = re.sub(r'\s', "", maker) #空白

  #除外項目をスキップ
  if not maker in skip_list:
    export_list.append([])

    export_list[row_index].append(str(row_index+1))
    export_list[row_index].append(maker)
    export_list[row_index].append(maker_code[0])

    row_index += 1


for cartype in cartypes:
  #メーカーコードの取得
  maker_code = r.findall("%s" %cartype)

  # テキスト部分の抽出
  cartype = cartype.text

  # 正規表現で余分なものを取る
  cartype = re.sub(r'\(\d*\)', "", cartype) #(数字)

  if cartype == "その他": continue

  export_list.append([])
  export_list[row_index].append(str(row_index+1))
  export_list[row_index].append(cartype)
  export_list[row_index].append(maker_code[2])

  for maker in export_list:
    #もしメーカーコードが一致すればarticle_tag_id(maker[0])を付与
    if maker_code[2] == maker[2]:
      export_list[row_index].append(maker[0])
      break

  row_index += 1


#csvに書き込み
with open('article_tags.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(export_list)


# ブラウザを終了
browser.quit()