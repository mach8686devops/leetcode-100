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
        # 列表生成式 迭代使用
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
        print(res)

        for i in digits[1:]:
            res = [m + n for m in res for n in digit2chars[i]]
            print(res)

        return res


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 使用列表替代字典的做法
        digit2char = [
            "_",
            "_",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

        res = [i for i in digit2char[int(digits[0])]]

        for item in digits[1:]:
            res = [m + n for m in res for n in digit2char[int(item)]]

        return res


digits = "2394"
print(Solution().letterCombinations2(digits))
