import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size <= 1:
            return size
        heap = []
        for interval in sorted(intervals):
            if heap and interval[0] >= heap[0]:
                heapq.heappushpop(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        return len(heap)
