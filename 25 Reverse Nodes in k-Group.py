# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        if k == 1:
            return head
        pre,pre.next = self,head
        while pre.next:
            tmp = pre.next
            for _ in range(k-1):
                if not tmp.next:
                    return self.next
                tmp = tmp.next
            first = pre.next
            sec = first.next
            last = first.next
            pre.next,sec.next,first.next = sec,first,sec.next
            sec = first.next
            first = pre.next
            last = first.next
            for _ in range(k-2):
                pre.next,sec.next,last.next = sec,first,sec.next
                sec = last.next
                first = pre.next
            pre = last
        return self.next
		
