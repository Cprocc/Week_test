def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    cache, st = {}, []
    for x in nums2:
        if len(st) == 0:
            st.append(x)
        elif x <= st[-1]:
            st.append(x)
        else:
            while st and st[-1] < x:
                cache[st.pop()] = x
            st.append(x)
    result = []
    for x in nums1:
        if x in cache:
            result.append(cache[x])
        else:
            result.append(-1)
    return result


if __name__ == '__main__':
    nums1 = [2,4]
    nums2 = [1, 2, 3, 4]
    print(nextGreaterElement(nums1, nums2))
