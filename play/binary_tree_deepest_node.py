import collections

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.data}'


def bfs(root):
    res = []
    to_visit = collections.deque([root])
    while to_visit:
        node = to_visit.popleft()
        res.append(node.data)
        if node.left:
            to_visit.append(node.left)
        if node.right:
            to_visit.append(node.right)
    return res[-1]



"""
    a
  b   c
d  e  f
      g

"""

d = Node('d')
e = Node('e')
g = Node('g')
f = Node('f', g)
b = Node('b', d, e)
c = Node('c', f)
a = Node('a', b, c)


print( bfs(a) )


