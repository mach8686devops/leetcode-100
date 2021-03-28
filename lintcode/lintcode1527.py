# 1.分别枚举数字1-9添加已知的13张牌中，注意如果这13张牌中已经有4张i则不能添加i，因为每个数字最多出现4次。我们可以用一个数组times[]记录每个数字的出现次数。
# 2.对于每种14张牌的情况，再分别枚举每个数字j作为雀头(如果j有两张以上)，判断是否可以和牌。
# 3.然后从1-9开始遍历，如果数字k出现次数times[k]>=3，说明数字k可以组成一个刻子"kkk"，那么优先组成刻子，times[k]-=3。若判断剩下的k是否可以组成顺子，那么判断k,k+1,k+2如果都存在牌，说明可以组成一个顺子"kk+1k+2"，这三个元素的出现次数都-1；如果不能组成顺子，说明不可以和牌，因为剩下的所有牌都需要被分配到刻子或顺子中，不能落单。


class Solution:
    """
    @param cards: A list of cards.
    @return: A list of feasible solution.
    """

    # 判断此时的14张牌是否可以和牌
    def check(self, times):
        tmp = [0] * 10
        # i作为雀头
        for i in range(1, 10):
            if times[i] < 2:
                continue
            # ok标记是否可以和牌的状态
            ok = True
            for k in range(1, 10):
                tmp[k] = times[k]
            tmp[i] -= 2
            for j in range(1, 10):
                if not ok:
                    break
                # 刻子jjj
                if tmp[j] >= 3:
                    tmp[j] -= 3
                while tmp[j] and ok:
                    if j + 2 > 9:
                        ok = False
                        break
                    # 顺子(j, j + 1, j + 2)
                    if tmp[j + 1] and tmp[j + 2]:
                        tmp[j] -= 1
                        tmp[j + 1] -= 1
                        tmp[j + 2] -= 1
                    else:
                        ok = False
            if ok:
                return True
        return False

    def getTheNumber(self, cards):
        # times[i]表示数字i出现的次数
        times = [0] * 10
        ans = []
        for i in range(13):
            times[cards[i]] += 1
        # 和牌：雀头+4*顺子/刻子
        for i in range(1, 10):
            if times[i] < 4:
                times[i] += 1
                if self.check(times):
                    ans.append(i)
                times[i] -= 1
        if len(ans) == 0:
            return [0]
        return ans
