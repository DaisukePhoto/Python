import networkx as nx


def find_specific_attribute_node(G, attr, value):

    result = []

    d = nx.get_node_attributes(G, attr)

    for key, v in d.items():
        if(v == value):
            result.append(key)

    return result
