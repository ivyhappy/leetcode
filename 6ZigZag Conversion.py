class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        ans = [''] * numRows
        line = 0
        step = 1
        for i in s:
            ans[line] += i
            if line == 0:
                step = 1
            elif line == numRows -1:
                step = -1
            line += step
        return ''.join(ans)
