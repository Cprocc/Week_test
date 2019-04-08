class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        self.permuteRecursive(nums, 0, res)

        return res

    def permuteRecursive(self, nums, begin, res):
        if begin >= len(nums):
            temp = nums.copy()
            res.append(temp)
            return

        for i in range(begin, len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.permuteRecursive(nums, begin+1, res)
            nums[begin], nums[i] = nums[i], nums[begin]

    def permute1(self, nums):
        res = []
        li = []
        self.permuteHelp(res, li, nums)
        return res

    def permuteHelp(self,res, li, nums):
        temp = li.copy()
        if len(temp) == len(nums):
            res.append(temp)

        else:
            for i in range(len(nums)):
                # if nums[i] in li: continue
                if nums[i] == -100:
                    continue

                if i > 0 and nums[i-1] != -100 and nums[i - 1] == nums[i]:
                    continue

                li.append(nums[i])

                te = nums[i]
                nums[i] = -100
                self.permuteHelp(res, li, nums)
                nums[i] = te

                li.pop()

    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: break  # handles duplication
            ans = new_ans
        return ans


if __name__ == '__main__':
    nums = [1, 1, 2]
    Sol = Solution()
    # print(Sol.permute(nums))
    # print(Sol.permute1(nums))
    print(Sol.permuteUnique(nums))
