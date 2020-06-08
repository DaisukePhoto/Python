import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import numpy as np
import sys

args = sys.argv
if len(args) == 1:
  st_id = int(input('駅のidを入力してください : '))
else:
  st_id = int(args[1])

df_header = pd.read_csv('data/aggregate_people_5min.csv')
data = df_header[ (st_id - 1) : st_id ]

left = ['6', '6A','6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K',
        '7', '7A','7B', '7C', '7D', '7E', '7F', '7G', '7H', '7I', '7J', '7K',
        '8', '8A','8B', '8C', '8D', '8E', '8F', '8G', '8H', '8I', '8J', '8K',
        '9', '9A','9B', '9C', '9D', '9E', '9F', '9G', '9H', '9I', '9J', '9K',
        '10', '10A','10B', '10C', '10D', '10E', '10F', '10G', '10H', '10I', '10J', '10K',
        '11', '11A','11B', '11C', '11D', '11E', '11F', '11G', '11H', '11I', '11J', '11K',
        ]

# height = np.array([
#           int(data.bef0600), int(data.af0600), int(data.af0605), int(data.af0610), int(data.af0615), int(data.af0620), int(data.af0625),
#           int(data.af0630), int(data.af0635), int(data.af0640), int(data.af0645), int(data.af0650), int(data.af0655),
#           int(data.af0700), int(data.af0705), int(data.af0710), int(data.af0715), int(data.af0720), int(data.af0725),
#           int(data.af0730), int(data.af0735), int(data.af0740), int(data.af0745), int(data.af0750), int(data.af0755),
#           int(data.af0800), int(data.af0805), int(data.af0810), int(data.af0815), int(data.af0820), int(data.af0825),
#           int(data.af0830), int(data.af0835), int(data.af0840), int(data.af0845), int(data.af0850), int(data.af0855),
#           int(data.af0900), int(data.af0905), int(data.af0910), int(data.af0915), int(data.af0920), int(data.af0925),
#           int(data.af0930), int(data.af0935), int(data.af0940), int(data.af0945), int(data.af0950), int(data.af0955),
#           int(data.af1000), int(data.af1005), int(data.af1010), int(data.af1015), int(data.af1020), int(data.af1025),
#           int(data.af1030), int(data.af1035), int(data.af1040), int(data.af1045), int(data.af1050), int(data.af1055),
#           int(data.af1100), int(data.af1105), int(data.af1110), int(data.af1115), int(data.af1120), int(data.af1125),
#           int(data.af1130), int(data.af1135), int(data.af1140), int(data.af1145), int(data.af1150), int(data.af1155),
#         ])

fuchu = [385,481,588,643,976,1420,1690,2809,2351,4863,5835,9376,12768,11078,17629,16693,25143,26540,37344,37685,46090,46226,45831,48105,48763,46884,49605,47173,46468,45147,39937,36657,36778,30683,30110,25275,24624,21052,15898,20069,16917,17920,17324,13714,13173,8458,10326,9662,9149,9203,7627,6983,6394,5476,4773,4562,3261,3126,2507,2280,2351,2080,2094,1932,1742,1070,3087,2414,2487,2673,1942,1983
]

normal = [438,700,681,592,800,1502,2156,2819,3565,4674,6848,10814,13755,13704,16932,21585,25509,31418,38340,44544,46353,46114,47759,48420,48528,47687,47205,49499,48550,40276,37209,37368,34387,29749,25814,24601,22505,19292,15890,17178,20514,17830,14919,12230,10968,8853,8735,10675,11212,8281,6419,5995,5478,6146,4541,2909,3072,2541,2054,2752,2292,1658,2010,1523,1839,1765,2384,3674,2855,1873,2130,1919
]

diff = []

for fu, nor in zip(fuchu, normal):
  diff.append(fu-nor)

print(len(diff), len(left))
height = np.array(diff)


plt.figure(figsize=(50, 30), dpi=70)
plt.bar(left, height)

# タイトルとラベルの設定
plt.title('station id : ' + str(st_id))
plt.xlabel('time range')
plt.ylabel(('difference of people'))
plt.ylim(-10000, 10000)
plt.bar(left, height, color='red')

# 軸の範囲を設定
# plt.ylim(0, 70000)
plt.grid(which='major', axis='y', color='gray',linestyle='-')
# plt.show()

# pdfファイルの初期化
name = f"station_{st_id}"
print(name)
# pp = PdfPages()

# figureをセーブする
plt.savefig(f"figs/5min/difference/{name}.png")

# pdfファイルをクローズする。
plt.close()
