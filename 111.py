class Solution(object):
    def recurMinDepth(self, root, depth):
        if root is None:
            return 0
        elif not root.left and not root.right:
            return 1

        left_depth = (self.recurMinDepth(root.left, depth) if root.left is not None else 0)
        right_depth = (self.recurMinDepth(root.right, depth) if root.right is not None else 0)

        # warn: a node just have a child, a node have two child, their height calculation method are different.
        if left_depth > 0 and right_depth > 0:
            return min(left_depth, right_depth) + 1
        elif left_depth > 0:
            return left_depth + 1
        else:  # right_depth > 0, or (left_depth == 0 and right_depth == 0)
            return right_depth + 1

    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        return self.recurMinDepth(root, 0)
