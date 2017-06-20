class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ans = []
        for i, row in enumerate(board):
        	for j, c in enumerate(row):
        		if c !='.':
        			ans+=[(c, i), (j, c), (i//3, j//3, c)]
        c = collections.Counter(ans)
        for x in ans:
        	if c[x] > 1:
        		return False
        return True
