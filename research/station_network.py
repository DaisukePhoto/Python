#インポート
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import csv
import numpy

def convert_pos(lon, lat):
  lon = int( ( float(lon) - 139000000 ) * 0.6 ) + 139000000
  lat = int( ( float(lat) - 35000000 ) * 0.6 ) + 35000000
  return lon, lat

G = nx.Graph()

csv_file = open("data/station_pos.csv", "r", encoding="utf_8", errors="", newline="")
f = csv.reader(csv_file)
pos = {}
for i, row in enumerate(f):
  # 頂点を設定する．引数はid．
  G.add_node("%s" % row[2])

  # 座標を設定する．indexがid，代入している値が座標．
  lon, lat = convert_pos(row[1], row[0])
  pos["%s" % row[2]] = (int(lon), int(lat))


csv_file = open("data/station_links.csv", "r", encoding="utf_8", errors="", newline="")
f = csv.reader(csv_file)
for row in f:
  G.add_edge("%s" % row[0], "%s" % row[1])

for i in range(2, 62):
  plt.figure(figsize=(18, 12), dpi=150)
  csv_file = open("data/people_5min_percentage.csv", "r", encoding="utf_8", errors="", newline="")
  f = csv.reader(csv_file)

  over_50 = []
  over_65 = []
  over_80 = []
  for row in f:
    if int(row[i]) >= 80:
      over_80.append(str(row[1]))
    elif int(row[i]) >= 65:
      over_65.append(str(row[1]))
    elif int(row[i]) >= 50:
      over_50.append(str(row[1]))


  # グラフオブジェクト（点と辺）に座標を関連付けて描画
  nx.draw(G, pos, node_size=8, node_color='yellowgreen', edge_color='white', weight=1)
  nx.draw(G, pos, nodelist=over_50, node_size=35, node_color='yellow')
  nx.draw(G, pos, nodelist=over_65, node_size=40, node_color='orange')
  nx.draw(G, pos, nodelist=over_80, node_size=50, node_color='red')

  #図を描画
  plt.axis('off')
  plt.savefig(f"figs_net/station_network_{i-1}.png")
  plt.close()
