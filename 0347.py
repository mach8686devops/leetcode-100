class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [*next(zip(*collections.Counter(nums).most_common(k)))]


# Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value
#
# 非内置解法：

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {n: 0 for n in nums}
        for n in nums:
            d[n] += 1

        r = []
        for _ in range(k):
            n = max(d, key=d.get)
            r.append(n)
            d[n] = -1

        return r