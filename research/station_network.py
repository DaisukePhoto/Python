#インポート
import networkx as nx
import matplotlib.pyplot as plt
import csv
import numpy

# G = nx.read_edgelist('station_links.csv', nodetype=int)
G = nx.Graph()

csv_file = open("data/station_pos.csv", "r", encoding="utf_8", errors="", newline="")
f = csv.reader(csv_file)
pos={}
for i, row in enumerate(f):
  # 頂点を設定する．引数はid．
  G.add_node("st_%s" % row[2])
  # 座標を設定する．indexがid，代入している値が座標．
  pos["st_%s" % row[2]] = (int(row[1]), int(row[0]))

csv_file = open("data/station_links.csv", "r", encoding="utf_8", errors="", newline="")
f = csv.reader(csv_file)
for row in f:
  G.add_edge("st_%s" % row[0], "st_%s" % row[1])





# グラフオブジェクト（点と辺）に座標を関連付けて描画
nx.draw(G, pos, node_size=1)
# nx.draw_networkx_labels(G, pos, font_size=7)

#図を描画
plt.show()
