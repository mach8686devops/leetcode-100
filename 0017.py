from typing import List
# 此题product 函数的使用 或者确切是类使用

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from itertools import product
        l = '- - abc def ghi jkl mno pqrs tuv wxyz'.split()
        return [''.join(c) for c in product(*[l[int(i)] for i in digits])] if digits else []

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = [i for i in digit2chars[digits[0]]]

        for i in digits[1:]:
            res = [m + n for m in res for n in digit2chars[i]]

        return res
