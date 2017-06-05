class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]+nums[1]+nums[2]
            
        if len(nums) < 3:
            return 0
        nums.sort() 
        res = nums[0]+nums[1]+nums[2]
        closest = nums[0]+nums[1]+nums[2]- target
        for i in xrange(0,len(nums)-2):
            j, k = i+1, len(nums) - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == target:
                    return tmp
                
                if abs(tmp - target) < abs(res - target):
                    res = tmp
                if tmp > target:
                    k -= 1
                else:
                    j += 1
        return res 
