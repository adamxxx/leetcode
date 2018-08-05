# Definition for singly-linked list.
# You are here! 
# Your runtime beats 99.88 % of python submissions.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getLen(self, p):
        c = 0
        while p != None:
            c+=1
            p = p.next
        return c

    def getIntersectionNode(self, headA, headB):
        """
        This wrong solution will return the node d, not the node b
        b should be the first intersection node.
        Alternative solution is the hased map.
        But space complexity is higher.
        :type head: ListNode
        :rtype: bool
        """
        c1 = self.getLen(headA)
        c2 = self.getLen(headB)

        head_l = headA
        head_s = headB
        if c1 < c2:
            head_l = headB
            head_s = headA

        # align the longer linkedlist with the short one
        c3 = abs(c1 - c2)
        while c3 > 0:
            c3 -= 1
            head_l = head_l.next

        while head_l != None and head_s != None:
            if head_l == head_s:
                return head_s
            head_l = head_l.next
            head_s = head_s.next
        return None


a1 = ListNode('a1')
a2 = ListNode('a2')
a3 = ListNode('a3')
a4 = ListNode('a4')

b1 = ListNode('b1')
b2 = ListNode('b2')
b3 = ListNode('b3')

c1 = ListNode('c1')
c2 = ListNode('c2')
c3 = ListNode('c3')

# a1.next = b2
# a2.next = a3
# a3.next = a4
# a4.next = c1

b1.next = a1
# b2.next = a1
# b3.next = c1

# c1.next = c2
# c2.next = c3

r = Solution().getIntersectionNode(a1,b1)
print(r)
        