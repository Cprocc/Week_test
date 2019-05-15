class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        dp = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
            ans = max(dp[i], ans)

        print(dp)
        return ans


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Sol = Solution()
    print(Sol.maxSubArray(nums))
