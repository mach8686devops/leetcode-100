from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:

        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                # 猫
                if grid[i][j] == 'C':
                    cp = (i, j)
                # 老鼠
                if grid[i][j] == 'M':
                    mp = (i, j)
                # 食物
                if grid[i][j] == 'F':
                    fp = (i, j)

        f = {}

        def work(status):
            cp, mp, r, steps = status
            if cp == fp or steps == 40 or cp == mp:
                return r == 1
            elif mp == fp:
                return r == 0
            if status not in f:
                n, m = len(grid), len(grid[0])
                if r == 0:
                    x, y = mp
                    jp = mouseJump
                else:
                    x, y = cp
                    jp = catJump
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    for i in range(jp + 1):
                        xx, yy = x + dx * i, y + dy * i
                        if 0 <= xx < n and 0 <= yy < m and grid[xx][yy] != '#':
                            nw = (
                                cp if r == 0 else (xx, yy),
                                mp if r == 1 else (xx, yy),
                                r ^ 1,
                                steps + (0 if r == 0 else 1))
                            if not work(nw):
                                f[status] = True
                                return True
                        else:
                            break
                f[status] = False
            return f[status]

        return work((cp, mp, 0, 0))
