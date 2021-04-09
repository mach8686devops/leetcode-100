# 岛屿的数量


from typing import List


class Solution:
    def numIslands(self, grid):
        n = len(grid)

        def sink(i, j):
            if 0 <= i < n and 0 <= j < len(grid[i]) and int(grid[i][j]):
                grid[i][j] = '0'
                for i, j in zip((i, i + 1, i, i - 1), (j + 1, j, j - 1, j)):
                    sink(i, j)
                return 1
            return 0

        return sum(sink(i, j) for i in range(n) for j in range(len(grid[i])))

    def numberOfIslands2(self, grid: List[List[str]]) -> int:
        if not len(grid) or len(grid[0]):
            return 0
        row, col, count = len(grid), len(grid[0]), 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    self.dfs(grid, r, c)
        return count

    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)


class Solution2:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c),
                     (r + 1, c), 
                     (r, c - 1), 
                     (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        cnt = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    cnt += 1
                    self.dfs(grid, r, c)

        return cnt
