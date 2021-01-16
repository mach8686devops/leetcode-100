# 回文都做烂了，双指针，栈，reverse，三种做法


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        a = []
        # 如果是字母或者数字，添加到数组元素中
        for i in s:
            # if i in "abcdefghijklmnopqrstuvwxyz0123456789":
            if i.isalnum():
                a.append(i)
        # 比较顺序跟逆序，返回结果
        return a[::1] == a[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1

        return True
