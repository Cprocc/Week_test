class Solution(object):
    def minimumTotal(self, triangle):
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]

                print(res)
        return res[0]


if __name__ == '__main__':
    Sol = Solution()
    tri = [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
    print(Sol.minimumTotal(tri))
