class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0


b = TreeNode(val=7)
c = TreeNode(val=3)
d = TreeNode(val=15)
e = TreeNode(val=9)
f = TreeNode(val=20)
b.left = c
b.right = d
d.left = e
d.right = f

cc = BSTIterator(b)
print(cc.next())
print(cc.next())
print(cc.hasNext())
print(cc.next())
print(cc.hasNext())
print(cc.next())
print(cc.hasNext())
print(cc.next())
print(cc.hasNext())
