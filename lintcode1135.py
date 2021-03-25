class Solution:
    """
    @param frames: A series of frames
    @return: Find the longest feature movement
    """

    def FeatureExtraction(self, frames):
        # 存储上一行键值对出现的次数信息
        preFeaTimes = {}
        # 存储本行键值对在上一行的基础上出现的次数信息
        feaTimes = {}
        # 保存结果
        count = 0
        n = len(frames)
        for i in range(n):
            for j in range(frames[i][0]):
                k = tuple([frames[i][j * 2 + 1], frames[i][j * 2 + 2]])
                if k in preFeaTimes:
                    # 判断如果本次输入的键值对在上一行出现过，那么该键值对的次数\
                    # 等于上一行中记录的出现次数+1
                    feaTimes[k] = preFeaTimes[k] + 1
                else:
                    # 如果该键值对没有出现过或者没在上一行出现过，说明该键值对
                    # 要么根本没出现过要么中间断了，所以重新置为1
                    feaTimes[k] = 1
                count = max(count, feaTimes[k])
            # 清理：是因为本行已经遍历完了，键值对的更新信息已经保存在feaTimes中了
            preFeaTimes.clear()
            # 因为要继续判断下一行的键值对信息，下一行是依赖本行的
            preFeaTimes = feaTimes.copy()
            feaTimes.clear()
        return count


frames = [[2, 1, 1, 2, 2],
          [2, 1, 1, 1, 4],
          [2, 1, 1, 2, 2],
          [2, 2, 2, 1, 4],
          [0],
          [0],
          [1, 1, 1],
          [1, 1, 1]]

print(Solution().FeatureExtraction(frames))
