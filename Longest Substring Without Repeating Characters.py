
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictarr = {}
        length = len(s)
        beg = 0
        begtmp = 0
        tmplength = 0
        maxlength = 0
        i = 0
        while i < length:
            if s[i] not in dictarr:
                tmplength += 1
            elif begtmp > dictarr[s[i]]:
                tmplength += 1
            else:
                if tmplength > maxlength:
                    maxlength = tmplength
                    beg = begtmp
                tmplength = i - dictarr[s[i]]
                begtmp = dictarr[s[i]] + 1
            dictarr[s[i]] = i
            i += 1
        if tmplength > maxlength:
            maxlength = tmplength
            beg = begtmp
        return maxlength
        
        
