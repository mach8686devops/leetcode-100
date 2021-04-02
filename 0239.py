import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = collections.deque()
        # 双端队列
        res = []
        n = len(nums)
        for i in range(n):
            # 如果当前元素大于单调队列中的尾端元素的话：pop单调队列中的尾端元素
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            # 当单调队列的第一个元素（即最大的元素）不在[i - k + 1, i]，
            # 说明该最大元素在当前的窗口之外，则popleft单调队列中的第一个元素
            if q[0] <= i - k:
                q.popleft()
            # 在当前index >= k - 1的时候（即这时候已经能够构成长度为k的窗口）把单调队列的第一个元素加入到结果中去
            if i >= k - 1:
                res.append(nums[q[0]])
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
