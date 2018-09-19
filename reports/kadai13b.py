#kadai13b 16D8101021C 野口大輔 2018-1-15

import networkx as nx
import matplotlib.pyplot as plt

G=nx.read_edgelist("pert_kadai13b.txt",create_using=nx.DiGraph(),nodetype=int,data=[("weight",int)])
#print("グラフの辺情報：",G.edges(data=True))
"""
nx.draw_networkx(G)
plt.show()
"""
T=nx.topological_sort(G)
n=nx.number_of_nodes(G)
m=nx.number_of_edges(G)

print("グラフの点の数：",n)
print("グラフの辺の数：",m)
print("トポロジカルオーダー：",T)

"""
グラフの点の数： 9
グラフの辺の数： 13
トポロジカルオーダー： [1, 2, 4, 6, 3, 5, 7, 8, 9]
"""
