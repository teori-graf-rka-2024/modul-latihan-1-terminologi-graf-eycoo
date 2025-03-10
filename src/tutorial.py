import networkx as nx
from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5), (5, 6)]

g = create_graph(edges)

print(get_degree(g,2))

print(dfs_traversal(g,3))

print(bfs_traversal(g,1))

print(find_shortest_path(g,1,6))

visualize_graph(g)
