
# 汇总区间


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.sort()
        res = []
        for num in nums:
            if res and num == res[-1][-1] + 1:
                res[-1] = [res[-1][0], num]
            else:
                res.append([num])
        return ['->'.join(map(str, p)) for p in res]
