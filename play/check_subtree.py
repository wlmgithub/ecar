
####################
def serialize(root):
    out = []
    def encode(node):
        if node:
            out.append(node.val)
            encode(node.left)
            encode(node.right)
        else:
            out.append('#')
    encode(root)
    return out

def deserialize(data):
    def decode(vals):
        val = next(vals)
        if val == '#':
            return
        node = TreeNode(val)
        node.left = decode(vals)
        node.right = decode(vals)
        return node
    return decode(iter(data))

############################

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def print_tree_0(self):
        q = [self]
        while q:
            node = q.pop(0)
            print(f'{node.val}', end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    def print_tree(self):
        if self:
            print(f'{self.val}', end=' ')
            if self.left:
                self.left.print_tree()
            if self.right:
                self.right.print_tree()


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
c.left = d
c.right = e

tree2 = c


print('###################')
print('\n Serialization')
s = serialize(a)
print( s )
a.print_tree()
print("\n Deserialization: ")
root = deserialize(s)
root.print_tree()
print()
print( serialize(root))
print('###################')

print('--------------------------------------------------')

tree2.print_tree()


def is_subseq(s1, s2):
    i, j = 0, 0
    while i < len(s2) and j < len(s1):
        if s2[i] == s1[j]:
            i += 1
        j += 1
    return i == len(s2)

# check t2 is subtree of t1
def is_subtree(t1, t2):
    s1 = serialize(t1)
    s2 = serialize(t2)

    # check s2 is subseq of s1
    return is_subseq(s1, s2)


print('\n is_subtree(t1, t2): ', is_subtree(a, tree2))

# https://github.com/shiyanhui/Algorithm/blob/master/LeetCode/Python/297%20Serialize%20and%20Deserialize%20Binary%20Tree.py
# https://medium.com/@dimko1/serialize-and-deserialize-binary-tree-e9811ead85ed
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/326308/Python-pickle-cheating-and-consice-bfs
# https://www.google.com/search?safe=active&client=firefox-b-1-d&channel=cus&ei=0toiXabROKOR0gK4qorwAw&q=serialize+deserialize+binary+tree+python&oq=serialize+deserialize+binary+tree+&gs_l=psy-ab.1.1.0l3j0i22i30l7.1909.1909..5401...0.0..0.81.81.1......0....1..gws-wiz.......0i71.sxrWI7w9q84



