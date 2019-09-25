

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'{self.val}'

def print_list(node):
    if node:
        print(node.val, end=' ')
        print_list(node.next)

def mergeTwoLists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        start = None
        if l1.val < l2.val:
            start = l1;
            start.next = mergeTwoLists(l1.next, l2)
        else:
            start = l2;
            start.next = mergeTwoLists(l1, l2.next)

        return start


if __name__ == '__main__':
    l1 = Node(1, Node(2, Node(3, Node(6))))
    l2 = Node(1, Node(3, Node(4)))

    print('\nl1: ')
    print_list(l1)
    print('\nl2: ')
    print_list(l2)
    merged_list = mergeTwoLists(l1, l2)
    print('\n==== merged list')
    print_list(merged_list)
