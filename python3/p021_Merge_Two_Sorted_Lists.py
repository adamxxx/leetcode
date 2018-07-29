# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # apply the list to sort
    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     list_merged = []
    #     while l1 != None:
    #         list_merged.append(l1.val)
    #         l1 = l1.next
    #     while l2 != None:
    #         list_merged.append(l2.val)
    #         l2 = l2.next
    #     print(list_merged)
    #     list_merged.sort()

    #     head = []
    #     if not list_merged:
    #         return head
        
    #     head = ListNode(list_merged[0])

    #     curr = head
    #     for i in range(1, len(list_merged)):
    #         curr.next = ListNode(list_merged[i])
    #         curr = curr.next
    #     return head
    def mergeTwoLists(self, l1, l2):
        """
        Solution without the list
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return []

        head = cur = ListNode(0)
        # if two list node not empty
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                # move the pointer to shorter the list from left
                l1 = l1.next 
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        
        # if l1 != None:
        #     cur.next = l1
        
        # if l2 != None:
        #     cur.next = l2
        cur.next = l1 or l2

        return head.next
       

a = ListNode(3)
b = ListNode(1)
# c = ListNode(2)
a.next = b
# b.next = c

Solution().mergeTwoLists(None, a)
        