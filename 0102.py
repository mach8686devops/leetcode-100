# 二叉树的层次遍历


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 递归写法
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node:
            return

        if len(self.result) < level + 1:
            self.result.append([])

        self.result[level].append(node.val)

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
