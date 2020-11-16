vertex_size = 5
graph_matrix = [[0 for col in range(vertex_size)] for row in range(vertex_size)]


def add_undirected_edge(v1, v2):
    graph_matrix[v1][v2] = 1
    graph_matrix[v2][v1] = 1


add_undirected_edge(0, 1)
add_undirected_edge(1, 2)
add_undirected_edge(1, 4)
add_undirected_edge(2, 3)
add_undirected_edge(2, 4)
add_undirected_edge(3, 4)

for row in graph_matrix:
    print(row)


