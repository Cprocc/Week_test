def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    res = 0
    p = cur = q = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            p, cur, q = i - 1, i, i + 2
            res += 1

    if res > 1:
        return False

    if res == 1 and p >= 0:
        if nums[q] < nums[p]:
            return False

    return True


if __name__ == '__main__':
    print(checkPossibility([2,3,3,2,4]))
