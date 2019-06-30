import collections

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.data}'


def bfs_0(root):
    q = collections.deque([root])
    while q:
        node = q.popleft()
        print(node.data, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def bfs(root):
    q = [root]
    while q:
        node = q.pop(0)
        print(node.data, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def invert_rec(root):
    if root:
        root.left, root.right = \
            invert_rec(root.right), invert_rec(root.left)
    return root


def invert(root):
    q = [root]
    while q:
        node = q.pop(0)
        if node:
            #print(node.data, end=' ')
            node.left, node.right = node.right, node.left
            q.append(node.left)
            q.append(node.right)

    return root

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


bfs(a)
print()
bfs(invert(a))
print()


