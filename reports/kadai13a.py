#kadai13a 16D8101021C 野口大輔 2018-1-15

import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
G.add_edge(1,2,weight=2,name="b")
G.add_edge(1,4,weight=4,name="a")
G.add_edge(2,3,weight=5,name="e")
G.add_edge(4,3,weight=4,name="d")
G.add_edge(4,2,weight=0,name="c")

#print("グラフの辺情報：",G.edges(data=True))

nx.draw_networkx(G)
plt.show()


"""
グラフの辺情報： [(1, 2, {'weight': 2, 'name': 'b'}), (1, 4, {'weight': 4, 'name': 'a'}), (2, 3, {'weight': 5, 'name': 'e'}), (4, 3, {'weight': 4, 'name': 'd'}), (4, 2, {'weight': 0, 'name': 'c'})]
"""
