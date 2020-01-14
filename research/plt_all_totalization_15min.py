# coding: UTF-8

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import numpy as np
import sys

df_header = pd.read_csv('data/aggregate_people_15min_edogawa.csv')
print('data/aggregate_people_15min_edogawa.csv')

for i in range(1, 650):
  st_id = i
  data = df_header[ (st_id - 1) : st_id ]
  st_name = data.values.tolist()[0][0]

  left = ['~6', '6', '615', '630', '645', '7', '715', '730',
          '745', '8', '815', '830', '845', '9', '915', '930', '945',
          '10', '1015', '1030', '1045', '11', '1115', '1130', '1145'
        ]

  height = np.array([
            int(data.bef0600), int(data.af0600), int(data.af0615), int(data.af0630), int(data.af0645),
            int(data.af0700), int(data.af0715), int(data.af0730), int(data.af0745),
            int(data.af0800), int(data.af0815), int(data.af0830), int(data.af0845),
            int(data.af0900), int(data.af0915), int(data.af0930),int(data.af0945),
            int(data.af1000), int(data.af1015), int(data.af1030), int(data.af1045),
            int(data.af1100), int(data.af1115), int(data.af1130), int(data.af1145)
          ])

  plt.figure(figsize=(25, 10), dpi=80)
  plt.bar(left, height)

  # タイトルとラベルの設定
  plt.title('station id : ' + str(st_id))
  plt.xlabel('time range')
  plt.ylabel(('number of people'))

  # 軸の範囲を設定
  if st_name in ['新宿', '渋谷', '池袋', '東京', '上野', '品川', '秋葉原', '北千住', '赤羽','日暮里', '高田馬場']:
    plt.ylim(0, 100000)
  else:
    plt.ylim(0, 20000)

  plt.grid(which='major', axis='y', color='gray',linestyle='-')

  # figureをセーブする
  plt.savefig(f"figs/15min/edogawa/{st_id}_{st_name}.png")
  # ファイルをクローズする。
  plt.close()
