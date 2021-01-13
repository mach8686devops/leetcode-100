class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode, first=True) -> bool:
        if not root: return first or []
        l = self.isValidBST(root.left, 0) + [root.val] + self.isValidBST(root.right, 0)
        return all([a > b for a, b in zip(l[1:], l)]) if first else l
