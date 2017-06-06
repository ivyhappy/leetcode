class Solution(object):
    def fourSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort() 
        if len(nums) < 4 or target < 4 * nums[0] or target > 4*nums[-1] :
            return []
        else:
            self.res = []
            restmp = []
            self.getsum(nums,0,restmp,target,4)
            return self.res
    def getsum(self,nums,start,restmp,target,N):
        l,r=start,len(nums)-1
        if N == 2:
        	while l < r:
        	    tmp = nums[l]+nums[r]
        	    if tmp == target:
        	        self.res.append((restmp + [nums[l],nums[r]]))
        	        l += 1
        	        r -= 1
        	        while l < r and nums[l] == nums[l-1]:
        	        	l += 1
        	        while l < r and nums[r] == nums[r+1]:
        	        	r -= 1
        	    elif tmp > target:
        	    	r -= 1
        	    	while l < r and nums[r] == nums[r+1]:
        	    		r -= 1
        	    else:
        	    	l += 1
        	    	while l < r and nums[l] == nums[l-1]:
        	    		l += 1
        else:
        	for i in range(start,len(nums)):
        		if i > start and nums[i] == nums[i-1]:
        			continue
        		self.getsum(nums, i+1, restmp + [nums[i]], target-nums[i], N-1)
