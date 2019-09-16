#インポート
import networkx as nx
import matplotlib.pyplot as plt
import csv

G = nx.read_edgelist('csv_roseneki.csv')

station_data = []

csv_file = open("csv_roseneki.csv", "r", encoding="utf_8", errors="", newline="")
f = csv.DictReader(csv_file)
for row in f:
    station_datum = {"id": row['station_id'], "lat": row['station_lat'], "lon": row['station_lon']}
    station_data.append(station_datum)

# グラフオブジェクトを作成．
# G = nx.MultiGraph()

pos = {}
for station in station_data:
  # 頂点を設定する．引数はid．
  G.add_node(station['id'])
  pos[station['id']] = (float(station['lat']) * 1000000, float(station['lon']) * 1000000)


#図の作成。figsizeは図の大きさ
plt.figure(figsize=(9, 7))


# グラフオブジェクト（点と辺）に座標を関連付けて描画
nx.draw(G, pos, node_size=1)
nx.draw_networkx_labels(G, pos, font_size=5)
#X軸Y軸を表示する設定
plt.axis('on')
#図を描画
plt.show()
