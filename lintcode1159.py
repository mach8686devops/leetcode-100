class Solution:
    """
    @param arr: string array
    @param query: query array
    @return: return  LCP ans array
    """

    def common_pre(self, str1, str2):
        cnt = 0
        for a, b in zip(str1, str2):
            if a != b:
                break
            cnt += 1
        return cnt

    def queryLCP(self, arr, query):
        if not arr or not query:
            return []

        res = []
        dic = {}

        for idx1, idx2 in query:
            if (idx1, idx2) in dic:
                res.append(dic[(idx1, idx2)])
            else:
                str1, str2 = arr[idx1], arr[idx2]
                num = self.common_pre(str1, str2)
                dic[(idx1, idx2)] = num
                res.append(num)
        return res
