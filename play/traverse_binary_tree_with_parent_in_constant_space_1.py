#!/usr/bin/env python3

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
#         7

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        if self.left is not None:
            self.left.parent = self

        if self.right is not None:
            self.right.parent = self

        self.parent = None


def inorder(root):
    leftdone = False
    while root:
        if not leftdone:
            while root.left:
                root = root.left

        print(root.val, end=' ')
        leftdone = True

        if root.right:
            leftdone = False
            root = root.right
        else:
            while root.parent and root == root.parent.right:
                root = root.parent
            root = root.parent


if __name__ == '__main__':
    t1 = Node(5,
        Node(2,
            Node(1),
            Node(3)),
        Node(6,
            None,
            Node(8,
                Node(7))))

    inorder(t1)
