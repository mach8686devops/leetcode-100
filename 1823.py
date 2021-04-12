class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        val = 0
        for i in range(2, n + 1):
            cur = (val + k) % i
            val = cur
            print(cur)
        return val + 1


print(Solution().findTheWinner(n=5, k=2))
