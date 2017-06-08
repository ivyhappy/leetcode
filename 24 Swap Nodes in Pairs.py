class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            first = pre.next
            sec = first.next
            pre.next, sec.next, first.next = sec, first, sec.next
            pre = first
        return self.next
