"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""


# http://bookshadow.com/weblog/2015/10/26/leetcode-serialize-and-deserialize-binary-tree/

import json

class Codec:

    def serialize(self, root):
        def tuplify(root):
            return root and (root.val, tuplify(root.left), tuplify(root.right))
        return json.dumps(tuplify(root))

    def deserialize(self, data):
        def detuplify(t):
            if t:
                root = TreeNode(t[0])
                root.left = detuplify(t[1])
                root.right = detuplify(t[2])
                return root

        return detuplify(json.loads(data))


####################
def serialize(root):
    vals = []
    def code(root):
        if root:
            vals.append(str(root.val))
            code(root.left)
            code(root.right)
        else:
            vals.append(str('#'))
    code(root)
    return ' '.join(vals)


def deserialize(data):

    def decode(vals):
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = decode(vals)
        node.right = decode(vals)
        return node

    vals = iter(data.split())
    return decode(vals)
############################

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
c.left = d
c.right = e

codec = Codec()
s = codec.serialize(a)
print( s )
root = codec.deserialize(s)
print( codec.serialize(root))

#node = TreeNode('root', TreeNode('left', TreeNode('left.left')), TreeNode('right'))
node = TreeNode('root')
left = TreeNode('left')
left_left = TreeNode('left.left')
right = TreeNode('right')

node.left = left
node.left.left = left_left
node.right = right

print( codec.deserialize(codec.serialize(node)).left.left.val )
assert codec.deserialize(codec.serialize(node)).left.left.val == 'left.left'

print('###################')
s = serialize(a)
print( s )
print("**********")
root = deserialize(s)
print( serialize(root))
print('###################')


# https://github.com/shiyanhui/Algorithm/blob/master/LeetCode/Python/297%20Serialize%20and%20Deserialize%20Binary%20Tree.py
# https://medium.com/@dimko1/serialize-and-deserialize-binary-tree-e9811ead85ed
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/326308/Python-pickle-cheating-and-consice-bfs
# https://www.google.com/search?safe=active&client=firefox-b-1-d&channel=cus&ei=0toiXabROKOR0gK4qorwAw&q=serialize+deserialize+binary+tree+python&oq=serialize+deserialize+binary+tree+&gs_l=psy-ab.1.1.0l3j0i22i30l7.1909.1909..5401...0.0..0.81.81.1......0....1..gws-wiz.......0i71.sxrWI7w9q84
