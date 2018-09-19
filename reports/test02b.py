#test02b 16D8101021C 野口大輔　2018-1-22

import networkx as nx

G=nx.read_edgelist("reg_graph.txt",nodetype=int,data=[("weight",int)])

print("グラフの点数：",nx.number_of_nodes(G))
print("グラフの辺数：",nx.number_of_edges(G))

v1=int(input("input v1:"))
v2=int(input("input v2:"))

sp=nx.shortest_path(G,source=v1,target=v2,weight="weight")
len=nx.shortest_path_length(G,source=v1,target=v2,weight="weight")

print("最短路",sp)
print("長さ",len)

"""
グラフの点数： 100
グラフの辺数： 300
input v1:1
input v2:29
最短路 [1, 28, 93, 29]
長さ 9


グラフの点数： 100
グラフの辺数： 300
input v1:20
input v2:69
最短路 [20, 60, 58, 67, 69]
長さ 6
"""
