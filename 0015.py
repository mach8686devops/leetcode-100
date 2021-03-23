# 三数之和


class Solution(object):
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            # 剪枝叶 优化
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return list(res)

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = set()

        for k in range(n - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, n - 1
            while i < j:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    i += 1
                elif sum > 0:
                    j -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    i += 1
                    j -= 1

        return list(res)
