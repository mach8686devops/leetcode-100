class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [0] + nums + [0]
        n = len(nums)
        res = float('-inf')
        stack = []
        # 维护一个找最小值的单调栈 对应的是数组的序号 不是值

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                tmp = nums[stack.pop()]
                if stack[-1] + 1 <= k + 1 <= i - 1:
                    res = max(res, (i - stack[-1] - 1) * tmp)
            stack.append(i)
            print(stack)

        return res


nums = [5, 5, 4, 5, 4, 1, 1, 1]
k = 0
print(Solution().maximumScore(nums, k))
