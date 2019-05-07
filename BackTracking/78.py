class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    #     ans = []
    #     for i in range(0, len(nums)+1):
    #         self.dfs(ans, nums, i, 0, [])
    #
    #     return ans
    #
    # def dfs(self, ans, nums, n, s, cur):
    #     if len(cur) == n:
    #         temp = cur.copy()
    #         ans.append(temp)
    #         return
    #
    #     for i in range(s, len(nums)):
    #         cur.append(nums[i])
    #         self.dfs(ans, nums, n, i+1, cur)
    #         cur.pop()
        ans = []
        for s in range(1 << len(nums)):
            cur = []
            for i in range(len(nums)):
                if s & (1 << i):
                    cur.append(nums[i])
            ans.append(cur)

        return ans


Sol = Solution()
print(Sol.subsets([1, 2, 3]))
