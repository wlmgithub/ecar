

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



# credit: https://www.geeksforgeeks.org/inorder-non-threaded-binary-tree-traversal-without-recursion-or-stack/

# Function to print inorder traversal
# using parent pointer
def inorder(root):
    leftdone = False

    # Start traversal from root
    while root:

        # If left child is not traversed,
        # find the leftmost child
        if leftdone == False:
            while root.left:
                root = root.left

        # Print root's data
        print(root.val, end = " ")

        # Mark left as done
        leftdone = True

        # If right child exists
        if root.right:
            leftdone = False
            root = root.right

        # If right child doesn't exist, move to parent
        elif root.parent:

            # If this node is right child of its
            # parent, visit parent's parent first
            while root.parent and root == root.parent.right:
                root = root.parent
            if root.parent == None:
                break
            root = root.parent
        else:
            break

# credit: http://www.algoqueue.com/algoqueue/default/view/8388608/inorder-traversal-of-bst-without-extra-space
def morris(root):
    prev = None
    current = root
    while current:
        if current.left is None:
            print(current.val, end=' ')
            current = current.right
        else:
            prev = current.left
            while prev.right is not None and prev.right != current:
                prev = prev.right

            if prev.right is None:
                prev.right  = current
                current = current.left
            else:
                prev.right = None
                print(current.val, end=' ')
                current = current.right



t1 = Node(5,
    Node(2,
        Node(1),
        Node(3)),
    Node(6,
        None,
        Node(8,
            Node(7))))

#print_tree(t1)
# 5 2 6 1 3 8 7

inorder(t1)
print('\n===== morris traversal ===\n')
morris(t1)
