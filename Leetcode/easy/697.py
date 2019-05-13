def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    times = [0] * (max(nums)+1)
    for i in range(len(nums)):
        times[nums[i]] += 1

    max_times = max(times)
    min_dis = len(nums)

    for i in range(len(times)):
        if times[i] ==  max_times:
            for k in range(len(nums)):
                if nums[k] == i:
                    star = k
                    break
            for l in range(len(nums)):
                if nums[len(nums)-1-l] == i:
                    end = len(nums)-1-l
                    break
            min_dis = min(min_dis, end -star + 1)

    return min_dis


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1]
    print(findShortestSubArray(nums))