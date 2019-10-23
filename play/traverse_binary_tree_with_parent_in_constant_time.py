# Suppose you are given a binary tree where each node has a pointer to its
# parent, left and right children, and an integer value. You want to print the
# value at each node exactly once using O(1) memory. Design and implement an
# algorithm to do this.
#
# Example tree:
#       5
#      / \
#     2   6
#    / \   \
#   1   3   8
#          /
#         7




# 5 2 1 3 6 8 7
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left

        if self.left is not None:
            self.left.parent = self

        self.right = right

        if self.right is not None:
            self.right.parent = self

        self.parent = None


def traverse(root):

    if root:
        yield(root.val)
        traverse(root.left)
        traverse(root.right)

def print_tree(root):
    node = root
    while node:
        if node.left is None and node.right is None:
            # node is leaf
            print(node.val)

        if node.left is not None:
            print(node.left.val)
            node = node.left
        else:
            node = node.parent


        if node.right is not None:
            print(node.right.val)
            node = node.right
        else:
            node = node.parent







t1 = Node(5,
    Node(2,
        Node(1),
        Node(3)),
    Node(6,
        None,
        Node(8,
            Node(7))))

print_tree(t1)
# 5 2 6 1 3 8 7
