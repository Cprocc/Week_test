class Solution(object):
    def addDigits(self, num):
        return num if num == 0 else num % 9 or 9


if __name__ == '__main__':
    sol = Solution()
    print(sol.addDigits(9))
