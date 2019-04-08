def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    res = 1
    for i in range(3):
        print(nums[len(nums)-1-i])
        res *= nums[-i]

    return res


if __name__ == '__main__':
    print(maximumProduct([1,2,3,4]))