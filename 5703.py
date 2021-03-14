from heapq import heappush, heappop
from typing import List


class Solution:
    def maxAverageRatio(self, c: List[List[int]], e: int) -> float:
        heap = []

        def dif(a, b):
            return (a + 1) / (b + 1) - (a / b)

        for u, v in c:
            heappush(heap, [-dif(u, v), u, v])
        while e:
            cur, u, v = heappop(heap)
            u += 1
            v += 1
            e -= 1
            heappush(heap, [-dif(u, v), u, v])
        ans = 0
        for dif, u, v in heap:
            ans += u / v
        return ans / len(heap)


classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents = 4

print(Solution().maxAverageRatio(classes, extraStudents))
