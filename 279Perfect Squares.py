import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
        	return 0
        squres = [n] * (n+1)
        squres[0] = 0
        for i in range(1,n+1):
        	for j in range(1,int(math.sqrt(i))+1):
        		if j *j > i:
        			break
        		squres[i] = min(squres[i],squres[i - j*j] + 1)
        return squres[n]
