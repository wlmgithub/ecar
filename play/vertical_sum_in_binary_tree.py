
# https://stackoverflow.com/questions/14485255/vertical-sum-in-a-given-binary-tree

# https://codereview.stackexchange.com/questions/151208/vertical-sum-in-a-given-binary-tree

d = {}

def traverse(node, hd):
  if not node:
    return
  if not hd in d:
    d[hd] = 0
  d[hd] = d[hd] + node.value
  traverse(node.left, hd - 1)
  traverse(node.right, hd + 1)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""
    1
  /   \
 2     3
/ \   / \
4  5  6  7
"""

node7 = Node(70)
node6 = Node(60)
node5 = Node(50)
node4 = Node(40)
node3 = Node(3)
node2 = Node(2)

root = Node(1)
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

traverse(root, 0)



print(sorted(d.items()))

