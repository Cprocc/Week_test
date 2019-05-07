class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        cur = []
        self.dfs(k, n, 1, cur, ans)
        return ans

    def dfs(self, k, n, s, cur, ans):
        if k == 0:
            if n == 0:
                temp = cur.copy()
                ans.append(temp)
            return

        for i in range(s, 10):
            if i > n:
                return
            cur.append(i)
            self.dfs(k-1, n-i, i+1, cur, ans)
            cur.pop()
    #     ans = []
    #     for i in range(0, 1 << 9):
    #         cur = []
    #         sums = 0
    #         for j in range(1, 10):
    #             if i & (i << (j-1)):
    #                 sums += j
    #                 cur.append(j)
    #
    #         from copy import deepcopy
    #         if sums == n and len(cur) == k:
    #             temp = deepcopy(cur)
    #             ans.append(temp)
    #
    #     return ans


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.combinationSum3(3, 9))
