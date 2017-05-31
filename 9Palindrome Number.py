class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>0 and x<10:
            return True
        if x<0 :
            return False
        y=0
        temp = x
        while temp > 0:
            y = y*10 + temp % 10
            temp=temp//10
        y += temp
        if y==x:
            return True
        else:
            return False
