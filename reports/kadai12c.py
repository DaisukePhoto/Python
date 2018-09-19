#kadai12c 16D8101021C 野口大輔　2017-12-18

import networkx as nx
import matplotlib.pyplot as plt

"""
def search(goal, path):
    n = path[len(path) - 1]
    if n == goal:
        print(path)
    else:
        for x in adjacent[n]:
            if x not in path:
                path.append(x)
                search(goal, path)
                path.pop()

"""
G=nx.Graph()
G.add_nodes_from([1,2,3,4,5,6,7,8,9,10])
G.add_edges_from([(1,2),(1,8),(1,9),(2,3),(2,4),(4,5),(6,7),(6,10),(6,8),(8,9),(8,10)])

#nx.draw_networkx(G) #確認OK
#plt.show()

a=int(input("点a:"))
b=int(input("点b:"))
search(b, [a])

"""
spath=nx.shortest_path(G,source="a",target="b")
print(spath)
allpath=nx.all_simple_paths(G,source="a",target="b")
for path in allpath:
 print(path)
mst=nx.minimum_spanning_tree(G)
"""
