
import collections

graph = {
#    'C': ['D', 'B', 'A'],
    'C': ['A', 'B', 'D'],
    'E': ['C'],
    'D': ['B'],
    'B': ['A'],
    'A': [],
}

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'C'],
    'D': ['C'],
    'C': ['E'],
    'E': [],
}


res = []
seen = set()

def tsort(node):
    res.append(node)
    for n in graph[node]:
        if n not in seen:
            seen.add(n)
            tsort(n)

tsort('A')

print(res)

"""
def toposort(graph, node):
    res = []
    seen = set()

    def helper(node):
        for n in graph[node]:
            if n not in seen:
                seen.add(n)
                helper(n)
        res.insert(0,node)

    helper(node)

    return res

print(toposort(graph, 'E'))
"""


