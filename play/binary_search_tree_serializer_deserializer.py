from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


bst =  TreeNode(50,
        TreeNode(20,
            TreeNode(10),
            TreeNode(40)),
        TreeNode(70,
            TreeNode(60),
            TreeNode(90,
                None,
                TreeNode(100))
            ),
        )


def print_tree(node):
    if node is not None:
        print(node.val, end=' ')
        print_tree(node.left)
        print_tree(node.right)


def serialize(node):
    vals = []

    def encode(node):
        if node is not None:
            vals.append(node.val)
            encode(node.left)
            encode(node.right)

        return vals

    encode(node)
    return ' '.join([str(i) for i in vals])


def deserialize(given_string):
    def decode(min_val=float('-inf'), max_val=float('inf')):
        if vals and min_val < vals[0] < max_val:
            val = vals.popleft()
            root = TreeNode(val)
            root.left = decode(min_val, val)
            root.right = decode(val, max_val)

            return root

    vals = deque([int(i) for i in given_string.split()])

    return decode()

if __name__ == '__main__':


    print('Print bst: ')
    print_tree(bst)
    print()

    serialized_string = serialize(bst)
    print('Serialized string: ', serialized_string)

    print('DeSerialized tree: ')
    deserialized_tree = deserialize(serialized_string)
    print_tree(deserialized_tree)


