from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 左指针 右指针
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            res, l, r = (max(res, height[l] * (r - l)), l + 1, r) if height[l] < height[r] else (
                max(res, height[r] * (r - l)), l, r - 1)
        return res
