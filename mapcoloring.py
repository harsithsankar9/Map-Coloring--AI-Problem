import networkx as nx
import matplotlib.pyplot as plt

def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0
    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return
    print("Solution exists. Following are the assigned colors:")
    for i in range(len(graph)):
        print(f"Vertex {i + 1}: Color {color[i]}")

    # Convert adjacency matrix to edge list
    edges = []
    for i in range(len(graph)):
        for j in range(i + 1, len(graph[i])):
            if graph[i][j] == 1:
                edges.append((i, j))

    # Display the graph with assigned colors
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    node_colors = [f'C{c}' for c in color]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, node_size=200)
    plt.rcParams['figure.figsize'] = [10, 10]
    plt.show()

if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 4, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0]
    ]
    # Number of colors to be used
    m = 3

    graph_coloring(graph, m)
