class Solution(object):
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        if len(wordDict) == 0:
            return False

        dp = [None] * (len(s))

        for i in range(1, len(s)):
            for j in range(0, i+1):
                sub = s[j:i+1]

                if sub in wordDict and(j == 0 or dp[j-1]):
                    dp[i] = True
                    break

        return dp[len(s)-1]


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
