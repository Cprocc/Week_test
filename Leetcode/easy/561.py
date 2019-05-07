def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    res = 0
    for i in range(int(len(nums) / 2)):
        res += nums[2*i]
    return res


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(arrayPairSum(nums))