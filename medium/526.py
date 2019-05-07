class Solution:
    ans = 0

    def countArrangement(self, N):
        cur = [0] * (N + 1)
        self.dfs(cur, N, 1)
        return self.ans

    def dfs(self,cur, N, s):
        if s == N + 1:
            self.ans += 1
            return

        for i in range(1, N + 1):
            if cur[i] == 0 and (i % s == 0 or s % i == 0):
                cur[i] = 1
                self.dfs(cur, N, s + 1)
                cur[i] = 0


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.countArrangement(4))
