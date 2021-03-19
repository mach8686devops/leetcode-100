#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
链接：https://www.nowcoder.com/questionTerminal/1d18c0841e64454cbc3afaea05e2f63c?toCommentId=2380191
来源：牛客网
居然有假币！ 现在猪肉涨了，但是农民的工资却不见涨啊，没钱怎么买猪肉啊。nowcoder这就去买猪肉，
结果找来的零钱中有假币！！！可惜nowcoder 一不小心把它混进了一堆真币里面去了。只知道假币的重量比真币的质量要轻，
给你一个天平（天平两端能容纳无限个硬币），请用最快的时间把那个可恶的假币找出来。
输出：
    最多要称几次一定能把那个假币找出来？
"""


def find(n):
    """
    思路： 分治， 三分法
     - 分为 3 份 n//3,
        - n%3 = 0, 即 n//3, n//3, n//3, 最坏剩余 n//3
        - n%3 = 1， 即 n//3, n//3, n//3 +1, 最坏剩余 n//3 + 1
        - n%3 = 2， 即 n//3, n//3 + 1, n//3 + 1, 最坏剩余 n//3 + 1
    - 终止条件：当 n < 1 时
    """
    count = 0
    while n > 1:
        count += 1
        if n % 3:
            n = n // 3 + 1
        else:
            n = n // 3
    return count


if __name__ == '__main__':

    print("result is", find(4))
