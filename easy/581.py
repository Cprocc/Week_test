def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    import copy
    nums_re = copy.copy(nums)
    nums.sort()

    star, en = [0, 0]
    for i in range(len(nums)):
        if nums_re[i] != nums[i]:
            star = i
            break

    for j in range(len(nums)):
        if nums_re[len(nums) - j - 1] != nums[len(nums) - j - 1]:
            en = len(nums) - j
            break

    return en -star


if __name__ == '__main__':
    nums = [2, 12, 4, 15]
    print(findUnsortedSubarray(nums))
