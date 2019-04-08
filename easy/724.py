def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    le = 0
    ri = len(nums)-1
    le_sum = nums[le]
    ri_sum = nums[ri]

    while le < ri:
        if le_sum > ri_sum:
            ri -= 1
            ri_sum += nums[ri]

        elif le_sum < ri_sum:
            le += 1
            le_sum += nums[le]

        else:
            le += 1
            le_sum += nums[le]

    if le_sum == ri_sum and ri == le:
        return ri
    else:
        return -1


if __name__ == '__main__':
    nums = [-1,-1,-1,-1,-1,0]
    print(pivotIndex(nums))
