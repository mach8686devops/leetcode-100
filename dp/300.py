class Solution(object):

    # 此题 dp效果不佳
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]表示nums[i]这个数结尾的最长递增子序列的长度
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 1
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i + 1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 耐心排序的算法 二分 另外此处建议除了 长度为n之类的 其他变量尽量要做到见名知意
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = l + (r - l) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)
