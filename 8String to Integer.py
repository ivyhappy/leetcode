class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        s = str.strip()
    
        ans = 0
        neg = 1
        if s[0] == '-':
            neg = -1
        for i in range(len(s)):
            if s[i].isdigit():
                ans = ans* 10 + ord(s[i]) - ord('0')
            else:
                if i!=0:
                    return max(-2147483648, min(ans*neg, 2147483647))
                elif s[i] != '-' and  s[i] != '+':
                    return 0
           
        return max(-2147483648, min(ans*neg, 2147483647))
