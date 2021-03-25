import heapq

# 把比 median 小的放在 maxheap 里，把比 median 大的放在 minheap 里。median 单独放在一个变量里。
# 每次新增一个数的时候，先根据比当前的 median 大还是小丢到对应的 heap 里。
# 丢完以后，再处理左右两边的平衡性:
#
# 如果左边太少了，就把 median 丢到左边，从右边拿一个最小的出来作为 median。
# 如果右边太少了，就把 median 丢到右边，从左边拿一个最大的出来作为新的 median。

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """

    def medianII(self, nums):
        self.minheap = []
        self.maxheap = []
        medians = []
        for num in nums:
            self.add(num)
            medians.append(self.median)
        return medians

    @property
    def median(self):
        return -self.maxheap[0]

    def add(self, value):
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -value)
        else:
            heapq.heappush(self.minheap, value)

        if len(self.minheap) == 0 or len(self.maxheap) == 0:
            return

        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
