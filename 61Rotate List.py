# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        length, p = 0, head
        while p:
            length += 1
            p = p.next
        k = k % length
        if k == 0:
            return head
        left, right = head, head
        while k:
            right = right.next
            k -= 1
        
        while right and right.next:
            right = right.next
            left = left.next
        headnode = left.next
        left.next = None
        right.next = head
        return headnode
