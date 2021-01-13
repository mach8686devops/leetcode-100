# 设计并实现一个 TwoSum 的类，使该类需要支持 add 和 find 的操作。
#
# add 操作 -  对内部数据结构增加一个数。
# find 操作 - 寻找内部数据结构中是否存在一对整数，使得两数之和与给定的数相等。
#
# 示例 1:
#
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# 示例 2:
#
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.dict = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.dict[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key, val in self.dict.items():
            if value - key in self.dict:
                if key * 2 == value and self.dict[key] > 1:
                    return True
                elif key * 2 != value:
                    return True
        return False
