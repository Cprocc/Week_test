class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lens = len(prices)
        if lens <= 1:
            return 0

        max_earn = [0] * lens
        min_buy = prices[0]
        for i in range(1, lens):
            max_earn[i] = max(max_earn[i-1], prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])

        max_earn_is = prices[lens - 1]

        print(max_earn)

        ans = max_earn[-1]
        max_profit = 0
        for i in range(lens - 1):
            j = lens - 2 - i
            max_earn_is = max(max_earn_is, prices[j+1])
            max_profit = max(max_profit, max_earn_is - prices[j])
            ans = max(ans, max_earn[j] + max_profit)

        return ans


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.maxProfit([1,2,3,4,5]))
