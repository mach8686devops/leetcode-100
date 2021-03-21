import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell_ans = []
        buy_ans = []
        heapq.heapify(sell_ans)
        heapq.heapify(buy_ans)
        for price, cnt, t in orders:
            if t == 0:  # 买，就找最小的sell
                while cnt > 0 and sell_ans and sell_ans[0][0] <= price:  # sell的价格小。能买到
                    if cnt > sell_ans[0][1]:  # 买很多
                        cnt -= sell_ans[0][1]  # 最小售价的买了
                        heapq.heappop(sell_ans)
                    elif cnt == sell_ans[0][1]:  # 刚好买了
                        cnt = 0
                        heapq.heappop(sell_ans)
                    elif cnt < sell_ans[0][1]:  # 买完，堆里还能剩下
                        tmp = sell_ans[0][1] - cnt
                        cnt = 0
                        new_ = [sell_ans[0][0], tmp]
                        heapq.heappop(sell_ans)
                        heapq.heappush(sell_ans, new_)
                if cnt > 0:
                    heapq.heappush(buy_ans, [(-1) * price, cnt])

            else:  # 卖，找价格最高的buy 
                while cnt > 0 and buy_ans and (-1) * buy_ans[0][0] >= price:
                    if cnt > buy_ans[0][1]:
                        cnt -= buy_ans[0][1]
                        heapq.heappop(buy_ans)
                    elif cnt == buy_ans[0][1]:
                        cnt = 0
                        heapq.heappop(buy_ans)
                    elif cnt < buy_ans[0][1]:
                        tmp = buy_ans[0][1] - cnt
                        cnt = 0
                        new_ = [buy_ans[0][0], tmp]
                        heapq.heappop(buy_ans)
                        heapq.heappush(buy_ans, new_)
                if cnt > 0:
                    heapq.heappush(sell_ans, [price, cnt])
        res = 0
        while sell_ans:
            res += sell_ans[0][1]
            res %= 1000000007
            heapq.heappop(sell_ans)
        while buy_ans:
            res += buy_ans[0][1]
            res %= 1000000007
            heapq.heappop(buy_ans)
        return res
