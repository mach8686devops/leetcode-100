# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
# 每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
#
#  
#
# 示例 1:
#
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
#


class Solution(object):
    def openLock(self, deadends, target):
        def rot_at(s, i, move):
            return s[:i] + str((int(s[i]) + move + N) % N) + s[i + 1:]

        vis, q1, q2 = set(deadends), set(), set()
        n, N, step = len(target), 10, 0
        q1.add('0000')
        q2.add(target)
        # 单独处理初始无解情况
        if '0000' in vis:
            return -1
        while q1:
            temp = set()  # 创建临时set，保存下层的所有结果
            for cur in q1:
                # check
                if cur in q2:
                    return step  # 如果双向BFS相遇
                vis.add(cur)
                # put all node into q
                for i in range(n):
                    t = rot_at(cur, i, +1)
                    if t not in vis:
                        temp.add(t)

                    t = rot_at(cur, i, -1)
                    if t not in vis:
                        temp.add(t)
            step += 1
            # 交替探测，谁节点少优先检测
            if len(q2) < len(temp):
                q1 = q2
                q2 = temp
            else:
                q1 = temp
        return -1
