from collections import defaultdict


class Solution(object):
    def findWhetherExistsPath(self, n, graph, start, target):
        """
        :type n: int
        :type graph: List[List[int]]
        :type start: int
        :type target: int
        :rtype: bool
        """
        gra = defaultdict(set)
        for key, value in graph:
            gra[key].add(value)
        print(gra)

        def dfs(start, target, visited):
            if start == target:
                return True
            if visited[start]:
                return False
            visited[start] = True
            judge = False
            if start in gra:
                for cur in gra[start]:
                    judge = judge or dfs(cur, target, visited)
            return judge

        visited = [False] * n
        return dfs(start, target, visited)


n = 5
graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
start = 0
target = 4

print(Solution().findWhetherExistsPath(n, graph, start, target))
