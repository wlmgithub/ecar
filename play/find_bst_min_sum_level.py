import collections

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root):
    q = collections.deque([root])
    while q:
        node = q.popleft()
        if node:
            print(node.val, end=' ')
            q.append(node.left)
            q.append(node.right)


def level_order(root):
#    if root is None:
#        return []

    res, current_level = [], [root]
    while current_level:
        vals, next_level = [], []
        for node in current_level:
            vals.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current_level = next_level
        res.append(sum(vals))

    return res

if __name__ == '__main__':
    """
      5
  10    9
2   2
    """

    root = Node(5,
            Node(10,
                Node(2),
                Node(2)
                ),
            Node(9)
            )
    
    
    print_tree(root)
    
    r = level_order(root)
    print(r)
    print(r.index(min(r)))
    
