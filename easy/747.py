def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    ind = -1
    max_nums = -1
    sec_nums = -1
    for i in range(len(nums)):
        if nums[i] > max_nums:
            sec_nums = max_nums
            max_nums = nums[i]
            ind = i
        elif nums[i] > sec_nums:
            sec_nums = nums[i]

    if max_nums >= 2 * sec_nums:
        return ind
    else:
        return -1


if __name__ == '__main__':
    print(dominantIndex([0,0,2,1]))