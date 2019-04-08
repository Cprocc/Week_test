class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if abs(self.height_of_tree(root.left) - self.height_of_tree(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height_of_tree(self, root):
        if root is None:
            return 0
        return max(self.height_of_tree(root.left), self.height_of_tree(root.right)) + 1

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 求左子树和右子树的和 的差
        # 顺便记录所有 的差 的和
        self.res = 0

        def sumofson(root):
            if not root: return 0
            left, right = sumofson(root.left), sumofson(root.right)
            self.res += abs(left - right)
            return root.val

        sumofson(root)
        return self.res

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # 层次遍历
        if not root: return[]
        stack = [root]
        count = 1
        res = []
        while stack != []:
            temp = 0
            for _ in range(count):
                if stack[0].left:
                    stack.append(stack[0].left)
                if stack[0].right:
                    stack.append(stack[0].right)
                temp += stack.pop(0).val
            res.append(temp/count)
            count = len(stack)

        return res

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 每一次中序遍历遍历拿到的第一个节点
        self.res = 0

        def inorder(root):
            if not root: return 0
            print(root.val)
            inorder(root.left)
            inorder(root.right)

        inorder(root)

        return self.res


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)
    Sol = Solution()
    # print(Sol.isBalanced(root))
    # print(Sol.height_of_tree(root))
    # print(Sol.check(root))
    # print(Sol.findTilt(root))
    # print(Sol.averageOfLevels(root))
    print(Sol.sumOfLeftLeaves(root))
