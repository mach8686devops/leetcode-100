from pprint import pprint


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # if m<2 or n <2:
        #     return 0
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]
        # return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))


# print(Solution().uniquePaths(m=7,n=3))
print(Solution().uniquePaths(m=3, n=7))
