from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        a = [min(i) for i in rectangles]
        # print(a)
        cnt = max(a)
        ans = 0
        for item in a:
            if item == cnt:
                ans += 1

        return ans


rectangles = [[5, 8], [3, 9], [3, 12]]
print(Solution().countGoodRectangles(rectangles=rectangles))
