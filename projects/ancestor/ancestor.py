from graph import Graph
from util import Stack
from util import Stack, Queue


def createGraph(ancestors):
    pass


def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = {}
    current_level = 1
    ancestors_in_level = {}

    # build ancestor tree
    for relationship in ancestors:
        child = relationship[1]
        parent = relationship[0]

        if child in ancestor_graph:
            ancestor_graph[child].add(parent)
        else:
            ancestor_graph[child] = set()
            ancestor_graph[child].add(parent)

    if starting_node not in ancestor_graph:
        return -1

    stack = Stack()
    visited = set()
    stack.push([starting_node])
    path_list = []

    while stack.size() > 0:
        path = stack.pop()
        path_list.append(path)
        print(path_list)
        vertex = path[-1]
        print(f"vertex: {vertex}")

        if vertex not in visited and vertex in ancestor_graph:

            visited.add(vertex)

            for next_vert in ancestor_graph[vertex]:
                new_path = list(path)
                new_path.append(next_vert)
                stack.push(new_path)

    if len(path_list[-1]) > len(path_list[-2]):
        return path_list[-1][-1]

    elif len(path_list[-1]) == len(path_list[-2]) and len(path_list[-2]) > len(path_list[-3]):
        return min(path_list[-1][-1], path_list[-2][-1])

    else:
        return min(path_list[-1][-1], path_list[-2][-1], path_list[-3][-1])

    # gg = Graph()
    # for person in ancestors:
    #     gg.add_vertex(person[1])
    #     gg.add_vertex(person[0])

    # for person in ancestors:
    #     gg.add_edge(person[1], person[0])
    # print(gg.vertices)

    # stack, path = Stack(), []
    # stack.push(starting_node)

    # while stack:
    #     vertex = stack.pop()
    #     print(f"{vertex}-")
    #     if vertex in path:
    #         continue

    #     if vertex is None:
    #         if path[len(path) - 1] == starting_node:
    #             return -1
    #         else:
    #             return path[len(path) - 1]

    #     path.append(vertex)

    #     for adj_vertex in gg.vertices[vertex]:
    #         stack.push(adj_vertex)

    # return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(f"ans: {earliest_ancestor(test_ancestors, 8)}")
