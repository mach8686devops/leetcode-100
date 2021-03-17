class Solution:
    def superEggDrop2(self, K: int, N: int) -> int:
        ans, dp = 0, [0 for _ in range(K + 1)]
        while dp[K] < N:
            for i in range(K, 0, -1):
                dp[i] = dp[i] + dp[i - 1] + 1
            ans += 1

        return ans

    def superEggDrop(self, K, N):
        mem = {}

        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in mem:
                return mem[(K, N)]
            res = float('inf')
            # for i in range(1, N + 1):
            #     res = min(res, max(dp(K, N - i), dp(K - 1, i - 1)) + 1)
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                b = dp(K - 1, mid - 1)
                nb = dp(K, N - mid)
                if b > nb:
                    hi = mid - 1
                    res = min(res, b + 1)
                else:
                    lo = mid + 1
                    res = min(res, nb + 1)
            mem[(K, N)] = res
            return res

        return dp(K, N)


print(Solution().superEggDrop(2, 100))

# 利用dp函数的单调性 二分法快速搜索
# 修改状态转移方程 简化求解 利用数学和二分进一步优化

# class Solution {
#     public int superEggDrop(int K, int N) {
#         int[][] dp=new int[K+1][N+1];
#         int m=0;
#         while (dp[K][m]<N) {
#             m++;
#             for(int k=1;k<=K;k++)
#                 dp[k][m]=dp[k][m-1]+dp[k-1][m-1]+1;
#         }
#         return m;
#
#     }
# }
