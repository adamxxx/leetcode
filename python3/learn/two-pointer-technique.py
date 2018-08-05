# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        p2 = head
        while p1 != None and p2 != None and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next.next
            if p1 == p2:
                return True
        return False


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = a

r = Solution().hasCycle(a)
print(r)
        