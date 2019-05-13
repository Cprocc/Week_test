class Solution:
    def searchRange(self, nums, target):
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = int((lo + hi) / 2)
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]


if __name__ == '__main__':
    Sol = Solution()
    nums = [1,1,2,2,3,4,4,5,5,5,5,7,7,7,7,7,7]; target = 5
    print(Sol.searchRange(nums, target))