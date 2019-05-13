def nextPermutation(nums):
    if not nums:
        return None

    i = len(nums) - 1
    j = -1  # j is set to -1 for case `4321`, so need to reverse all in following step
    while i > 0:
        if nums[i - 1] < nums[i]:  # first one violates the trend
            j = i - 1
            break
        i -= 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > nums[j]:  #
            nums[i], nums[j] = nums[j], nums[i]  # swap position
            nums[j + 1:] = sorted(nums[j + 1:])  # sort rest
            print(nums)
            return




if __name__ == '__main__':
    print(nextPermutation([1,4,3,2]))