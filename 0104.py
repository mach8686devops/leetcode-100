class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return max(map(self.maxDepth, (root.left, root.right))) + 1 if root else 0
