# https://leetcode.com/problems/sort-list/discuss/206679/Python-Merge-Sort-from-bottom-to-top.-space-O(1)-time-O(n-log-n)
# http://zxi.mytechroad.com/blog/list/leetcode-148-sort-list/

class Solution:
  def sortList(self, head):
    def merge(l1, l2):
      dummy = ListNode(0)
      tail = dummy
      while l1 and l2:
        if l1.val > l2.val: l1, l2 = l2, l1
        tail.next = l1
        l1 = l1.next
        tail = tail.next
      tail.next = l1 if l1 else l2
      return dummy.next

    if not head or not head.next: return head
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
