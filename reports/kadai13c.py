#kadai13c 16D8101021C 野口大輔 2018-1-15

import networkx as nx
import matplotlib.pyplot as plt

G=nx.read_edgelist("pert_kadai13c.txt",create_using=nx.DiGraph(),nodetype=int,data=[("weight",int)])
#print("グラフの辺情報：",G.edges(data=True))

#nx.draw_networkx(G)
#plt.show()

T=nx.topological_sort(G)
n=nx.number_of_nodes(G)
m=nx.number_of_edges(G)

print("グラフの点の数：",n)
print("グラフの辺の数：",m)
w_sum=0
print("トポロジカルオーダー：",T)
for i in range(1,n+1):
 A=G.in_edges(i,data=True)
 for e in A:
  #print(e)
  w=e[2]["weight"]
  #print(w)
  f=e[0]
  #print(f)

"""
トポロジカルオーダー： [1, 2, 4, 6, 3, 5, 8, 7, 9]
(1, 2, {'weight': 4})
w 4
f 1
(2, 3, {'weight': 2})
w 2
f 2
(6, 3, {'weight': 0})
0
6
(2, 4, {'weight': 6})
6
2
(3, 5, {'weight': 4})
4
3
(4, 6, {'weight': 2})
2
4
(5, 7, {'weight': 8})
8
5
(6, 7, {'weight': 10})
10
6
(8, 7, {'weight': 0})
0
8
(6, 8, {'weight': 13})
13
6
(7, 9, {'weight': 6})
6
7
(8, 9, {'weight': 4})
4
8
"""
