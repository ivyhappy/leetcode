class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans, l, r = 0, 0, len(height) - 1
        if len(height) < 2:
            return 0
        #从两边往中间走，若l的高度<r的高度，则l+1,
        #因为r-1的高度若高于r，则按照l的高度计算，r-l减小，容量减小
        #若低于r则容量明显减小
        while l < r:
            if height[l] < height[r]:
                ans, l = max(ans, height[l] * (r - l)), l + 1
            else:
                ans, r = max(ans, height[r] * (r - l)), r - 1
        return ans
