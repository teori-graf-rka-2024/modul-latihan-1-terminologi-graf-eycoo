import networkx as nx
import matplotlib.pyplot as plt

def create_graph(edges):
    
    return(nx.Graph(edges))

def get_degree(G, node):
    
    return G.degree[node]

def dfs_traversal(G, start):
    
    return list(nx.dfs_preorder_nodes(G,start))

def bfs_traversal(G, start):
    
    return list(nx.bfs_tree(G,start))

def find_shortest_path(G, source, target):
    
    return list(nx.shortest_path(G, source, target))

def visualize_graph(G):
    
    nx.draw(G)
    plt.show()
