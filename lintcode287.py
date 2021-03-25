# 先排序，然后贪婪 + 双指针
# 右指针尽量右移，有一过程中纪录右边界，然后将左指针移到最右边界指针处循环。
#
# 代码实现
# 边界条件检查
# 右指针的向右移动时要纪录最右边界的位置作为下一个left指针的位置。
# 时空复杂度分析
# 均为O(N), 空间O(N)的原因是要存sorted pos

pos = [[0, 4], [0, 3], [2, 4], [4, 5]]
L = 5


class Solution:
    """
    @param pos: the vision ward can control interval
    @param L: you need to control interval length
    @return: return the minium number of vision ward to control the interval
    """

    def solve(self, eyes, L):

        eyes.sort()
        print(eyes)
        end = 0
        max_length = 0
        n = len(eyes)
        time = 1  # 需要的守卫，刚开始就要有一个
        for i in range(n):
            if max_length >= L:
                break  # 长度达到退出
            if eyes[i][0] > end:  # 如果中间空开了，比如【0,6】和【8,27】那么说明中间必有一个
                time += 1  # 守卫数量+1
                end = max_length
                max_length = max(eyes[i][1], max_length)  # ***
            elif eyes[i][1] > max_length:  # 如果和前一个仍然是重叠关系，且延伸长度更长，更新最大延伸长度
                max_length = eyes[i][1]
                # print(eyes[i][1])
        # if max_length < eyes[-1][0]:
        #     return -1
        print(max_length)
        return time

        # print(time)
        # print(end)

    def getMiniumVisionWard(self, pos, L):
        pos.sort(key=lambda x: (x[0], -x[0]))
        n, ans = len(pos), 0
        pre, last = 0, 0

        i = 0
        while i < n:
            while i < n and pos[i][0] <= pre:
                last = max(last, pos[i][1])
                i += 1
            ans += 1
            pre = last
            if i < n and pos[i][0] > pre:
                return -1
            if last >= L:
                break
        return ans


print(Solution().getMiniumVisionWard(pos, L))
print(Solution().getMiniumVisionWard(
    pos=[[47, 62], [42, 44], [35, 45], [13, 32], [0, 11], [28, 28], [15, 25], [28, 31], [2, 18], [0, 13], [16, 25],
         [54, 71], [8, 9], [7, 25], [0, 5], [32, 50], [9, 20], [9, 22], [56, 72], [0, 11]], L=60))
print(Solution().getMiniumVisionWard(pos=[[0, 4], [5, 5]], L=5))
