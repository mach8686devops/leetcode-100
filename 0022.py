from functools import lru_cache
from typing import List


class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


# 回溯法的代码套路是使用两个变量： res 和 path，res 表示最终的结果，
# path 保存已经走过的路径。如果搜到一个状态满足题目要求，就把 path 放到 res 中。
#
# 代码后面的判断条件都是 if，而不是 elif，因为是满足两个条件的任意一个就可以继续向下搜索，
# 而不是同时只能满足其中的一个。
