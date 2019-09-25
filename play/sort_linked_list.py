# https://leetcode.com/problems/sort-list/discuss/206679/Python-Merge-Sort-from-bottom-to-top.-space-O(1)-time-O(n-log-n)
# http://zxi.mytechroad.com/blog/list/leetcode-148-sort-list/

class Solution:
  def sortList(self, head):
    def merge(l1, l2):
      if not l1:
        return l2
      if not l2:
        return l1
      start = None
      if l1.val < l2.val:
        start = l1
        start.next = merge(l1.next, l2)
      else:
        start = l2
        start.next = merge(l1, l2.next)
      return start

#    if not head or not head.next: return head
    if not head.next:
        return  head
    slow = head
    fast = head.next
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    mid = slow.next
    slow.next = None
    return merge(self.sortList(head), self.sortList(mid))



class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def print_list(head):
    if head:
        print(head.val, end=' ')
        print_list(head.next)

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

print_list(head)

s = Solution()
ret = s.sortList(head)
print('\n---- res --- ')
print_list(ret)
