class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  return False
        col = list(list(zip(*matrix))[0])  # set() -> list()
        index = bisect.bisect_left(col, target, 0, len(matrix)-1)  # 二分查找
        return target in (matrix[index] + matrix[index-1])