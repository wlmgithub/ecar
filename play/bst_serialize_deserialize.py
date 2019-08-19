
# BST

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)

def serialize(root):
    vals = []
    def encode(node):
        if node:
            encode(node.left)
            vals.append(node.val)
            encode(node.right)
    encode(root)
    return vals

def get_next_bigger(root, node):
    s = serialize(root)
    node_index = s.index(node.val)
    print(node_index)
    try:
        return s[node_index + 1]
    except IndexError:
        return 'Oops, this is last one'


# http://sunilarora.org/deserialize-a-binary-search-tree-from-an-inor/

def deserialize(vals, low, high):
    if low > high:
        return
    if low == high:
        return Node(vals[low])
    mid = (low + high) // 2
    node = Node(vals[mid])
    node.left = deserialize(vals, low, mid - 1)
    node.right = deserialize(vals, mid + 1, high)
    return node


root = Node( 10,
    Node(5),
    Node(30,
        Node(22),
        Node(35)
    )
)


print_tree(root)

s = serialize(root)
print(s)
res = get_next_bigger(root, Node(22))
print(res)

print('--------- deserialized ----')
ds_tree = deserialize(s, 0, len(s) - 1)
print_tree(ds_tree)

