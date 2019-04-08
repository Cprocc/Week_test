def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    import sys
    min_int = -sys.maxsize
    max_int = max(nums)
    recode = max_int
    for _ in range(2):
        for i in range(len(nums)):
            if nums[i] == max_int:
                nums[i] = min_int

        max_int = max(nums)

    if nums == [min_int] * len(nums):
        return recode
    else:
        return max(nums)


if __name__ == '__main__':
    nums = [2,3]
    print(thirdMax(nums))