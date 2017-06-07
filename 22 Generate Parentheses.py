class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        left, right, res = n, n, []
        self.dfs(left,right, res, "")
        return res
    
    def dfs(self, left, right, res, tmp):
        if right < left:
            return
        if not left and not right:
            res.append(tmp)
            return
        if left:
            self.dfs(left-1, right, res, tmp + "(")
        if right:
            self.dfs(left, right-1, res, tmp + ")")
