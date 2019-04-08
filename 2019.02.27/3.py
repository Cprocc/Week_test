class Solution(object):
    def insertIntoMaxTree(self, root, vall):
        if root is None or vall > root.val:
            n = TreeNode(vall)
            n.left = root
            return n
        root.right = self.insertIntoMaxTree(root.right,vall)
        return root

# 998
