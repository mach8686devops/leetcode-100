import math


class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     # 海象算子
    #     return (k:=str(x)) == k[::-1]

    def isPalindrome2(self, x: int) -> bool:
        r = list(map(lambda i: int(10 ** -i * x % 10), range(int(math.log10(x)), -1, -1))) if x > 0 else [0, x]
        return r == r[::-1]


# 海象算子

# Loop over fixed length blocks
# while (block := f.read(256)) != '':
#     process(block)
#
# 背景：代码读取一个文件，当不为空执行操作,同样看没有海象运算符，我们会怎么写：
#
# while 1:
#     block = f.read(256)
#     if block != '':
#         process(block)
# 	else:
# 		break
#
# 同样是 赋值一气呵成，这让我认为海象运算符的作用在于，把计算语句的结果赋值给变量，然后，变量可以在代码块里执行运用.

# 咱们这新开发了一种语法，它是一个强大的表达式，会把表达式的一部分赋值给变量，
#
# 因为很像海象的眼睛和象牙，所以成为海象操纵者(掌控雷电的感觉(~-^)。


# f string
# >>> name = 'Eric'
# >>> f'Hello, my name is {name}'
# 'Hello, my name is Eric'
#
# >>> number = 7
# >>> f'My lucky number is {number}'
# 'My lucky number is 7'
#
# >>> price = 19.99
# >>> f'The price of this book is {price}'
# 'The price of this book is 19.99'


# 类型注解


# python3.5引入
# 对函数的参数进行类型注解
# 对函数的返回值进行类型注解
# 只对函数参数做一个辅助说明，并不对函数参数进行类型检查
# 提供给第三方工具，做代码分析，发现隐形bug
# 函数注解的信息，保存在__annotations__属性中
# python3.6中引入变量注解
# i:int = 3