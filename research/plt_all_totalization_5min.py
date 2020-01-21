import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import numpy as np
import sys

area_name = 'tokyo'
df_header = pd.read_csv(f"data/complete_5min/re_aggregate_5min_{area_name}.csv")

for i in range(1, 650):
  print(f"\r Progress : {i}/649", end = '')
  st_id = i
  data = df_header[ (st_id - 1) : st_id ]
  st_name = data.values.tolist()[0][0]

  left = ['~6', '6', '6A','6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K',
          '7', '7A','7B', '7C', '7D', '7E', '7F', '7G', '7H', '7I', '7J', '7K',
          '8', '8A','8B', '8C', '8D', '8E', '8F', '8G', '8H', '8I', '8J', '8K',
          '9', '9A','9B', '9C', '9D', '9E', '9F', '9G', '9H', '9I', '9J', '9K',
          '10', '10A','10B', '10C', '10D', '10E', '10F', '10G', '10H', '10I', '10J', '10K',
          '11', '11A','11B', '11C', '11D', '11E', '11F', '11G', '11H', '11I', '11J', '11K',
          ]

  height = np.array([
            int(data.bef0600), int(data.af0600), int(data.af0605), int(data.af0610), int(data.af0615), int(data.af0620), int(data.af0625),
            int(data.af0630), int(data.af0635), int(data.af0640), int(data.af0645), int(data.af0650), int(data.af0655),
            int(data.af0700), int(data.af0705), int(data.af0710), int(data.af0715), int(data.af0720), int(data.af0725),
            int(data.af0730), int(data.af0735), int(data.af0740), int(data.af0745), int(data.af0750), int(data.af0755),
            int(data.af0800), int(data.af0805), int(data.af0810), int(data.af0815), int(data.af0820), int(data.af0825),
            int(data.af0830), int(data.af0835), int(data.af0840), int(data.af0845), int(data.af0850), int(data.af0855),
            int(data.af0900), int(data.af0905), int(data.af0910), int(data.af0915), int(data.af0920), int(data.af0925),
            int(data.af0930), int(data.af0935), int(data.af0940), int(data.af0945), int(data.af0950), int(data.af0955),
            int(data.af1000), int(data.af1005), int(data.af1010), int(data.af1015), int(data.af1020), int(data.af1025),
            int(data.af1030), int(data.af1035), int(data.af1040), int(data.af1045), int(data.af1050), int(data.af1055),
            int(data.af1100), int(data.af1105), int(data.af1110), int(data.af1115), int(data.af1120), int(data.af1125),
            int(data.af1130), int(data.af1135), int(data.af1140), int(data.af1145), int(data.af1150), int(data.af1155),
          ])

  plt.figure(figsize=(25, 10), dpi=80)
  plt.bar(left, height)

  # タイトルとラベルの設定
  plt.title('station id : ' + str(st_id))
  plt.xlabel('time range')
  plt.ylabel(('number of people'))

  # 軸の範囲を設定
  if st_name in ['新宿', '渋谷', '池袋', '東京', '上野', '品川', '秋葉原', '北千住', '赤羽','日暮里']:
    plt.ylim(0, 55000)
  else:
    plt.ylim(0, 15000)

  plt.grid(which='major', axis='y', color='gray',linestyle='-')
  # plt.show()

  plt.savefig(f"figs/5min/{area_name}/{st_id}_{st_name}.png")

  # ファイルをクローズする。
  plt.close()
