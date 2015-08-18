__author__ = 'Allen'

graph = {'A': ['B'],
         'B': ['E', 'C'],
         'C': ['B', 'D', 'G'],
         'G': ['C'],
         'E': ['B'],
         'F': ['M', 'D', 'J'],
         'D': ['C', 'K', 'F', 'H'],
         'K': ['D'],
         'H': ['L', 'D', 'I', 'M'],
         'L': ['H'],
         'M': ['F', 'H', 'I'],
         'I': ['H', 'M', 'J', 'Z'],
         'J': ['F', 'I', 'Q', 'R'],
         'R': ['J', 'Q'],
         'Q': ['J', 'R'],
         'Z': ['I']


}

# DFS


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


# Non recursive


def find_new_path(graph, start, end):

    path = []
    stack = []
    visited = {}
    for node in graph.keys():
        visited[node] = False
    visited[start] = True
    stack.append(start)

    while stack:

        if stack[-1] == end:
                return stack

        # if children get one and push on stack
        child = get_child(graph, visited, stack[-1])
        if child:
            stack.append(child)
            visited[child] = True
        else:
            stack.pop()
    return path

# BFS


def find_best_path(graph, start, end):
    pass


def get_child(graph, visited, current):
    for node in graph[current]:
        if not visited[node]:
            return node

print str(find_path(graph, 'A', 'Z'))