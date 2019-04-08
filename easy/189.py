def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if k >= len(nums):
        k = k % len(nums)


    for j in range(k):
        temp = nums[len(nums) - k + j]
        for i in range(len(nums) - k + 1):
            nums[len(nums) - k + j - i] = nums[len(nums) - k + j - i - 1]

        nums[j], temp = temp, nums[j]


if __name__ == '__main__':
    nums = [1,2]
    k = 3
    rotate(nums, k)
    print(nums)
# Output: [3,99,-1,-100]
