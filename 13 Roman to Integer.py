class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        ans = 0
        for i in range(1 , len(s)):
            if trans[s[i]] > trans[s[i-1]]:
               ans -= trans[s[i-1]]
            else:
                ans +=trans[s[i-1]]
        ans += trans[s[len(s)-1]]
        return ans 
