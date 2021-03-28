class Solution:
    def mySqrt(self, x: int) -> int:
        # 牛顿迭代法
        r = x
        while r * r > x:
            r = (r + x / r) // 2
        return int(r)
