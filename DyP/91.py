class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n+1):
            first = int(s[i-1:i])
            second = int(s[i-2:i])
            print(first, second)
            if first != 0:
                dp[i] += dp[i-1]
            if 26 >= second >= 10:
                dp[i] += dp[i-2]

        return dp[n]


if __name__ == '__main__':
    s = '226'
    Sol = Solution()
    print(Sol.numDecodings(s))
