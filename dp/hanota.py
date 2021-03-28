from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)

        def hano(n, A, B, C):
            if n == 1:
                C.append(A.pop())
            else:
                hano(n - 1, A, C, B)
                hano(1, A, B, C)
                hano(n - 1, B, A, C)

            return C

        return hano(n, A, B, C)
