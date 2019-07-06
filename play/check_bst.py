# https://simplyexplained.tech/how-to-check-if-a-binary-tree-is-a-binary-search-tree-bst

"""
Python program to check if the given tree is Binary Search Tree (BST)
"""

import sys

class Node:
    """
    Class holding the data and methods for a node in a tree
    """

    def __init__(self, value, left=None, right=None):
        """
        This method initialized node instance
        :param value: Value of the node
        :param left: reference to left child node
        :param right: reference to right child node
        """
        self.value = value
        self.left = left
        self.right = right


"""
NOTE: Maximum integer value is sys.maxsize and minimum integer value is one less number on negative side i.e. -(sys.maxsize - 1)
"""


def is_BST(node, min_value=-(sys.maxsize - 1) , max_value=sys.maxsize):
    """
    This methods checks if the tree/sub-tree rooted by the specified
    node is BST or not. Returns True if it's BST, else returns False
    :param node: Instance of the class Node
    :param min_value: Lower bound for node values in the tree
    :param max_value: Upper bound for node values in the tree
    :return: True if the tree rooted by the specified node
             is BST else returns False.
    """

    if node is None:
        return True

    if node.value < min_value or node.value > max_value:
        return False

    return is_BST(node.left, min_value, node.value-1) and \
           is_BST(node.right, node.value+1, max_value)



"""
  Testing the code
"""

root_false = Node(20, Node(18, None, Node(25)), Node(30))
print("Result if tree is BST = ", is_BST(root_false))
# Result if tree is BST =  False


root_true = Node(30, Node(25), Node(40, Node(35)))
print("Result if tree is BST = ", is_BST(root_true))
# Result if tree is BST =  True


root = Node(50)
root.left = Node(30)
root.right = Node(80)
root.left.left = Node(20)
root.left.right = Node(60) # False

root.right.left = Node(70)
root.right.right = Node(90)

print("Result if tree is BST = ", is_BST(root))


root = Node(50)
root.left = Node(30)
root.right = Node(80)
root.left.left = Node(20)
root.left.right = Node(45)  # True

root.right.left = Node(70)
root.right.right = Node(90)

print("Result if tree is BST = ", is_BST(root))
