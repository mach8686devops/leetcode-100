class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = [[0] * len(i) if 0 in i else i for i in matrix]
        col = [[0] * len(j) if 0 in j else list(j) for j in zip(*matrix)]
        col2row = list(map(list, zip(*col)))
        # 上面一行效果等同：
        # col2row = [list(i) for i in zip(*col)]
        for i in range(len(matrix)):
            matrix[i] = col2row[i] if row[i] != [0] * len(matrix[0]) else row[i]