# 回溯 位运算

class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        def backtrack(index, col, pos, neg):
            nonlocal res
            if index == n:
                res += 1
                return
                # 获取可供选择的状态位，1为不可选，0为可选
            pre = col | pos | neg
            for i in range(n):
                cur = 1 << i
                if cur & pre == 0:
                    backtrack(index + 1, col | cur, (pos | cur) >> 1, (neg | cur) << 1)

        backtrack(0, 0, 0, 0)
        return res

    def totalNQueens2(self, n: int) -> int:
        res = 0

        def backtrack(i, col, pos, neg):
            nonlocal res
            if i == n:
                res += 1
                return
                # 其中1表示可以被选
            pre = ((1 << n) - 1) & (~(col | pos | neg))

            while pre:
                cur = pre & (-pre)
                backtrack(i + 1, col | cur, (pos | cur) >> 1, (neg | cur) << 1)
                pre &= pre - 1

        backtrack(0, 0, 0, 0)
        return res

