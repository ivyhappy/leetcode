class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            #print(left,right,mid)
            if nums[mid] == target:
                ans = mid
                break
            if nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) / 2
            else:
                if  nums[mid] > target and nums[left] <= target:
                    right = mid -1
                else:
                    left = mid + 1
            
        if ans == -1:
            return [-1,-1]
        else:
            left = ans
            right = ans
            while left >= 0:
                if nums[left] == target:
                    left -= 1
                else:
                    break
            while right < len(nums):
                if nums[right] == target:
                    right += 1
                else:
                    break
            return [left+1,right-1]
