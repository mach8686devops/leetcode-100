import math


class Solution:
    def numSquares2(self, n: int) -> int:
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return bool(a) + bool(b)
            a += 1

        return 3

    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq * sq == n

    def numSquares(self, n: int) -> int:
        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2  # reducing the 4^k factor from number
        if (n & 7) == 7:  # mod 8
            return 4

        if self.isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n ** (0.5)) + 1):
            if self.isSquare(n - i * i):
                return 2
        # bottom case from the three-square theorem
        return 3
