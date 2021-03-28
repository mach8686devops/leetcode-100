# 有效的完全平方数


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 4:
            return False
        if num == 4:
            return True
        # left, right = 2, num // 2
        # while left <= right:
        #     mid = (right + left) >> 1
        #     if mid ** 2 == num:
        #         return True
        #     if mid ** 2 < num:
        #         left = mid + 1
        #     if mid ** 2 > num:
        #         right = mid - 1
        # return False

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num
