class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = [""]
        for digit in digits:
            chars = mapping[digit]
            tmp = []
            for cha in chars:
                for strs in res:
                    tmp.append(strs+cha)
            res = tmp
        return res
