def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    res = 0

    for i in range(k):
        res += nums[i]
    for i in range(0, len(nums) - k):
        cur = nums[i]
        nums[i] = res
        res += (nums[i+k] - cur)

    nums[len(nums) -k] = res

    return max(nums[0:len(nums) - k + 1]) /float(k)


if __name__ == '__main__':
    print(findMaxAverage([0,4,0,3,2], 1))