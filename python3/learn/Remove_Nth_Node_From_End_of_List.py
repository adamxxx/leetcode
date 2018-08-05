# Definition for singly-linked list.
# You are here! 
# Your runtime beats 99.88 % of python submissions.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        This's a non two pointer solution.
        """
        list = []
        h = head
        while h != None:
            list.append(h)
            h = h.next
        len_list = len(list)
        # if the first one
        if n == len_list:
            # if one only element
            if n == 1:
                head = None
            else:
                head = list[len_list - n + 1]

        # if the last one
        elif n == 1:
            list[len_list - n - 1].next = None
        else:
            list[len_list - n - 1].next = list[len_list - n + 1]
        return head

a1 = ListNode('a1')
a2 = ListNode('a2')
a3 = ListNode('a3')
a4 = ListNode('a4')
a5 = ListNode('a5')

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

r = Solution().removeNthFromEnd(a1, 1)
print(r)
        