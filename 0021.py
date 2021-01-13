# 合并有序链表
# 直接递归


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
        # if l1 is None or l2 is None:
        #     return l1 or l2
        # if l1.val <= l2.val:
        #     l1.next = self.merge_two(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.merge_two(l1, l2.next)
        #     return l2
