class Solution:
    def myPow(self, a, b):
        if b == 0: return 1
        if b < 0: return 1.0 / self.myPow(a, -b)
        half = self.myPow(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a


if __name__ == '__main__':
    Sol = Solution()
    Sol.myPow(5, 20)


# B: 1, 5, 10 ,20
