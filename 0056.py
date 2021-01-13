# 合并空间
# 排序的做法


class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        result = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if len(result) == 0 or interval[0] > result[-1][-1]:
                result.append(interval)
            else:
                result[-1][-1] = max(result[-1][-1], interval[1])
        return result
