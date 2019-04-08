def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 1
    cur_longest = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            cur_longest += 1
        else:
            cur_longest = 1

        if cur_longest > res:
            res = cur_longest

    return res


if __name__ == '__main__':
    nums = [3, 3, 3, 3, 3]
    print((findLengthOfLCIS(nums)))
