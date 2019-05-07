class Solution:
    def combinationSum2(self, candidates, target):
        ans = []
        cur = []
        candidates.sort()
        if len(candidates) == 0:
            return list(ans)

        self.dfs(0, target, candidates, ans, cur)

        return ans

    def dfs(self, s, target, candidates, ans, cur):
        if target < 0:
            return

        if target == 0:
            temp = cur.copy()
            ans.append(temp)
            return

        for i in range(s, len(candidates)):
            if target - candidates[i] < 0:
                return
            if i > s and candidates[i] == candidates[i - 1]:
                continue
            cur.append(candidates[i])
            self.dfs(i + 1, target - candidates[i], candidates, ans, cur)
            cur.pop()


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
