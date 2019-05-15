class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0

        n = len(matrix[0])

        if n == 0: return 0

        dp = [[0] * n for _ in range(m)]

        flag = 0
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                flag = 1

        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                flag = 1

        if m == 1 or n == 1:
            return 1 if flag == 1 else 0

        res = 0 if flag == 0 else 1
        for i in range(1, m):
            for j in range(1, n):
                if dp[i - 1][j - 1] > 0 and matrix[i - 1][j] == '1' and matrix[i][j - 1] == '1' and matrix[i][j] == '1':
                    dp[i][j] = (min(dp[i - 1][j - 1],dp[i-1][j],dp[i][j-1]) + 1)
                else:
                    dp[i][j] = int(matrix[i][j])

                res = max(dp[i][j], res)

        print(dp)
        return res * res



Sol = Solution()
print(Sol.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]))