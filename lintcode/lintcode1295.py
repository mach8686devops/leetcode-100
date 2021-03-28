class Solution:
    """
    @param N: a number
    @return: the number of prime numbers.
    """
    def Count_PrimeNum(self, N):
        r = 0
        v = [False] * 100005
        p = [1] * 100005
        for i in range(2, N + 1):
            r += p[i]
            k = int(min(N / i, i))
            for j in range(2, k + 1):
                print(i*j)
                if v[i * j]:
                    continue
                v[i * j] = True
                p[i * j] = p[i] + p[j]
        return r

print(Solution().Count_PrimeNum(N=32))