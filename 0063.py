class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        opt = [[0] * w for i in range(h)]

        # 从上到下，从左到右
        for m in range(h):  # 每一行
            for n in range(w):  # 每一列
                if not obstacleGrid[m][n]:  # 如果这一格没有障碍物
                    if m == n == 0:  # 或if not(m or n)
                        opt[m][n] = 1
                    else:
                        a = opt[m - 1][n] if m != 0 else 0  # 上方格子
                        b = opt[m][n - 1] if n != 0 else 0  # 左方格子
                        opt[m][n] = a + b
        return opt[-1][-1]
