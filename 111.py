class Solution(object):

    def minDepth(self, root) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1

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
    def minDepth2(self, root):
        return self.recurMinDepth(root, 0)
