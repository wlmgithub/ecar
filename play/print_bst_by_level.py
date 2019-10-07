import collections

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self):
        return f'{self.data}'


def traverse(root):
    if root is not None:
        print(root.data)
        traverse(root.left)
        traverse(root.right)

def print_tree_0(root):
    q = collections.deque([root])
    while q:
        node = q.popleft()
        if node:
            print(node.data, end=' ')
            q.append(node.left)
            q.append(node.right)


def print_tree(root):
    current_level = [root]
    while current_level:
        print(' '.join( str(n) for n in current_level) )
        next_level = []

        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)

        current_level = next_level

def testme():
    '''
          1
        2   3
      4  5    6
    '''
    root = Node(1,
                Node(2,
                     Node(4), Node(5)),
                Node(3, None, Node(6)))

    traverse(root)

    print()

    print_tree(root)

if __name__ == '__main__':
    testme()

