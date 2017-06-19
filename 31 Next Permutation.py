class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        notchange = True
        for i in range(n - 1):
            if nums[n-1-i] > nums[n-2-i]:
                j = n-1
                while nums[j] <= nums[n-2-i]:
                    j-=1
                nums[j],nums[n-2-i]=nums[n-2-i],nums[j]
                nums[n-1-i:] = reversed(nums[n-1-i:])
                notchange = False
                break
        if notchange:
            nums.sort()
