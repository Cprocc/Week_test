class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root):
        res = self.sumRoot(root)
        r = 0
        for x in res:
            r += int(x, 2)

        return r

    def sumRoot(self, root: TreeNode) -> int:
        res = []
        if not root:
            return res
        self.sumHelp(root, res, str(root.val))
        return res

    def sumHelp(self, root, res, st):
        if not root.left and not root.right:
            res.append(st)
            return

        if root.left:
            self.sumHelp(root.left, res, st + str(root.left.val))
        if root.right:
            self.sumHelp(root.right, res, st + str(root.right.val))


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    Sol = Solution()
    print(Sol.sumRootToLeaf(root))

