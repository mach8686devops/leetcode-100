class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        l, r, f = root.left, root.right, lambda x: self.hasPathSum(x, sum - root.val)
        return l is r and sum == root.val or f(l) or f(r)
