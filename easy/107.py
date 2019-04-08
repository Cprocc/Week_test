def levelOrderBottom1(root):
    res = []
    dfs(root, 0, res)
    return res


def dfs(root, level, res):
    if root:
        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level+1)].append(root.val)
        dfs(root.left, level+1, res)
        dfs(root.right, level+1, res)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(13)
    print(levelOrderBottom1(root))
