import collections


def findPairs(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if k == 0:
        return sum(v>1 for v in collections.Counter(nums).values())
    res = 0

    has_done = []
    for i in range(len(nums)):
        has_pair = []
        temp = nums[i] + k
        if nums[i] not in has_done and temp not in has_pair and temp in nums:
            res += 1
            has_done.append(nums[i])
            has_pair.append(temp)

    return res


if __name__ == '__main__':
    nums = [3, 1, 4, 1, 5, 5]
    k = 2
    print(findPairs(nums, k))