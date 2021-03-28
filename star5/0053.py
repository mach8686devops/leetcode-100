class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        ans = pos = nums[0]
        for i in range(1, n):
            pos = max(pos + nums[i], nums[i])
            ans = max(ans, pos)
        return ans
        # return reduce(lambda r, x: (max(r[0], r[1] + x), max(r[1] + x, x)), nums, (max(nums), 0))[0]
