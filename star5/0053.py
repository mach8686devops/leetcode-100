import copy


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
            pos = max(pos, 0) + nums[i]
            ans = max(ans, pos)
        return ans
        # return reduce(lambda r, x: (max(r[0], r[1] + x), max(r[1] + x, x)), nums, (max(nums), 0))[0]

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Copy:
        #
        # 只是Copy了集合对象，并没有Copy子元素，所以子元素修改，会影响Copy前和Copy后的值
        #
        # DeepCopy:
        #
        # 相当于复制整个对象与子元素。不管类型是否可以修改，都是一个全新的对象。新老对象修改互不影响。
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = copy.deepcopy(nums)
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], 0) + dp[i]
        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(Solution().maxSubArray(nums))
print(Solution().maxSubArray2(nums))
