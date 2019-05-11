class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]

        for j in range(1, len(grid)):
            grid[j][0] += grid[j-1][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]


if __name__ == '__main__':
    grid = [
          [1, 3, 1, 1],
          [1, 5, 1, 1],
          [4, 2, 1, 1]
        ]
    Sol = Solution()
    print(Sol.minPathSum(grid))
