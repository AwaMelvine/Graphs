from graph import Graph
from util import Stack


def createGraph(ancestors):
    pass


def earliest_ancestor(ancestors, starting_node):
    gg = Graph()
    for person in ancestors:
        gg.add_vertex(person[1])
        gg.add_vertex(person[0])

    for person in ancestors:
        gg.add_edge(person[1], person[0])
    print(gg.vertices)

    stack, path = Stack(), []
    stack.push(starting_node)

    while stack:
        vertex = stack.pop()
        print(f"{vertex}-")
        if vertex in path:
            continue
        

        if vertex is None:
            if path[len(path) - 1] == starting_node:
                return -1
            else:
                return path[len(path) - 1]

        path.append(vertex)

        for adj_vertex in gg.vertices[vertex]:
            stack.push(adj_vertex)

    return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(f"ans: {earliest_ancestor(test_ancestors, 8)}")
