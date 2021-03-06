import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

args = sys.argv
if len(args) == 1:
  st_id = int(input('駅のidを入力してください : '))
else:
  st_id = int(args[1])

df_header = pd.read_csv('data/aggregate_people_15min.csv')
data = df_header[ (st_id - 1) : st_id ]

left = ['~6', '6', '615', '630', '645', '7', '715', '730', 
        '745', '8', '815', '830', '845', '9', '915', '930', '945', 
        '10', '1015', '1030', '1045', '11', '1115', '1130', '1145']

height = np.array([int(data.bef0600), int(data.af0600), int(data.af0615), int(data.af0630), int(data.af0645), int(data.af0700), int(data.af0715), int(data.af0730),
                int(data.af0745), int(data.af0800), int(data.af0815), int(data.af0830), int(data.af0845), int(data.af0900), int(data.af0915), int(data.af0930),
                int(data.af0945), int(data.af1000), int(data.af1015), int(data.af1030), int(data.af1045), int(data.af1100), int(data.af1115), int(data.af1130), int(data.af1145)])

plt.figure(figsize=(12, 10), dpi=80)
plt.bar(left, height)

# タイトルとラベルの設定
plt.title('station id : ' + str(st_id))
plt.xlabel('time range')
plt.ylabel(('number of people'))

# 軸の範囲を設定
plt.ylim(0, 100000)

plt.show()
