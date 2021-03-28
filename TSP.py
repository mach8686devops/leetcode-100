import random
from dataclasses import dataclass
from math import inf


@dataclass
class State:
    minDistance: int


def dfs(begin, end, graph, cities, distance, state):
    if distance >= state.minDistance:
        return

    if max(cities) == 0:
        distance += graph[begin][end]
        if distance < state.minDistance:
            state.minDistance = distance
        return

    for i in range(len(cities)):
        if cities[i] == 0:
            continue

        cities[i] = 0
        dfs(i, end, graph, cities, distance + graph[begin][i], state)
        cities[i] = 1


class Solution:
    """
    @param arr: the distance between any two cities
    @return: the minimum distance Alice needs to walk to complete the travel plan
    """

    def travelPlan(self, arr):
        n = len(arr)
        if n == 0 or any(len(row) != n for row in arr):
            return 0

        cities = [1] * n
        cities[0] = 0

        state = State(inf)
        for i in range(1, n):
            for j in range(1, n):
                if i == j:
                    continue

                cities[i] = 0
                cities[j] = 0
                dfs(i, j, arr, cities, arr[0][i] + arr[j][0], state)
                cities[i] = 1
                cities[j] = 1

        return state.minDistance


# print(Solution().travelPlan(arr=[[0, 1, 2], [1, 0, 2], [2, 1, 0]]))
# print(Solution().travelPlan(arr=[[0, 10000, 2], [5, 0, 10000], [10000, 4, 0]]))


class TSP:
    # 给定某条路径，计算它的成本
    def distcal(self, path, dist):
        # 计算路径成本（路径，距离）
        sum_dist = 0  # 总成本
        for j in range(0, len(path) - 1):
            di = dist[int(path[j]) - 1][int(path[j + 1]) - 1]  # 查找第j和j+1个城市之间的成本
            sum_dist = sum_dist + di  # 累加
        di = dist[int(path[len(path) - 1]) - 1][path[0] - 1]  # 最后一个城市回到初始城市的成本
        sum_dist = sum_dist + di
        return sum_dist  # 返回路径的成本

    # 构造随机路径
    def randompath(self, inc):  # Inc城市列表
        allcity = inc[:]  # 城市列表
        path = []  # 路径
        loop = True
        while loop:
            if len(allcity) == 1:  # 如果是最后一个城市
                tmp = random.choice(allcity)
                path.append(tmp)
                loop = False  # 结束
            else:  # 如果不是最后一个城市
                tmp = random.choice(allcity)  # 在城市列表中随机选择一个城市
                path.append(tmp)  # 添加路径
                allcity.remove(tmp)  # 在城市列表中移除该城市
        return path

    def solve(self, arr):
        n = len(arr)
        ans = []
        citys = [i + 1 for i in range(n)]
        opt = 10000
        for i in range(10):
            pd = self.distcal(self.randompath(citys), arr)
            if pd < opt:
                opt = pd
            ans.append(pd)
        # print(opt)
        print(ans)
        return min(ans)


arr = [[0, 1, 2], [1, 0, 2], [2, 1, 0]]
# print(TSP().solve(arr))
print(TSP().solve(arr=[[0, 10000, 2], [5, 0, 10000], [10000, 4, 0]]))
