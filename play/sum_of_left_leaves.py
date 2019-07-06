
"""
404. Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.
    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

def print_tree_0(root):
    stack = [root]
    while stack:
        node = stack.pop(0)
        if node:
            print(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


def print_tree(root):
    if root:
        print(root.val)
    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)





def sum_of_left_leaves_0(root):

    def f(root, collect):
            res = 0

            if not root:
                return

            f(root.left, True)

            if collect and not root.left and not root.right:
                res += root.val
                return

            f(root.right, False)
            print('-----', res)
            return res

    return f(root, False)

# https://leetcode.com/problems/sum-of-left-leaves/discuss/324765/faster-than-96.33-of-Python3-easy-understanding-solution
def sum_of_left_leaves(root):

  def isLeaf(node):
        if node is None:
            return False

        if node.left is None and node.right is None:
            return True

        return False

  res=0
  if root:

        if isLeaf(root.left):
            res+=root.left.val
        else:
            res+=sum_of_left_leaves(root.left)

        res+=sum_of_left_leaves(root.right)

  return res

root = Node(3, Node(9), Node(20, Node(15), Node(7)))


print_tree(root)

print(sum_of_left_leaves(root))
