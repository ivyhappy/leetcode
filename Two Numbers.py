# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tens = 0
        root = tmp = ListNode(0)
        while l1 or l2 or tens:
            tmpl1 = 0
            tmpl2 = 0
            if l1:
                tmpl1 = l1.val
                l1 = l1.next
            if l2:
                tmpl2 = l2.val
                l2 = l2.next
            tens,tmpans = divmod(tmpl1 + tmpl2 + tens,10)
         
         # firstly, wrongly made a new object to tmp itself, then the root only pointed to the previous space.
         
            tmp.next = ListNode(tmpans)
            tmp = tmp.next
        return root.next
