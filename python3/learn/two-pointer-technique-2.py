# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        This wrong solution will return the node d, not the node b
        b should be the first intersection node.
        Alternative solution is the hased map.
        But space complexity is higher.
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        p2 = head
        hasCycle = False
        while p1 != None and p2 != None and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            # print(id(p1))
            # print(id(p2))

            if p1 == p2:
                hasCycle = True
                break
        
        if hasCycle == False:
            return None

        # cycle detected
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1



a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-1)
a.next = b
b.next = c
c.next = d
d.next = a

r = Solution().detectCycle(a)
print(r)
        