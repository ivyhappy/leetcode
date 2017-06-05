class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp < 0:
                    j +=1 
                elif tmp > 0:
                    k -= 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while j<k and j > i+1 and nums[j-1] == nums[j]:
                        j += 1
                    while j<k and j < len(nums)-1 and nums[k] == nums[k+1]:
                        k -= 1
                    
        return res
