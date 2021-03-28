class Solution:

    # build cost graph
    def build_min_cost_graph(self, costs):
        n = len(costs)
        min_cost_graph = [[float('inf') for _ in range(n)] for _ in range(n)]
        for city1, city2, cost in costs:
            u = city1 - 1
            v = city2 - 1
            min_cost_graph[u][v] = min(min_cost_graph[u][v], cost)
            min_cost_graph[v][u] = min(min_cost_graph[v][u], cost)
        return min_cost_graph

    def minCost(self, n, costs):

        def dfs(idx, city, cost, visited):
            if idx == n:
                if cost < self.min_cost:
                    self.min_cost = cost
                return

            if cost > self.min_cost:
                return

            for ncity in range(n):
                if is_valid(city, ncity):
                    visited.add(ncity)
                    ncost = cost + min_cost_graph[city][ncity]
                    dfs(idx + 1, ncity, ncost, visited)
                    visited.remove(ncity)

        is_valid = lambda city, ncity: ncity not in visited \
                                       and min_cost_graph[city][ncity] != float('inf')
        self.min_cost = float('inf')
        visited = set([0])
        min_cost_graph = self.build_min_cost_graph(costs)
        dfs(1, 0, 0, visited)
        return self.min_cost

    def travelPlan(self, arr):

        def dfs(idx, city, dist):
            if idx == n:
                if city == 0:
                    self.mindist = min(self.mindist, dist)
                return
            # pruning
            if dist > self.mindist:
                return
            for ncity in range(n):
                if ncity == city:
                    continue
                ndist = arr[city][ncity]
                if ncity not in visited:
                    visited.add(ncity)
                    dfs(idx + 1, ncity, dist + ndist)
                    visited.remove(ncity)

        self.mindist = float('inf')
        n = len(arr)
        visited = set()
        idx, start_city, dist = 0, 0, 0
        dfs(idx, start_city, dist)
        return self.mindist
