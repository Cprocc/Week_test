def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max1 = 0
    max_cur = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            max_cur += 1
        else:
            max_cur = 0

        if max1 <= max_cur:
            max1 = max_cur

    return max1


if __name__ == '__main__':
    nums = [1,0,0,1,1,1,0,0,1,1,0,0]
    print(findMaxConsecutiveOnes(nums))