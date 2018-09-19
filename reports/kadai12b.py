#kadai12b 16D8101021C 野口大輔　2017-12-18

import networkx as nx
import matplotlib.pyplot as plt

G=nx.read_edgelist("facebook_edge.txt",nodetype=int)
#nx.write_edgelist(G,"new_filename.txt")
G2=nx.read_adjlist("facebook_adj.txt",nodetype=int)

print("ファイル名　facebook_adj.txt")
print("点数:",nx.number_of_nodes(G))
print("辺数:",nx.number_of_edges(G))
print("ファイル名　facebook_edge.txt")
print("点数:",nx.number_of_nodes(G2))
print("辺数:",nx.number_of_edges(G2))

"""
(py361) [16D8101021C@ise31c ~]$ python kadai12b.py
ファイル名　facebook_adj.txt
点数: 4039
辺数: 88234
ファイル名　facebook_edge.txt
点数: 4039
辺数: 88234
"""

#参考
#print(G.nodes())
#print(G.edges())

"""
n=nx.number_of_nodes(G)
print(n) #4
m=nx.number_of_edges(G)
print(m) #4
D=nx.degree(G)
print(D) #{1: 3, 2: 1, 3: 2, 5: 2}
Dv=nx.degree(G).values()
print(Dv) #dict_values([3, 1, 2, 2])
dv=G.degree(a)
print(dv) #3
"""
"""
nx.draw_networkx(G)
plt.show()
"""
