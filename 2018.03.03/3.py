def longestOnes1(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    longest = 0
    for i in range(len(A)):
        long_one = 0
        re_times = K
        for cur in range(i, len(A)):
            if A[cur] == 1:
                long_one += 1
            elif A[cur] == 0 and re_times > 0:
                long_one += 1
                re_times -= 1
            else:
                break
        longest = max(longest, long_one)
    return longest


def longestOnes(A, K):
        res = i = 0
        for j in range(len(A)):
            K -= A[j] == 0
            if K < 0:
                K += A[i] == 0
                i += 1
            res = max(res, j - i + 1)
        return res


if __name__ == '__main__':
    A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    K = 3
    print(longestOnes(A, K))
