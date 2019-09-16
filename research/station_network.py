#インポート
import networkx as nx
import matplotlib.pyplot as plt
import csv
import numpy

# G = nx.read_edgelist('station_links.csv', nodetype=int)
G = nx.Graph()

csv_file = open("station_pos.csv", "r", encoding="utf_8", errors="", newline="")
f = csv.reader(csv_file)
pos={}
for i, row in enumerate(f):
  # 頂点を設定する．引数はid．
  G.add_node("node%d" % i)
  # 座標を設定する．indexがid，代入している値が座標．
  pos["node%d" % i] = (int(row[0]), int(row[1]))

csv_file = open("station_links.csv", "r", encoding="utf_8", errors="", newline="")
f = csv.reader(csv_file)
for row in f:
  print("node%d" % int(row[0]), " node%d" % int(row[1]))
  G.add_edge("node%d" % int(row[0]), "node%d" % int(row[1]))





# グラフオブジェクト（点と辺）に座標を関連付けて描画
nx.draw(G, pos, node_size=1)

#図を描画
plt.show()
