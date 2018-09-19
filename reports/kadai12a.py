#kadai12a 16D8101021C 野口大輔　2017-12-18

import networkx as nx
import matplotlib.pyplot as plt
a=1
b=2
c=3
d=4
G=nx.Graph()
G.add_nodes_from([a,b,c,d])
G.add_edges_from([(a,b),(a,c),(a,d),(c,d)])

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
av=G.degree(a)
bv=G.degree(b)
cv=G.degree(c)
dv=G.degree(d)
print("各点の次数は｛'a':",av,",'b':",bv,",'c':",cv,",'d':",dv,"}")

nx.draw_networkx(G)
plt.show()


"""
(py361) [16D8101021C@ise31c ~]$ python kadai12a.py
各点の次数は｛'a': 3 ,'b': 1 ,'c': 2 ,'d': 2 }
"""
