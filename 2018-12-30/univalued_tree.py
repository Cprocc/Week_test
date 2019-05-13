# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        root_list = []

        def DFS(root):
            if root.val != None:
                root_list.append(root.val)
                if root.left != None:
                    DFS(root.left)
                if root.right != None:
                    DFS(root.right)

        DFS(root)
        for i in range(len(root_list) - 1):
            if root_list[i] not in root_list[i + 1:len(root_list)]:
                return False
            else:
                pass
        return True


"""
将树结构转化为列表
"""



