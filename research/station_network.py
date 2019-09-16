#インポート
import networkx as nx
import matplotlib.pyplot as plt
import csv
import json

# G = nx.read_edgelist('csv_roseneki_13.csv', nodetype=str)

station_data = []

csv_file = open("csv_roseneki_13.csv", "r",
                encoding="utf_8", errors="", newline="")
#リスト形式
# f = csv.reader(csv_file, delimiter=",", doublequote=True,
#                lineterminator="\r\n", quotechar='"', skipinitialspace=True)
f = csv.DictReader(csv_file)
for row in f:
    station_datum = {"name": row['station_name'], "lat": row['station_lat'], "lon": row['station_lon']}
    station_data.append(station_datum)
    
station_list = list(map(json.loads, set(map(json.dumps, station_data))))
print(station_list)


# グラフオブジェクトを作成．
G = nx.Graph()

pos = {}
for station in station_data:
  # 頂点を設定する．引数はid．
  G.add_node(station['name'])
  pos[station['name']] = (float(station['lat']) * 1000000, float(station['lon']) * 1000000)
  # print(pos)

#図の作成。figsizeは図の大きさ
plt.figure(figsize=(9, 7))


# グラフオブジェクト（点と辺）に座標を関連付けて描画
nx.draw(G, pos, node_size=0.1)
#X軸Y軸を表示しない設定
plt.axis('on')
#図を描画
plt.show()
