# https://codereview.stackexchange.com/questions/150467/find-smallest-subset-prefixes

from collections import defaultdict

class TrieTreeNode:
    def __init__(self):
        self.children = defaultdict(TrieTreeNode)
        self.is_end = False

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.isEnd = True


if __name__ == "__main__":
    words = ['foo', 'foog', 'food', 'asdf', 'astr']
    root = TrieTreeNode()
    for word in words:
        root.insert(word)

    output = []
    for char, child in root.children.items():
        word = [char]
        while not child.is_end and len(child.children) == 1:
            children = child.children
            letter = list(children.keys())[0]
            word.append(letter)
            child = children[letter]
        output.append(''.join(word))
    print (output )
