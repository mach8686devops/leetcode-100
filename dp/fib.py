# 没有工具就是最好的工具
# 指数级别的递归 有重复 如何进行化简
# 改变时间复杂度 记忆化搜索


def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(1, n - 1):
        a, b = b, a + b
    return a + b


for i in range(10):
    print(i, fib(i))
