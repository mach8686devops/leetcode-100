# 线段树

class SegmentTree:
    'Simple SegmentTree, ref: https://oi-wiki.org/ds/seg/'

    def __init__(self, n, val_obj=int, init=None):
        'init_arr: None for empty SegmentTree, or list/tuple which len(init_arr) == n'
        self.val_obj = val_obj

        class STNode:
            __slots__ = ('lower', 'upper', 'lazy', 'total')

        empty_node = STNode()
        self.TREE = [empty_node] * (4 * n)

        def dfs_build_tree(arr, node, lower, upper):
            self.TREE[node] = STNode()
            self.TREE[node].lazy = None
            self.TREE[node].lower = lower
            self.TREE[node].upper = upper
            if lower < upper:
                mid = (lower + upper) // 2
                sum_ = self.val_obj()
                sum_ += dfs_build_tree(arr, node * 2, lower, mid)
                sum_ += dfs_build_tree(arr, node * 2 + 1, mid + 1, upper)
                self.TREE[node].total = sum_
            else:
                self.TREE[node].total = arr[lower - 1] if arr else self.val_obj()
            return self.TREE[node].total

        dfs_build_tree(init, 1, 1, n)

    def _dfs_segment_apply(self, current, lower, upper, mod_val):
        cur = self.TREE[current]
        cur.total += (upper - lower + 1) * mod_val
        if cur.lower == lower and cur.upper == upper:
            if cur.lazy:
                cur.lazy += mod_val
            else:
                cur.lazy = mod_val
        else:
            mid = (cur.lower + cur.upper) // 2
            if lower <= mid:
                self._dfs_segment_apply(current * 2, lower, min(mid, upper), mod_val)
            if mid < upper:
                self._dfs_segment_apply(current * 2 + 1, max(mid + 1, lower), upper, mod_val)

    def segment_mod(self, lower, upper, mod_val):
        self._dfs_segment_apply(1, lower, upper, mod_val)

    def segment_queue(self, lower, upper):
        def dfs_segment_queue(current, lower, upper):
            cur = self.TREE[current]
            if cur.lower == lower and cur.upper == upper:
                return cur.total

            mid = (cur.lower + cur.upper) // 2
            if cur.lazy:
                self._dfs_segment_apply(current * 2, cur.lower, mid, cur.lazy)
                self._dfs_segment_apply(current * 2 + 1, mid + 1, cur.upper, cur.lazy)
                cur.lazy = None
            sum_ = self.val_obj()
            if lower <= mid:
                sum_ += dfs_segment_queue(current * 2, lower, min(mid, upper))
            if mid < upper:
                sum_ += dfs_segment_queue(current * 2 + 1, max(mid + 1, lower), upper)
            return sum_

        return dfs_segment_queue(1, lower, upper)


class Node:
    __slots__ = ('subs', 'lower', 'upper')

    def __init__(self):
        self.subs = []

    def dfs_trans_id(self, new_id):
        self.lower = new_id
        new_id += 1
        for s in self.subs:
            new_id = s.dfs_trans_id(new_id)
        self.upper = new_id - 1
        return new_id


class Solution:
    def bonus(self, n, leadership, operations):
        pmap = [Node() for _ in range(n + 1)]
        for p, s in leadership:
            pmap[p].subs.append(pmap[s])

        pmap[1].dfs_trans_id(1)

        st = SegmentTree(n)
        ans = []
        for ins in operations:
            p_node = pmap[ins[1]]
            if ins[0] == 1:
                st.segment_mod(p_node.lower, p_node.lower, ins[2])
            elif ins[0] == 2:
                st.segment_mod(p_node.lower, p_node.upper, ins[2])
            elif ins[0] == 3:
                result = st.segment_queue(p_node.lower, p_node.upper)
                ans.append(result % 1000000007)

        return ans
