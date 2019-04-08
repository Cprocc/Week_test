class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:return 0
        min_deep = 1
        pice_stack = [root]
        while True:
            s = len(pice_stack)
            for _ in range(s):
                cur_root = pice_stack.pop(0)
                if cur_root.right is None and cur_root.left is None:
                    return min_deep
                if cur_root.right is not None:
                    pice_stack.append(cur_root.right)
                if cur_root.left is not None:
                    pice_stack.append(cur_root.left)
            min_deep += 1

    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(7)
    root.right.right = TreeNode(13)
    Sol = Solution()
    # print(Sol.minDepth(root))
    print(Sol.binaryTreePaths1(root))
