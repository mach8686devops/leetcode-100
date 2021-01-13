from typing import List



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root: TreeNode, distance: int) -> (List[int], int):
            depths = [0] * (distance + 1)
            isLeaf = not root.left and not root.right
            if isLeaf:
                depths[0] = 1
                return (depths, 0)

            leftDepths, rightDepths = [0] * (distance + 1), [0] * (distance + 1)
            leftCount = rightCount = 0

            if root.left:
                leftDepths, leftCount = dfs(root.left, distance)
            if root.right:
                rightDepths, rightCount = dfs(root.right, distance)

            for i in range(distance):
                depths[i + 1] += leftDepths[i]
                depths[i + 1] += rightDepths[i]

            cnt = 0
            for i in range(distance + 1):
                for j in range(distance - i - 1):
                    cnt += leftDepths[i] * rightDepths[j]

            return (depths, cnt + leftCount + rightCount)

        _, ret = dfs(root, distance)
        return ret
