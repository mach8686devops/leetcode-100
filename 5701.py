class Solution(object):
    def areAlmostEqual(self, str1, str2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import Counter
        a = Counter(str1)
        b = Counter(str2)
        if a == b:
            count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count += 1
            return count == 2 or count == 0
        return False
