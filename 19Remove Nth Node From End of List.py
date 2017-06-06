# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        end = head
        i = 0
        while i < n:
            end = end.next
            i += 1
        if not end:
            return head.next
        bef = head
        while end.next:
            end = end.next
            bef = bef.next
        bef.next = bef.next.next
        return head
            
