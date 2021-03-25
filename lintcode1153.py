class Solution:
    """
    @param s: string
    @return: sort string in lexicographical order
    """

    def sorting(self, s):
        # write your code here
        strings = s.split(',')
        self.qsort(0, len(strings) - 1, strings)
        ans = ""
        for i in range(len(strings)):
            if i > 0:
                ans += ","
            ans += strings[i]
        return ans

    def qsort(self, n, m, a):
        i = n
        j = m
        k = a[(n + m) // 2]
        while i <= j:
            while a[i] < k:
                i += 1
            while a[j] > k:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        if i < m:
            self.qsort(i, m, a)
        if n < j:
            self.qsort(n, j, a)
