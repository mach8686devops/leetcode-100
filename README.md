

套路篇


+ 数组与字符串
+ 哈希表
+ 并查集
+ dp
+ 查找
+ 排序
+ 链表
+ 递归
+ 栈与队列



自我介绍
数据库索引
B+树存储 不用别的
数据库范式
mysql数据库底层存储
数据库类型
内存泄露


2的幂次：https://leetcode-cn.com/problems/power-of-two/
颜色分类：https://leetcode-cn.com/problems/sort-colors/
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
猫捉老鼠：https://zhuanlan.zhihu.com/p/80701068

线程同步

通信的方式

位运算 x&1==1 奇偶 x>>1 处以2 x=x&(x-1)清掉低位0 x&-x 得到低位的1 x&~x 0

树的遍历方式 栈  队列 深度 广度

有挑战性的问题

知识盲区很正常

一些沟通和思考

谦卑的程序员


脑图总结


先看 背 自己做 隔周做 面试前做


打家劫舍

```
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now, last = 0, 0
        for i in nums: 
            last, now = now, max(last + i, now)
        return now
```


```python

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        
        return second

```


```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            return max(self.rob_helper(nums, 0, n-2), self.rob_helper(nums, 1, n-1))
        
    def rob_helper(self, nums, start, end):
        pre = nums[start]
        cur = max(nums[start+1], pre)
        next = start+2
        while next <= end:
            temp = cur
            cur = max(pre+nums[next], cur)
            pre = temp
            next += 1
        return cur
        
        
        
        
```


18个代码模版
50个题目解析
300真题服务






