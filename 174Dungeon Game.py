class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0
        
        m = len(dungeon)
        n = len(dungeon[0])
        if m == 1 and n== 1:
            return -1*dungeon[0][0]+1  if dungeon[0][0] < 0 else 1  
        
        dp =m* [n*[0]]
        dp[-1][-1] = max(1,1-dungeon[-1][-1])
        
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
            	
            	if i < m-1 or j < n-1:
            		
	            	down,right = 100000000,100000000

	            	if i+1 < m:
	            		print(dp[i+1][j])
	            		down = max(1,dp[i+1][j]-dungeon[i][j])
	            	if j+1 < n:
	            		print(dp[i][j+1])
	            		right = max(1,dp[i][j+1]-dungeon[i][j])
	            	dp[i][j] = min(down,right)
        return dp[0][0]
