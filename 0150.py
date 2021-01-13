from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t, f = tokens.pop(), self.evalRPN
        if t in '+-*/':
            b, a = f(tokens), f(tokens)
            t = eval('a' + t + 'b')
        return int(t)