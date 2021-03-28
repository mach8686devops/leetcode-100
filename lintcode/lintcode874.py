class Solution:
    """
    @param flights: the airline status from the city i to the city j
    @param days: days[i][j] represents the maximum days you could take vacation in the city i in the week j
    @return: the maximum vacation days you could take during K weeks
    """

    def maxVacationDays(self, flights, days):
        # 先枚举周数，然后枚举终点，然后是起点，
        # 判断是否前往(temp[j] = max(temp[j], dp[k] + days[j][i]))，即是否进行转移。
        # Write your code here
        N, K = len(flights), len(days[0])
        dp = [-0x7f for i in range(0, N)]
        dp[0] = 0
        for i in range(0, K):  # 逐渐扩大枚举周
            temp = [-0x7f for i in range(0, N)]
            for j in range(0, N):  # 枚举终点
                for k in range(0, N):  # 枚举起点
                    if j == k or flights[k][j] == 1:  # 如果城市k到城市j存在航班
                        temp[j] = max(temp[j], dp[k] + days[j][i])  # 则再对当前答案进行选择，即是否从k前往j
            dp = temp

        return max(dp)


flights = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
days = [[1, 3, 1], [6, 0, 3], [3, 3, 3]]
print(Solution().maxVacationDays(flights, days))
