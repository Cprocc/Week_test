class Solution:
    def permuteUnique(self, nums):
        ans = []
        cur = []
        nums.sort()
        print(nums)
        used = [0] * len(nums)
        self.dfs(ans, cur, used, nums)
        return ans

    def dfs(self, ans, cur, used, nums):
        if len(cur) == len(nums):
            temp = cur.copy()
            ans.append(temp)
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and used[i-1] == 1:
                continue
            if used[i] != 1:
                cur.append(nums[i])
                used[i] = 1
                self.dfs(ans, cur, used, nums)
                cur.pop()
                used[i] = 0


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.permuteUnique([1, 1,1, 2]))
