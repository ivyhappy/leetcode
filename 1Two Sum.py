class Solution(object):
    def twoSum(self, nums, target):
    #369 ms
    #Firstly, not take length<=1 into consideration; then it will be 482 ms
        dictarr = {}
        length = len(nums)
        if length <= 1:
            return False
        for i in range(length):
            if ((target-nums[i]) in dictarr):
                return [dictarr[target-nums[i]],i]
            dictarr[nums[i]] = i
