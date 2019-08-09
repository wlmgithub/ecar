
###############
#
# https://codeforces.com/blog/entry/16823
#
###############

# https://www.python.org/doc/essays/graphs/

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

graph = {
    'C': ['D', 'B', 'A'],
#    'C': ['A', 'B', 'D'],
    'E': ['C'],
    'D': ['B'],
    'B': ['A'],
    'A': [],
}


def find_path(graph, start, end, path=None):
    if path is None:
        path = []
    path += [start]

    if start == end:
        return path
    if start not in graph:
        return
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return




# https://stackoverflow.com/questions/47192626/deceptively-simple-implementation-of-topological-sorting-in-python

def iterative_topological_sort(graph, start):
    seen = set()
    stack = []    # path variable is gone, stack and order are new
    order = []    # order will be in reverse order at first
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v) # no need to append to path any more
            q.extend(graph[v])

            while stack and v not in graph[stack[-1]]: # new stuff here!
                order.append(stack.pop())
            stack.append(v)

    return stack + order[::-1]   # new return value!



def recursive_topological_sort(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.insert(0, node)              # this line replaces the result.append line

    recursive_helper(node)
    return result

# https://codeforces.com/blog/entry/16823
def dfs(graph,s):
    stack=[]
    visited=[]
    stack=[s]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            stack=stack+graph[node]
    return visited


print(graph)

print('****** find_path: ')
print(find_path(graph, 'E', 'A'))

print('****** iterative_topological_sort: ')
print(iterative_topological_sort(graph, 'E'))

print('****** recursive_topological_sort: ')
print(recursive_topological_sort(graph, 'E'))

print('****** codeforce dfs: ')
print(dfs(graph, 'E'))
