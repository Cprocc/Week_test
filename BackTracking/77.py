class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        temp = []
        self.dfs(0, n, k, temp, ans)
        return ans

    def dfs(self, i, n, k, temp, ans):
        if n - i + len(temp) < k:
            return
        if len(temp) == k:
            t = temp.copy()
            ans.append(t)
            return

        for j in range(i + 1, n + 1):
            temp.append(j)
            self.dfs(j, n, k, temp, ans)
            temp.pop()

        return
