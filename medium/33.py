class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            # 前一段完全递增的情况被排除
            if target < nums[0] < nums[M]: # -inf
                L = M+1

            # 只能落在两个序列的跨度上
            elif target >= nums[0] > nums[M]: # +inf
                H = M

            # 单纯前一半递增区间
            elif nums[M] < target:
                L = M+1

            # 单纯后一半递增区间
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1


if __name__ == '__main__':
    Sol = Solution()
    nums = [7,8,9,10,11,0,1,2,3,4,5,6]; target = 5
    print(Sol.search(nums, target))
